from django.urls import path
from .views import (
    home,
    room,
    createRoom,
    updateRoom,
    deleteRoom,
    loginPage,
    logoutUser,
    registerPage,
    deleteMessage,
    userProfile,
    updateUser,
    topicsRequired,
    activityPage,
)


urlpatterns = [
    path("", home, name="home"),
    path("room/<str:pk>", room, name="room"),
    path("create_room", createRoom, name="create_room"),
    path("update_room/<str:pk>", updateRoom, name="update_room"),
    path("delete_room/<str:pk>", deleteRoom, name="delete_room"),
    path("delete_message/<str:pk>", deleteMessage, name="delete_message"),
    path("update_user/", updateUser, name="update_user"),
    path("profile/<str:pk>", userProfile, name="user-profile"),
    path("login/", loginPage, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("logout/", logoutUser, name="logout"),
    path("register/", registerPage, name="register"),
    path("topics/", topicsRequired, name="topics"),  # mobile screen
    path("activity/", activityPage, name="activity"),  # mobile screen
]
