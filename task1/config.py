from pydantic_settings import BaseSettings, SettingsConfigDict

from task1 import constants


class Settings(BaseSettings):
    GROQ_API_KEY: str

    model_config = SettingsConfigDict(env_file=constants.ENV_FILE)


settings = Settings()