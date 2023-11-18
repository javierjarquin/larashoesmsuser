from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from confg.connection import Base


class Session(Base):
    __tablename__ = 'session'
    
    id           = Column(Integer, primary_key=True, index=True)
    userId       = Column(Integer, ForeignKey('user.id'), nullable=False)
    creationDate = Column(DateTime, nullable=False)
    ip           = Column(String(10), nullable=False)
    description  = Column(String(300))
    
    def __init__(self, userId=None, creationDate=None, ip="", description=""):
        self.userId = userId
        self.creationDate = creationDate
        self.ip = ip
        self.description = description
