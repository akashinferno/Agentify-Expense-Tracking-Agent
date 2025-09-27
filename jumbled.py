import json
import google.generativeai as genai
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os
from dotenv import load_dotenv

# AI-Powered Expense Tracker - Simple Implementation Code Blocks
# This file contains core functions matching the main.py functionality

# Load environment variables
load_dotenv()

# Configuration constants
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
SHEET_ID = os.getenv('SHEET_ID')
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# =============================================================================
# CODE BLOCK 1: AI NATURAL LANGUAGE PROCESSING
# =============================================================================

def parse_with_ai_and_fallback(model, user_input_text):
    """
    Complete AI parsing with JSON extraction, validation, and fallback.
    Handles all aspects of converting natural language to structured data.
    """
    # Ask AI to parse the expense
    prompt = f"""
    Parse: "{user_input_text}"
    Return only JSON: {{"items": [{{"item": "name", "amount": 100, "category": "Food"}}]}}
    Categories: Food, Transport, Shopping, Other
    """
    
    response = model.generate_content(prompt)
    json_text = response.text.strip()
    
    # Clean up response
    if '```json' in json_text:
        json_text = json_text.split('```json')[1].split('```')[0]
    if '```' in json_text:
        json_text = json_text.split('```')[1]
    
    return json.loads(json_text.strip())

# =============================================================================
# CODE BLOCK 2: VALIDATION AND ERROR HANDLING
# =============================================================================

def validate_and_check_system():
    """
    Simple validation matching main.py functionality.
    Checks if API keys are configured properly.
    """
    # Check if keys are set
    if not GEMINI_API_KEY:
        print("❌ Please set your GEMINI_API_KEY in the .env file!")
        return False
    
    if not SHEET_ID or SHEET_ID == "your_sheet_id_here":
        print("❌ Please set your SHEET_ID in the .env file!")
        print("Create a Google Sheet and copy its ID from the URL")
        return False
    
    return True

# =============================================================================
# CODE BLOCK 3: DATA INSERTION AND MANAGEMENT
# =============================================================================

def insert_data_with_setup(sheets_service, expense_data):
    """
    Data insertion matching main.py add_to_sheet functionality.
    Adds expenses to the sheet with simple row management.
    """
    # Setup headers if they don't exist
    setup_sheet_with_formatting(sheets_service)
    
    # Get next empty row
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=SHEET_ID, 
        range='A:A'
    ).execute()
    next_row = len(result.get('values', [])) + 1
    
    # Add each item (matching main.py logic)
    for item in expense_data['items']:
        row = [[
            "Today",  # Date
            item['item'],  # Item name
            item['amount'],  # Amount
            item['category']  # Category
        ]]
        
        sheets_service.spreadsheets().values().update(
            spreadsheetId=SHEET_ID,
            range=f'A{next_row}:D{next_row}',
            valueInputOption='USER_ENTERED',
            body={'values': row}
        ).execute()
        
        print(f"Added: {item['item']} - ₹{item['amount']}")
        next_row += 1

# =============================================================================
# CODE BLOCK 4: MAIN EXECUTION WITH STATISTICS
# =============================================================================

def run_main_with_stats():
    """
    Main execution matching main.py functionality.
    Simple expense tracking without extra features.
    """
    print("Simple Expense Tracker")
    print("----------------------")
    
    # Check if keys are set (matches main.py validation)
    if not validate_and_check_system():
        return
    
    model, service = initialize_system()  # This function is defined AFTER this one!
    print("✅ Setup complete!")
    print("Type expenses like: lunch 200, cab 150")
    
    while True:
        expense = input("\nExpense (or 'quit'): ")
        
        if expense.lower() == 'quit':
            break
        
        try:
            parsed = parse_with_ai_and_fallback(model, expense)
            insert_data_with_setup(service, parsed)
            total = sum(item['amount'] for item in parsed['items'])
            print(f"Added total: ₹{total}")
        except Exception as e:
            print(f"Error: {e}")

# =============================================================================
# CODE BLOCK 5: SHEET FORMATTING AND HEADERS
# =============================================================================

def setup_sheet_with_formatting(sheets_service):
    """
    Sheet header setup matching main.py setup_sheet_headers functionality.
    Simple header creation with total formula.
    """
    # Check if headers exist
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=SHEET_ID, 
        range='A1:F1'
    ).execute()
    
    if not result.get('values'):
        # Add headers and total cell (matches main.py)
        headers = [
            ['Date', 'Item', 'Amount', 'Category', 'TOTAL:', '=SUM(C:C)']
        ]
        
        sheets_service.spreadsheets().values().update(
            spreadsheetId=SHEET_ID,
            range='A1:F1',
            valueInputOption='USER_ENTERED',
            body={'values': headers}
        ).execute()
        print("✅ Added headers with total formula")

# =============================================================================
# CODE BLOCK 6: SYSTEM INITIALIZATION - AI + SHEETS
# =============================================================================

def initialize_system():
    """
    System setup matching main.py setup() functionality.
    Initializes Gemini AI and Google Sheets service.
    """
    # Setup Gemini (matches main.py)
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
    
    # Setup Google Sheets (matches main.py)
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', 
            ['https://www.googleapis.com/auth/spreadsheets']
        )
        creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    service = build('sheets', 'v4', credentials=creds)
    return model, service

if __name__ == "__main__":
    run_main_with_stats()
