from sqlalchemy import (Column, Integer, String, Float, Table, MetaData)
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base



from database import Base


class Apt(Base):
    __tablename__ = "apt"

    id = Column(Integer, primary_key=True)
    지역코드 = Column(String)
    도로명 = Column(String)
    법정동 = Column(String)
    지번 = Column(String)
    아파트 = Column(String)
    건축년도 = Column(Integer)
    층 = Column(Integer)
    전용면적 = Column(Float)
    년 = Column(Integer)
    월 = Column(Integer)
    일 = Column(Integer)
    거래금액 = Column(Integer)
    도로명건물본번호코드 = Column(String)
    도로명건물부번호코드 = Column(String)
    도로명시군구코드 = Column(String)
    도로명일련번호코드 = Column(String)
    도로명지상지하코드 = Column(String)
    도로명코드 = Column(String)
    법정동본번코드 = Column(String)
    법정동부번코드 = Column(String)
    법정동시군구코드 = Column(String)
    법정동읍면동코드 = Column(String)
    법정동지번코드 = Column(String)
    일련번호 = Column(String)
    거래유형 = Column(String)
    중개사소재지 = Column(String, nullable=True)
    해제사유발생일 = Column(String, nullable=True)
    해제여부 = Column(String, nullable=True)