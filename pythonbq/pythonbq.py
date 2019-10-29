import os
import pandas_gbq
from google.cloud import bigquery
import google.cloud

class pythonbq:
    def __init__(self, bq_key_path, project_id, dialect='standard'):
        self.credentials=google.oauth2.service_account.Credentials.from_service_account_file(bq_key_path)
        self.project_id=project_id
        self.dialect=dialect

    def query(self, sql):
        return pandas_gbq.read_gbq(sql, project_id=self.project_id, credentials=self.credentials, dialect=self.dialect)
