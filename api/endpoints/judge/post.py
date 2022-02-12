from db import SESSION
from fastapi import Depends, File, Form, UploadFile
from fastapi.responses import PlainTextResponse
from loguru import logger
from models import Result, User
# pylint: disable=E0611
from pydantic import BaseModel
from utils import FileManager


class Payload(BaseModel):
    uid: str
    pid: int
    token: str
    file: UploadFile

    @classmethod
    def as_form(
        cls,
        uid: str = Form(...),
        pid: int = Form(...),
        token: str = Form(...),
        file: UploadFile = File(None),
    ):
        return cls(uid=uid, pid=pid, token=token, file=file)


FILEMANAGER = FileManager()
DOC = {
    200: {
        "description": "API response successfully",
        "content": {"text/plain": {"example": "OK"}},
    },
    400: {
        "description": "File type not match",
        "content": {"text/plain": {"example": "Invalid file type"}},
    },
    401: {
        "description": "Username or token not match",
        "content": {"text/plain": {"example": "Unauthorized"}},
    },
    500: {
        "description": "Something unknow error happen",
        "content": {"text/plain": {"example": "Internal Server Error"}},
    },
}


async def post(payload: Payload = Depends(Payload.as_form)):
    try:
        user = (
            SESSION.query(User).filter_by(uid=payload.uid, token=payload.token).first()
        )

        if not user:
            return PlainTextResponse("Unauthorized", 401)

        if payload.file.content_type != "application/zip":
            return PlainTextResponse("Invalid file type", 400)

        # write file into user folder and extract
        await FILEMANAGER.accept_file(payload.file, payload.uid)

        # need check if problem id match later
        SESSION.add(Result(**{"uid": payload.uid, "pid": payload.pid, "score": 0}))
        SESSION.commit()
        return PlainTextResponse("OK", 200)
    except Exception as error:
        SESSION.rollback()
        logger.error(error)
        return PlainTextResponse("Internal Server Error", 500)
