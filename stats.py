from fastapi import APIRouter

from app.deps import StorageDep

router = APIRouter(tags=["stats"])


@router.get("/stats")
def get_stats(store: StorageDep) -> dict[str, int]:
    messages = store.get_all()

    return {
        "users": len(store.get_users()),
        "rooms": len(store.get_rooms()),
        "messages": len(messages),
        "pinned": sum(message.pinned for message in messages),
    }