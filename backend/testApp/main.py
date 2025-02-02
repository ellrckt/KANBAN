from fastapi import FastAPI
from fastapi import APIRouter
from db.db import db_helper
from contextlib import asynccontextmanager
from fastapi.responses import ORJSONResponse
import bcrypt
from testApp.routers.user import router as user_router
from testApp.routers.user_registration import router as user_registration_router
from testApp.routers.login import router as login_router



# @asynccontextmanager
# async def lifespan(application: FastAPI):

#     yield

#     await db_helper.dispose()


app = FastAPI(
    # lifespan=lifespan,
    default_response_class=ORJSONResponse,
    )

app.include_router(user_router)
app.include_router(user_registration_router)
app.include_router(login_router)

@app.get("/get_users/")
def get_users():
    print("hello world")    