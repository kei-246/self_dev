from services.bedrock_client import call_bedrock
from utils.prompts import TITLE_PROMPT, ARTICLE_PROMPT

def generate_article():
    title = call_bedrock(TITLE_PROMPT).strip()
    article_prompt = ARTICLE_PROMPT.replace("{{TITLE}}", title)
    content = call_bedrock(article_prompt).strip()
    return title, content
