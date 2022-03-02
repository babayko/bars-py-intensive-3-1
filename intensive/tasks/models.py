from django.db import models
from django.db.models import Manager
from django.db import connection


class WorkerManager(models.Manager):
    """
    Менеджер для работы с активными сотрудниками
    """
    def get_queryset(self):
        """
        Переопределенный кверисет с фильтрацией сотрудников с заданной датой
        принятия на работу и с не пустым табельным номером отличным от 0
        """

        return super().get_queryset().filter(startwork_date__isnull=False, tab_num__gt=0)

    def get_workers_info(self):
        """
            Получение  списка строк в которых содержится
        фамилия, имя, табельный номер сотрудника а также название подразделения в котором числится
        Строки упорядочены по фамилии и имени сотрудника.
        Каждая строка должна быть в формате вида: Васильев Василий, 888, Подразделение №1
        """
        list_lists = super().get_queryset().values_list(
            'first_name', 'last_name', 'tab_num', 'department__name'
                           ).order_by('last_name', 'first_name')
        result = [(val[0] + ' '.join(val[1]) + ', ' + str(val[2]) + ', ' + val[3]) for val in list_lists]
        return result


class Department(models.Model):
    name = models.CharField('Наименование', max_length=30)

    def __str__(self):

        return self.name

    @classmethod
    @property
    def get_active_worker_count(cls):
        """
        Количество активных сотрудников подразделения
        """
        queryset = cls.objects.filter(worker__startwork_date__isnull=False,
                                      worker__tab_num__gt=0).values_list('id', flat=True).count()
        return queryset

    @classmethod
    @property
    def get_all_worker_count(cls):
        """
        Количество всех сотрудников подразделения
        """
        queryset = cls.objects.filter(
            worker__department__isnull=False
            ).values_list('id', flat=True).count()
        return queryset

    class Meta:
        db_table = 'department'


class Worker(models.Model):
    """
    Сотрудник
    """

    objects = WorkerManager()
    objects_all = Manager()

    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    startwork_date = models.DateField('Дата выхода на работу', null=True, )
    tab_num = models.IntegerField('Табельный номер', default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.last_name} + {self.first_name}'

    class Meta:
        db_table = 'workers'
