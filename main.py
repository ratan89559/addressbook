from typing import List, Union, Optional

from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

import storage, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AddressBook API",
    description="Get Add, update, delete addresses.",
    version="1.0",
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency set
def get_db():
    """
    Set the database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses/", response_model=schemas.Address, dependencies=[Depends(get_db)],
          status_code=status.HTTP_201_CREATED)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    """
    Create address book data
    @param db: Database session
    @param address: AddressCreate model
    @return address: Address model data
    """
    db_address = storage.get_address_by_email(db, email=address.email)
    if db_address:
        raise HTTPException(status_code=400, detail="Email already registered")
    return storage.create_address(db, address=address)


@app.get("/addresses/", response_model=List[schemas.Address], dependencies=[Depends(get_db)])
def get_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all the address book data's
    @param db: Database session
    @param skip: int starting index
    @param limit: int limit of the records.
    @return list: List of Addresses model data
    """
    addresses = storage.get_addresses(db, skip=skip, limit=limit)
    return addresses


@app.get(
    "/addresses/{address_id}", response_model=schemas.Address, dependencies=[Depends(get_db)]
)
def get_address(address_id: int, db: Session = Depends(get_db)):
    """
    Get address book data
    @param db: Database session
    @param address_id: int
    @return Address model data
    """
    db_address = storage.get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


@app.patch(
    "/addresses/{address_id}", response_model=schemas.Address, dependencies=[Depends(get_db)],
    status_code=status.HTTP_200_OK
)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    """
    Update the address book
    @param db: Database session
    @param address_id: int
    @param address: AddressUpdate model
    @return Address model data
    """
    db_address = storage.get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")

    address_data = address.dict(exclude_unset=True)
    for key, value in address_data.items():
        setattr(db_address, key, value)

    db.add(db_address)
    db.commit()
    db.refresh(db_address)

    return db_address


@app.delete(
    "/address/", dependencies=[Depends(get_db)], status_code=status.HTTP_204_NO_CONTENT
)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    """
    Delete the address book
    @param db: Database session
    @param address_id: int
    @return boolean True
    """
    storage.delete_address(db, address_id=address_id)
    return True


@app.get("/address/", response_model=List[schemas.Address], dependencies=[Depends(get_db)])
def get_addresses(latitude: Optional[str] = None, longitude: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Get all the address book data's
    @param db: Database session
    @param latitude: string
    @param longitude: string
    @return addresses: List of Addresses model data
    """
    addresses = storage.get_query_address(db, latitude=latitude, longitude=longitude)
    return addresses
