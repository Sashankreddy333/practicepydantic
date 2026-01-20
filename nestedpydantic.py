from pydantic import BaseModel
class address(BaseModel):
    city:str
    pincode:int
    state:str
class patient(BaseModel):
    name:str
    age:int
    address:address
address_info={"city":"tad","pincode":515411,"state":"andhra"}
new_address=address(**address_info)
patient_info={"name":"ram","age":21,"address":new_address}
new_patient=patient(**patient_info)
print(new_patient.address.state)
