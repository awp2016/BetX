from django.contrib import admin

# Register your models here.
from . import models 

from .models import Pronostic
from .models import SignUp
from .models import Match
from .models import Commnent

class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp


admin.site.register(Pronostic)
admin.site.register(Match)
admin.site.register(models.UserProfile)
<<<<<<< HEAD
admin.site.register(models.Commnent)
=======
admin.site.register(Commnent)
>>>>>>> 8cc189c0576f8934ed503e4a66d81394ce41857d
