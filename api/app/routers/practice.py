from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Word, PracticeSession
from app.schemas import ValidateSentenceRequest, ValidateSentenceResponse
from app.utils import mock_ai_validation

router = APIRouter()


@router.post("/validate-sentence", response_model=ValidateSentenceResponse)
def validate_sentence(
    request: ValidateSentenceRequest,
    db: Session = Depends(get_db)
):
    """
    Receive user sentence and validate it (mock AI)
    Save results to database
    """
    # Get word data
    # Mock AI validation
    # Save to database
    ...
    word = db.query(Word).filter(Word.id == request.word_id).first()

    if not word:
        raise HTTPException(status_code=404, detail="Word not found")
    
    result = mock_ai_validation(
        request.sentence,
        word.word,
        word.difficulty_level
    )

    practice = PracticeSession(
        word_id=request.word_id,
        sentence=request.sentence,
        score=result["score"],
        level=result["level"],
        suggestion=result["suggestion"],
        corrected_sentence=result["corrected_sentence"]
    )

    db.add(practice)
    db.commit()
    db.refresh(practice)

    # 4. ส่ง Response กลับ
    return ValidateSentenceResponse(
        score=result["score"],
        level=result["level"],
        suggestion=result["suggestion"],
        corrected_sentence=result["corrected_sentence"]
    )

