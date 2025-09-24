from fastapi import FastAPI

from task1.router import messages_router

app = FastAPI(title="NexusHubTestTask")

app.include_router(messages_router)
