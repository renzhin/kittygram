from rest_framework import viewsets 

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import Cat
# from .serializers import CatSerializer


# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         # Чтобы сериализатор был готов принять список объектов,
#         # в конструктор сериализатора нужно передать
#         # именованный параметр many=True
#         # serializer = CatSerializer(data=request.data, many=True)
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def cat_update(request, id):
#     cat = Cat.objects.get(id=id)
#     serializer = CatSerializer(cat, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])  # Применили декоратор и указали разрешённые методы
# def hello(request):
#     # По задумке, в ответ на POST-запрос нужно вернуть JSON с теми данными,
#     # которые получены в запросе.
#     # Для этого в объект Response() передаём словарь request.data.
#     if request.method == 'POST':
#         return Response({'message': 'Получены данные', 'data': request.data})


# @api_view(['PATCH'])
# def cat_patch(request, id):
#     cat = Cat.objects.get(id=id)
#     serializer = CatSerializer(cat, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def api_posts(request):
#     if request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def api_posts_detail(request, pk):
#     post = Post.objects.get(id=pk)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)

##########

# #  импортируйте в код всё необходимое
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Post
# from .serializers import PostSerializer


# @api_view(['GET', 'POST'])
# def api_posts(request):
#     if request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def api_posts_detail(request, pk):
#     post = Post.objects.get(id=pk)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)


#####

# from rest_framework import generics

# from .models import Post
# from .serializers import PostSerializer


# class APIPostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class APIPostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
