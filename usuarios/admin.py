from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_referral')
    fieldsets = UserAdmin.fieldsets + (
        ('Indicação', {'fields': ('referral_parent',)}),
    )

    @admin.display(description='Indicado por')
    def get_referral(self, obj):
        return obj.referral_parent.get_full_name() if obj.referral_parent else '-'