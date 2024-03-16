import boto3
import pandas as pd
from io import StringIO

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the Lambda event trigger
    print(event)
    srcbucket = event['Records'][0]['s3']['bucket']['name']
    srckey = event['Records'][0]['s3']['object']['key']
    tgtbucket='doordash-target-zn-vj'
    tgtkey='2024-03-09-processed_output.json'

    # Use boto3 to get the CSV file from S3
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=srcbucket, Key=srckey)
    file_content = response["Body"].read().decode('utf-8')

    # Read the content using pandas
    data = pd.read_csv(StringIO(file_content))
    print(data)
    #Filter records where status is "delivered"
    delivered_df = data[data['status'] == 'delivered']
    print('Delivered Data :n', delivered_df)

    # write filtered data frame to target S3
    filetoupload=StringIO()
    delivered_df.to_json(filetoupload)

    response = s3_client.put_object(Body=filetoupload.getvalue(), Bucket=tgtbucket, Key=tgtkey, )
    print(response)

