from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas,models
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
)
@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserBase,db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@router.get("/users/", response_model=list[schemas.UserResponse])
def get_users(user_name:str=None,db: Session = Depends(get_db)):
    query=db.query(models.User)
    if user_name:
        query = query.filter(models.User.username.ilike(f"%{user_name}%"))

    return query.all()
@router.put("/users/{user_id}/", response_model=schemas.UserResponse)
def update_user(user_id:int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    query_user = db.query(models.User).filter(models.User.id == user_id).first()
    if query_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    query_user.name = user.name
    db.commit()
    db.refresh(query_user)
    return query_user
@router.delete("/{user_id}/")
def delete_user(user_id:int, db: Session = Depends(get_db)):
    query_user = db.query(models.User).filter(models.User.id == user_id).first()
    if query_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="kullanıcı bulunamadı")
    db.delete(query_user)
    db.commit()
    return {"message":"Kullanıcı başarıyla slindi"}