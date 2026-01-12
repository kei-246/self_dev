from services.post_generator import generate_article
from services.s3_client import save_to_s3
from services.dynamodb_client import save_title
from services.rss_publisher import update_rss

def lambda_handler(event, context):
    title, content = generate_article()

    s3_key = save_to_s3(title, content)
    save_title(s3_key, title)
    update_rss(title, s3_key)

    return {
        "statusCode": 200,
        "body": f"success: {title}"
    }
