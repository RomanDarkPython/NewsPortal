from django.urls import path

from .views import NewsList, PostDetail, IndexView
from .views import PostCreate, PostUpdate, PostDelete
from .views import NewsCreate, NewsUpdate, NewsDelete
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from .views import upgrade_me
from .views import CategoryList
from .views import CategoryListView
from .views import subscribe


urlpatterns = [
    path('', NewsList.as_view(),  name='posts_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('index/', IndexView.as_view(template_name = 'index.html'), name='index'),
    path('login/signup/', BaseRegisterView.as_view(template_name = 'signup.html'), name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
    path('categories/', CategoryList.as_view(template_name = 'categories.html'), name='categories'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='posts_of_categories_list'),
    path('subscribe/', subscribe, name = 'subscribe')
]