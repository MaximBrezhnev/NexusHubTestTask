import json

from fastapi import HTTPException, status
from openai import AsyncOpenAI

from task1 import constants
from task1.config import settings
from task1.exceptions import UnacceptableLLMAPIResponse
from task1.schemas import ClassifiedMessageSchema, MessageSchema


class MessagesService:
    @staticmethod
    async def classify_message(
        message: MessageSchema,
    ) -> ClassifiedMessageSchema:

        prompt = constants.PROMPT_TEMPLATE.format(
            bio=message.bio, text=message.text,
        )
        client = AsyncOpenAI(
            api_key=settings.GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

        try:
            response = await client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "Ты — строгий JSON-генератор."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.0
            )

            content = response.choices[0].message.content.strip()
            result = json.loads(content)

            return ClassifiedMessageSchema(
                lead=bool(result.get("lead"))
            )

        except Exception as e:
            raise UnacceptableLLMAPIResponse(exc=e) from None


