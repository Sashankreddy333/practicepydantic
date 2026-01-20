from pydantic import BaseModel, EmailStr,AnyUrl,Field,field_validator,model_validator
from typing import List,Dict,Optional,Annotated

class patient(BaseModel):
    name:str
    age:Annotated[int,Field(strict=True)]
    email:EmailStr
    @model_validator(mode="after")
    @classmethod
    def checksomedetails(cls, model):
        if 10<model.age<100 and len(model.name)<20:
            return model
        raise ValueError("check age and name once again")
patient_info={"name":"ram","age":21,"email":"raj@hdfc.com"}
new_patient=patient(**patient_info)
print(new_patient)  