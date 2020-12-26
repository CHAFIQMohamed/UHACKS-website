from django.contrib import admin
from . import models

class participantAdmin(admin.ModelAdmin):
	list_display = ("upper_case_f_name", "email", "num_tel", "school", "project_name")
	search_fields = ['f_name', "email", "school", "project_name"]
	ordering = ['created']
	list_filter = ["school", "theme"]
	date_hierarchy = 'created'
	list_per_page = 100
	view_on_site = False

	def upper_case_f_name(self, obj):
		return obj.f_name.upper()
	upper_case_f_name.short_description = 'f_name'


admin.site.register(models.participant, participantAdmin)
