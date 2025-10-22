from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

router = APIRouter()

def get_session_local():
    yield database.SessionLocal()


@router.post("/blog_posts/", response_model=schemas.BlogPost)
def create_blog_post(blog_post: schemas.BlogPostCreate, db: Session = Depends(get_session_local)):
    return crud.create_blog_post(db=db, blog_post=blog_post)

@router.get("/blog_posts/{blog_post_id}", response_model=schemas.BlogPost)
def read_blog_post(blog_post_id: int, db: Session = Depends(get_session_local)):
    db_blog_post = crud.get_blog_post(db, blog_post_id=blog_post_id)
    if db_blog_post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return db_blog_post

@router.get("/blog_posts/", response_model=list[schemas.BlogPost])
def read_blog_posts(skip: int = 0, limit: int = 10, sort_by: str = 'created_at', descending: bool = False, db: Session = Depends(get_session_local)):
    return crud.get_blog_posts(db, skip=skip, limit=limit, sort_by=sort_by, descending=descending)

@router.delete('/blog_posts/{blog_post_id}', response_model=schemas.BlogPost)
def delete_blog_post(blog_post_id: int, db: Session = Depends(get_session_local)):
    db_blog_post = crud.delete_blog_post(db, blog_post_id=blog_post_id)
    if db_blog_post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return db_blog_post

@router.put("/blog_posts/{blog_post_id}", response_model=schemas.BlogPost)
def update_blog_post(blog_post_id: int, blog_post: schemas.BlogPostCreate, db: Session = Depends(get_session_local)):
    db_blog_post = crud.get_blog_post(db, blog_post_id=blog_post_id)
    if db_blog_post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    db_blog_post.title = blog_post.title
    db_blog_post.content = blog_post.content
    db.commit()
    db.refresh(db_blog_post)
    return db_blog_post
