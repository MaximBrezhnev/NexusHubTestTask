from pydantic_settings import BaseSettings, SettingsConfigDict

from task2 import constants


class Settings(BaseSettings):
    API_ID: int
    API_HASH: str
    PHONE: str
    TARGET_CHAT: str

    model_config = SettingsConfigDict(env_file=constants.ENV_FILE)

settings = Settings()