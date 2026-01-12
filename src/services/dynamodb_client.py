import boto3
import os
from datetime import datetime

dynamodb = boto3.resource("dynamodb")

def save_title(key, title):
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    table.put_item(Item={
        "pk": key,
        "title": title,
        "createdAt": datetime.now().isoformat()
    })
