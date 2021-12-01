from pydantic import BaseModel, validator, root_validator


class User(BaseModel):
    name: str
    email: str
    mobile: str
    password: str
    confirm_password: str
    
    @validator('password')
    def validate_password(cls, value):
        if str(value).isalpha() or str(value).isdigit():
            raise ValueError('Password must be alphanumeric')
        
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long')
        
        return value
    
    
    @root_validator(pre=True)
    def validate_all(cls, values):
        if values['password'] != values['confirm_password']:
            raise ValueError('Passwords do not match')
        
        return values
    
    