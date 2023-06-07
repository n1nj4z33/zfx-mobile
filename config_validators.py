from dynaconf import Validator

validators = [
    Validator("test_service_name", must_exist=True, env="default"),
]
