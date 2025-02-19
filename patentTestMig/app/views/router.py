import mimetypes
from pathlib import Path
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from starlette.staticfiles import StaticFiles

from app.database import variants
from app.dependencies import get_db
from app.schemas import schema
from app.crud import counterCrud as crud

# Directory where static files are stored
FILES_DIR = Path("media")

router = APIRouter(prefix='/test', tags=["test"])

# ✅ Get Variant Data
@router.get("/variants/{versionId}")
async def get_files(versionId: int):
    if versionId not in range(1, 8):  # Ensuring range is 1-7
        raise HTTPException(status_code=404, detail="version is not found")

    try:
        return variants.variants[versionId - 1]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An unexpected error occurred: {str(e)}")

# ✅ Get Count of Something from DB
@router.get("/count", response_model=schema.Counter)
def get_count(db: Session = Depends(get_db)):
    try:
        count_value = crud.get_counter(db)
        return schema.Counter(count=count_value)  # Wrap response
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception:
        raise HTTPException(status_code=500, detail="Server error")

# ✅ Serve Static Media Files (Images, Audio, etc.)
@router.get("/media/{file_name}")
async def get_file(file_name: str):
    """Returns the requested media file (image, audio, etc.)"""
    file_path = FILES_DIR / file_name

    # Prevent directory traversal attacks
    if not file_path.resolve().is_relative_to(FILES_DIR):
        return JSONResponse(content={"error": "Invalid file path"}, status_code=403)

    # Ensure the file exists
    if file_path.exists() and file_path.is_file():
        media_type, _ = mimetypes.guess_type(file_path)
        return FileResponse(file_path, media_type=media_type or "application/octet-stream")

    return JSONResponse(content={"error": "File not found"}, status_code=404)

# ✅ Get Answer Based on Version ID
@router.get("/answer/{versionId}")
async def get_answer(
    versionId: int,
    db: Session = Depends(get_db)
):
    if versionId not in range(1, 8):  # Ensure valid range (1-7)
        raise HTTPException(status_code=404, detail="version is not found")

    try:
        date_obj = datetime.now()  # Current timestamp
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use DD.MM.YYYY HH:MM:SS")

    try:
        crud.create_counter(db, date_obj)
        return schema.AnswerResponse(answers=variants.answers[versionId - 1])
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An unexpected error occurred: {str(e)}")
