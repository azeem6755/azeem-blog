from sqlalchemy.orm import Session
from . import models, schemas

def get_blog_post(db: Session, blog_post_id: int):
    return db.query(models.BlogPost).filter(models.BlogPost.id == blog_post_id).first()

def get_blog_posts(db: Session, skip: int = 0, limit: int = 10, sort_by: str = 'created_at', descending: bool = False):
    sort_column = getattr(models.BlogPost, sort_by, None)
    if descending:
        sort_column = sort_column.desc()
    return db.query(models.BlogPost).order_by(sort_column).offset(skip).limit(limit).all()

def create_blog_post(db: Session, blog_post: schemas.BlogPostCreate):
    db_blog_post = models.BlogPost(**blog_post.model_dump())
    print(db_blog_post)
    db.add(db_blog_post)
    db.commit()
    db.refresh(db_blog_post)
    return db_blog_post

def delete_blog_post(db: Session, blog_post_id: int):
    db_blog_post = db.query(models.BlogPost).filter(models.BlogPost.id == blog_post_id).first()
    if db_blog_post:
        db.delete(db_blog_post)
        db.commit()
    return db_blog_post