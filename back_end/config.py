HOST = 'rm-bp13c38ecy79tdunvbo.mysql.rds.aliyuncs.com'
PORT = '3306'
USERNAME = 'hqb1'
PASSWORD = 'Nj1902520'
DATABASE = 'hqb_data'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

