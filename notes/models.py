import uuid
from datetime import datetime
from .mongo_db import db 

class User:
    collection = db.users  

    @staticmethod
    def create_user(user_name, user_email, password):
        user = {
            "user_id": str(uuid.uuid4()),
            "user_name": user_name,
            "user_email": user_email,
            "password": password,
            "last_update": datetime.utcnow(),
            "created_on": datetime.utcnow(),
        }
        User.collection.insert_one(user)
        return user

    @staticmethod
    def find_user_by_email(user_email):
        return User.collection.find_one({"user_email": user_email})

class Note:
    collection = db.notes 

    @staticmethod
    def create_note(user_id, note_title, note_content):
        note = {
            "note_id": str(uuid.uuid4()),
            "user_id": user_id,
            "note_title": note_title,
            "note_content": note_content,
            "last_update": datetime.utcnow(),
            "created_on": datetime.utcnow(),
        }
        result = Note.collection.insert_one(note)
        note["_id"] = str(result.inserted_id)  
        return note

    @staticmethod
    def find_note_by_id(note_id):
        note = Note.collection.find_one({"note_id": note_id})
        if note:
            note["_id"] = str(note["_id"])  
        return note

    @staticmethod
    def update_note(note_id, note_title, note_content):
        result = Note.collection.find_one_and_update(
            {"note_id": note_id},
            {"$set": {
                "note_title": note_title,
                "note_content": note_content,
                "last_update": datetime.utcnow()
            }},
            return_document=True
        )
        if result:
            result["_id"] = str(result["_id"]) 
        return result

    @staticmethod
    def get_notes_by_user(user_id):
        notes = list(Note.collection.find({"user_id": user_id}))
        for note in notes:
            note["_id"] = str(note["_id"])  
            note["last_update"] = note["last_update"].isoformat()
            note["created_on"] = note["created_on"].isoformat()
        return notes