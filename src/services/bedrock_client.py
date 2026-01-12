import boto3
import json
import os

bedrock = boto3.client("bedrock-runtime")

def call_bedrock(prompt):
    model_id = os.environ["BEDROCK_MODEL"]

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4000,
        "messages": [{"role": "user", "content": prompt}]
    }

    res = bedrock.invoke_model(
        modelId=model_id,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json",
    )
    
    response_body = json.loads(res["body"].read())
    return response_body["content"][0]["text"]
