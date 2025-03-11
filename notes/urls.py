from django.urls import path
from .views import SignupView, LoginView, CreateNoteView, UpdateNoteView, GetUserNotesView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('create/', CreateNoteView.as_view(), name='create_note'),
    path('update/<str:note_id>/', UpdateNoteView.as_view(), name='update_note'),
    path('user/<str:user_id>/', GetUserNotesView.as_view(), name='get_user_notes'),
]
