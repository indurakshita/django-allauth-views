
from django.urls import path,include
# from .views import person_create,person_list,person_update,person_delete,person_retrieve
from .views import PersonCreateView, PersonListView, PersonRetrieveView, PersonUpdateView, PersonDeleteView



urlpatterns = [
    # path('',person_create,name="person"),
    # path('personlist/',person_list,name='person_list'),
    # path('retrive/<int:pk>/',person_retrieve,name='person_retrieve'),
    # path('update/<int:pk>/', person_update, name='person_update'),  # Update URL
    # path('delete/<int:pk>/', person_delete, name='person_delete'),



    path('create/', PersonCreateView.as_view(), name='person_create'),
    path('list/', PersonListView.as_view(), name='person_list'),
    path('detail/<int:pk>/', PersonRetrieveView.as_view(), name='person_detail'),
    path('update/<int:pk>/', PersonUpdateView.as_view(), name='person_update'),
    path('delete/<int:pk>/', PersonDeleteView.as_view(), name='person_delete'),
]
