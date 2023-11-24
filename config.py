from dataclasses import dataclass

from environs import Env


@dataclass
class Django:
    secret_key: str
    debug: bool


@dataclass
class DataBase:
    user: str
    password: str
    db_name: str
    host: str


@dataclass
class Config:
    django: Django
    db: DataBase


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
                  django=Django(
                      secret_key=env.str('SECRET_KEY'),
                      debug=env.bool('DEBUG')
                  ),
                  db=DataBase(
                      db_name=env.str('POSTGRES_DB'),
                      user=env.str('POSTGRES_USER'),
                      password=env.str('POSTGRES_PASSWORD'),
                      host=env.str('DB_HOST')
                  )
              )
