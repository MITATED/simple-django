from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from .models import TableFirst, TableSecond


def index(request):
    table_first = TableFirst.objects.first()
    if table_first is None:
        raise ObjectDoesNotExist('There are no records in TableFirst!')
    fields_second = TableSecond.objects.filter(table_first_id=table_first.id).values_list('field_second',
                                                                                          flat=True).all()

    context = {
        'title': 'Simple project',
        'field_first': table_first.field_first,
        'fields_second': list(fields_second)
    }
    return render(request, 'hello_world/hello-world.html', context)
