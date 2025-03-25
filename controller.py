from fastapi import APIRouter, HTTPException
from services import check_email_validity

router = APIRouter()

@router.post("/check_email")
async def check_email(email: str):
    """Check email validity, domain details, and blacklist status."""
    result = await check_email_validity(email)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result)
    return result
