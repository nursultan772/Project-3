from django.urls import path, include, re_path
from .views import *


urlpatterns = [

    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),


    path('user_profiles/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='user_profile_list'),
    path('user_profiles/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_profile_detail'),

    path('categories/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('categories/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('products/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='product_list'),
    path('products/<int:pk>/', ProductViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),

    path('product_photos/', ProductPhotosViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='product_photos_list'),
    path('product_photos/<int:pk>/', ProductPhotosViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_photos_detail'),

    path('reviews/', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='review_list'),
    path('reviews/<int:pk>/', ReviewViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='review_detail'),

    path('ratings/', RatingViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='rating_list'),
    path('ratings/<int:pk>/', RatingViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='rating_detail'),

    path('favorites/', FavoriteViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='favorite_list'),
    path('favorites/<int:pk>/', FavoriteViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='favorite_detail'),

    path('baskets/', BasketViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='basket_list'),
    path('baskets/<int:pk>/', BasketViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='basket_detail'),
]