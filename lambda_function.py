import json
import requests
import pandas as pd

def lambda_handler(event, context):
    print("Event Data ->", event)
    response = requests.get("https://ww.google.com/")
    print(response.text)

    d={'col1': [1,2], 'col2':[3,4]}
    df=pd.DataFrame(data=d)
    print(df)
    print('demo completed')