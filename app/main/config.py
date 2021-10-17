import os

class Config(object):
    user_name = 'username'
    password = 'password'

    db = 'dev database connection string'

    LOG_EMAIL_TOADDRS = ['your_email@example.com']
    LOG_EMAIL_FROMADDR = 'from_email@example.com'
    LOG_EMAIL_SUBJECT = ['Error Logs']
    LOG_EMAIL_MAILHOST = ("gmail host ", "port")

    LOG_FILE_PATH = "path to log files"
    LOG_ERROR_NAME = "name of error file"
    LOG_INFO_NAME = "name of info file"
    LOG_WHEN = "midnight" # rotates every day
    LOG_INTERVAL = 1
    LOG_BACKUP_COUNT = 10

class DevelopmentConfig(Config):
    DEBUG = False
    LOG_EMAIL_FROMADDR = "dev_email@example.com"

class TestingConfig(Config):
    DEBUG=False
    LOG_EMAIL_FROMADDR = "test_email@example.com"
    db = 'test database connection string'

class ProductionConfig(Config):
    DEBUG=False
    LOG_EMAIL_FROMADDR = 'prod_email@example.com'
    db = 'production database connection string'

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)