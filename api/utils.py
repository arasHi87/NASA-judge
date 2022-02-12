import os
import random
import string
import zipfile

import aiofiles
from fastapi import UploadFile
from loguru import logger


class FileManager:
    def __init__(self):
        self.root = "data"

    def _get_name(self):
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=7))

    def _extract(self, path: str, filename: str):
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(path)
        logger.warning(f"Extracted {filename} into {path}")

    async def accept_file(self, file: UploadFile, uid: str):
        """accept zip file and extract to user folder"""

        path = os.path.join(self.root, uid, self._get_name())
        os.makedirs(path)
        filename = os.path.join(path, self._get_name() + ".zip")

        async with aiofiles.open(filename, "wb") as target:
            while content := await file.read(1024):
                await target.write(content)
        logger.warning(f"Wrote file into {filename}")

        self._extract(path, filename)
