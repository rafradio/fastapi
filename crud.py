from sqlalchemy.orm import Session

import models, schemas

def create_client(db: Session, client: schemas.ClientCreate, first_name: str, second_name: str):
    print("create client")
    db_client = models.Client(**client.dict(), first_name=first_name, second_name=second_name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client