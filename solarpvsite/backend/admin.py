from django.contrib import admin
from .models import Certificate, Client, Location, Performancedata, Product, Service, Testsequence, Teststandard, User

admin.site.register(Certificate)
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Performancedata)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Testsequence)
admin.site.register(Teststandard)
admin.site.register(User)
