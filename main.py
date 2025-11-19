from fastapi import FastAPI
from models import Party, Voter, Vote , AdminPasswordCheck
from createParty import addparty
from auth import Auth

app = FastAPI()

@app.get("/check")
def check():
    return {"status": "API is working"}

@app.post("/auth/check_admin_password")
def check_password(password_check: AdminPasswordCheck):
    auth_instance = Auth()
    is_valid = auth_instance.check_admin_password(password_check.input_password)
    return {"is_valid": is_valid}
    

@app.post("/create_party")
def create_party(party: Party):
    party_creator = addparty(party.party_name,)
    result = party_creator.create_party(party.party_president, party.party_candidate)
    return {"message": result}

@app.post("/vote")
def vote(vote: Vote):
    from vote import Voting
    voting_instance = Voting()
    result = voting_instance.add_vote(vote.party_id, vote.voter_id)
    return {"message": result}

@app.get("/parties")
def get_parties():
    from Parties import Parties
    parties_instance = Parties()
    result = parties_instance.get_parties()
    return {"parties": result}
