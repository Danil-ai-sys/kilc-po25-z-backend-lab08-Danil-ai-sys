from fastapi import APIRouter

from app.deps import StorageDep
from app.models import Room
from app.schemas import RoomIn

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.get("", response_model=list[Room])
def get_rooms(store: StorageDep) -> list[Room]:
    return store.get_rooms()


@router.get("/{room_id}", response_model=Room)
def get_room(room_id: int, store: StorageDep) -> Room:
    return store.get_room(room_id)


@router.post("", status_code=201, response_model=Room)
def add_room(data: RoomIn, store: StorageDep) -> Room:
    return store.add_room(data)