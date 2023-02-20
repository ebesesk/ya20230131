from fastapi import APIRouter, HTTPException, Depends, status, Request
from sqlalchemy.orm import Session

from . import schema
from databases.realestate.database import get_db
from . import crud
from . import util

router =APIRouter()


@router.get("/dbupdate", response_model=schema.YearMonths)
def get_list(db: Session=Depends(get_db)):
    yms = util.YearMonth(100)   # 100 개월치 날자 리스트 만들기
    crud.del_yms(db, yms.now_yms)   # 최근 6개월 데이터 삭제하기
    yms_db = crud.get_yms_list(db)  # db저장된 날짜 리스트 불러오기
    yms_dn = list(set(yms.yms) - set(yms_db))   # DB 저장된 날짜 삭제
    yms_dn.sort()                               # 다운받을 날짜 정렬
    params = {                                  # 다운받을 params 
        'property_type': '아파트',
        'trade_type': '매매',
        'sigungu_code': '42150',
        'year_month': None,
        'start_year_month': yms_dn[0],
        'end_year_month': yms_dn[-1],
    }
    df = util.get_data(params)                # 자료 다운받기
    crud.df_to_sql(db=db, df=df, table='apt') # 자료 DB에 저장
    
    return {"yms_dn": yms_dn}