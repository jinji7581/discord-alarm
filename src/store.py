from db import SessionLocal
from model import Player
from datetime import datetime
from sqlalchemy import Time


def create_player(username: str, time: datetime.time):
    session = SessionLocal()
    try:
        player = Player(
            username=username,
            time=time
        )
        session.add(player)
        session.commit()
        session.refresh(player)
        return player
    finally:
        session.close()
