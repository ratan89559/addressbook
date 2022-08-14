from sqlalchemy import Column, Integer, String

from database import Base


class Address(Base):
    """
    defined address model here
    """
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False)
    address1 = Column(String, nullable=False)
    address2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(Integer, nullable=False)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
