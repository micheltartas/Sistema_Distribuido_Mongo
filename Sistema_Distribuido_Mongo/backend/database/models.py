from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MusicaDB(Base):

    __tablename__ = "musica"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    artist = Column(String(100), nullable=False)
    gender = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Musica(title='{self.title}', artist='{self.artist}',gender='{self.gender}')>"