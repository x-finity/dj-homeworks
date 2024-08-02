from django.urls import path

from measurement.views import SensorsList, SensorsDetail, MeasurementCreate

urlpatterns = [
    path("sensors/", SensorsList.as_view()),
    path("sensors/<int:pk>/", SensorsDetail.as_view()),
    path("measurements/", MeasurementCreate.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
