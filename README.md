# Agentify-Expense-Tracking-Agent


## Google Sheets Expense Tracker Agent
This project implements an AI-powered agent that automates expense tracking using natural language input. Users can type expenses in plain English, and the system automatically parses, categorizes, and logs them into Google Sheets.

## Features

- **Natural Language Processing**: Parse expenses like "lunch ₹200, cab ₹150, gave my friend 300"
- **AI-Powered Categorization**: Automatically categorizes expenses using LLM
- **Google Sheets Integration**: Direct logging to Google Sheets with real-time totals
- **Dynamic Calculations**: Running totals and summary calculations
- **Simple Terminal Interface**: Easy-to-use command-line interface

## Setup Instructions

### 🚀 1. Clone & Setup

```bash
# Clone the repo
git clone https://github.com/akashinferno/Agentify-Expense-Tracking-Agent.git
cd Expense-Tracking-Agent

# Create virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```



### ☁️ 2. Google Cloud Project & Sheets API Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **Select Project** → **New Project** → name it `ExpenseTrackerAI`
3. After it's created, select it
4. Go to **APIs & Services** → **Library**:
   - Enable **Google Sheets API**
   
### 🧑‍💻 3. Configure OAuth Consent Screen
1. Go to **APIs & Services** → **OAuth consent screen**
2. Set **User Type** = **External** (works fine for personal Gmail testing)
3. Fill in **App name** and **Support email**
4. Scroll to **Test Users** → **Add Users**
5. Add your Gmail (example):
   ```
   urpersonalmail@gmail.com
   ```
6. Save

### 🔐 4. Create OAuth Credentials
1. Go to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **OAuth client ID**
3. Choose **Desktop App**
4. Name it `ExpenseTrackerClient`
5. Download JSON → rename it to:
   ```
   credentials.json
   ```
6. Place it in the same folder as `main.py`

### 🔑 5. Setup Gemini API
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click **Get API Key** and copy it
3. Add it to your `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 🔓 6. Authorize & Generate Token
1. On first run, the script will open a browser for login
2. Log in with your Gmail → approve permissions
3. A `token.pickle` file will be saved → so you don't need to log in every time

### 📊 7. Setup Google Sheet
1. Open [Google Sheets](https://sheets.google.com)
2. Create a new blank sheet
3. Copy the Sheet ID from the URL:
   ```bash
   https://docs.google.com/spreadsheets/d/1A2B3C4D5E6F7G8H9I0J/edit#gid=0
   👉 Sheet ID = 1A2B3C4D5E6F7G8H9I0J
   ```
4. Add it to your `.env` file:
   ```env
   SHEET_ID=1A2B3C4D5E6F7G8H9I0J
   ```
5. (Optional) Add headers manually in your Google Sheet:
   ```
   Date | Item | Amount | Category | TOTAL: | =SUM(C:C)
   ```

### ▶️ 8. Run the Expense Tracker
```bash
python main.py
```

Example input:
```
Lunch 200, sent 50 to friend
```
Data will be parsed by Gemini and stored in your Google Sheet.

## Usage Examples

### Natural Language Input Examples:
- `lunch ₹200, coffee ₹50`
- `cab fare ₹150 today`
- `grocery shopping ₹800, medicines ₹300`
- `movie tickets ₹500, dinner ₹400 yesterday`


## Project Structure

```
expense-sheets-tracker/
├── main.py              # Main application
├── .env                 # Environment variables (API keys)
├── credentials.json     # Google API credentials (you need to add this)
├── token.pickle        # OAuth token (auto-generated)
└── README.md           # This file
```

## How It Works

1. **Input Processing**: User enters expense in natural language
2. **AI Parsing**: Gemini AI extracts structured data (item, amount, category, date)
3. **Sheet Integration**: Data is automatically added to Google Sheets
4. **Dynamic Calculations**: Running totals and summaries are updated automatically

## Categories

The system automatically categorizes expenses into:
- Food
- Transportation  
- Shopping
- Entertainment
- Health
- Bills
- Travel
- Other

## Security Notes

- Keep your API keys secure and never commit them to version control
- The `.env` file is ignored by git
- OAuth tokens are stored locally in `token.pickle`
