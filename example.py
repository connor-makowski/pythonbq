from pythonbq import pythonbq

myProject=pythonbq(
  key_path='./keys/bq_key.json',
  project='my-project',
  legacy_sql=False
)
output=myProject.query(sql="""SELECT * FROM `my_table`""")
