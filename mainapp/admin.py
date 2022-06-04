from django.contrib import admin
from mainapp.models import Course, News, Lesson, CoursesTeachers


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'deleted', 'created_at',)
    list_filter = ('deleted', 'created_at')
    ordering = ('pk',)
    search_fields = ('title', 'intro', 'body',)
    actions = ('mark_as_delete')

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass

@admin.register(CoursesTeachers)
class CoursesTeachersAdmin(admin.ModelAdmin):
    pass

