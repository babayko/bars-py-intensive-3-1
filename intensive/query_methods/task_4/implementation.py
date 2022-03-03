from query_methods.models import OrderItem
from django.db.models import Sum


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """
    item = OrderItem.objects.filter(
        order__date_formation__range=[begin, end]
    ).values(
        'product__name'
    ).annotate(
        amount=Sum('count')
    ).order_by(
        '-amount'
    ).first()
    return [(item['product__name'], int(item['amount']))] if item else []
