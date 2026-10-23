from typing import Literal

from fastapi import APIRouter, Query, Response, status

from app.deps import StorageDep
from app.models import Message
from app.schemas import MessageIn, MessagePatch

router = APIRouter(
    prefix="/rooms/{room_id}/messages",
    tags=["messages"],
)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=Message)
def add_message(
    room_id: int,
    data: MessageIn,
    store: StorageDep,
) -> Message:
    return store.add(room_id, data)


@router.get("", response_model=list[Message])
def get_messages(
    room_id: int,
    store: StorageDep,
    author: str | None = None,
    pinned: bool | None = None,
    q: str | None = None,
    order: Literal["asc", "desc"] = "asc",
    limit: int = Query(default=10, ge=1),
    offset: int = Query(default=0, ge=0),
) -> list[Message]:
    return store.find(
        room_id,
        author=author,
        pinned=pinned,
        q=q,
        order=order,
        limit=limit,
        offset=offset,
    )


@router.get("/{message_id}", response_model=Message)
def get_message(
    room_id: int,
    message_id: int,
    store: StorageDep,
) -> Message:
    return store.get(room_id, message_id)


@router.patch("/{message_id}", response_model=Message)
def update_message(
    room_id: int,
    message_id: int,
    data: MessagePatch,
    store: StorageDep,
) -> Message:
    changes = data.model_dump(exclude_unset=True)
    return store.update(room_id, message_id, changes)


@router.delete(
    "/{message_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_message(
    room_id: int,
    message_id: int,
    store: StorageDep,
) -> Response:
    store.delete(room_id, message_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)