from django.contrib import admin
from userauths.models import User, ContactUs, Profile

# render admin look for user model
class UserAdmin(admin.ModelAdmin):
    # set list display to control which fields are displayed on the change_list page of the admin
    list_display = ['username', 'email', 'bio']

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject']

# imports an admin module in each installed app. Registers model within each admin
admin.site.register(User, UserAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Profile)