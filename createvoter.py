from sqlite3 import connect
import bcrypt

class AddVoter:
    def __init__(self, voter_name, password):
        self.voter_name = voter_name
        self.password = password

        with connect("./Database/voting.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS VoterList(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    voteingstate BLOB NOT NULL DEFAULT 'False'
                );
            """)
            conn.commit()

    def create_voter(self):
        with connect("./Database/voting.db") as conn:
            cursor = conn.cursor()
            password_hash = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
            cursor.execute("INSERT INTO VoterList (name, password) VALUES (?, ?)", (self.voter_name, password_hash))
            conn.commit()

        return f"Voter '{self.voter_name}' created successfully."
    
