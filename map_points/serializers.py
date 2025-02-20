from rest_framework import serializers
from .models import MapPoints
from django.contrib.gis.geos import Point

# class MapPointSerializer(serializers.ModelSerializer):
#     latitude = serializers.FloatField(write_only=True)
#     longitude = serializers.FloatField(write_only=True)

#     class Meta:
#         model = MapPoints
#         fields = '__all__'

#     # def get_latitude(self,obj):
#     #     return obj.location.coords[1]


#     # def get_longitude(self,obj):
#     #     return obj.location.coords[0]

#     def create(self, validated_data):
#         latitude = validated_data.pop('latitude')
#         longitude = validated_data.pop('longitude')

#         # Create a Point object and assign it to the location field
#         validated_data['location'] = Point(longitude, latitude)

#         return super().create(validated_data)
    



class MapPointSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)

    class Meta:
        model = MapPoints
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['location'] = {
            'type': 'Point',
            'coordinates': [instance.location.coords[0], instance.location.coords[1]],
        }
        return representation

    def create(self, validated_data):
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')

        # Create a Point object and assign it to the location field
        validated_data['location'] = Point(longitude, latitude)

        return super().create(validated_data)