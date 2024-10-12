from fastapi import APIRouter, status, Depends, HTTPException
from config.db import get_db
from models.user import User
from sqlalchemy.orm import Session
from schemas.user import UserBase

router = APIRouter(prefix="/users")

@router.get("/", status_code=status.HTTP_200_OK)
async def list_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_a_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_a_user(id: int, user: UserBase, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    update_data = user.model_dump(exclude_unset=True)

    # Loop through the update data and assign values to db_user
    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_user(id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db.delete(db_user)
    db.commit()
