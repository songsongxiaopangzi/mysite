from django.urls import path

from .views import calcVote
from .views import IndexView, QuestionDetailView, QuestionResultView

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>', QuestionDetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', calcVote, name='vote'),
    path('<int:pk>/result/', QuestionResultView.as_view(), name='result'),
]