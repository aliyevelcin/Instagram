from django.contrib import admin
from accounts.models import User

admin.site.register([User])



# class UserAdmin(admin.ModelAdmin):
#   list_display = ("firstname", "lastname", "joined_date",)
#   prepopulated_fields = {"slug": ("firstname", "lastname")}
  
# admin.site.register(User, UserAdmin)