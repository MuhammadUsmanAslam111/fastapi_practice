from apis import app as api_router
from fastapi import FastAPI
from database import  engine,model
from database import model


app = FastAPI()
app.include_router(api_router)


# Creating the database tables
model.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
  