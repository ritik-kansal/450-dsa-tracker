from django.contrib import admin
from .models import Mark_update, Pair_programmer, Question, Question_user_mark, Topic, User, User_asked_for_pair_programming

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','user_name','password','linkedin','github']

# can also register like this
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Question_user_mark)
admin.site.register(Pair_programmer)
admin.site.register(User_asked_for_pair_programming)
admin.site.register(Mark_update)