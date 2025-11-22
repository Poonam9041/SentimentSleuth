# SentimentSleuth

A Flask-based web application that analyzes text sentiment using **Microsoft Azure Text Analytics API**. Input any text or paragraph, and the app returns real-time sentiment classification (positive, negative, neutral, mixed).

## Features
- **Real-time sentiment analysis** via Azure Cognitive Services
- **Clean, responsive web UI** built with Flask and HTML/CSS
- **Secure credential management** using environment variables (no hardcoded secrets)
- **Modular package structure** for scalability and maintainability
- **CI/CD pipeline** with GitHub Actions (Python 3.9–3.11 testing, linting)

## Quick Start (Windows PowerShell)

### 1. Clone and set up environment
```powershell
git clone https://github.com/Poonam9041/SentimentSleuth.git
cd SentimentSleuth
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Configure Azure credentials
Copy `.env.example` to `.env` or set environment variables for the session:
```powershell
$env:AZURE_TEXT_ANALYTICS_ENDPOINT = "https://<your-resource-name>.cognitiveservices.azure.com/"
$env:AZURE_TEXT_ANALYTICS_KEY = "<your-api-key>"
```

### 3. Run the app
```powershell
python app.py
```
Visit `http://127.0.0.1:5000/` in your browser.

## Demo

![SentimentSleuth Demo](docs/screenshot.png)

*Add a screenshot or GIF of the app in action! See `docs/README.md` for instructions.*

## Project Structure
```
SentimentSleuth/
├── app.py                           # Flask entry point
├── pssentimentapp/
│   ├── __init__.py                  # App factory and Azure client setup
│   ├── routes.py                    # Route handlers
│   └── templates/
│       └── index.html               # Web UI
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variable template
├── .github/workflows/ci.yml         # GitHub Actions CI/CD
└── README.md                        # This file
```

## Security & Best Practices
- **Never commit Azure keys** — use environment variables or a secrets manager.
- **CI/CD integration** — tests and linting run automatically on push/PR.
- **Package-based architecture** — clean separation of concerns, easy to extend.

## Technologies Used
- **Framework**: Flask (Python web framework)
- **NLP**: Microsoft Azure Text Analytics
- **Frontend**: HTML5 + CSS3
- **CI/CD**: GitHub Actions
- **Version Control**: Git / GitHub

## Future Enhancements
- Add unit tests and pytest suite
- Deploy to Azure App Service or AWS Lambda
- Add support for batch sentiment analysis
- Build a REST API endpoint
- Add Swagger/OpenAPI documentation

## License
This project is part of IMT 598C (University of Washington).

## Contact
For questions or suggestions, reach out via GitHub Issues or contact [poonamsingh251@gmail.com](mailto:poonamsingh251@gmail.com).
