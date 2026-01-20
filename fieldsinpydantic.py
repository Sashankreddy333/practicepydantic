from pydantic import BaseModel ,EmailStr,AnyUrl, Field
from typing import List, Dict,Optional,Annotated

class patient(BaseModel):
    name:Annotated[str,Field(max_length=20,title="Name of the patient", example="Ram")]
    age:int=Field(gt=0, lt=100)
    email:EmailStr
    linkdinurl:AnyUrl
    married:Annotated[Optional[bool], Field(default=None, title="Marriage Status")]
    weight:Annotated[Optional[int],Field(gt=0,lt=200,title="Weight of the Patient")]
    allerges:Annotated[Optional[List[str]],Field(title="Allerges of the patient",max_length=5,default=None)]
    contactdetails:Dict[str,str]
patient_info={"name":"ram","email":"sas@gmail.com","age":10,"linkdinurl":"https://kfjdekj/linkdin.com","weight":23,"married":True,"contactdetails":{"mom":"23433"}}
new_patient=patient(**patient_info)
print(new_patient)
    
    
    