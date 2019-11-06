from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

connection_string = "postgres://postgres:brightspace@team-db.cezw9lbsfclc.us-west-2.rds.amazonaws.com:5432/postgres"

engine = create_engine(connection_string, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'users'
    iduser = Column(Integer, primary_key=True) #make sure no column names end with the letters "id"
    username = Column(String)
    userpassword = Column(String)