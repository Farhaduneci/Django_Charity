from accounts.models import User
from django.shortcuts import render


def about_us(request):
    users = User.objects.all()
    return render(
        request, "about_us.html", {"names": [user.get_full_name() for user in users]}
    )
