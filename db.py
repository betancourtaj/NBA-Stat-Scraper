# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date
from base import Base


engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)

Base = declarative_base()
 
########################################################################

class Teams(Base):
    """"""
    __tablename__ = "team"
 
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    position = Column(String)
    team = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, first_name, last_name, position, team, date):
        """"""
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team

class Player(Base):
    """"""
    __tablename__ = "players"
 
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    position = Column(String)
    team = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, first_name, last_name, position, team, date):
        """"""
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team

class Match(Base):
    """"""
    __tablename__ = "match"
 
    id = Column(Integer, primary_key=True)
    first_team = Column(String)
    second_team = Column(String)
    first_team_score = Column(String)
    second_team_score = Column(String)
    player_id = Column(Integer, ForeignKey('playes.id'))
 
    #----------------------------------------------------------------------
    def __init__(self, first_team, second_team, first_team_score, second_team_score):
        """"""
        self.first_team = first_team
        self.second_team = second_team
        self.first_team_score = first_team_score
        self.second_team_score = second_team_score
 
# create tables
Base.metadata.create_all(engine)

player1 = Player("chad", 'SF', 'celtics', datetime(1977,3,12))

session.add(player1)

session.commit()
