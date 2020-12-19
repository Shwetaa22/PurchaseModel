from django.db import connection
from django.shortcuts import render
from django.db.models import Sum, Count
from django.http import JsonResponse
from .models import PurchaseModel,PurchaseStatusModel


def home(request):
    return render(request, 'home.html')


def bar_chart(request):
    labels = []
    data = []
    date_range = (request.GET.get("date_rang")).split(" - ") if request.GET.get("date_rang") else None

    queryset = PurchaseStatusModel.objects.values('purchase__purchaser_name','purchase__quantity','created_at').order_by(
        '-created_at')

    truncate_date = connection.ops.date_trunc_sql('month', 'created_at')
    qs = PurchaseStatusModel.objects.extra({'month': truncate_date})
    queryset = qs.values('month').annotate(total_quant=Sum('purchase__quantity')).order_by('month')
    if date_range:
        queryset = queryset.filter(created_at__range=date_range)

    for entry in queryset:
        labels.append(entry['month'])
        data.append(entry['total_quant'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })