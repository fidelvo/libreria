class Config:
  SECRET_KEY = 'lyJEgS$2^Cd_'

class DevelopmentConfig(Config):
  DEBUG = True
  MYSQL_HOST = 'localhost'
  MYSQL_USER = 'root'
  MYSQL_PASSWORD = ''
  MYSQL_DB = 'db_libreria'

config = {
  'development' : DevelopmentConfig,
  'default' : DevelopmentConfig
}