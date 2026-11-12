from django.db import models
from django.core.exceptions import ValidationError

class Station(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва станції")
    city = models.CharField(max_length=100, verbose_name="Місто")

    def __str__(self):
        return f"{self.name} ({self.city})"

    class Meta:
        verbose_name = "Станція"
        verbose_name_plural = "Станції"


class Train(models.Model):
    number = models.CharField(max_length=20, unique=True, verbose_name="Номер потяга")
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Назва потяга (маршрут)")
    total_seats = models.IntegerField(verbose_name="Кількість місць")

    def __str__(self):
        return f"Потяг №{self.number} {self.name if self.name else ''}"

    class Meta:
        verbose_name = "Потяг"
        verbose_name_plural = "Потяги"


class Route(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, verbose_name="Потяг")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна квитка (грн)")

    def __str__(self):
        return f"Маршрут для потяга №{self.train.number}"

    class Meta:
        verbose_name = "Маршрут / Рейс"
        verbose_name_plural = "Маршрути руху"


class RoutePoint(models.Model):

    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='points', verbose_name="Маршрут")
    station = models.ForeignKey(Station, on_delete=models.CASCADE, verbose_name="Станція")
    
    arrival_time = models.TimeField(blank=True, null=True, verbose_name="Час прибуття")
    departure_time = models.TimeField(blank=True, null=True, verbose_name="Час відправлення")
    
    station_order = models.PositiveIntegerField(verbose_name="Порядковий номер зупинки")

    def __str__(self):
        arr = self.arrival_time if self.arrival_time else "Н/Д"
        dep = self.departure_time if self.departure_time else "Н/Д"
        return f"{self.station_order}. {self.station.name} (Приб: {arr}, Відпр: {dep})"

    class Meta:
        verbose_name = "Зупинка маршруту"
        verbose_name_plural = 'Зупинки маршруту'
        ordering = ['station_order']
