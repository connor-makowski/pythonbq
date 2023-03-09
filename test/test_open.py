from pythonbq import pythonbq

print("\n===============\nOpen Data Test Failures:\n===============")

# Test 1: Open Data
query = """
    SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = "TX"
    LIMIT 5
"""

myProject = pythonbq(
    key_path="./private/bq_key.json",
)
output = myProject.query(sql=query)
if output != [
    {"name": "Mary"},
    {"name": "Roberta"},
    {"name": "Marguerite"},
    {"name": "Katie"},
    {"name": "Eunice"},
]:
    print("Open Data Test Failed!")

print("\n===============\nData Structure Test Failures:\n===============")
output = myProject.query(sql=query, out_type="list")
if output != [
    ["name"],
    ["Mary"],
    ["Roberta"],
    ["Marguerite"],
    ["Katie"],
    ["Eunice"],
]:
    print("Data Structure (list) Test Failed!")
output = myProject.query(sql=query, out_type="raw")
if output != [["Mary"], ["Roberta"], ["Marguerite"], ["Katie"], ["Eunice"]]:
    print("Data Structure (raw) Test Failed!")
