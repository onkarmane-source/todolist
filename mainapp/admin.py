from django.contrib import admin
from .models import ToDoList, Tag


@admin.action(description='Mark selected task as done')
def mark_done(modeladmin, request, queryset):
    queryset.update(status='D')


class ToDoListAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "timestamp",
        "title",
        "description",
        "due_date",
        "status"
    ]

    ordering = ['timestamp']
    actions = [mark_done]

    search_fields = ('title',)


admin.site.register(ToDoList, ToDoListAdmin)
admin.site.register(Tag)
