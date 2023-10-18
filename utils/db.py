from data.config import POSTGRES_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Sequence, Integer, String, BIGINT
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass


engine = create_engine(POSTGRES_URL)

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    full_name = Column(String)
    username = Column(String, unique=True)
    tg_id = Column(BIGINT, unique=True)


class RecordedUser(Base):
    __tablename__ = "recorded_users"
    id = Column(Integer, Sequence("recorded_user_id_seq"), primary_key=True)
    name = Column(String)
    tg_id = Column(BIGINT)
    phone = Column(String)
    choised_course = Column(String)
    choised_day = Column(String)
    choised_time = Column(String)


async def add_user(full_name, username, tg_id):
    user = User(full_name=full_name, username=username, tg_id=tg_id)
    session.add(user)
    session.commit()


async def record_user(name, tg_id, phone, choised_course, choised_day, choised_time):
    user = RecordedUser(name=name, tg_id=tg_id, phone=phone, choised_course=choised_course, choised_day=choised_day,
                        choised_time=choised_time)
    session.add(user)
    session.commit()


Base.metadata.create_all(engine)
