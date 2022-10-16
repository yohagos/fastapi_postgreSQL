from fastapi import FastAPI

from database.database import engine
from database.models import Base

from routes import user

app = FastAPI()

app.include_router(user.router)

Base.metadata.create_all(engine)