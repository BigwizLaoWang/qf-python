# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import FireCart
# Create your views here.
def my_carts(req):
    data = FireCart.objects.filter(speed__lte=280).order_by("-speed")
    result = {
        "title":"火cart",
        "carts":data
    }
    return render(req,"trains.html",result)

def search_by_name(req):
   # print(dir(req))
    param=req.GET
    kw = param.get("kw")
    res = FireCart.objects.filter(
        name__contains=kw
    )
    # res=FireCart.objects.filter(
    # name__endswith=kw
    # )
    # res=FireCart.objects.filter(
    #     speed__in=[300,251]
    # )
    # req = FireCart.objects.filter(
    #     create_date__year=2018
    # )

    return render(req,"trains.html",{"carts":res})

