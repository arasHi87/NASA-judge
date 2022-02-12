from endpoints.classes import Resource

from .post import DOC as post_doc
from .post import post

JUDGE = [
    Resource("POST", "/judge", post, "Upload file to judge", "UPLOAD judge", post_doc)
]
