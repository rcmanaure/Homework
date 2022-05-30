from django.urls import path

from adventure import views

urlpatterns = [
    path("create-vehicle/", views.CreateVehicleAPIView.as_view()),
    path("create-service-area/", views.CreateServiceAreaAPIView.as_view()),
    path("start/", views.StartJourneyAPIView.as_view()),
    path("stop/<int:pk>", views.StopJourneyAPIView.as_view()),
    path("list-vehicles/", views.ListVehicleViewSet.as_view()),
    path("get-vehicle/<str:number_plate>", views.GetVehicleViewSet.as_view()),
    path("list-service-area/", views.ListServiceAreaViewSet.as_view()),
    path("get-service-area/<int:kilometer>", views.ListServiceAreaViewSet.as_view()),
]
