from fastapi import FastAPI

app = FastAPI()

@app.get("/")   # 127.0.0.1:8000
def home():
    return "Hello FastAPI"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",
                reload=True,                # 코드 변경시 서버로 바로 적용
                host="0.0.0.0",             # 0.0.0.0 외부 접속 허용
                port=8000)                  # 서버 포트를 8000번 사용
                                            #  ㄴ AWS EC2 인바운드 규칙 고려 