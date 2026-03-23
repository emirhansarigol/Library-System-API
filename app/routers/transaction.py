from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db


router = APIRouter(
    prefix="/transaction",
    tags=["transaction"],
)
@router.post("/", response_model=schemas.TransactionResponse)
def book_borrow(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == transaction.book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="kitap bulunamadı")
    if not book.is_active:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="kitap zaten emanette")
    user = db.query(models.User).filter(models.User.id == transaction.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="kullanıcı bulunamadı")
    new_transaction = models.Transaction(user_id= transaction.user_id,book_id = transaction.book_id)
    db.add(new_transaction)
    book.is_active = False
    db.commit()
    db.refresh(new_transaction)
    return new_transaction
@router.post("/return/",response_model=schemas.TransactionResponse)
def book_return(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == transaction.book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="kitap bulunamadı")
    if book.is_active:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="kitap zaten müsait")
    user = db.query(models.User).filter(models.User.id == transaction.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="kullanıcı bulunamadı")
    new_transaction = models.Transaction(user_id= transaction.user_id,book_id = transaction.book_id)
    db.add(new_transaction)
    book.is_active = True
    db.commit()
    db.refresh(new_transaction)
    return new_transaction