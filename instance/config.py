import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    DATABASE_NAME = 'stackoverflow_db'
    

class DevelopmentConfig(Config):
    """Configuration fro Development."""
    DEBUG = True
    DATABASE_NAME = 'stackoverflow_db'
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"
    JWT_BLACKLIST_ENABLED = False
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']

class TestingConfig(Config):
    """Configuration for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_NAME = "test_data"
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

class StagingConfig(Config):
    """Configuration for Staging."""
    DEBUG = False
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

class ProductionConfig(Config):
    """Configration for Production"""
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = "gvhbjnkmsjbknmlnjk"

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'staging' : StagingConfig,
    'production' : ProductionConfig
}