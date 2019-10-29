Pixelator
==========
Python wrapper for easy use of big query

Features
--------

- Easily pull big query data from python

Setup
----------

Make sure you have Python 3.6.x (or higher) installed on your system. You can download it [here](https://www.python.org/downloads/).

### Installation

```
pip install pythonbq
```

### Getting Started
1) Import pythonbq into your project
```
from pythonbq import pythonbq
```

2) Set the location of your `bq_key_path` (App engine default service account json object):
  - If you do not have one, you can generate one [here](https://console.cloud.google.com/apis/credentials/serviceaccountkey)
  - Example:
    ```
    bq_key_path='path/to/bq/key.json'
    ```

3) Set the `project_id` you wish to query from:
  - These can be found in your [Google Cloud Console](https://console.cloud.google.com)
  - Example:
    ```
    project_id='myGoogleProjectID'
    ```

4) Optional - Set a Big Query `dialect`:
  - `standard` (Default)
  - `legacy`
  - Example:
    ```
    dialect='legacy'
    ```

5) Initialize your project object:
  - Example:
    ```
    myProject=pythonbq(
      bq_key_path='path/to/bq/key.json',
      project_id='myGoogleProjectID'
    )
    ```

6) Write some `sql` code:
  - Example:
    ```py
    sql="""select * from myProjectTable"""
    ```

7) Run a query:
  - Example:
    ```
    output=myProject.query(sql="""select * from myProjectTable""")
    ```

### Output Data
- Output from the `query` function is stored as a pandas object
  - It comes with all of the standard pandas features baked in
  - For those not familiar with pandas, the output can be converted directly to:
    - List of Dictionary Objects -> `myProject.query(sql="...").to_dict('records')`
    - Numpy -> `myProject.query(sql="...").output.values()`



### Full Example
```py
from pythonbq import pythonbq
myProject=pythonbq(
  bq_key_path='path/to/bq/key.json',
  project_id='myGoogleProjectID'
)
output=myProject.query(sql="""select * from myProjectTable""")
```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)
