from query_methods.models import Customer
from django.db.models import Count, Min


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """

    obj_model = Customer.objects.filter(
        order__date_formation__range=[begin, end]
    ).annotate(
        cnt=Count('order'),
        order_before=Min('order__date_formation')
    ).values(
        'name', 'cnt'
    ).order_by(
        '-cnt', 'order_before', 'name'
    ).first()

    return (obj_model['name'], obj_model['cnt']) if obj_model else None
