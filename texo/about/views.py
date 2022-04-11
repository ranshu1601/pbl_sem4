from django.shortcuts import render
from .models import detail
def show(request):
    details = detail.objects.all()
    return render(request,'about/about.html',{'detail':details})
