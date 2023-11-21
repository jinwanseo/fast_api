from fastapi import APIRouter, Depends
from users import user_service as userService
from common.database.db import get_db
from users.dtos.create_user import CreateUserInput
from sqlalchemy.orm import Session
from users.dtos.read_users import ReadUsersInput
from users.dtos.update_user import UpdateUserInput

app = APIRouter(prefix="/user")


@app.post("/create")
def createUser(
    user: CreateUserInput,
    db: Session = Depends(get_db),
):
    return userService.create_user(
        user,
        db,
    )


@app.get("/profile")
def getProfileByUserName(
    username: str,
    db: Session = Depends(get_db),
):
    return userService.get_by_name(
        username,
        db,
    )


@app.get("/profile/{userId}")
def getProfile(
    userId: int,
    db: Session = Depends(get_db),
):
    return userService.get_by_id(
        userId,
        db,
    )
