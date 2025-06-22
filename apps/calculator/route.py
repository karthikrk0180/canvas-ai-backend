from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_Image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
async def run(image_data: ImageData):
    decoded_image_data = base64.b64decode(image_data.image.split(',')[1])
    image_bytes = BytesIO(decoded_image_data)
    image = Image.open(image_bytes)
    responses = analyze_Image(image, dict_of_vars=image_data.dict_of_vars)
    
    return {
        "message": "Image Processed",
        "type": "success",
        "data": responses,
    }