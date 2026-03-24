from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas,models


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)
@router.post("/", response_model=schemas.CategoryResponseDTO)
def create_category(category: schemas.CategoryCreateDTO, db: Session = Depends(get_db)):
    new_category = models.Category(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.get("/", response_model=list[schemas.CategoryResponseDTO])
def get_categories(cat_name:str=None,db: Session = Depends(get_db)):
    query=db.query(models.Category)
    if cat_name:
        query = query.filter(models.Category.name.ilike(f"%{cat_name}%"))

    return query.all()
@router.put("/{category_id}", response_model=schemas.CategoryResponseDTO)
def update_category(id:int,up_veriler:schemas.CategoryUpdateDTO,db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found : kategori bulunamadı")
    category.name = up_veriler.name
    db.commit()
    db.refresh(category)
    return category
@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found : kategori bulunamadı")
    db.delete(category)
    db.commit()
    return {"message": "kategori başarıyla silindi."}
