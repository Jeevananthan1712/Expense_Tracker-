import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Jeeva","Anil"]
usernames = ["gva","ani"]
password = ["XXX","XXX"]

hashed_password = stauth.Hasher(password).generate()  #uses bcrypt alogorithm -> very secure

file_path = Path(__file__).parent / "hashed_pw.pk1"
with file_path.open("wb") as file:
    pickle.dump(hashed_password,file)
