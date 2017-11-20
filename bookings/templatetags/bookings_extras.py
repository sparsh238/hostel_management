from django import template
from bookings.models import booking

register = template.Library()

@register.assignment_tag
def is_occupied(roomno):
    occu = 0
    arr = booking.objects.filter(room_number=roomno).values_list("occupied",flat=True)

    if not arr:
        return 0
    else:
        fil = booking.objects.filter(room_number=roomno).values_list("occupied", flat=True)[0]
        if fil == True:
            occu = 1
            return occu
        else:
            return occu

