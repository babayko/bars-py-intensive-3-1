from query_methods.models import OrderItem, ProductCost
from django.db.models import Count, Min, Sum, F, Max, Avg
from decimal import (
    Decimal,
)

def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """

