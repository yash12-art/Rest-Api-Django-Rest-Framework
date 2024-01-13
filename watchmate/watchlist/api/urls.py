from django.contrib import admin
from django.urls import path,include
from watchlist.api import views
from rest_framework.routers import DefaultRouter
import watchlist

router = DefaultRouter()
router.register('stream',views.StreamPlatformview,basename="streamplateform")

urlpatterns = [
    path('list/',views.WatchListAV.as_view(),name="movie"),
    path('list/<int:pk>',views.WatchDetailAV.as_view(),name="perform_task"),
    
    path('',include(router.urls)),
    # path('stream/',views.StreamPlatformAV.as_view(),name="stream"),
    # path('stream/<int:pk>',views.StreamPlatformDetailsAV.as_view(),name="stream-details"),
    # path('review/<int:pk>',views.ReviewDetails.as_view(),name="review-details"),
    # path('review/',views.ReviewList.as_view(),name="review-details"),
    
    #Review for particular movie yha mein chcek kr rha hu ki suppose move 2 ko kitne reqvies mile hai
    path('<int:pk>/reviews',views.ReviewList.as_view(),name="review-list"),
    
    #individual review  yha mein check krunga mere dwara diya gya koi bhioi review kholo or usko edit krdo
    path('reviews/<int:pk>',views.ReviewDetails.as_view(),name="review-details"),
    
    #review create for particular movie kisi particular movie ko review dunga
    path('<int:pk>/review-create',views.ReviewCreate.as_view(),name="review-create"),


]
