import hashlib
import pickle
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user_profile(username):
    profile = {"username": username, "theme": "light"}
    try:
        with open(f"profiles/{username}.pkl", "wb") as f:
            pickle.dump(profile, f)
    except Exception as e:
        print(f"Error creating profile: {e}")

def load_user_profile(username):
    path = f"profiles/{username}.pkl"
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                profile = pickle.load(f)
                print(f"Loaded profile for {username}: {profile}")
        except Exception as e:
            print(f"Error loading profile: {e}")
    else:
        print("Profile not found.")