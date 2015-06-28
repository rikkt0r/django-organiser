from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Q

from .models import UserProfile, RegularUser, Staff


class UserDetailsInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'details'


class UserAdmin(UserAdmin):
    inlines = (UserDetailsInline,)

    readonly_fields = ('date_joined', 'last_login')

    list_display = ('id', 'username', 'email', 'date_joined', 'is_staff', 'is_active')
#
#     fieldsets = [
#         ('General',     {'fields': ['name', 'email']}),
#         ('Password',    {'fields': ['password']}),
#         ('Dates',       {'fields': ['date_created', 'date_logged']})
#     ]


class StaffAdmin(UserAdmin):
    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        qs = qs.filter(Q(is_staff=True) | Q(is_superuser=True))
        return qs


class RegularUserAdmin(StaffAdmin):
    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        qs = qs.filter(Q(is_staff=False) | Q(is_superuser=False))
        return qs


admin.site.unregister(User)
admin.site.register(Staff, StaffAdmin)
admin.site.register(RegularUser, RegularUserAdmin)
