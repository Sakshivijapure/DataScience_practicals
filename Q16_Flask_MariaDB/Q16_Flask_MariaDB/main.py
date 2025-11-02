# # from fastapi import FastAPI, HTTPException
# # from pydantic import BaseModel
# # from typing import List
# # from sqlalchemy import create_engine, Column, Integer, String, Float
# # from sqlalchemy.orm import sessionmaker, declarative_base

# # # -----------------------------
# # # Database setup (MariaDB official driver)
# # # -----------------------------
# # DB_USER = "course_user"
# # DB_PASSWORD = "password123"
# # DB_HOST = "localhost"
# # DB_NAME = "coursesdb"

# # # Using MariaDB official driver
# # DATABASE_URL = f"mariadb+mariadbconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# # engine = create_engine(DATABASE_URL, echo=True)
# # SessionLocal = sessionmaker(bind=engine)
# # Base = declarative_base()

# # # -----------------------------
# # # DB Model
# # # -----------------------------
# # class Course(Base):
# #     __tablename__ = "courses"

# #     id = Column(Integer, primary_key=True, autoincrement=True)
# #     course_name = Column(String(255))
# #     provider = Column(String(255))
# #     skills = Column(String(255))
# #     rating = Column(Float)
# #     total_reviews = Column(Integer)
# #     level = Column(String(50))
# #     duration = Column(String(50))

# # Base.metadata.create_all(bind=engine)

# # # -----------------------------
# # # Pydantic model for API
# # # -----------------------------
# # class CourseSchema(BaseModel):
# #     id: int
# #     course_name: str
# #     provider: str
# #     skills: str
# #     rating: float
# #     total_reviews: int
# #     level: str
# #     duration: str

# #     class Config:
# #         orm_mode = True

# # # -----------------------------
# # # FastAPI app
# # # -----------------------------
# # app = FastAPI(title="Courses API with MariaDB")

# # @app.get("/courses", response_model=List[CourseSchema])
# # def get_courses():
# #     db = SessionLocal()
# #     courses = db.query(Course).all()
# #     db.close()
# #     if not courses:
# #         raise HTTPException(status_code=404, detail="No courses found")
# #     return courses

# # @app.get("/courses/{course_id}", response_model=CourseSchema)
# # def get_course(course_id: int):
# #     db = SessionLocal()
# #     course = db.query(Course).filter(Course.id == course_id).first()
# #     db.close()
# #     if not course:
# #         raise HTTPException(status_code=404, detail="Course not found")
# #     return course

# from fastapi import FastAPI, HTTPException, Depends
# from sqlalchemy import Column, Integer, String, Float, create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base, Session
# from pydantic import BaseModel

# DATABASE_URL = "mariadb+mariadbconnector://course_user:password123@localhost:3306/coursesdb"

# engine = create_engine(DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # ---------------- Models ----------------
# class Course(Base):
#     __tablename__ = "courses"
#     id = Column(Integer, primary_key=True, index=True)
#     course_name = Column(String(255), unique=True, nullable=False)
#     provider = Column(String(100))
#     skills = Column(String(255))
#     rating = Column(Float)
#     total_reviews = Column(Integer)
#     level = Column(String(50))
#     duration = Column(String(50))

# Base.metadata.create_all(bind=engine)

# # ---------------- Schemas ----------------
# class CourseCreate(BaseModel):
#     course_name: str
#     provider: str
#     skills: str | None = ""
#     rating: float | None = 0.0
#     total_reviews: int | None = 0
#     level: str | None = ""
#     duration: str | None = ""

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # ---------------- App ----------------
# app = FastAPI()

# # Get all courses
# @app.get("/courses")
# def read_courses(db: Session = Depends(get_db)):
#     return db.query(Course).all()

# # Get course by id
# @app.get("/courses/{course_id}")
# def read_course(course_id: int, db: Session = Depends(get_db)):
#     course = db.query(Course).filter(Course.id == course_id).first()
#     if not course:
#         raise HTTPException(status_code=404, detail="Course not found")
#     return course

# # Create course
# @app.post("/courses")
# def create_course(course: CourseCreate, db: Session = Depends(get_db)):
#     db_course = Course(**course.dict())
#     db.add(db_course)
#     db.commit()
#     db.refresh(db_course)
#     return db_course

# # Update course
# @app.put("/courses/{course_id}")
# def update_course(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
#     db_course = db.query(Course).filter(Course.id == course_id).first()
#     if not db_course:
#         raise HTTPException(status_code=404, detail="Course not found")
#     for key, value in course.dict().items():
#         setattr(db_course, key, value)
#     db.commit()
#     db.refresh(db_course)
#     return db_course

# # Delete course
# @app.delete("/courses/{course_id}")
# def delete_course(course_id: int, db: Session = Depends(get_db)):
#     db_course = db.query(Course).filter(Course.id == course_id).first()
#     if not db_course:
#         raise HTTPException(status_code=404, detail="Course not found")
#     db.delete(db_course)
#     db.commit()
#     return {"detail": "Course deleted"}

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel

DATABASE_URL = "mariadb+mariadbconnector://course_user:password123@localhost:3306/coursesdb"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ---------------- Models ----------------
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String(255), unique=True, nullable=False)
    provider = Column(String(100))
    skills = Column(String(255))
    rating = Column(Float)
    total_reviews = Column(Integer)
    level = Column(String(50))
    duration = Column(String(50))

Base.metadata.create_all(bind=engine)

# ---------------- Schemas ----------------
class CourseCreate(BaseModel):
    course_name: str
    provider: str
    skills: str | None = ""
    rating: float | None = 0.0
    total_reviews: int | None = 0
    level: str | None = ""
    duration: str | None = ""

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- App ----------------
app = FastAPI()

# Get all courses
@app.get("/courses")
def read_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

# Get course by id
@app.get("/courses/{course_id}")
def read_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

# Create course
@app.post("/courses")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# Update course
@app.put("/courses/{course_id}")
def update_course(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in course.dict().items():
        setattr(db_course, key, value)
    db.commit()
    db.refresh(db_course)
    return db_course

# Delete course
@app.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(db_course)
    db.commit()
    return {"detail": "Course deleted"}
