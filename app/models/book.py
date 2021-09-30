from core.database import Base
from sqlalchemy import Column, Integer, String

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
