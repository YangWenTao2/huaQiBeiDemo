HOST = 'localhost'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'ygwt010825'
DATABASE = 'dbtest'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

