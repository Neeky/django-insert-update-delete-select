from django.urls import path
from .views import person, aritcle

urlpatterns = [
    path('api/person/detail/<int:pk>', person.PersonDetailView.as_view(),
         name="person-detail-view"),
    path('api/person/list-all/', person.PersonListView.as_view(),
         name="person-list-all-view"),
    path('api/person/list-last/<int:lmt>',
         person.PersonListLastView.as_view(), name="person-list-last-view"),
    path('api/person/create', person.PersonCreateView.as_view(),
         name="person-create-view"),
    path('api/person/update/<int:pk>',
         person.PersonUpdateView.as_view(), name="person-update-view"),
    path('api/person/delete/<int:pk>',
         person.PersonDeleteView.as_view(), name="person-delete-view"),
    # aritcle
    path('api/article/create', aritcle.ArticleCreateView.as_view(),
         name="article-create-view")
]
