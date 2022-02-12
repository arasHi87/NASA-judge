import random
import string

from config import Config
from db import SESSION
from sqlalchemy import VARCHAR, Column, Enum, Integer
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class Result(BASE):

    __tablename__ = "results"

    rid = Column(
        Integer, unique=True, primary_key=True, nullable=False, autoincrement=True
    )  # result id
    uid = Column(VARCHAR, nullable=False)  # user id
    pid = Column(Integer, nullable=False)  # problem id
    score = Column(Integer, nullable=True)
    status = Column(
        Enum("pending", "evaluating", "done"), server_default="pending", nullable=False
    )

    def dumps(self):
        return {
            "jid": self.jid,
            "uid": self.uid,
            "pid": self.pid,
            "score": self.score,
            "status": self.satus,
        }


class User(BASE):

    __tablename__ = "users"

    uid = Column(Integer, unique=True, primary_key=True, nullable=False)
    token = Column(VARCHAR, nullable=False)

    def dumps(self):
        return {
            "uid": self.uid,
            "token": self.token,
        }


def init_db():
    for _id in Config.IDS:
        user = SESSION.query(User).filter_by(uid=_id).first()
        if not user:
            token = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
            SESSION.add(User(**{"uid": _id, "token": token}))
    SESSION.commit()
