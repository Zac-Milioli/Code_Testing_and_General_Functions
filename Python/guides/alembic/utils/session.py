from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from contextlib import contextmanager

from models.table_registry import table_registry

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))
table_registry.metadata.create_all(engine)

@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    except:
        session.rollback()
    finally:
        session.close()
