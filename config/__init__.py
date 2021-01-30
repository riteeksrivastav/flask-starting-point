from os import environ, path
from dotenv import load_dotenv

class AppConfig:
    """Handle the configuration. Set the flask configuration from .evn file"""
    
    basedir = path.abspath(path.dirname(__file__))
    config_file_path = path.join(basedir, 'development.env')
    
    env = environ.get("ENV")
    config_file_path = ""
    if env == "TEST":
        config_file_path = path.join(basedir, 'test.env')
    else:
        config_file_path = path.join(basedir, 'development.env')
        
    load_dotenv(config_file_path)
    
    SQLALCHEMY_DATABASE_USERNAME= environ.get("SQLALCHEMY_DATABASE_USERNAME")
    SQLALCHEMY_DATABASE_PASSWORD= environ.get("SQLALCHEMY_DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_HOSTNAME= environ.get("SQLALCHEMY_DATABASE_HOSTNAME")
    SQLALCHEMY_DATABASE_PORT= environ.get("SQLALCHEMY_DATABASE_PORT")
    SQLALCHEMY_DATABASE_NAME= environ.get("SQLALCHEMY_DATABASE_NAME")

    SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@{host}:{port}/{db_name}".format(username = SQLALCHEMY_DATABASE_USERNAME, 
                                                                            password = SQLALCHEMY_DATABASE_PASSWORD,
                                                                            host = SQLALCHEMY_DATABASE_HOSTNAME,
                                                                            port = SQLALCHEMY_DATABASE_PORT,
                                                                            db_name = SQLALCHEMY_DATABASE_NAME
                                                                            )
    # These are the recommended values we are setting according to the sqlalchemy documentation. Ref: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    LOG_LEVEL=environ.get("LOG_LEVEL")