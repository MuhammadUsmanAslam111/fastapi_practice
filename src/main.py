from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from database import engine
import model
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
#creating THE APP INSTANCE
app = FastAPI()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creating the database tables
model.Base.metadata.create_all(bind=engine)

#i have created two pydantic models, one for creating a user 
# and another for responding with user data.
#  The UserCreate model is used to validate the input data 

class UserCreate(BaseModel):
    name: str
    email: str
    password: str = Field(..., min_length=6)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = {
        "from_attributes": True
    }

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
    return db_user


@app.get("/users/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(model.User).all()
    return users
  
@app.get("/about")
def get_about():
    return {"message": "This is a sample FastAPI application."}
