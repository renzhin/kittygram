from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet

# Создаётся роутер
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]

# from django.urls import path

# from cats.views import cat_list, hello, cat_update, cat_patch

# urlpatterns = [
#    path('cats/', cat_list),
#    path('hello/', hello),
#    path('cat_update/<int:id>/', cat_update),
#    path('cat_patch/<int:id>/', cat_patch),
# ]




# from django.urls import path
# # Импортируйте необходимые view-функции
# from posts.views import api_posts, api_posts_detail

# urlpatterns = [
#     path('api/v1/posts/', api_posts),
#     path('api/v1/posts/<int:pk>/', api_posts_detail)
# ]