from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), #to show an individual component in the database
    path('', PostList.as_view(), name='listcreate'), #to show all the data in the database
]

