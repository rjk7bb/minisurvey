from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Question, Response, Player

# Register your models here.


class PlayerInLine(admin.StackedInline):
    model = Player
    can_delete = False
    verbose_name_plural = 'Player'



class ResponseInline(admin.StackedInline):
    model = Response
    extra = 0


class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),

    ]
    inlines = [ResponseInline]

    list_display = ('question_text',)

    search_fields = ['question_text']


class CustomUserAdmin(UserAdmin):
    inlines = (PlayerInLine, QuestionInLine)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Response)

