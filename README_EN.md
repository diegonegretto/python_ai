# 🐍 PythonAI
[🇧🇷 Versão em Português](./README.md) | [🇺🇸 English Version](./README_EN.md)

A **Python** application that consumes the **Google Gemini API** to
answer natural language questions.\
The project follows **OOP best practices** and uses **environment
variables** to protect the API key.

------------------------------------------------------------------------

## 🚀 Requirements

-   Python **3.10+**\
-   Virtual environment set up (recommended)\
-   Dependencies installed via **pip**

------------------------------------------------------------------------

## 📦 Installation

Clone this repository:

``` bash
git clone https://github.com/diegonegretto/python_ai.git
cd python_ai
```

Create and activate a virtual environment:

``` bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

Install the dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🔑 API Key Configuration

Create a `.env` file in the project root based on the `.env.example`
template:

``` bash
cp .env.example .env
```

Open the `.env` file and insert your API key:

``` env
API_KEY=your_api_key_here
```

------------------------------------------------------------------------

## ▶️ Running the Application

To run the application:

``` bash
python main.py
```

You will see a terminal menu with options to interact with the AI.

------------------------------------------------------------------------

## 📂 Project Structure

    python_ai/
    │── ai_client.py      # PythonAI class that connects to the API
    │── main.py           # Application class with the main menu
    │── .env              # Contains your API key (DO NOT version)
    │── .env.example      # Template for environment variables
    │── .gitignore        # Ignores sensitive files
    │── requirements.txt  # Project dependencies

------------------------------------------------------------------------

## ⚠️ Important

-   Never share the **.env** file on GitHub.\
-   Use only **.env.example** to indicate the required variables.
