from pydantic import BaseModel, EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class patient(BaseModel):
    name:str
    age:Annotated[int,Field(strict=True)]
    email:EmailStr
    @field_validator("email")
    @classmethod
    def ismailcorrect(csl,email):
        domains=["hdfc.com","icici.com"]
        given_domain=email.split('@')[-1]
        if given_domain not in domains:
            raise ValueError(f"{given_domain} not in domains")
        return email
    @field_validator("age")
    @classmethod
    def checkage(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError(f"{value} not in range of 1 to 100")
    @field_validator("name")
    @classmethod
    def transform(cls,value):
        return value.upper()
patient_info={"name":"ram","age":21,"email":"raj@hdfc.com"}
new_patient=patient(**patient_info)
print(new_patient)  
    