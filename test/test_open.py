from pythonbq import pythonbq

print("\n===============\nOpen Data Test Failures:\n===============")

# Test 1: Open Data
query = """
WITH ranked_names AS (
    SELECT name, SUM(number) as total FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = "TX"
    GROUP BY name
    ORDER BY total DESC
    LIMIT 5
)
SELECT name FROM ranked_names
"""

myProject = pythonbq(
    key_path="./private/bq_key.json",
)
output = myProject.query(sql=query)

if output != [
    {"name": "James"},
    {"name": "John"},
    {"name": "Michael"},
    {"name": "Robert"},
    {"name": "David"},
]:
    print("Open Data Test Failed!")

print("\n===============\nData Structure Test Failures:\n===============")
output = myProject.query(sql=query, out_type="list")
if output != [
    ["name"],
    ["James"],
    ["John"],
    ["Michael"],
    ["Robert"],
    ["David"],
]:
    print("Data Structure (list) Test Failed!")

output = myProject.query(sql=query, out_type="raw")
if output != [["James"], ["John"], ["Michael"], ["Robert"], ["David"]]:
    print("Data Structure (raw) Test Failed!")
