from fastapi import APIRouter, HTTPException

from app.registry.manager import RegistryManager

router = APIRouter()

registry = RegistryManager()


@router.get("/ais")
def list_ais():
    return registry.list_all()


@router.get("/ais/{ai_id}")
def get_ai(ai_id: str):

    ai = registry.get(ai_id)

    if ai is None:
        raise HTTPException(
            status_code=404,
            detail="AI not found."
        )

    return ai


@router.delete("/ais/{ai_id}")
def delete_ai(ai_id: str):

    registry.delete(ai_id)

    return {
        "success": True,
        "message": "AI deleted successfully."
    }