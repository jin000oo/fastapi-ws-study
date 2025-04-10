from fastapi import FastAPI

app = FastAPI()

@app.get("/")   # 127.0.0.1:8000
def home():
    return "Hello FastAPI"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
    