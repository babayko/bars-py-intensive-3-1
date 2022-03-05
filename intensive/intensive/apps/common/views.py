import json

from django.http import (
    JsonResponse,
)
from django.shortcuts import (
    render,
)
from django.views import (
    View,
)



class Task1View(View):
    """
    Вывести список всех рецептов. Элементом списка будет являться список, содержащий следующие значения:
        - Email автора;
        - Название рецепта;
        - Описание рецепта.
    """

    def get(self, request, **kwargs):
        recipes = list(
            Recipe.objects.values_list(
                'userrecipe__user',
                'title',
                'description'
            )
        )

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строку ниже
        return render(request, 'task.html', {'json_data': json.dumps(dict(recipes=recipes), ensure_ascii=False)})

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse
        #return JsonResponse(dict(recipes=recipes), json_dumps_params=dict(ensure_ascii=False))


class Task2View(View):
    """
    Вывести детальную информацию рецепта с идентификатором 1.
    Нужно получить информацию о шагах приготовления, списке необходимых продуктов для приготовления

    Шаги представляют собой список:
        - Название шага;
        - Описание шага.

    Продукты представляют собой список:
        - Название продукта;
        - Описание продукта;
        - Количество продукта;
        - Аббревиатура единицы измерения продукта.
    """

    def get(self, request, **kwargs):
        recipe = Recipe.objects.get(id=1)

        steps = list(
            CookStep.objects.values_list(
                'title', 'description'
            ).filter(
                recipe=recipe)
            )

        products = list(
            Recipe.objects.values_list(
                'product__title',
                'product__description',
                'count',
                'unit__abbreviation'
            ).filter(recipe=recipe)
        )

        recipe_data = {
            'steps': steps,
            'products': products,
        }

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строки ниже
        return render(
             request=request,
             template_name='task.html',
             context={'json_data': json.dumps(dict(recipe_data=recipe_data), ensure_ascii=False, default=str)},
         )

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse
        #return JsonResponse(dict(recipe_data=recipe_data), json_dumps_params=dict(ensure_ascii=False, default=str))


class Task3View(View):
    """
    Вывести список рецептов, аналогичный заданию 1, только дополнительно должно быть выведено количество лайков. Сам
    список должен быть отсортирован по количеству лайков по убыванию.
    Элементом списка будет являться список, содержащий следующие значения:
        - Email автора;
        - Название рецепта;
        - Описание рецепта;
        - Количество лайков.
    """

    def get(self, request, **kwargs):
        recipes = list(
            Recipe.objects.annotate(
                likes=Count('vote', filter=F('vote__is_like'))
            ).values_list(
                'userrecipe__user',
                'title',
                'description',
                'likes'
            ).order_by('likes')
        )

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строки ниже
        return render(
             request=request,
             template_name='task.html',
             context={'json_data': json.dumps(dict(recipes=recipes), ensure_ascii=False, default=str)},
         )

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse
        #return JsonResponse(dict(recipes=recipes), json_dumps_params=dict(ensure_ascii=False, default=str))


class Task4View(View):
    """
    Вывести списки TOP 3 авторов и TOP 3 голосующих с количеством рецептов для первых и количеством
    голосов для вторых. В выборке должен быть указан тип в отдельной колонке - Автор или Пользователь.

    Элементом списка авторов будет являться список, содержащий следующие значения:
        - Статус;
        - Email;
        - Количество рецептов.

    Элементом списка пользователей будет являться список, содержащий следующие значения:
        - Статус;
        - Email;
        - Количество лайков.

    """

    def get(self, request, **kwargs):
        authors = list(
            CustomUser.objects.filter(
                author__isnull=False
            ).annotate(
                status=Value('Автор'),
                number_of_recipes=Count('userrecipe')
            ).values_list(
                'status',
                'email',
                'number_of_recipes'
            ).order_by('-number_of_recipes')[:3]
        )

        voters = list(
            CustomUser.objects.filter(
                author__isnull=True
            ).annotate(
                status=Value('Пользователь'),
                number_of_likes=Count('vote')
            ).values_list(
                'status',
                'email',
                'number_of_likes'
            ).order_by('-number_of_likes'[:3])
        )

        data = {
            'authors': authors,
            'voters': voters,
        }

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строки ниже
        return render(
             request=request,
             template_name='task.html',
             context={'json_data': json.dumps(dict(data=data), ensure_ascii=False, default=str)},
         )

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse
        #return JsonResponse(dict(data=data), json_dumps_params=dict(ensure_ascii=False, default=str))


class Task5View(View):
    """
    Все продукты указаны для приготовления одной порции блюда. Нужно вывести список необходимых продуктов для
    приготовления блюда с идентификатором 3 в количестве пяти порций.

    Элементом списка продуктов будет являться список, содержащий следующие значения:
        - Название рецепта;
        - Описание рецепта;
        - Название продукта;
        - Количество;
        - Аббревиатура единицы измерения.
    """

    def get(self, request, **kwargs):
        recipe_products = list(
            RecipeProduct.objects.filter(
                recipe_id=3,
            ).annotate(
                number_of=(F('count') * 5),
            ).values_list(
                'recipe__title',
                'recipe__description',
                'product__title',
                'number_of',
                'unit__abbreviation'
            )
        )

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строки ниже
        return render(
             request=request,
             template_name='task.html',
             context={'json_data': json.dumps(dict(recipe_products=recipe_products), ensure_ascii=False, default=str)},
         )

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse
        #return JsonResponse(
        #    data=dict(recipe_products=recipe_products), json_dumps_params=dict(ensure_ascii=False, default=str),
        #)
