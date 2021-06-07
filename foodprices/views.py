import datetime

from django.http import HttpResponse
from django.shortcuts import render


def get_date():
    return datetime.datetime.now()


def home_food_prices(request):
    my_list = []
    now = get_date()
    person = {"name": "Gaby!", "now": now, "my_list": my_list}

    return render(request, 'foodprices/index.html', person)


def about_view(request):
    now = get_date()
    return render(request, 'foodprices/about.html', {"now": now})


def calculate_age(request, age, year):
    period = year - 2021
    future_age = age + period
    return HttpResponse(f"En el año {year} tendrás {future_age}")
