from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats = models.IntegerField()
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    days = models.CharField(max_length=50, default="2 Day / 3 Night")
    travel_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name



class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    guest = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.destination.name}"




class Blog_Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title