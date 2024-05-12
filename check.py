from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///tg.db')
Base.metadata.create_all(engine)

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
def check(u_id):
    data = session.get(User, u_id)
    print(u_id)
    if data != None:
        return True
    else:
        return 'Вас нет в базе! Чтобы использовать команды, сначала добавьтесь в неё!'