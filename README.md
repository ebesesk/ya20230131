### python 가상환경 + express 설정
#### python venv + npm
python -m venv .venv  
source .venv/bin/activate  
pip install --upgrade pip  
#### 가상환경 내에서 nodeenv를 병합 독립적인 npm 사용가능
pip install nodeenv  
nodeenv --version  
nodeenv -p   활성화된 가상환경에 독립적인 node 환경 추가  




#### svelte 설치 실행
npm create vite@latest frontend ---template svelte  
cd frontend  
npm install  
jsconfig.json  "checkJs": false  # 자바스크립트 타입 체크 설정 끄기  
npm run dev  


#### alembic 설치
pip install alembic  
초기화  alembic init migrations  
설정  alembic.ini sqlalchemy.url = sqlite:///./myapi.db  
      migrations/env.py import models  target_metadata=models.Base.metadata  
리비전파일 생성 alembic revision --autogenerate  
리비전파일 실행 alembic upgrade head  


#### svelte 라우터
npm install svelte-spa-router  
routes/Home.svelte 작성  
src/lib/Counter.svelte 삭제 lib/ap.js 작성 fetch 함수 같이 사용  

#### npm i qs
application/x-www-form-urlencoded 형식에 맞게금 변화는 역할  

#### .env
frontend/.env VITE_SERVER_URL = http://192.168.0.43:7443  

#### 답변 등록 API
api명: 답변등록  
url: /api/answer/create/{question_id}  
요청방법:  post  
설명:  질문(question_id)에 대한 답변은 등록한다.  


#### 부트스트랩 설치
npm install bootstrap  
frontend/src/main.js  
import 'bootstrap/dist/css/bootstrap.min.css'  
import 'bootstrap/dist/js/bootstrap.min.js'  


#### 질문 등록 API 명세
API명: 질문 등록  
URL: /api/question/create  
요청방법: post  

#### 질문 등록 API 입력항목
-subject 등록할 질문의 제목  
-content 등록할 질문의 내용  

#### 질문 등록 API 출력 항목
없음  

#### 질문데이터 생성

#### python 셀

from database import SessionLocal  
from models import Question  
from datetiem import datetime  

db = SessionLocal()  
for i in range(300):  
      q = Question(subject="테스트입니다:[%03d]"%i, content='내용무',  create_data=datetime.  now())  
      db.add(q)  
db.commit()  


## 스토어 변수 생성하기  
frontend/src/lib/store.js  
import { writable } from 'svelte/store'  
export const page = writable(0) # 초기값 0  
이전 페이지가 없으면 비활성   {page <= && 'disable'}  
이전 페이지 번호              page 1  
다음 페이지가 없으면 비활성   {page >= total_page 1 && 'disable'}  
다음 페이지 번호              page +1  
페이지 리스트 루프            {#each Array(total_page) as _, loop_page}  
현재 페이지와 같으면 활성화   {loop_page === page && 'active}  


##회원 가입


### 회원 모델
username    사용자이름(id)  
password    비밀번호  
email       이메일  

모델 작성후 alembic revision --autogenerate alembic upgrade head  

### API
API명:      회원가입  
URL:        /api/user/create  
요청방법:   post  
설명:       회원등록을 한다  

### 회원가입 API 입력 항목
username, password1(비밀번호) password2(비밀번호확인) email  

회원 가입 API 출력 항목  
없음  


### 로그인 API

#### 로그인 API 명세
API명       로그인  
URL         /api/user/login  
요청방법    post  
설명        로그인을 한다.  


#### 로그인 스키마

로그인 crud  
로그인 라우터  
로그인 API 테스트  


#### 로그인 화면 만들기
로그인 라우터 등록하기  
로그인 화면 작성하기  
fastapi 함수 작성하기  
http request 헤더 Content-type 을 application/json -> application/x-www-form-urlencoded 로   변환  
qs패키지 설치  
엑세스 토큰과 로그인 사용자명 저장하기  
내비게이션 바에 로그인 여부 표시하기  
로그아웃  

#### sqlite 버그패치 
[파일명: projects/myapi/database.py]  
from sqlalchemy import create_engine, MetaData  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker  
(... 생략 ...)  
Base = declarative_base()  
naming_convention = {  
    "ix": 'ix_%(column_0_label)s',  
    "uq": "uq_%(table_name)s_%(column_0_name)s",  
    "ck": "ck_%(table_name)s_%(column_0_name)s",  
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",  
    "pk": "pk_%(table_name)s"  
}  
Base.metadata = MetaData(naming_convention=naming_convention)  
(... 생략 ...)  
[파일명: projects/myapi/migrations/env.py]  
(... 생략 ...)  
def run_migrations_offline() -> None:  
   (... 생략 ...)  
    url = config.get_main_option("sqlalchemy.url")  
    context.configure(  
        url=url,  
        target_metadata=target_metadata,  
        literal_binds=True,  
        dialect_opts={"paramstyle": "named"},  
        render_as_batch=True,  
    )  
    (... 생략 ...)  
def run_migrations_online() -> None:  
    (... 생략 ...)  
    with connectable.connect() as connection:  
        context.configure(  
            connection=connection,  
            target_metadata=target_metadata,  
            render_as_batch=True,  
        )  

        (... 생략 ...)  



(myapi) c:/projects/myapi> alembic revision --autogenerate  
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.  
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.  
INFO  [alembic.autogenerate.compare] Detected added unique constraint 'uq_user_email' on '  ['email']'
INFO  [alembic.autogenerate.compare] Detected added unique constraint 'uq_user_username'   on '['username']'
  Generating /Users/pahkey/projects/myapi/migrations/versions/f77ce8f209c6_.py ...  done  
(myapi) c:/projects/myapi> alembic upgrade head            
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.  
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.  
INFO  [alembic.runtime.migration] Running upgrade 87416c9d163d -> f77ce8f209c6, empty   message
혹시 이 과정에서 오류가 발생할 경우에는 alembic stamp head 명령을 실행한 후에 다시 위의 과정을   반복해 보자.


#### 글쓴이 정보 가져오기  

1. 프론트엔드에서 로그인을 성공한 후에 엑세스 토큰을 저장
2. 백엔드 API 호출시 헤더 정보에 액세스 토큰을 포함하여 요청
3. 백엔드에서 액세스 토큰을 분석하여 사용자명 취득
4. 사용자명으로 사용자 조회


 질문 수정  

 질문수정 API 명세  
 API명:      질문수정  
 URL:        /api/question/update  
 요청방법:   put  
 설명        질문을 수정한다.  

 질문 수정 API 입력 항목  
 question_id:      수정할 질문의 고유번호  
 subject:          수정할 질문의 제목   
 content:          수정할 질문의 내용  

 질문 수정 API 출력 항목  
 없음  

 질문 수정 스키마  
 질문 수정 crud  
 질문 수정 라우터  
 질문 수정 버튼  
 질문 수정 화면  


### 질문 삭제

질문삭제 API 명세  
api명:      질문삭제  
url:        /api/question/delete   
요청방법:   delete  
설명:       질문을 삭제한다  

질문 삭제 API 입력항목  
question_id:    삭제할 질문의 고유번호  

질문 삭제 API 출력 항목  
없음  

질문 삭제 스키마  
질문 삭제 CRUD  
질문 삭제 라우터  

질문 삭제 버튼  
질문 삭제 확인  


# 답변 조회


답변 조회 API 명세  
API명:      답변조회  
URL:        /api/answer/detail  
요청방법:   get  
설명:       답변을 조회한다  
  
답변 수정 API 입력 항목  
answer_id 조회할 답변의 고유번호  
  
답변 수정 API 출력 항목  
ANSWER 스키마  
답변 조회 스키마  
답변 조회 CRUD  
답변 조회 라우터  
  
답변 수정  
답변 수정 API 명세  
API명:      답변수정  
URL:        /api/answer/update  
요청 방법:  put  
설명:       답변을 수정한다  

1. 답변 수정 스키마
2. 답변 수정 CRUD
3. 답변 수정 라우터
4. 답변 수정 버튼
5. 답변 수정 화면


답변 삭제  

답변 삭제 API 명세  
API명:      답변 삭제  
URL:        /api/answer/delete  
요청 방법:  delete  
설명:       답변을 삭제한다  

1. 답변 삭제 스키마
2. 답변 삭제 CRUD
3. 답변 삭제 라우터
4. 답변 삭제 버튼
5. 답변 삭제 확인


수정일시 표시하기  
Question, Answer 스키마 수정  
질문 상세 화면에 수정일시 표시  



