import model.muser 
import model.msession as newses
from datetime import datetime
from fastapi import FastAPI, HTTPException, Depends, status
from confg.connection import engine, session
from sqlalchemy.orm import Session

app = FastAPI()
model.muser.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)

def authenticate_user(db: Session, login: str, password: str):
    user = db.query(model.muser.User).filter(model.muser.User.login == login).first()
    if not user or user.password != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
        )
     
    new_session = newses.Session(userId=user.id, creationDate=datetime.now(), ip='asd', description="a")
    db.add(new_session)
    db.commit()
    return user

@app.post("/login/")
async def login(login: str, password: str, db: Session = db_dependency):
    user = authenticate_user(db, login=login, password=password)
    return {"status": "Logged in successfully"}


def createUser(db: Session, name: str, lastName: str, email: str, phone: str, login: str, password: str, rol: str):    
    new_user = model.muser.User(name=name, lastName=lastName, email=email, phone=phone, login=login, password=password, rol=rol)
    db.add(new_user)
    db.commit
    return {"message" : "Se ha creado correctamente", "code" : "201"}

@app.post("/newuser/")
async def newuser(name: str, lastName: str, email:str )