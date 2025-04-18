# Smart Attendance Management System

An IoT-based, smart digital solution designed to streamline operations, enhance transparency, and improve accountability in Working sites (which includes - mining, oil refineries, etc.) . The system uses facial recognition for attendance, ensures and enables efficient supervisor reporting—all through an intuitive web dashboard.
This project focuses on building a scalable and user-centric system for managing the daily operations of on-site Refinaries and rigs using Raspberry Pi, AI camera modules, and Python-based automation.
The system ensures transparency and accuracy in attendance logging and supervisor reporting, while supporting offline functionality with real-time synchronization when the internet is available.

## Key Features

1. Facial Recognition for Attendance

Automated facial recognition using OpenCV and dlib for workers, helpers, and children.
Data is captured and processed via an AI camera module connected to Raspberry Pi.
Prevents fraudulent attendance entries.

2. Web Dashboard Interface

Built with CustomTkinter for an interactive and full-screen UI.
Provides real-time status updates for each operational script.
Options to:
Run the entire process (from facial data capturing to attendance logging).
Directly initiate the attendance logging process.

3. Offline Functionality

Supports data operations even in regions with limited connectivity.
Automatically syncs data to SQLite when internet access is restored.

## Video
Running the program on the Raspberry Pi OS, which is Linux compatible
https://youtu.be/PPci1tRa728
