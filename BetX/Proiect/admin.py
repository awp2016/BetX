from django.contrib import admin

# Register your models here.
from . import models 

from .models import Pronostic
from .models import SignUp
from .models import Match

class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp


admin.site.register(Pronostic)
admin.site.register(Match)
admin.site.register(models.UserProfile)
admin.site.register(models.Commnent)