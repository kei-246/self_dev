import json
import boto3
import os
from datetime import datetime

s3 = boto3.client("s3")

def save_to_s3(title, content):
    bucket = os.environ["S3_BUCKET"]
    key = f"articles/{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    data = {
        "title": title,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(data, ensure_ascii=False),
        ContentType="application/json",
    )

    return key
