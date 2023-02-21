import datetime
from pydantic import BaseModel, validator, EmailStr
from typing import List, Optional


class Apt(BaseModel):
    id: int
    # 지역코드: str
    도로명: str
    법정동: str
    지번: str
    아파트: str
    건축년도: int
    층: int
    전용면적: float 
    년: int
    월: int
    일: int
    거래금액: int
    # 도로명건물본번호코드: str
    # 도로명건물부번호코드: str
    # 도로명시군구코드: str
    # 도로명일련번호코드: str
    # 도로명지상지하코드: str
    # 도로명코드: str
    # 법정동본번코드: str
    # 법정동부번코드: str
    # 법정동시군구코드: str
    # 법정동읍면동코드: str
    # 법정동지번코드: str
    # 일련번호: str
    # 거래유형: str | None = None
    # 중개사소재지: str | None = None
    # 해제사유발생일: str | None = None
    # 해제여부: str | None = None
    
    class Config:
        orm_mode = True
        
class AptList(BaseModel):
    # apt_names: list = []
    dongs: list = []
    apts: list[Apt] = []
    
class YearMonths(BaseModel):
    yms_dn: list[str] = None