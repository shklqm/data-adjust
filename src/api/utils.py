from django.db.models import Sum, FloatField
from django.db.models.functions import Cast

from api.models import Record


def filter_queryset(request, queryset):
    """
    Parse filter fields and return the new queryset

    :param request:
    :param queryset:
    :return QuerySet:
    """
    filter_field_options = {}

    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    date = request.GET.get('date', None)
    date_from = request.GET.get('date_from', None)
    date_to = request.GET.get('date_to', None)

    channels = request.GET.getlist('channel')
    countries = request.GET.getlist('country')
    operating_systems = request.GET.getlist('os')

    if date:
        filter_field_options['{}'.format('date')] = date
    if year:
        filter_field_options['{}__{}'.format('date', 'year')] = year
    if month:
        filter_field_options['{}__{}'.format('date', 'month')] = month
    if date_from:
        filter_field_options['{}__{}'.format('date', 'gt')] = date_from
    if date_to:
        filter_field_options['{}__{}'.format('date', 'lte')] = date_to
    if channels:
        filter_field_options['{}__{}'.format('channel', 'in')] = channels
    if countries:
        filter_field_options['{}__{}'.format('country', 'in')] = countries
    if operating_systems:
        filter_field_options['{}__{}'.format('os', 'in')] = operating_systems

    if filter_field_options:
        queryset = queryset.filter(**filter_field_options)

    return queryset


def sort_queryset(request, queryset):
    """
    Parse sort field and sort type and return the new queryset

    :param request:
    :param queryset:
    :return QuerySet:
    """
    sort_field = request.GET.get('order_by', None)
    if sort_field is not None:
        order_type = request.GET.get('order_type', '')
        if order_type.lower() == 'desc':
            sort_field = '-' + sort_field

    if sort_field:
        queryset = queryset.order_by(sort_field)

    return queryset


def get_group_by_fields(request):
    """
    Parse group by fields and return the new queryset

    :param request:
    :param queryset:
    :return QuerySet:
    """
    group_by_field_names = []
    for field in request.GET.getlist('group_by'):
        group_by_field_names.append(field)

    return group_by_field_names


def get_range_queryset(request):
    group_by_field_names = get_group_by_fields(request)

    queryset = Record.objects.values(*group_by_field_names).\
        annotate(impressions=Sum('impressions'), clicks=Sum('clicks'))

    queryset = filter_queryset(request, queryset)
    queryset = sort_queryset(request, queryset)

    return queryset


def get_installs_queryset(request):
    group_by_field_names = get_group_by_fields(request)

    queryset = Record.objects.values(*group_by_field_names).annotate(installs=Sum('installs'))

    queryset = filter_queryset(request, queryset)
    queryset = sort_queryset(request, queryset)

    return queryset


def get_revenue_queryset(request):
    group_by_field_names = get_group_by_fields(request)

    queryset = Record.objects.values(*group_by_field_names).annotate(revenue=Sum('revenue'))

    queryset = filter_queryset(request, queryset)
    queryset = sort_queryset(request, queryset)

    return queryset


def get_metric_queryset(request):
    group_by_field_names = get_group_by_fields(request)

    queryset = Record.objects.values(*group_by_field_names).\
        annotate(cpi=Cast(Sum('spend') / Sum('installs'), FloatField()))

    queryset = filter_queryset(request, queryset)
    queryset = sort_queryset(request, queryset)

    return queryset
