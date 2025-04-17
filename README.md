## 1. Python 개발환경 구축
    python -m venv venv                # venv 가상환경 생성
    .\venv\Scripts\activate            # venv 가상환경 접속
    pip install -r requirements.txt    # venv 가상환경에 라이브러리 설치
    pip list                           # venv 가상환경 라이브러리 목록
 
 

 ## 2. 형상관리도구(Github)
1) 로컬(노트북)
    git init                                                    # (.git) git 프로젝트 생성
        --- Github에서 Repository 생성
        --- git remote add origin "github repository URL"
        --- git remote -v                                       # git remote 연결 상태 확인
        --- git branch -M main                                  # Master -> Main 변경
    git status                                                  # git의 버전관리 상태
    git add [파일명]                                            # [파일명]을 앞으로 Tracking 하세요!
    git add .                                                   # 전체 파일을 Tracking 하세요!
    git commit -m "버전1"                                       # "버전1" 버전을 로컬에 생성
    git push origin main                                        # 글로벌 main 보랜치에 내가 만든 버전들을 업로드

2) 글로벌(Github)
        --- Github에서 Repository 생성
    git clone "github repository URL"
    git status                                                  # git의 버전관리 상태
    git add [파일명]                                            # [파일명]을 앞으로 Tracking 하세요!
    git add .                                                   # 전체 파일을 Tracking 하세요!
    git commit -m "버전1"                                       # "버전1" 버전을 로컬에 생성
    git push origin main                                        # 글로벌 main 보랜치에 내가 만든 버전들을 업로드