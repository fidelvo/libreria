class Config:
  SECRET_KEY = 'lyJEgS$2^Cd_'

class DevelopmentConfig(Config):
  DEBUG = True

config = {
  'development' : DevelopmentConfig,
  'default' : DevelopmentConfig
}