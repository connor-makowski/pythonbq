from pythonbq import pythonbq
from decouple import Config, RepositoryEnv
import json

env = Config(RepositoryEnv("./private/.env"))

print("\n===============\nPrivate Data Test Failures:\n===============")

# Test 1: Open Data
query = env.get("PRIVATE_QUERY")
project = env.get("PRIVATE_PROJECT")
expected_output = json.loads(env.get("PRIVATE_EXPECTED_OUTPUT"))

myProject = pythonbq(
    key_path="./private/bq_key.json",
    project=project,
)
output = myProject.query(sql=query)

if output != expected_output:
    print("Private Data Test Failed!")
