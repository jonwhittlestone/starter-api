import os

from pathlib import Path

from dynaconf import LazySettings


common_settings = "settings.toml"  # all configurations
secrets_settings = ".secrets.toml"  # secrets only
logger_configuration = "cfg_logger.json"  # loguru  settings

PROJECT_PATH = Path(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
WORKSPACE = Path(os.path.dirname(os.path.dirname(__file__)))

LOGGER_CONF_PATH = Path(os.path.join(os.path.dirname(__file__), logger_configuration))
SETTINGS_PATH = Path(os.path.join(os.path.dirname(__file__), common_settings))
SECRETS_PATH = Path(os.path.join(os.path.dirname(__file__), secrets_settings))

settings = LazySettings(
    warn_dynaconf_global_settings=False,
    environments=True,
    settings_files=[SETTINGS_PATH, SECRETS_PATH],
    load_dotenv=True,
    ignore_unknown_envvars=True,
    envvar_prefix=False,
)
