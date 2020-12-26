from django.db import models
from datetime import datetime

# Create your models here
class participant(models.Model):
	f_name = models.CharField(max_length=100)
	l_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=250)
	num_tel = models.IntegerField()
	choix_1 = (
		('Al Khwarizmi','Al Khawarizmi'),
		('FGSES','FGSES'),
		('EMINES','EMINES'),
		('ABS','ABS'),
		('SCI','SCI'),
		('SHBM','SHBM'),
		('SAP+D','SAP+D'),
		('CBS/GPE','CBS/GPE'),
		('MSN','MSN'),
		('GTI','GTI'),
		('GSM','GSM'),
		('CIAM','CIAM'),
		('1337','1337'),
		('MAHIR','MAHIR'),
	)
	school = models.CharField(max_length=250,choices=choix_1)
	first_participant = models.CharField(max_length=100,blank=True,null=True)
	second_participant = models.CharField(max_length=100,blank=True,null=True)
	third_participant = models.CharField(max_length=100,blank=True,null=True)
	project_name = models.CharField(max_length=100,blank=True,null=True)
	choix_2=(
		('Education','Education'),
		('Mental Health And Wellness','Mental Health And Wellness'),
		('Student Organizations And Events','Student Organizations And Events'),
	)
	theme = models.CharField(max_length=250,choices=choix_2,blank=True,null=True)
	description = models.CharField(max_length=500,blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True,null=True)

	def __str__(self):
		return self.l_name +'    '+ self.f_name +'    '+ self.email + '    ' + str(self.num_tel)




