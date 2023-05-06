from django.urls import path

from .views import HomePageView, AboutPageView, RegisterPageView, TestQuestionListView, \
    question_detail_view, user_results_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name="about"),
    path("register/", RegisterPageView.as_view(), name="register"),
    path("test/", TestQuestionListView.as_view(), name="test"),
    path("<int:pk>/", question_detail_view, name="answers"),
    path("results/", user_results_view, name="results"),

]
