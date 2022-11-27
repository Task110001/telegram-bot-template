from sqlalchemy.exc import PendingRollbackError, IntegrityError
from .models import Users
from sqlalchemy.orm import Session
from core.config import db


def add_user(message, db: Session = db):
  username = message.from_user.username if message.from_user.username else None
  user = Users(id=int(message.from_user.id), name=username, is_banned=False)
  
  db.add(user)
  try:
    db.commit()
    db.refresh(user)
    return True
  except:
    db.rollback()
    return False