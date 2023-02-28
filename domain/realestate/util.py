import PublicDataReader as pdr
from PublicDataReader import TransactionPrice
import sqlite3
import datetime
from config import settings
# from database import SessionLocal
# from models import Apt
from math import ceil

service_key = settings.DATA_GO_KR_SERVICE_KEY
api = TransactionPrice(service_key)
sigungu_name = "강릉시"
code = pdr.code_bdong()
c = code.loc[(code['시군구명'].str.contains(sigungu_name, na=False)) &
        (code['읍면동명'].isna())]

# 데이터 가져오기
def get_data(params):
    df = api.get_data(**params)
    return df

# df sql로 저장
def to_sql_gubun(df, table, con):
    df.to_sql(
        name=table,
        con=con,
        if_exists='append',
        index=False,
        index_label=None,
        chunksize=None,
        dtype=None
    )

class YearMonth:
    def __init__(self, _range):
        self.__n = 6
        self.__range = _range
        self.yms = self.__get_period()
        self.now_yms = self.__get_period()[-self.__n:]
        # self.__db = SessionLocal()
    def __get_period(self):
        now = datetime.datetime.now().strftime('%Y%m')
        period = []
        year = int(now)//100
        month = int(now)%100
        for i in range(self.__range):
            period.append(str(year)+str(month).zfill(2))
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        period.sort(reverse=False)
        print(period)
        return period
    # def __get_yms(self):
        #     yms = self.__get_period()[:-self.__n]
    #     yms_db = self.__get_yms_db()
    #     yms = list(set(yms) - set(yms_db))
    #     yms.sort(reverse=False)
    #     return yms
    # def __get_yms_db(self):
    #     db = self.__db
    #     yms_db = []
    #     for i in db.query(Apt.년, Apt.월).all():
    #         ym = str(i[0]) + str(i[1]).zfill(2)
    #         if ym not in yms_db:
    #             yms_db.append(ym)
    #     return yms_db
class YeartoYms:
    def __init__(self, _year):
        self.year = _year
        self.yms = self.yeartoyms()
    def yeartoyms(self):
        now = datetime.datetime.now().strftime('%Y%m')
        return now


def main():

    yms = YearMonth(12, 200)
    gubun = '아파트'
    trade_type = '매매'
    table = 'apt'
    now_yms = yms.now_yms
    now_yms.sort(reverse=False)
    start_year_month = yms.now_yms[0]
    end_year_month = yms.now_yms[-1]
    print(start_year_month, end_year_month)
    con = sqlite3.connect("d:/lang/jupyter-notebook/realestate/realestate.db")
    for year_month in yms.yms:
        df = get_data(gubun=gubun, 
                    trade_type=trade_type, 
                    year_month=year_month)
        to_sql_gubun(df=df, table=table, con=con)
        print(year_month, '....Done')

    df = api.get_data(
        property_type=gubun,
        trade_type=trade_type,
        sigungu_code='42150',
        # year_month=year_month,
        start_year_month=start_year_month,
        end_year_month=end_year_month,
        verbose=True,
    )
    
    return df  


if __name__ == '__main__':
    df = main()
    print(df.tail)