from fastapi import status, APIRouter

route = APIRouter()

@route.get("/")
def health():
    return {"status": status.HTTP_200_OK}