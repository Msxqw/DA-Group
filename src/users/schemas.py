from pydantic import BaseModel, EmailStr

class RegisterUserSchema(BaseModel):
    username: str
    email: EmailStr
    phone_number: str
    password: str

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: str