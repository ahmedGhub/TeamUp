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

# class Team_Student_Assoc(Base):
#     __tablename__ = "team_student_assoc"
#     idteam = Column(Integer, ForeignKey('teams.idteam'), primary_key=True)
#     idprof = Column(Integer, ForeignKey('teams.idprof'), primary_key=True)
#     idcourse = Column(String, ForeignKey('teams.idcourse'), primary_key=True)
#     iduser = Column(Integer, ForeignKey('users.iduser'), primary_key=True)


association_table = Table('team_student_assoc', Base.metadata,
    Column('idteam', Integer, ForeignKey('teams.idteam')),
    Column('iduser', Integer, ForeignKey('users.iduser'))
)

# liason_request_association_table = Table('req_lias_assoc', Base.metadata,
#     Column('idreq', Integer, ForeignKey('teams.idteam')),
#     Column('idliason', Integer, ForeignKey('users.iduser'))
# )

# req_assoc_table = Table('team_join_requests', Base.metadata, Column(), Column())

class Team_Join_Request(Base):
    __tablename__ = "team_join_requests"
    id = Column('idrequest',Integer , primary_key=True)
    idteam = Column(Integer, ForeignKey('teams.idteam'))
    idstudent = Column(Integer, ForeignKey('users.iduser'))
    idliason = Column(Integer, ForeignKey('users.iduser'))
    email = Column(String)

class User(Base):
    __tablename__ = 'users'
    id = Column('iduser', Integer, primary_key=True)
    # iduser = Column( Integer) #make sure no column names end with the letters "id"
    username = Column(String)
    userpassword = Column(String)
    usert = Column(String)
    teams = relationship('Team', secondary=association_table)
    requests = relationship('Team_Join_Request', foreign_keys='[Team_Join_Request.idliason]')
    email = Column(String)

class Course(Base):
	__tablename__ = 'courses'
	idprof = Column(Integer, ForeignKey('users.iduser'), primary_key=True)
	idcourse = Column(String, primary_key=True)
	minstudents = Column(Integer)
	maxstudents = Column(Integer)
	deadline = Column(Integer)	
 
class Team(Base):
    __tablename__ = 'teams'
    idliason=Column(Integer)
    id = Column('idteam', Integer, primary_key=True)
    idprof = Column(Integer)
    idcourse = Column(String)
    teamname= Column(String)
    created_at = Column(Integer)
    users = relationship(User, secondary=association_table)
    members_count = Column(Integer)
    # requests = relationship('Team_Join_Request')

# class Team_Join_Request(Base):
#     __tablename__ = "team_join_requests"
#     idteam = Column(Integer, ForeignKey('teams.idteam'), primary_key=True)
#     idprof = Column(Integer, ForeignKey('teams.idprof'), primary_key=True)
#     idcourse = Column(String, ForeignKey('teams.idcourse'), primary_key=True)
#     # team = relationship('Team')
#     idstudent = Column(Integer, ForeignKey('users.iduser'), primary_key=True)

class Email(Base):
	__tablename__ = "dummy"
	email = Column(String, primary_key=True)
	idteam = Column(Integer, primary_key=True)
	idcourse = Column(String)

class Team_Student_Assoc(Base):
	__tablename__ = "team_student_assoc"
	__table_args__ = {'extend_existing': True}
	idteam = Column(Integer, ForeignKey('teams.idteam'), primary_key=True)
	iduser = Column(Integer, ForeignKey('users.iduser'), primary_key=True)
