from fastapi import status, HTTPException


class UnacceptableLLMAPIResponse(HTTPException):
    def __init__(self, exc: str):
        super().__init__(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"API LLM вернул недопустимый ответ, что привело к ошибке: {exc}."
        )