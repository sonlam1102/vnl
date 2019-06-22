from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from .serializers import *


class ProvinceView(ListAPIView):
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()


class DistrictView(CreateAPIView):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        province = serializer.validated_data.get('province_id')

        response_data = self.get_serializer(instance=District.objects.filter(province=province), many=True)

        headers = self.get_success_headers(serializer.data)
        return Response(response_data.data, status=status.HTTP_201_CREATED, headers=headers)


class WardView(CreateAPIView):
    serializer_class = WardSerializer
    queryset = Ward.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        district = serializer.validated_data.get('district_id')

        response_data = self.get_serializer(instance=Ward.objects.filter(district=district), many=True)

        headers = self.get_success_headers(serializer.data)
        return Response(response_data.data, status=status.HTTP_201_CREATED, headers=headers)
