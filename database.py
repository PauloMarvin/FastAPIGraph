from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://admin:admin@postgresql:5432/fastapi", echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)


def create_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
