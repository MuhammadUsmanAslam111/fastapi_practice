
from database import SessionLocal,model
from schemas import UserCreate, UserResponse
from fastapi import FastAPI, Query, Depends, APIRouter
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

app = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = model.User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse(db_user)


@app.get("/users/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(model.User).all()
    return users

  
@app.get("/about")
def get_about():
    return {"message": "This is a sample FastAPI application."}