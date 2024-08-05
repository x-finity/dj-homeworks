from django.urls import path

from measurement.views import SensorsList, SensorsDetail, MeasurementList

urlpatterns = [
    path("sensors/", SensorsList.as_view()),
    path("sensors/<int:pk>/", SensorsDetail.as_view()),
    path("measurements/", MeasurementList.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
