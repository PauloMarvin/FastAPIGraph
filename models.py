from database import Base
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSONB

class Graph(Base):
    __tablename__ = "graph"
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(JSONB)
