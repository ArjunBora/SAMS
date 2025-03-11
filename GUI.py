import customtkinter as ctk
import subprocess
import os

# Set UI Theme
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")  

class FullScreenScriptRunner(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Anganwadi Attendance System")
        self.geometry("1280x720")  # Set initial size
        
        # Make window fullscreen on Raspberry Pi
        self.attributes("-fullscreen", True)
        
        # Header
        self.header = ctk.CTkLabel(self, text="Smart Attendance Management System", font=("Arial", 28, "bold"))
        self.header.pack(pady=20)
        
        # Main Frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Status Labels Frame
        self.status_frame = ctk.CTkFrame(self.main_frame)
        self.status_frame.pack(pady=20, fill="x", padx=20)
        self.status_labels = {}
        script_names = ["Capture Face Data", "Processing Facial Features", "Identify & Log Data", "Show Attendance Log"]
        
        for i, script in enumerate(script_names):
            label = ctk.CTkLabel(self.status_frame, text=f"{script}: Not Started", font=("Arial", 14), text_color="gray")
            label.grid(row=0, column=i, padx=20, pady=10)
            self.status_labels[script] = label
        
        # Button Frame
        self.button_frame = ctk.CTkFrame(self.main_frame)
        self.button_frame.pack(pady=20)
        
        # Start Buttons
        self.start_button = ctk.CTkButton(self.button_frame, text="Run Full System", fg_color="green", command=self.run_scripts)
        self.start_button.grid(row=0, column=0, padx=20, pady=10)
        
        self.attendance_button = ctk.CTkButton(self.button_frame, text="Attendance Only", fg_color="blue", command=self.run_attendance)
        self.attendance_button.grid(row=0, column=1, padx=20, pady=10)
        
        # Exit button for Raspberry Pi (since there's no window close button in fullscreen)
        self.exit_button = ctk.CTkButton(self.button_frame, text="Exit", fg_color="red", command=self.quit)
        self.exit_button.grid(row=0, column=2, padx=20, pady=10)
        
        # Script paths - adjusted for Linux/Raspberry Pi paths
        self.script_paths = {
            "Capture Face Data": "/home/bichitra/SAMS/entry.py",
            "Processing Facial Features": "/home/bichitra/SAMS/store_features.py",
            "Identify & Log Data": "/home/bichitra/SAMS/attendance.py",
            "Show Attendance Log": "/home/bichitra/SAMS/app.py"
        }
        
        # Bind escape key to exit fullscreen
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        
    def run_scripts(self):
        """Runs all scripts sequentially."""
        self.start_button.configure(state="disabled", fg_color="gray")
        self.attendance_button.configure(state="disabled", fg_color="gray")
        
        for script_name, script_path in self.script_paths.items():
            self.run_single_script(script_name, script_path)
        
        self.start_button.configure(state="normal", fg_color="green")
        self.attendance_button.configure(state="normal", fg_color="blue")
    
    def run_attendance(self):
        """Runs scripts starting from attendance logging."""
        self.attendance_button.configure(state="disabled", fg_color="gray")
        
        for script_name, script_path in list(self.script_paths.items())[2:]:  # Start from 3rd script
            self.run_single_script(script_name, script_path)
        
        self.attendance_button.configure(state="normal", fg_color="blue")
    
    def run_single_script(self, script_name, script_path):
        """Runs a single script and updates status."""
        try:
            self.status_labels[script_name].configure(text=f"{script_name}: Running...", text_color="orange")
            self.update()
            
            # Use 'python3' explicitly for Raspberry Pi
            # Also make sure the script is executable
            if not os.access(script_path, os.X_OK):
                subprocess.run(["chmod", "+x", script_path], check=True)
                
            subprocess.run(["python3", script_path], check=True)
            self.status_labels[script_name].configure(text=f"{script_name}: Completed", text_color="green")
        except subprocess.CalledProcessError as e:
            self.status_labels[script_name].configure(text=f"{script_name}: Error", text_color="red")
            print(f"Error running {script_name}: {e}")
        except Exception as e:
            self.status_labels[script_name].configure(text=f"{script_name}: Error", text_color="red")
            print(f"Unexpected error with {script_name}: {e}")

# Run the GUI
if __name__ == "__main__":
    app = FullScreenScriptRunner()
    app.mainloop()

