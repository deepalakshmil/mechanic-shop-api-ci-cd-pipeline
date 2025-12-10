import os

class DevelopmentConfig:
    #"""Used when running locally on your laptop."""
    SQLALCHEMY_DATABASE_URI ='mysql+mysqlconnector://root:welcomesql1@localhost/mechanic_shop_db'  ## local database
    DEBUG = True
    # Caching
    CACHE_TYPE = 'SimpleCache' ## Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT=300  ## 5 mintues once cache could be refresh
    SQLALCHEMY_TRACK_MODIFICATIONS = True ## to suppress a warning message


class TestingConfig:
    #"""Used for pytest + unit tests."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'  ## which is a lightweight database suitable for testing the creation and manipulation of data.
    DEBUG = True
    CACHE_TYPE = 'SimpleCache'

class ProductionConfig:
    # """Used on Render or real server."""

    # Render automatically provides DATABASE_URL environment variable 
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    print("ProductionConfig.SQLALCHEMY_DATABASE_URI:",os.environ.get("SQLALCHEMY_DATABASE_URI"))
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI','mysql+mysqlconnector://root:welcomesql1@localhost/mechanic_shop_db')
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:welcomesql1@localhost/mechanic_shop_db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = False






