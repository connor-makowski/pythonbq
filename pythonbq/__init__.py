"""
# PythonBQ
[![PyPI version](https://badge.fury.io/py/pythonbq.svg)](https://badge.fury.io/py/pythonbq)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python wrapper for easy use of big query

## Features

- Easily pull big query data from python

## Setup

Make sure you have Python 3.7.x (or higher) installed on your system. You can download it [here](https://www.python.org/downloads/).

### Installation

```
pip install pythonbq
```

### Example
```
from pythonbq import pythonbq
myProject=pythonbq(
  bq_key_path='path/to/bq/key.json',
  project_id='myGoogleProjectID',
  legacy_sql=False
)
output=myProject.query(sql='''select * from myProjectTable''')
```

### Documentation for pythonbq Functions

https://connor-makowski.github.io/pythonbq/pythonbq.html

### Output Data
- Output from the `query` function is returned as a list of dictionaries
  - This can be modified by specifying the argument `out_type` in your `.query()`
    - `dict`: list of dictionaries
    - `list`: list of lists (header as the first row)
    - `raw`: list of lists (with no header row)
    - EG:
      ```
      output=myProject.query(sql='''select * from myProjectTable''', out_type='list')
      ```
- EG: 
  ```
  query = '''
      SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013`
      WHERE state = "TX"
      LIMIT 5
  '''

  myProject = pythonbq(
      key_path='./private/bq_key.json',
  )
  output = myProject.query(sql=query)
  # output = [{'name': 'Mary'}, {'name': 'Roberta'}, {'name': 'Marguerite'}, {'name': 'Katie'}, {'name': 'Eunice'}]
  ```"""
from .pythonbq import pythonbq
