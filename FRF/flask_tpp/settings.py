import datetime


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "hgerwhtrejrtejhrtehtre"

    PERMANENT_SESSION_LIFETIME = datetime.timedelta(14)

    dbinfo = {
        "ENGINE": "sqlite",
        "DRIVER": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "NAME": ""
    }


class TestConfig(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "",
        "DRIVER": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "NAME": ""
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagineConfig(Config):
    dbinfo = {
        "ENGINE": "",
        "DRIVER": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "NAME": ""
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "",
        "DRIVER": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "NAME": ""
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flask_tpp"
    }
    # dbinfo = {
    #     "ENGINE": "sqlite",
    #     "DRIVER": "",
    #     "USER": "",
    #     "PASSWORD": "",
    #     "HOST": "",
    #     "PORT": "",
    #     "NAME": ""
    # }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagineConfig,
    "product": ProductConfig,
    "default": DevelopConfig,
}
