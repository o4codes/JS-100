from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from schema.user import User
from services.user_services import UserServices
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "Welcome"}


@app.post("/api/v1/users", status_code=status.HTTP_201_CREATED, response_model=User)
async def signup(user: User):
    user_services = UserServices("DB/users.json")
    response = user_services.sign_up(user)
    if response:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "User created successfully", "data": user.dict()}
        )
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User already exists")
