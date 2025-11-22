from flask import Flask
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os

app = Flask(__name__, template_folder="templates")

# Load Azure credentials from environment variables
endpoint = os.environ.get("AZURE_TEXT_ANALYTICS_ENDPOINT")
key = os.environ.get("AZURE_TEXT_ANALYTICS_KEY")
if not endpoint or not key:
    raise RuntimeError(
        "Azure credentials not found. Set AZURE_TEXT_ANALYTICS_ENDPOINT and AZURE_TEXT_ANALYTICS_KEY environment variables."
    )

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Import routes to register them on the app
from . import routes  # noqa: E402,F401
