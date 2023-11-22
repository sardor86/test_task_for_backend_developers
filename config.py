from dataclasses import dataclass

from environs import Env


@dataclass
class Django:
    secret_key: str
    debug: bool


@dataclass
class DataBase:
    host: str
    port: int
    user: str
    password: str
    db_name: str


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
                      host=env.str('DB_HOST'),
                      port=env.int('DB_PORT'),
                      user=env.str('DB_USER'),
                      password=env.str('DB_PASS'),
                      db_name=env.str('DB_NAME')
                  )
              )
