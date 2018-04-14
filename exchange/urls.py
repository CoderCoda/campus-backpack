from django.urls import path, include
from . import views

app_name = 'exchange'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ListingsView.as_view(), name='course_listings'),
    path('details/<int:pk>/', views.DetailView.as_view(), name='book_details'),

    # users
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('my_profile/<int:pk>', views.UserView.as_view(), name='my_profile'),

    # adding/editing/deleting textbooks
    path('add/', views.TextbookCreateInd.as_view(), name='add_listing'),
    path('edit/<int:book_id>/', views.TextbookUpdate.as_view(), name='edit_listing'),
    path('delete/<int:pk>/', views.TextbookDelete.as_view(), name='delete_listing'),
]