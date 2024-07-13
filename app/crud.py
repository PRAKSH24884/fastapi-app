# app/crud.py
from sqlalchemy.orm import Session
from app.db_models import User
from app.models import UserCreate
import logging

logging.basicConfig(level=logging.INFO)


def get_user(db: Session, user_id: int):
    logging.info(f"Fetching user with ID {user_id}")
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    logging.info(f"Fetching user with email {email}")
    user = db.query(User).filter(User.email == email).first()
    logging.info(f"User found: {user}")
    return user


def create_user(db: Session, user: UserCreate):
    logging.info(
        f"Creating user with username {user.username} and email {user.email}")
    try:
        db_user = User(username=user.username, email=user.email,
                       hashed_password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logging.info(f"User created: {db_user}")
        return db_user
    except Exception as e:
        logging.error(f"Error creating user: {e}")
        db.rollback()
        raise e


def update_user(db: Session, user_id: int, user: UserCreate):
    logging.info(f"Updating user with ID {user_id}")
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db_user.hashed_password = user.password
        db.commit()
        db.refresh(db_user)
        logging.info(f"User updated: {db_user}")
    return db_user


def delete_user(db: Session, user_id: int):
    logging.info(f"Deleting user with ID {user_id}")
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        logging.info(f"User deleted: {db_user}")
    return db_user
