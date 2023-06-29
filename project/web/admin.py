from django.contrib import admin
# from .models import Employee, Position#, Genre
from mptt.admin import MPTTModelAdmin
from .models import Role, Worker


class Admin(admin.ModelAdmin):
    pass

class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

# admin.site.register(Employee, CustomMPTTModelAdmin)
# admin.site.register(Position, CustomMPTTModelAdmin)
#admin.site.register(Genre, CustomMPTTModelAdmin)

admin.site.register(Role, Admin)
admin.site.register(Worker, CustomMPTTModelAdmin)
