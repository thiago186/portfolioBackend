from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import computed_field

load_dotenv()

class Settings(BaseSettings):
    debug: bool = False
    mongodb_user: str
    mongodb_password: str
    mongodb_port: int = 27017
    delete_password: str

    @computed_field
    def mongodb_uri(self) -> str:
        return f"mongodb://{self.mongodb_user}:{self.mongodb_password}@localhost:{self.mongodb_port}/"

settings = Settings()
