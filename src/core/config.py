import os
import google.auth # type: ignore
from google.cloud import bigquery
from openai import OpenAI

class ConfigBigQuery:
    """
    Configures a BigQuery client using the default Google Cloud credentials.
    This class is used to set up the necessary BigQuery client for interacting with BigQuery in the application.
    """
    def __init__(self):    
        self.credentials, self.project_id = google.auth.default()
        self.client = bigquery.Client(project=self.project_id, credentials=self.credentials)

class ConfigOpenAI:
    """
    Configures an OpenAI client using the OPENAI_API_KEY environment variable.
    This class is used to set up the necessary OpenAI client for interacting with the OpenAI API in the application.
    """
    def __init__(self):
        self.open_ai_api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.open_ai_api_key)

if __name__=="__main__":
    ConfigBigQuery()
    ConfigOpenAI()
