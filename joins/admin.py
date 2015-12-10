from django.contrib import admin

# Register your models here.

from .models import Join

class JoinAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'friends', 'timestamp', 'update', 'ref_id', 'ip_addres']
	class Meta:
		model = Join

admin.site.register(Join, JoinAdmin)
