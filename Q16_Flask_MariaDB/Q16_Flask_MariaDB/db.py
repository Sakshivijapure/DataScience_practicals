# db.py
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "mariadb+mariadbconnector://course_user:password123@localhost:3306/coursesdb"


engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    course_name = Column(String(255))
    provider = Column(String(100))
    skills = Column(String(500))
    rating = Column(Float)
    total_reviews = Column(Integer)
    level = Column(String(50))
    duration = Column(String(50))

Base.metadata.create_all(bind=engine)
