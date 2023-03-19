from typing import List
from fastapi import Depends
from backend.database.models import MusicaDB
from backend.repository.musica_repository import MusicaRepository
from backend.schemas.musica_schema import MusicaCreate

class MusicaService:

    def __init__(self, dummy_repository: MusicaRepository = Depends()):
        self._dummy_repository = dummy_repository

    def create(self, dummy: MusicaCreate) -> MusicaDB:
        return self._dummy_repository.insert(dummy)

    def get_all(self) -> List[MusicaDB]:
        return self._dummy_repository.get_all()
    
