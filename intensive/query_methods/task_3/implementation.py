from query_methods.models import OrderItem, ProductCost, ProductCount


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени
            Напишите функцию, которая выводит заказ с наибольшей общей суммой за период.
            Если несколько заказов имеют одинаковую сумму - вывести тот, чей номер больше.
    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """

    goods = OrderItem.objects.filter(
        order__date_formation__range=[begin, end]
    )

    product = {}
    for item in goods:
        """ Формируем кол-во товара в наличии, только за текущий период """
        remaining_items_in_stock = ProductCount.objects.filter(
            begin__lte=item.order.date_formation,
            end__gte=item.order.date_formation,
            product__name=item.product.name).first()

        if remaining_items_in_stock:
            if remaining_items_in_stock.value < item.count:
                final_count_of_items = remaining_items_in_stock.value
            else:
                final_count_of_items = item.count
        """ Формируем цену cost, только если попадаем в период активной цены """
        cost = ProductCost.objects.filter(
            begin__lte=item.order.date_formation,
            end__gte=item.order.date_formation,
            product__name=item.product.name).first()

        if cost:
            if product.get(item.order.number):
                sum = product[item.order.number] + cost.value * final_count_of_items
                product[item.order.number] = sum
            else:
                product[item.order.number] = cost.value * final_count_of_items

    if product:
        product_max = max(product, key=product.get)
        result = (product_max, product[product_max])
    else:
        result = None

    return result
