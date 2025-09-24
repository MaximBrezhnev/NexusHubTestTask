from fastapi import APIRouter, status

from task1.schemas import MessageSchema, ClassifiedMessageSchema
from task1.service import MessagesService

messages_router = APIRouter(prefix="/messages")

@messages_router.post(
    path="/classify_message",
    status_code=status.HTTP_200_OK
)
async def classify_message(
    message: MessageSchema,
) -> ClassifiedMessageSchema:
    return await MessagesService.classify_message(
        message=message,
    )