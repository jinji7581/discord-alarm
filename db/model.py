from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False, index=True)
    time = Column(Time)

    def __repr__(self):
        return f"<Player(username={self.username})>"
