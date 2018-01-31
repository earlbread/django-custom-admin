from django.contrib import admin

from user.models import User, UserForChangingEmail, EmailChangeRequest


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'mobile')
    readonly_fields = ('email', 'name', 'mobile')


class EmailChangeRequestInline(admin.StackedInline):
    model = EmailChangeRequest
    extra = 0

    readonly_fields = ('new_email', 'id_card')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(UserForChangingEmail)
class UserForChangingEmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name')
    fields = ('email', 'name')
    readonly_fields = ('email', 'name')
    inlines = [EmailChangeRequestInline]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(EmailChangeRequest)
class UserEmailChangeAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user.email = form.cleaned_data['new_email']
        obj.user.save()

        super().save_model(request, obj, form, change)
