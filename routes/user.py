from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.database import get_db
from database.schemas import User, ShowUser
from database.models import User as mUser
from hash.hashing import get_password_hashed

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('', response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    user = mUser(firstname=request.firstname, lastname=request.lastname, email=request.email, password=get_password_hashed(request.password) )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get('', response_model=List[ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(mUser).all()

@router.get('/{id}', response_model=ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(mUser).filter(mUser.id == id).first()