from typing import Union

from pydantic import BaseModel, EmailStr


class AddressCreate(BaseModel):
    email: EmailStr
    name: str
    address1: str
    address2: Union[str, None] = None
    city: str
    state: str
    zip: int
    latitude: str
    longitude: str


class Address(AddressCreate):
    id: int

    class Config:
        orm_mode = True


class AddressUpdate(BaseModel):
    email: Union[EmailStr, None] = None
    name: Union[str, None] = None
    address1: Union[str, None] = None
    address2: Union[str, None] = None
    city: Union[str, None] = None
    state: Union[str, None] = None
    zip: Union[int, None] = None
    latitude: Union[str, None] = None
    longitude: Union[str, None] = None
