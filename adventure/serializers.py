from rest_framework import serializers

from adventure import models


class JourneySerializer(serializers.Serializer):
    name = serializers.CharField()
    passengers = serializers.IntegerField()


class StopJourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Journey
        fields = ["id", "start", "end", "vehicle_id"]
        read_only_fields = ["id", "start", "vehicle_id"]


class ListVehicleSerializer(serializers.Serializer):

    name = serializers.CharField()
    passengers = serializers.IntegerField()
    number_plate = serializers.CharField()
    vehicle_type = serializers.CharField()
    fuel_efficiency = serializers.DecimalField(max_digits=6, decimal_places=2)
    fuel_tank_size = serializers.DecimalField(max_digits=6, decimal_places=2)


class ListServiceAreaSerializer(serializers.Serializer):
    kilometer = serializers.IntegerField()
    gas_price = serializers.IntegerField()
