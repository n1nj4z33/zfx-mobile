from dynaconf import Dynaconf

from config_validators import validators

settings = Dynaconf(
    environments=True,
    settings_files=[
        "settings.toml",
    ],
    validators=validators,
)
