import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an AI safety evaluator.

Analyze the text and return ONLY valid JSON with:

harm_score (float 0-1)
bias_score (float 0-1)
fairness_score (float 0-1)
confidence (float 0-1)
reason (string)
human_review (YES or NO)

No explanation outside JSON.
"""

def evaluate_with_ai(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ]
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        print("JSON parsing error.")
        return None
