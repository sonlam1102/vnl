from rest_framework import serializers

from location.models import Province, District, Ward


class ProvinceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Province
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    province_id = serializers.PrimaryKeyRelatedField(queryset=Province.objects.all(), write_only=True, required=True)
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = District
        fields = ['id', 'name', 'province_id']


class WardSerializer(serializers.ModelSerializer):
    district_id = serializers.PrimaryKeyRelatedField(queryset=District.objects.all(), write_only=True, required=True)
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Ward
        fields = ['id', 'name', 'district_id']
