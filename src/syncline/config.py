from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SYNCLINE_", env_file=".env")

    source_token: str
    target_token: str
    api_key: str
    migrations_dir: str = "migrations"
