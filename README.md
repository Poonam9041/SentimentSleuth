# PSSentimentApp

Small Flask app that uses Azure Text Analytics to analyze sentiment.

Getting started (Windows PowerShell)

1. Create a virtual environment and activate it

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install requirements

```powershell
pip install -r requirements.txt
```

3. Set Azure environment variables (temporary for current session)

```powershell
$env:AZURE_TEXT_ANALYTICS_ENDPOINT = "https://<your-resource-name>.cognitiveservices.azure.com/"
$env:AZURE_TEXT_ANALYTICS_KEY = "<your-key>"
```

Alternatively, copy `.env.example` to `.env` and use a tool like `python-dotenv` or set system environment variables.

4. Run the app

```powershell
python app.py
```

5. Git

- Initialize local repo and commit (this repository contains no Azure secrets).
- To publish to GitHub, create a remote repository and run:

```powershell
git remote add origin https://github.com/youruser/yourrepo.git
git branch -M main
git push -u origin main
```

If you have the GitHub CLI (`gh`) configured you can create and push in one step:

```powershell
gh repo create youruser/yourrepo --public --source=. --push
```

Security note: Do not commit your Azure keys. Use environment variables or a secrets manager.
