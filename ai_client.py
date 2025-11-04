import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

class AIClient:
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def chat(self, message, context=""):
        prompt = [
            {"role": "system", "content": (
                "Bạn là trợ lý AI của Đại học, chuyên giúp sinh viên giải bài tập và giải thích dễ hiểu."
                "Luôn viết câu trả lời có cấu trúc rõ ràng, gọn gàng, chuyên nghiệp và dùng markdown."
            )},
            {"role": "user", "content": message}
        ]
        if context:
            prompt.insert(1, {"role": "assistant", "content": context})

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=prompt
        )
        return response["choices"][0]["message"]["content"]

    def analyze_image(self, file_path):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Bạn là trợ lý AI giúp sinh viên giải bài tập từ hình ảnh."},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Hãy đọc và giải thích bài tập trong hình ảnh này."},
                        {"type": "image_url", "image_url": f"file://{file_path}"}
                    ]
                }
            ]
        )
        return response["choices"][0]["message"]["content"]
