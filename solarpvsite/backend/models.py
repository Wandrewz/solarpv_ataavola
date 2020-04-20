from django.db import models

class Client(models.Model):
    clientid = models.CharField(primary_key=True, max_length=200)
    clientname = models.CharField(max_length=200)
    clienttype = models.CharField(max_length=200)


class Testsequence(models.Model):
    sequence_id = models.CharField(primary_key=True, max_length=200)
    sequence_name = models.CharField(max_length=200)


class Teststandard(models.Model):
    standardid = models.CharField(primary_key=True, max_length=200)
    standardname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    publisheddate = models.DateField(auto_now_add=True)


class Product(models.Model):
    modelnumber = models.CharField(primary_key=True, max_length=200)
    productname = models.CharField(max_length=200)
    celltechnology = models.CharField(max_length=200)
    cellman = models.CharField(max_length=200)
    numcells = models.IntegerField()
    numcellsinseries = models.IntegerField()
    numseriesstrings = models.IntegerField()
    numdiodes = models.IntegerField()
    productlength = models.FloatField()
    productwidth = models.FloatField()
    productweight = models.FloatField()
    superstratetype = models.CharField(max_length=200)
    superstrateman = models.CharField(max_length=200)
    substratetype = models.CharField(max_length=200)
    substrateman = models.CharField(max_length=200)
    frametype = models.CharField(max_length=200)
    frameadhesive = models.CharField(max_length=200)
    encapsulanttype = models.CharField(max_length=200)
    encapsulantman = models.CharField(max_length=200)
    junctionboxtype = models.CharField(max_length=200)
    junctionboxman = models.CharField(max_length=200)


class Service(models.Model):
    serviceid = models.CharField(primary_key=True, max_length=200)
    servicename = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    isfirequired = models.CharField(max_length=3)
    fifrequency = models.CharField(max_length=200)
    standardid = models.ForeignKey(Teststandard, on_delete=models.CASCADE)


class User(models.Model):
    userid = models.CharField(primary_key=True, max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200)
    jobtitle = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    officephone = models.IntegerField()
    cellphone = models.IntegerField()
    prefix = models.CharField(max_length=200)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)


class Location(models.Model):
    locationid = models.CharField(primary_key=True, max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    postalcode = models.IntegerField()
    country = models.CharField(max_length=200)
    phonenumber = models.IntegerField()
    faxnumber = models.IntegerField()
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)


class Performancedata(models.Model):
    modelnumber = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequenceid = models.ForeignKey(Testsequence, on_delete=models.CASCADE)
    maxsystemvoltage = models.IntegerField()
    voc = models.FloatField()
    isc = models.FloatField()
    vmp = models.FloatField()
    imp = models.FloatField()
    pmp = models.FloatField()
    ff = models.FloatField()


class Certificate(models.Model):
    certificatenumber = models.IntegerField(primary_key=True)
    certid = models.CharField(max_length=200)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    reportnumber = models.CharField(max_length=200)
    issuedate = models.DateField(auto_now_add=True)
    standardid = models.ForeignKey(Teststandard, on_delete=models.CASCADE)
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE)
    modelnumber = models.ForeignKey(Product, on_delete=models.CASCADE)
