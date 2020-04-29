from django.contrib import admin
from .models import Certificate, Client, Location, Performancedata, Product, Service, Testsequence, Teststandard, User


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificatenumber', 'certid', 'userid',
                    'reportnumber', 'standardid', 'locationid', 'modelnumber')


admin.site.register(Certificate, CertificateAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientid', 'clientname', 'clienttype')


admin.site.register(Client, ClientAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('locationid', 'address1', 'address2', 'city', 'state',
                    'postalcode', 'country', 'phonenumber', 'faxnumber', 'clientid')


admin.site.register(Location, LocationAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('modelnumber', 'productname', 'celltechnology', 'cellman', 'numcells', 'numcellsinseries', 'numseriesstrings', 'numdiodes', 'productlength', 'productwidth', 'productweight',
                    'superstratetype', 'superstrateman', 'substratetype', 'substrateman', 'frametype', 'frameadhesive', 'encapsulanttype', 'encapsulantman', 'junctionboxtype', 'junctionboxman')


admin.site.register(Product, ProductAdmin)


class TeststandardAdmin(admin.ModelAdmin):
    list_display = ('standardid', 'standardname', 'description')


admin.site.register(Teststandard, TeststandardAdmin)
