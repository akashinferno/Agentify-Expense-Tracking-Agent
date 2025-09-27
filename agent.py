import json
import google.generativeai as genai
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os
from dotenv import load_dotenv

# AI-Powered Expense Tracker - Competition Template
# This file contains 6 TODOs corresponding to 6 functions in jumbled.py
# Participants need to copy the correct code blocks and implement each TODO

# Load environment variables
load_dotenv()

# Get API key and Sheet ID from .env file
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
SHEET_ID = os.getenv('SHEET_ID')

# =============================================================================
# TODO 1: SYSTEM INITIALIZATION
# =============================================================================
# Find CODE BLOCK  in jumbled.py: 
# This function should:
# - Configure Gemini AI with the API key
# - Handle Google Sheets OAuth authentication (token.pickle)
# - Create and return both model and service objects
# - Use gemini-2.5-flash-lite model

# =============================================================================
# TODO 2: AI NATURAL LANGUAGE PROCESSING
# =============================================================================
# Find CODE BLOCK  in jumbled.py: 
# This function should:
# - Create a simple AI prompt for expense parsing
# - Send request to Gemini AI model
# - Clean up JSON response (handle ```json``` blocks)
# - Return parsed expense data as dictionary

# =============================================================================
# TODO 3: SHEET HEADER SETUP
# =============================================================================
# Find CODE BLOCK in jumbled.py
# This function should:
# - Check if headers already exist in the sheet
# - Create header row: Date, Item, Amount, Category, TOTAL, =SUM(C:C)
# - Add the headers to row 1 of the sheet
# - Print success message

# =============================================================================
# TODO 4: DATA INSERTION
# =============================================================================
# Find CODE BLOCK  in jumbled.py: 
# This function should:
# - Call setup_sheet_headers() first
# - Find the next empty row in the sheet
# - Insert each expense item with "Today" as date
# - Print confirmation message for each added item

# =============================================================================
# TODO 5: SYSTEM VALIDATION
# =============================================================================
# Find CODE BLOCK  in jumbled.py: 
# This function should:
# - Check if GEMINI_API_KEY is set
# - Check if SHEET_ID is configured properly
# - Print error messages for missing configurations
# - Return True if valid, False if invalid

# =============================================================================
# TODO 6: MAIN EXECUTION LOOP
# =============================================================================
# Find CODE BLOCK  in jumbled.py: 
# This function should:
# - Print "Simple Expense Tracker" header
# - Validate system using the validation function
# - Initialize model and service using setup()
# - Run main loop asking for expense input
# - Handle 'quit' command to exit
# - Process expenses and add to sheet

# YOUR IMPLEMENTATION GOES HERE:
# Copy and paste the 6 code blocks from jumbled.py to complete the TODOs above

if __name__ == "__main__":
    run_main_with_stats()

# =============================================================================
# COMPETITION INSTRUCTIONS
# =============================================================================
"""
AGENT BUILDING COMPETITION CHALLENGE:

Your task is to implement the missing functionality in this expense tracker by using 
the code blocks provided in jumbled.py. The goal is to create a working AI-powered 
expense tracking system.

WHAT YOU NEED TO DO:
1. Study the function signatures and TODO comments above
2. Look at jumbled.py for implementation details
3. Copy and adapt the relevant code blocks to complete each function
4. Ensure the system works end-to-end

EVALUATION CRITERIA:
- Functionality: Does the expense tracker work correctly?
- Code Quality: Is the code clean and well-organized?
- AI Integration: Does it properly use Gemini AI for parsing?
- Error Handling: Does it handle edge cases gracefully?
- User Experience: Is it easy to use and understand?

BONUS POINTS:
- Add expense categories validation
- Implement summary statistics
- Add date parsing for past expenses
- Create expense visualization features
- Add data export functionality

RESOURCES PROVIDED:
- jumbled.py: Contains all the implementation code blocks
- .env.example: Environment variables template
- README.md: Setup and usage instructions
- requirements.txt: Required Python packages

SUBMISSION:
Submit your completed main.py file that implements all the required functionality
using the code blocks from jumbled.py.

Good luck! 🚀
"""
