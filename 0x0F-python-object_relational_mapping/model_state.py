#!/usr/bin/python3
"""
Now using ORM for abstraction
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('mysql+mysqldb://root:root@localhost:3306/ \
                      hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    """
    Defines a state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


"""
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
session.close()
"""
