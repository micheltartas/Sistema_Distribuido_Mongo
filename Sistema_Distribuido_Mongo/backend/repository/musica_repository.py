import pickle
from typing import List
from backend.database.models import MusicaDB
from backend.schemas.musica_schema import MusicaCreate
import redis
from pymongo import MongoClient


class MusicaRepository:

    def __init__(self):
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['musica_db']
        self._collection = self._db['musica']

    def insert(self, musica: MusicaCreate) -> MusicaDB:
        musica = MusicaDB(**musica.dict())
        musica_dict = {
            "title": musica.title,
            "artist": musica.artist,
            "gender": musica.gender,
        }
        result = self._collection.insert_one(musica_dict)
        musica.id = str(result.inserted_id)
        return musica

    
    def get_all(self) -> List[MusicaDB]:
        musicas = []
        for musica_dict in self._collection.find():
            musica = MusicaDB(
                id=str(musica_dict["_id"]),
                title=musica_dict["title"],
                artist=musica_dict["artist"],
                gender=musica_dict["gender"],
            )
            musicas.append(musica)
        return musicas
