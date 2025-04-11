import base64
import openai
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from PIL import Image
from io import BytesIO

openai.api_key = os.getenv("OPENAI_API_KEY")

class AnalyzeView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        height = request.data.get('height')
        weight = request.data.get('weight')
        image_data = request.data.get('image')

        # Process image (decode base64)
        if image_data:
            image_bytes = BytesIO(base64.b64decode(image_data))
            img = Image.open(image_bytes)

        prompt = f"使用者身高 {height} cm，體重 {weight} kg，請給予適合的穿搭建議。"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一位專業形象穿搭顧問"},
                {"role": "user", "content": prompt}
            ]
        )

        suggestion = response['choices'][0]['message']['content']
        return Response({"suggestion": suggestion})