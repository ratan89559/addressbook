from typing import Optional

from sqlalchemy.orm import Session

import models
import schemas


def get_address(db: Session, address_id: int):
    """
    Get address from database by address id and return first record.
    @param db: Database session
    @param address_id: int Address record id
    @return Address first record
    """
    return db.query(models.Address).filter(models.Address.id == address_id).first()


def get_address_by_email(db: Session, email: str):
    """
    Get address from database by email id and return first record.
    @param db: Database session
    @param email: str Address record email address
    @return Address first record
    """
    return db.query(models.Address).filter(models.Address.email == email).first()


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    """
    Get address from database by email id and return first record.
    @param db: Database session
    @param skip: int starting index
    @param limit: int limit of the records.
    @return All the address record's
    """
    return db.query(models.Address).offset(skip).limit(limit).all()


def create_address(db: Session, address: schemas.AddressCreate):
    """
    Create address book data
    @param address: AddressCreate model
    @param db: Database session
    @return address: Address model data
    """
    db_address = models.Address(email=address.email,
                                name=address.name,
                                address1=address.address1,
                                address2=address.address2,
                                city=address.city,
                                state=address.state,
                                zip=address.zip,
                                latitude=address.latitude,
                                longitude=address.longitude,
                                )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def delete_address(db: Session, address_id: int):
    """"
    Delete the address book
    @param db: Database session
    @param address_id: int
    @return boolean True
    """
    db.query(models.Address).filter(models.Address.id == address_id).delete()
    db.commit()


def get_query_address(db: Session, latitude: str, longitude: str):
    """
    Get address from database by email id and return first record.
    @param db: Database session
    @param latitude: string
    @param longitude: string
    @return All the address record's
    """
    query = {}
    if latitude:
        query.update({"latitude": latitude})
    if longitude:
        query.update({"longitude": longitude})

    print(latitude)
    print(longitude)
    return db.query(models.Address).filter(models.Address.latitude == latitude).all()
