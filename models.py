from sqlalchemy import (Column, Integer, String, Text, DateTime, 
                        ForeignKey, Boolean, Date, Table, MetaData,
                        PrimaryKeyConstraint, UniqueConstraint)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base


manga_voter = Table(
    'manga_voter',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('manga_id', Integer, ForeignKey('manga.id'), primary_key=True)
)

video_dislike = Table(
    'video_dislike',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('video_id', Integer, ForeignKey('video.id'), primary_key=True)
)

video_voter = Table(
    'video_voter', 
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('video_id', Integer, ForeignKey('video.id'), primary_key=True)
)


question_voter = Table(
    'question_voter',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('question_id', Integer, ForeignKey('question.id'), primary_key=True)
)

answer_voter = Table(
    'answer_voter',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('answer_id', Integer, ForeignKey('answer.id'), primary_key=True)
)

class Worked(Base):
    __tablename__='worked'
    
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    note = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", backref="worked_users")
    wage = Column(Integer, nullable=True)
    __table_args__ = (
        UniqueConstraint('year', 'month', 'day', 'user_id'),
    )

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="question_users")
    modify_date = Column(DateTime, nullable=True)
    voter = relationship('User', secondary=question_voter, backref='question_voters')


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="answer_users")
    modify_date = Column(DateTime, nullable=True)
    voter = relationship('User', secondary=answer_voter, backref='answer_voters')


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    

class Manga(Base):
    __tablename__ = "manga"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    # folder = Column(String, nullable=True)
    # page = Column(Integer, nullable=True)
    # images = Column(Text, nullable=True)
    tag = Column(Text, nullable=True)
    page = Column(Integer)
    created_date = Column(DateTime, nullable=True)
    voter = relationship('User', secondary=manga_voter, backref='manga_voters')

class Video(Base):
    __tablename__ = "video"
    
    id = Column(Integer, primary_key=True, index=True)
    dbid = Column(String, unique=True, nullable=False, index=True)
    width = Column(Integer)
    height = Column(Integer)
    showtime = Column(Integer)
    bitrate = Column(Integer)
    filesize = Column(Integer)
    cdate = Column(DateTime)
    
    display_quality = Column(String)
    
    country = Column(String)
    face = Column(String)
    look = Column(String)
    age = Column(String)
    pussy = Column(String)
    etc = Column(String)
    
    school_uniform = Column(Boolean)
    hip = Column(Boolean)
    group = Column(Boolean)
    pregnant = Column(Boolean)
    conversation = Column(Boolean)
    lesbian = Column(Boolean)
    ani = Column(Boolean)
    oral = Column(Boolean)
    masturbation = Column(Boolean)
    massage = Column(Boolean)
    uniform = Column(Boolean)
    family = Column(Boolean)
    
    ad_start = Column(Integer)
    ad_finish = Column(Integer)
    star = Column(Integer)
    
    date_posted = Column(Date)
    date_modified = Column(Date)
    voter = relationship('User', secondary=video_voter, backref='video_voters')
    dislike = relationship('User', secondary=video_dislike, backref='video_dislike')