from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Boolean
from sqlalchemy.orm import Session
from . import models, schemas, database
from .database import engine,get_db
from app.routers import categories,authors,users,books,transaction
from app.models import Base

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Kütüphane Sistemi API")
app.include_router(categories.router)
app.include_router(authors.router)
app.include_router(users.router)
app.include_router(books.router)
app.include_router(transaction.router)



