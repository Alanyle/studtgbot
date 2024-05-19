from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
def user():
    Base = declarative_base()
    engine = create_engine('sqlite:///tg.db')
    class User(Base):
        __tablename__ = 'users'
        __table_args__ = {'extend_existing': True}
        cmd = Column(String)
        typ = Column(String)
        town = Column(String)
        cfg = Column(String)
        id = Column(Integer, primary_key=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)  # creating table users if not exists
    return User, session