import sqlite3
import sqlalchemy
from sqlalchemy.orm import Session
from pandas import DataFrame
from databases.realestate import database
from databases.realestate.models import Apt


def get_apt_list(db: Session, _min:int, _max:int, _sort:str):
    apts = db.query(Apt).filter((
        Apt.년 * 100 + Apt.월 > _min) & (Apt.년 * 100 + Apt.월 <= _max)
    )
    if _sort == 'date':
        apts = apts.order_by(Apt.년.desc(), Apt.월.desc(), Apt.일.desc(), Apt.법정동,Apt.아파트).all()
    
    if _sort == 'price':
        apts = apts.order_by(Apt.거래금액.desc(), Apt.년.desc(), Apt.월.desc(), Apt.일.desc(), Apt.법정동,Apt.아파트).all()
    
    if _sort == 'area':
        apts = apts.order_by(Apt.전용면적.desc(), Apt.년.desc(), Apt.월.desc(), Apt.일.desc(), Apt.법정동,Apt.아파트).all()
    
    if _sort == 'construction':
        apts = apts.order_by(Apt.건축년도.desc(), Apt.년.desc(), Apt.월.desc(), Apt.일.desc(), Apt.법정동,Apt.아파트).all()
    
    return apts


# df sql로 저장
def df_to_sql(db: Session, df: DataFrame, table: str):
    db.bulk_insert_mappings(Apt, df.to_dict(orient="records"))
    db.commit()

def get_yms_list(db:Session):
        yms_db = []
        for i in db.query(Apt.년, Apt.월).all():
            ym = str(i[0]) + str(i[1]).zfill(2)
            if ym not in yms_db:
                yms_db.append(ym)
        return yms_db

def del_yms(db:Session, yms:list):
    # print(yms)
    q = []
    for ym in yms:
        y = int(ym[:4])
        m = int(ym[4:])
        q.append(sqlalchemy.and_(Apt.년 == y, Apt.월 == m))
    q = sqlalchemy.or_(*q)
    apts = db.query(Apt).filter(q).delete(synchronize_session='fetch')
    db.commit()
    # return get_yms_list(db)
    # synchronize_session=evaluate
    # 파이썬에 생성된 쿼리를 곧바로 평가해서 세션으로부터 제거되어야 할 객체를 
    # 결정한다. evaluate는 기본값이고 효율적이지만, 견고하지 않고 복잡한 쿼리는
    # evaluate될 수 없다. 만약 쿼리를 evaluate할 수 없다면, 
    # sqlalchemy.orm.evaluator.UnevaluatableError를 발생시킨다.

    # synchronize_session=fetch
    # 삭제되기 전에 select 쿼리를 수행하고 해당 결과를 사용해서 어떤 객체들이 
    # 세션에서 삭제되어야 할지 결정한다. 덜 효율적이지만 유효한 쿼리를 다룰 수 
    # 있게 된다.

    # synchronize_session=False
    # 세션 갱신을 시도하지 않기 때문에 매우 효율적이다. 그러나 삭제한 후에 
    # 세션을 사용하려고 하면 부정확한 결과를 얻을 수 있다.
    
    
    