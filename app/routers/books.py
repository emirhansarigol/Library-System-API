from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas,models
from app.database import get_db

router = APIRouter(
    prefix="/books",
    tags=["books"],
)
@router.post("/books/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate,db: Session = Depends(get_db)):
    new_book = models.Book(**book.dict())
    query_author = db.query(models.Author).filter(models.Author.id == book.author_id).first()
    query_category = db.query(models.Category).filter(models.Category.id == book.category_id).first()
    if query_author is None:
        raise HTTPException(status_code=404,detail="bu id ye sahip bir yazar yok")
    if query_category is None:
        raise HTTPException(status_code=404,detail="bu id ye sahip bir kategori yok")

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.get("/books/", response_model=list[schemas.BookResponse])
def get_books(book_name:str=None,author:str=None,db: Session = Depends(get_db)):
    query=db.query(models.Book)
    if book_name:
        query = query.filter(models.Book.name.ilike(f"%{book_name}%"))
    if author:
        query = query.join(models.Author).filter(models.Author.name == author)
    return query.all()

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    query_book=db.query(models.Book).filter(models.Book.id == book_id).first()
    if query_book is None:
        raise HTTPException(status_code=404, detail="kitap bulunamadı")
    if book_update.name:
        query_book.name = book_update.name
    if book_update.author_id:
        query_author = db.query(models.Author).filter(models.Author.id == book_update.author_id).first()
        if query_author is None:
            raise HTTPException(status_code=404,detail="böyle bir yazar yok, yazar eklemesi yapıp tekrar deneyiniz")
        query_book.author_id = book_update.author_id
    db.commit()
    db.refresh(query_book)
    return query_book
@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    query_delete=db.query(models.Book).filter(models.Book.id == book_id).first()
    if query_delete is None:
        raise HTTPException(status_code=404, detail="kitap bulunamadı")
    db.delete(query_delete)
    db.commit()
    return {"message":  "kitap başarıyla silindi."}