from pydantic import BaseModel, Field, EmailStr, ValidationError

class UserRegister(BaseModel):
    username: str = Field(min_length=5)
    email: EmailStr
    age: int = Field(ge=18)

try:
    user = UserRegister(username="eswar123", email="eswar@gmail.com", age=22)
    print("Valid user:", user)
except ValidationError as e:
    print(e)
