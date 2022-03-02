from query_methods.models import Order


def get_order_count_by_customer(name):
    """Возвращает количества заказов по имени покупателя

    Args:
        name: имя покупателя

    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """
    count_of_orderds = Order.objects.filter(customer__name=name).count()

    return count_of_orderds
