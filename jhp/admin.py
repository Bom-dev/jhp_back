from django.contrib import admin
from jhp.models import User, Application, Interview, Event, Study, History

# Register your models here.

admin.site.register(User)
admin.site.register(Application)
admin.site.register(Interview)
admin.site.register(Event)
admin.site.register(Study)
admin.site.register(History)