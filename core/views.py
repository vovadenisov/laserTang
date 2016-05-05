import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from core.models import Category


def get_items(request):
    all_category = Category.objects.all().prefetch_related("items")
    data = dict()
    for category in all_category:
        data.update(
            {unicode(category.name): [
                {"name": item.name, "img": item.img, "link": item.link} for item in category.items.all()]
            }
        )
    return HttpResponse(json.dumps(data), content_type="application/json")