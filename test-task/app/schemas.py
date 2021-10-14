from pydantic import BaseModel, Field, EmailStr


class PatientSchema(BaseModel):
    id: int = Field(default=None)
    date_of_birth: str = Field(...)
    diganoses: (str) = Field(...)
    created_at: str = Field(...)

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)