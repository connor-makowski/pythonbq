from pythonbq import pythonbq
myProject=pythonbq(
  bq_key_path='path/to/bq/key.json',
  project_id='myGoogleProjectID'
)
output=myProject.query(sql="""select * from myProjectTable""")
