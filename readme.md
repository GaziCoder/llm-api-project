# Gemini API Project

A simple Python application that sends prompts to Google Gemini and displays the generated response.

## Setup

Install dependencies:

```powershell
pip install google-genai python-dotenv
```

Create a `.env` file from `.env.example` and add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

## Running the Application

Navigate to the project directory and run:

```powershell
cd llm-api-project
python llm_api.py
```

or run directly from root:

```powershell
python llm-api-project/llm_api.py
```