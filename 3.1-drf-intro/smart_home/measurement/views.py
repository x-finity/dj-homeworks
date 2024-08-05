# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorsSerializer


class SensorsList(APIView):

    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorsSerializer(sensors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SensorsDetail(APIView):

    def get(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)

    def patch(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        serializer = SensorDetailSerializer(instance=sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def delete(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        sensor.delete()
        return Response(status=204)


class MeasurementList(APIView):

    def get(self, request):
        measurements = Measurement.objects.all()
        serializer = MeasurementSerializer(measurements, many=True)
        return Response(serializer.data)

    def post(self, request):
        # sensor_id = Sensor.objects.get(id=request.data['sensor'])
        # request.data['sensor'] = sensor_id
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)