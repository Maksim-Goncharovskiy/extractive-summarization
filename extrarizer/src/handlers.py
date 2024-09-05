from fastapi import APIRouter, HTTPException, Form, UploadFile
from src.summary import make_extract_summary
from src.utils import add_name_prefixes

router = APIRouter(prefix="/extract", tags=["extract"])


@router.post('/text')
async def extract_summary(
    text: str = Form(),
    ratio: float = Form(0.2),
    many_speakers: bool = True
):
    """
    Получение экстрактной суммаризации текста.
    Параметры:
        text - Текст, заданный как строка.
        ratio - Степень сжатия суммаризации(0 <= ratio <= 1)
        many_speakers - Текст представляет собой разговор нескольких людей(True/False). Если True,
            то в начале каждого предложения будет указан его автор.
    """

    if many_speakers:
        text = add_name_prefixes(text, 2)

    summary = make_extract_summary(text, ratio)

    return {
        'status': 200,
        'summary': summary
    }


@router.post('/file')
async def extract_summary(
        file: UploadFile,
        ratio: float = Form(0.2),
        many_speakers: bool = True
):
    """
    Получение экстрактной суммаризации текста.
    Параметры:
        file - Текстовый файл в кодировке utf-8.
        ratio - Степень сжатия суммаризации(0 <= ratio <= 1)
        many_speakers - Текст представляет собой разговор нескольких людей(True/False). Если True,
            то в начале каждого предложения будет указан его автор.
    """
    try:
        file_text = (await file.read()).decode('utf-8')
        if many_speakers:
            file_text = add_name_prefixes(file_text, 2)
        summary = make_extract_summary(file_text, ratio)
        return {
            'status': 200,
            'summary': summary
        }
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File should be UTF-8 encoded")
