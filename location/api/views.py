from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .serializers import *


class ProvinceListView(ListAPIView):
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()


class DistrictListView(CreateAPIView):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        province = serializer.validated_data.get('province_id')

        response_data = self.get_serializer(instance=District.objects.filter(province=province), many=True)

        headers = self.get_success_headers(serializer.data)
        return Response(response_data.data, status=status.HTTP_201_CREATED, headers=headers)


class WardListView(CreateAPIView):
    serializer_class = WardSerializer
    queryset = Ward.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        district = serializer.validated_data.get('district_id')

        response_data = self.get_serializer(instance=Ward.objects.filter(district=district), many=True)

        headers = self.get_success_headers(serializer.data)
        return Response(response_data.data, status=status.HTTP_201_CREATED, headers=headers)


class ProvinceObjectView(RetrieveAPIView):
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()

    @property
    def province_id(self):
        return self.kwargs.get('pk')

    def get_object(self):
        try:
            return Province.objects.get(pk=self.province_id)
        except Province.DoesNotExist:
            raise NotFound()


class DistrictObjectView(RetrieveAPIView):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

    @property
    def district_id(self):
        return self.kwargs.get('pk')

    def get_object(self):
        try:
            return District.objects.get(pk=self.district_id)
        except District.DoesNotExist:
            raise NotFound()


class WardObjectView(RetrieveAPIView):
    serializer_class = WardSerializer
    queryset = Ward.objects.all()

    @property
    def ward_id(self):
        return self.kwargs.get('pk')

    def get_object(self):
        try:
            return Ward.objects.get(pk=self.ward_id)
        except Ward.DoesNotExist:
            raise NotFound()
