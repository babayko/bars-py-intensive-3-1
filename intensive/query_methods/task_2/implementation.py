from query_methods.models import Customer
from django.db.models import Count, Min


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """

    queryset = Customer.objects.filter(
        order__date_formation__gte=begin,
        order__date_formation__lte=end
    ).annotate(
        _count=Count('order'),
        order_before=Min('order__date_formation')
    ).values(
        'name', '_count'
    ).order_by(
        '-_count', 'order_before', 'name'
    ).first()

    return (queryset['name'], queryset['_count']) if queryset else None
