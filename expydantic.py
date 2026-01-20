from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict, Optional, Annotated

class patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:int
    married:bool
    allerges:List[str]
    contactdetails:Dict[str,str]
patient_info={"name":"ram","email":"sas@gmail.com","age":23,"weight":23,"married":True,"allerges":["cough"],"contactdetails":{"mom":"23433"}}
pat=patient(**patient_info)
print(pat.name)