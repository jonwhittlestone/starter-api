
import os
from pydantic import BaseSettings

from .dyna import settings


class CoreSettings(BaseSettings):
    DEBUG: bool = False
    SERVICE_NAME: str = "starter-api"
    SERVICE_LABEL: str = f"starter-api {settings.current_env}"
    SERVICE_VERSION = "1.0.0"
    SERVICE_DESCRIPTION = "A no-brainer starter for a dockerised FastAPI app"
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "")
    APP_HOST: str = "0.0.0.0"  # nosec
    APP_PORT: int = 8000

class ModuleSettings(BaseSettings):
    ...

class Sett(CoreSettings, ModuleSettings):
    pass


setts = Sett()