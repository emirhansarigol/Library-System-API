from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship



class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete="SET NULL"))
    category = relationship("Category", back_populates="books")
    author_id = Column(Integer, ForeignKey('authors.id',ondelete="SET NULL"))
    author = relationship("Author", back_populates="books")
    transactions = relationship("Transaction", back_populates="book")
    is_active = Column(Boolean)