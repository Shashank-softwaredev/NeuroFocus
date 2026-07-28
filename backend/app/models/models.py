from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base


class HR(Base):
    __tablename__ = "hr"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Candidate(Base):
    __tablename__ = "candidate"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    trust_score = Column(Integer, default=100)
    interview_completed = Column(Boolean, default=False)