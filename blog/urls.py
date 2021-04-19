from django.urls import path

from blog.views import get_profile, get_my_age, PostView

urlpatterns = [
    path('hello/', get_profile),
    path('my-age/', get_my_age),
    path('posts/', PostView.as_view()),
]


