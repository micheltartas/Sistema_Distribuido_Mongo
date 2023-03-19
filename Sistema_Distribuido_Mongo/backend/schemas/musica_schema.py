from pydantic import BaseModel
from backend.schemas import CRUDModel, OrmModel

class MusicaBase(BaseModel):
    title: str
    artist: str
    gender: str

class Musica(MusicaBase, OrmModel):
    ...

class MusicaCreate(MusicaBase, CRUDModel):
    ...

class MusicaInternal(Musica):
    id: int
