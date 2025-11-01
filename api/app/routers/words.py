from fastapi import APIRouter, Depends, HTTPException
import random

from app.models import Word
from app.schemas import WordResponse

router = APIRouter()


words = [
    { "word": "Ephemeral", "definition": "Lasting for a very short time.", "difficulty_level": "Advanced" },
    { "word": "Ubiquitous", "definition": "Present, appearing, or found everywhere.", "difficulty_level": "Intermediate" },
    { "word": "Mellifluous", "definition": "(Of a voice or words) sweet or musical; pleasant to hear.", "difficulty_level": "Advanced" },
    { "word": "Serendipity", "definition": "The occurrence and development of events by chance in a happy or beneficial way.", "difficulty_level": "Intermediate" },
    { "word": "Happy", "definition": "Feeling or showing pleasure or contentment.", "difficulty_level": "Beginner" },
    { "word": "Run", "definition": "Move at a speed faster than a walk, never having both or all the feet on the ground at the same time.", "difficulty_level": "Beginner" }
]

@router.get("/word", response_model=WordResponse)
def get_random_word():
    if not words:
        raise HTTPException(
            status_code = 404,
            detail="No words available in database"
        )
    random_word = random.choice(words)
    return random_word