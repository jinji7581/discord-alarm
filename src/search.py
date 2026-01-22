from db import SessionLocal
from model import Player


def get_players_by_name(playername: str):
    session = SessionLocal()
    try:
        return (
            session.query(Player)
            .filter(Player.username == username)
            .all()
        )
    finally:
        session.close()
