from sqlalchemy import Column, Integer, String
from confg.connection import Base

class User(Base):
    __tablename__ = 'user'
    
    id       = Column(Integer,      primary_key=True, index=True)
    name     = Column(String(100),  nullable=False)
    lastName = Column(String(150),  nullable=False)
    email    = Column(String(150),  nullable=False)
    phone    = Column(String(12),   nullable=False)
    login    = Column(String(100),  nullable=False, unique=True)
    password = Column(String(1000), nullable=False)
    rol      = Column(String(3),    nullable=False)
    
    def __init__(self, name="", lastName="", email="", phone="", login="", password="", rol=""):
        self.name     = name
        self.lastName = lastName
        self.email    = email
        self.phone    = phone
        self.login    = login
        self.password = password
        self.rol      = rol