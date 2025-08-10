from app.models.payload import Payload
from app.lib.email import Email
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post('/send_email')
def send_email(payload: Payload):
    try:
        email = Email(payload)
        if email.send():
            return JSONResponse(
                content={'msg': 'Message Sent Successfully!'}, 
                status_code=200
            )

    except Exception as error:
        return JSONResponse(content={'msg': str(error)}, status_code=400)
