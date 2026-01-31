"""
AI Acknowledgment:
Developed with assistance from Claude (Anthropic) as a learning exercise in Python automation.

-------------------------------------------------
Purpose: Semester organization for class folders. 

This script is to make it easier and faster to create folders for future classes 
so that user doesn't have to manually create the folders each time. 
Could is designed for simple and easy use and modificatio for 
basic classroom organization for students. 

01/31/2026
"""

import os

# ============================================================================
# CONFIGURATION SECTION - EDIT THESE VALUES FOR YOUR SETUP
# ============================================================================

# Semester folder name (change this each semester)
SEMESTER = "Spring 2026"

# Your base path - REPLACE WITH YOUR OWN PATH
# Example: r"C:\Users\YourName\Documents\School\MSIT Program"
BASE_PATH = r"C:\Users\YourUsername\Documents\YourSchoolFolder\Program"

# Parent folders to create week folders inside (add or remove as needed)
PARENT_FOLDERS = [
    "Class Exercises",
    "Labs",
    "Notepad++ Lecture Minutes"
]

# Week range: Start week and End week (inclusive)
START_WEEK = 1
END_WEEK = 15

# ============================================================================
# SCRIPT - Not recommended to add below this line unless you know what you 
#          are modifying
# ============================================================================