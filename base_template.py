from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://user:password@localhost/Restaurant')#User is the username and pass is password
Session = sessionmaker(bind=engine)
Base = declarative_base()