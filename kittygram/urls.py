from django.urls import path

from cats.views import cat_list, hello, cat_update, cat_patch

urlpatterns = [
   path('cats/', cat_list),
   path('hello/', hello),
   path('cat_update/<int:id>/', cat_update),
   path('cat_patch/<int:id>/', cat_patch),
]
