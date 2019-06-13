from django.http import JsonResponse
from django.views import View

from api.utils import get_range_queryset, get_installs_queryset, get_revenue_queryset, get_metric_queryset


class RangeAPI(View):
    def get(self, request):
        query_set = get_range_queryset(request)

        data = list(query_set)
        return JsonResponse({'data': data}, safe=False)


class InstallsAPI(View):
    def get(self, request):
        query_set = get_installs_queryset(request)

        data = list(query_set)
        return JsonResponse({'data': data}, safe=False)


class RevenueAPI(View):
    def get(self, request):
        query_set = get_revenue_queryset(request)

        data = list(query_set)
        return JsonResponse({'data': data}, safe=False)


class MetricAPI(View):
    def get(self, request):
        query_set = get_metric_queryset(request)

        data = list(query_set)
        return JsonResponse({'data': data}, safe=False)
