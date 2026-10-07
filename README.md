# MoodPilot

MoodPilot is a lightweight Streamlit app that helps a user understand their emotional state and identify one practical next step. It uses a custom prompt and OpenAI's language model to analyze a user's message, infer mood, and suggest an actionable response.

## Overview

This project is designed to turn a simple question like:

> "How am I feeling?"

into a more useful answer:

> "What should I do next?"

The app reads the user's input, identifies the primary mood, emotional intensity, possible thought pattern, likely need, blocker, and a single next action.

## Features

- Analyzes emotional tone and mood from freeform user text
- Identifies likely thought patterns and blockers
- Suggests one practical next action instead of generic advice
- Provides a simple, friendly Streamlit interface
- Built with Python, Streamlit, and LangChain

## Tech Stack

- Python 3.11+
- Streamlit
- LangChain
- LangChain OpenAI
- python-dotenv

## Project Structure

```text
Mood_Analyzer/
├── main.py              # Streamlit application entry point
├── system_prompt.py     # Prompt used for emotional analysis
├── pyproject.toml       # Python project metadata and dependencies
├── .python-version      # Local Python version pin
├── .gitignore           # Git ignore rules
├── uv.lock              # Dependency lock file
└── README.md            # Project documentation
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/prudhvic/Mood_Analyzer.git
cd Mood_Analyzer
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

Using `pip`:

```bash
pip install -U pip
pip install langchain langchain-openai python-dotenv streamlit
```

Or using `uv` (recommended if available):

```bash
uv sync
```

4. Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run the App

```bash
streamlit run main.py
```

Then open the local URL shown in the terminal, typically:

```text
http://localhost:8501
```

## How It Works

The app creates a chat prompt using the instructions defined in `system_prompt.py`, then sends the user's message to the configured OpenAI model. The model returns an analysis in a structured format with sections like:

- Mood
- What I Notice
- What You Probably Need
- Possible Blocker
- Your Next Move
- Why?

## Important Note

This app is intended for reflective emotional support and practical self-guidance. It is not a diagnosis tool and should not replace professional mental health care.

## License

This project does not currently specify a license in the repository metadata.

## Author

Created by prudhvic.
