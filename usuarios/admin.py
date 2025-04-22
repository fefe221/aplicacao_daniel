from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # mostre o referral_parent na listagem
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'referral_parent')
    fieldsets = UserAdmin.fieldsets + (
        ('Indicação', {'fields': ('referral_parent',)}),
    )
