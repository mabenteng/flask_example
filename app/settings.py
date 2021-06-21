import os



BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dbinfo={
    "user":"root",
    "pwd":"root",
    "type":"mysql",
    "driver":"pymysql",
    "host":"localhost",
    "port":"3306",
    "db":"flask"
}


def get_db_uri(dbinfo):
    return "{}+{}://{}:{}@{}:{}/{}".format(dbinfo["type"],dbinfo["driver"],dbinfo['user'],dbinfo["pwd"],dbinfo["host"],dbinfo["port"],dbinfo["db"])

class Config: #SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)
    SECRET_KEY="dkjfkjdlafjaefjkreealfkaip"
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False



envs={
    "develop":Config
}


