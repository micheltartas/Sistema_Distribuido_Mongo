from typing import List
from fastapi import APIRouter, Depends

from backend.database.models import MusicaDB
from backend.schemas.musica_schema import Musica, MusicaCreate
from backend.service.musica_service import MusicaService

singular = APIRouter(prefix="/musica")

@singular.post(
    "/",
    summary="Endpoint para cadastro de musica",
    description="Este endpoint serve para cadastrar um musica",
    response_model=Musica,
)
def create(musica: MusicaCreate, musica_service: MusicaService = Depends()) -> MusicaDB:
    return musica_service.create(musica)


@singular.get(
    "/",
    summary="Endpoint para retornar a lista de musicas cadastrados ",
    description="Este endpoint serve para retornar a lista de musicas cadastrados",
    response_model=List[Musica],
)
def get_all(dummy_service: MusicaService = Depends()) -> List[Musica]:
    return dummy_service.get_all()
