from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas,models
from app.database import get_db

router = APIRouter(
    prefix="/authors",
    tags=["authors"],
)
@router.post("/", response_model=schemas.AuthorResponseDTO)
def create_author(author: schemas.AuthorCreateDTO,db: Session = Depends(get_db)):
    new_author = models.Author(**author.dict())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author
@router.get("/authors/", response_model=list[schemas.AuthorResponseDTO])
def get_categories(author_name:str=None,db: Session = Depends(get_db)):
    query=db.query(models.Author)
    if author_name:
        query = query.filter(models.Author.name.ilike(f"%{author_name}%"))

    return query.all()
@router.put("/", response_model=schemas.AuthorResponseDTO)
def update_author(id:int,authors:schemas.AuthorUpdateDTO,db: Session = Depends(get_db)):
    query_author = db.query(models.Author).filter(models.Author.id == id).first()
    if query_author is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Yazar bulunamadı")
    query_author.name = authors.name
    db.commit()
    db.refresh(query_author)
    return query_author

@router.delete("/authors/{author_id}")
def delete_author(author_id:int,db: Session = Depends(get_db)):
    query_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if query_author is None:
        raise HTTPException(status_code=404,detail="Yazar")
    db.delete(query_author)
    db.commit()
    return {"message":"Yazar başarıyla silindi"}