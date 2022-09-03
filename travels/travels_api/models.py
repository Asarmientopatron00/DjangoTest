from operator import mod
from django.db import models

# Create your models here.

class Passenger(models.Model):
  identification = models.CharField(max_length=15, unique=True)
  name = models.CharField(max_length=45)

  def __str__(self):
    return self.identification

class Driver(models.Model):
  identification = models.CharField(max_length=15, unique=True)
  name = models.CharField(max_length=45)

  def __str__(self):
    return self.identification

class Bus(models.Model):
  license_plaque = models.CharField(max_length=10, unique=True)
  driver_id = models.ForeignKey(Driver, on_delete= models.CASCADE)

  def __str__(self):
    return self.license_plaque

class Journey(models.Model):
  description = models.CharField(max_length=45)

  def __str__(self):
    return self.description

class JourneyBus(models.Model):
  description = models.CharField(max_length=45)
  journey_id = models.ForeignKey(Journey, on_delete= models.CASCADE)
  bus_id = models.ForeignKey(Bus, on_delete= models.CASCADE)
  datetime_start = models.DateTimeField()
  datetime_finish = models.DateTimeField()

  def __str__(self):
    return self.description, self.datetime_start, self.datetime_finish

class JorneyBusPassenger(models.Model):
  seatNumbers = [
    ('1', '01'),
    ('2', '02'),
    ('3', '03'),
    ('4', '04'),
    ('5', '05'),
    ('6', '06'),
    ('7', '07'),
    ('8', '08'),
    ('9', '09'),
    ('10', '10'),
  ]
  seat = models.CharField(max_length=3, choices=seatNumbers)
  journey_bus_id = models.ForeignKey(JourneyBus, on_delete=models.CASCADE)
  passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)

  def __str__(self):
    return self.seat

