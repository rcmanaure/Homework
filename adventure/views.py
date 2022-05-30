from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from adventure import models, notifiers, repositories, serializers, usecases


class CreateVehicleAPIView(APIView):
    def post(self, request: Request) -> Response:
        payload = request.data
        vehicle_type = models.VehicleType.objects.create(
            name=payload["vehicle_type"]["name"],
            max_capacity=payload["vehicle_type"]["max_capacity"],
        )
        vehicle = models.Vehicle.objects.create(
            name=payload["name"],
            passengers=payload["passengers"],
            vehicle_type=vehicle_type,
        )
        return Response(
            {
                "id": vehicle.id,
                "name": vehicle.name,
                "passengers": vehicle.passengers,
                "vehicle_type": vehicle.vehicle_type.name,
            },
            status=201,
        )


class CreateServiceAreaAPIView(APIView):
    def post(self, request: Request) -> Response:
        payload = request.data
        # left_station = (
        #     models.ServiceArea.objects.get(pk=payload["left_station"])
        #     if "left_station" in payload
        #     else None
        # )
        # right_station = (
        #     models.ServiceArea.objects.get(pk=payload["right_station"])
        #     if "right_station" in payload
        #     else None
        # )
        service_area = models.ServiceArea.objects.create(
            kilometer=payload["kilometer"],
            gas_price=payload["gas_price"],
            # left_station=4,
            # right_station=4,
        )

        return Response(
            {
                "id": service_area.id,
                "kilometer": service_area.kilometer,
                "gas_price": service_area.gas_price,
                "left_station": service_area.left_station,
                "right_station": service_area.right_station,
            },
            status=201,
        )


class StartJourneyAPIView(generics.CreateAPIView):
    serializer_class = serializers.JourneySerializer

    def perform_create(self, serializer) -> None:
        repo = self.get_repository()
        notifier = notifiers.Notifier()
        usecase = usecases.StartJourney(repo, notifier).set_params(
            serializer.validated_data
        )
        try:
            usecase.execute()
        except usecases.StartJourney.CantStart as e:
            raise ValidationError({"detail": str(e)})

    def get_repository(self) -> repositories.JourneyRepository:
        return repositories.JourneyRepository()


class StopJourneyAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Journey.objects.all()
    serializer_class = serializers.StopJourneySerializer


class ListVehicleViewSet(ListAPIView):
    """
    API endpoint to get full list of vehicles(GET)
    API endpoint of the Vehicle.
    """

    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.ListVehicleSerializer


class GetVehicleViewSet(RetrieveAPIView):
    """
    API endpoint to get vehicle data by license plate(GET)
    API endpoint of the Vehicle.
    """

    lookup_field = "number_plate"
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.ListVehicleSerializer


class ListServiceAreaViewSet(ListAPIView):
    """
    API endpoint to get full list of Service Area(GET)
    API endpoint to Service Area.
    """

    queryset = models.ServiceArea.objects.all()
    serializer_class = serializers.ListServiceAreaSerializer


class GetServiceAreaViewSet(RetrieveAPIView):
    """
    API endpoint to get service area by kilometer(GET)
    API endpoint of the Service Area.
    """

    lookup_field = "kilometer"
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.ListServiceAreaSerializer
