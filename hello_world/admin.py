from django.contrib import admin

from hello_world.models import TableFirst, TableSecond


class TableSecondInline(admin.TabularInline):
    model = TableSecond
    extra = 0


@admin.register(TableFirst)
class TableFirstAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    list_display = (
        'id',
        'field_first'
    )
    list_filter = (
        'id',
        'field_first'
    )
    inlines = (
        TableSecondInline,
    )


@admin.register(TableSecond)
class TableSecondAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    list_display = (
        'id',
        'field_second',
        'table_first_id'
    )
    list_filter = (
        'id',
        'field_second',
        'table_first_id'
    )
