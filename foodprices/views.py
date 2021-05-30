import datetime

from django.http import HttpResponse
from django.template import Template, Context


def home_food_prices(request):
    name = 'Gaby'
    external_index_doc = open('/code/templates/foodprices/index.html')
    index_template = Template(external_index_doc.read())
    external_index_doc.close()

    index_context = Context()
    index_doc = index_template.render(index_context)

    return HttpResponse(index_doc)


def get_date(request):
    now = datetime.datetime.now()
    return HttpResponse(now)


def calculate_age(request, age, year):
    period = year - 2021
    future_age = age + period
    return HttpResponse(f"En el año {year} tendrás {future_age}")
