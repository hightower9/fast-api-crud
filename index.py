from fastapi import FastAPI
from config.db import init_db
from routes.user import router

app = FastAPI()

# Call the init_db function to create tables
init_db()

app.include_router(router, tags=["Users"])