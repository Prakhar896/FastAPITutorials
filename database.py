from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://mainuser:mu2025@127.0.0.1:5432/FastQuizTutorial"

print('Database URL:', URL_DATABASE)  # Debugging line to check the database URL

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()