from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Note

class SignupView(APIView):
    def post(self, request):
        user_name = request.data.get('user_name')
        user_email = request.data.get('user_email')
        password = request.data.get('password')

        if User.find_user_by_email(user_email):
            return Response({"message": "Email already exists"}, status=status.HTTP_200_OK)

        hashed_password = make_password(password)
        user = User.create_user(user_name, user_email, hashed_password) 

        return Response(
            {
                "message": "User registered successfully",
                "user": {
                    "user_id": user["user_id"],  
                    "user_name": user["user_name"],  
                    "user_email": user["user_email"], 
                },
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    def post(self, request):
        user_email = request.data.get("user_email")
        password = request.data.get("password")

        user = User.find_user_by_email(user_email)

        if user and check_password(password, user["password"]):
            return Response(
                {
                    "message": "Login successful",
                    "user": {
                        "user_id": user["user_id"],  
                        "user_name": user["user_name"],
                        "user_email": user["user_email"],  
                    },
                },
                status=status.HTTP_200_OK,
            )

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class CreateNoteView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        note_title = request.data.get('note_title')
        note_content = request.data.get('note_content')

        if not user_id or not note_title or not note_content:
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        note = Note.create_note(user_id, note_title, note_content)
        return Response({
            "message": "Note created successfully",
            "note": {
                "note_id": note["note_id"],
                "user_id": note["user_id"],
                "note_title": note["note_title"],
                "note_content": note["note_content"],
                "last_update": note["last_update"].isoformat(),
                "created_on": note["created_on"].isoformat()
            }
        }, status=status.HTTP_201_CREATED)


class UpdateNoteView(APIView):
    def put(self, request, note_id):
        note_title = request.data.get('note_title')
        note_content = request.data.get('note_content')

        updated_note = Note.update_note(note_id, note_title, note_content)

        if updated_note:
            return Response({
                "message": "Note updated successfully",
                "note": {
                    "note_id": updated_note["note_id"],
                    "user_id": updated_note["user_id"],
                    "note_title": updated_note["note_title"],
                    "note_content": updated_note["note_content"],
                    "last_update": updated_note["last_update"].isoformat(),
                    "created_on": updated_note["created_on"].isoformat()
                }
            }, status=status.HTTP_200_OK)
        return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

class GetUserNotesView(APIView):
    def get(self, request, user_id):
        notes = Note.get_notes_by_user(user_id)

        if not notes:
            return Response({"message": "No notes found for this user"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"notes": notes}, status=status.HTTP_200_OK)
