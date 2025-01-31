from google.cloud import bigquery
from google.oauth2 import service_account
import type_enforced


@type_enforced.Enforcer
class pythonbq:
    def __init__(
        self,
        key_path: [None, str] = None,
        project: [None, str] = None,
        legacy_sql: bool = False,
        **kwargs,
    ):
        """
        Function:

        - Initializes a pythonbq object

        Optional:

        - `key_path`:
            - Type: str
            - What: The path to the key file
            - Note: If not provided, the default key file (specified for google.cloud) is used
        - `project`:
            - Type: str
            - What: The project to use
            - Note: If not provided, no project is used. You can specify the project in the query.
        - `legacy_sql`:
            - Type: bool
            - What: Whether to use legacy SQL
            - Note: If not provided, the default is False
            - Note: If True, this overrides the `use_legacy_sql` setting in the kwarg `default_query_job_config` (if provided)
        - `**kwargs`:
            - Type: kwargs
            - What: Additional keyword arguments to pass to the bigquery.Client (for client initialization)
            - See Additional keyword arguments to pass to the bigquery.Client (for client initialization):
                - https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client
                - https://github.com/googleapis/python-bigquery/blob/main/google/cloud/bigquery/client.py


        Examples:

        ```
        from pythonbq import pythonbq
        bq = pythonbq(
            key_path='path/to/key.json',
            project="my-project",
            legacy_sql=True
        )
        ```
        """
        if key_path is not None:
            kwargs["credentials"] = (
                service_account.Credentials.from_service_account_file(
                    key_path,
                    scopes=["https://www.googleapis.com/auth/cloud-platform"],
                )
            )
        if legacy_sql:
            if "default_query_job_config" not in kwargs:
                kwargs["default_query_job_config"] = {}
            kwargs["default_query_job_config"]["use_legacy_sql"] = legacy_sql
        self.kwargs = kwargs
        self.project_kwargs = {} if project is None else {"project": project}
        self.client = bigquery.Client(**kwargs)

    def query(self, sql: str, out_type: str = "dict", **kwargs):
        """
        Function:

        - Returns the results of a query

        Required:

        - `sql`:
            - Type: str
            - What: The SQL query to run
        - `out_type`:
            - Type: str
            - Options: [`dict`,`list`,`raw`]
            - What: The output type
            - Note: If not provided, the default is `dict`
            - Note:
                - If `dict`, the output is a list of dictionaries.
                - If `list`, the output is a list of lists (with the first list being a header row).
                - If `raw`, the output is a list of lists (with no header row).
        - `**kwargs`:
            - Type: kwargs
            - What: Additional keyword arguments to pass to the bigquery.Client.query (for query execution)
            - See
                - https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client#google_cloud_bigquery_client_Client_query
                - https://github.com/googleapis/python-bigquery/blob/main/google/cloud/bigquery/query.py
                - https://github.com/googleapis/python-bigquery/blob/main/google/cloud/bigquery/job/query.py

        Examples:
        ```
        from pythonbq import pythonbq
        bq = pythonbq(
            key_path='path/to/key.json',
            project="my-project"
        )

        out = bq.query(
            sql="SELECT * FROM `my-project.my_dataset.my_table`",
            out_type="dict"
        )
        ```
        """
        kwargs.update(self.project_kwargs)
        query_job = self.client.query(sql, **kwargs)
        out = query_job.result()
        fields = [i.name for i in out.schema]
        if out_type == "dict":
            return [dict(zip(fields, i)) for i in out]
        elif out_type == "list":
            return [fields] + [list(i) for i in out]
        elif out_type == "raw":
            return [list(i) for i in out]
        else:
            raise Exception(
                "query `out_type` must be one of the following: [`dict`,`list`,`raw`]"
            )
