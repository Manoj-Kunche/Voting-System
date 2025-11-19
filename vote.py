class voting:
    def add_vote(self,id):
        with open("partys/parties.txt","r+") as file:
            lines = file.readlines()
            votes=lines[id].split(':')[-1]
            votes=int(votes.strip())+1
            val=lines[id].split(":")
            lines[id]=f'{val[0]}:{val[1]}:{votes}\n'
            file.seek(0)
            file.writelines(lines)

        return "Vote added successfully"