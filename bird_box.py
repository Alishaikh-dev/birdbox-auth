from fastapi import FastAPI, Form, HTTPException, Depends, status
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from pydantic import EmailStr

# --------------------------------------------------
# DATABASE CONFIG
# --------------------------------------------------

engine = create_engine("postgresql://postgres:fatima.khadija@localhost:5432/testdb" , echo=False)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()

def di_injection():
    database = SessionLocal()
    try: 
        yield database
    finally:
        database.close()
        
# --------------------------------------------------
# DATABASE MODEL
# --------------------------------------------------

class birdbox(Base):
    __tablename__ = "Bird_Box"
    id = Column(Integer,primary_key=True,index=True)
    
    username = Column(String(255) , unique=True, nullable=False)
    hash_password = Column(String(255) , nullable=False)
    
# Base.metadata.create_all(engine)

# --------------------------------------------------
# SECURITY
# --------------------------------------------------

pwd_context = CryptContext(schemes=["bcrypt"] ,  deprecated="auto")

def hash_pass(password : str):
    hasheed = pwd_context.hash(password)
    return hasheed

def hash_verify(plain_password : str , password : str):
    verify = pwd_context.verify(plain_password , password)
    return verify

# --------------------------------------------------
# FASTAPI APP
# --------------------------------------------------

app = FastAPI(
    title="Login_Signup"
)

# --------------------------------------------------
# SignUp EndPoint
# --------------------------------------------------

@app.post("/SignUp")

def Sign(username : str = Form(...), password : str = Form(...) , database : Session = Depends(di_injection)):
    
 # ---------------- VALIDATIONS ----------------
 
    if len(username) > 255:
        raise HTTPException(
            status_code=400,
            detail="Sorry Your Username is So Big"
        )
    
    if len(password) > 255:
        raise HTTPException(
            status_code=400,
            detail="Your Password is So big"
        )
  

    # ---------------- CREATE USER ----------------
    
    create_user = birdbox(
        username = username,
        hash_password = hash_pass(password)
        
    )
    
    database.add(create_user)
    database.commit()
    database.refresh(create_user)
        
    return {
        "message": "Account created successfully",
        "username": create_user.username,
    }


# --------------------------------------------------
# Login EndPoint
# --------------------------------------------------

@app.post("/login")
def login(username : str , password : str , database : Session = Depends(di_injection)):
    user = database.query(birdbox).filter(birdbox.username == username).first()
    if not user:
        raise HTTPException(status_code=400 , detail="SORRY USER NOT FOUND")
    
    if not hash_verify(password , user.hash_password):
        raise HTTPException(
            status_code=400,
            detail="PASSWORD IS WORNG"
        )
    
    return {
        "message" : "LOGIN SUCESSSFULL",
        "username" : user.username
    }
    
    
    
       
    
    
    
    
    
        