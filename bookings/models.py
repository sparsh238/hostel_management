from django.db import models



class booking(models.Model):
    occupant = models.CharField(max_length=50, blank=True)
    room_number = models.CharField(max_length=10)
    roll_number = models.CharField(max_length = 10, blank=True)
    occupied = models.BooleanField(default=False)
    def __str__(self):
        return self.occupant + " - " + self.room_number + " - " + " roll number " + self.roll_number + "  -   " + str(self.occupied)





