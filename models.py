from pydantic import BaseModel

class Party(BaseModel):
    party_name: str
    party_president: str
    party_candidate: str
    
class Vote(BaseModel):
    party_id: int
    voter_id: int
    
class Voter(BaseModel):
    voter_id: int

class AdminPasswordCheck(BaseModel):
    input_password: str
