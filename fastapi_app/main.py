from fastapi import FastAPI
from routes import health, item

app = FastAPI()


app.include_router(health.route)
app.include_router(item.route)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7000)