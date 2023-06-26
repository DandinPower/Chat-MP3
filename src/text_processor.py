import os
import openai
from tqdm import tqdm
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API')

class TextProcessor:
    @staticmethod
    def asked_question_by_text(question, text):
        userContent = f'\"Transcript\":{text}'
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": question},
                {"role": "user", "content": userContent}
            ],
            max_tokens = 2048,
        )
        answer = completion.choices[0].message.content
        return answer