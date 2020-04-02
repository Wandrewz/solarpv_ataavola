# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Certificate(models.Model):
    certificatenumber = models.IntegerField(primary_key=True)
    id = models.CharField(db_column='ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    reportnumber = models.CharField(max_length=255, blank=True, null=True)
    issuedate = models.DateField(blank=True, null=True)
    standardid = models.ForeignKey('Teststandard', models.DO_NOTHING, db_column='standardID', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey('Location', models.DO_NOTHING, db_column='locationID', blank=True, null=True)  # Field name made lowercase.
    modelnumber = models.ForeignKey('Product', models.DO_NOTHING, db_column='modelnumber', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Certificate'


class Client(models.Model):
    clientid = models.CharField(db_column='clientID', primary_key=True, max_length=255)  # Field name made lowercase.
    clientname = models.CharField(max_length=255, blank=True, null=True)
    clienttype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Client'


class Location(models.Model):
    locationid = models.CharField(db_column='locationID', primary_key=True, max_length=255)  # Field name made lowercase.
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    postalcode = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.IntegerField(blank=True, null=True)
    faxnumber = models.IntegerField(blank=True, null=True)
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='clientID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Location'


class Performancedata(models.Model):
    modelnumber = models.ForeignKey('Product', models.DO_NOTHING, db_column='modelnumber', blank=True, null=True)
    sequenceid = models.ForeignKey('Testsequence', models.DO_NOTHING, db_column='sequenceID', blank=True, null=True)  # Field name made lowercase.
    maxsystemvoltage = models.IntegerField(blank=True, null=True)
    voc = models.FloatField(blank=True, null=True)
    isc = models.FloatField(blank=True, null=True)
    vmp = models.FloatField(blank=True, null=True)
    imp = models.FloatField(blank=True, null=True)
    pmp = models.FloatField(blank=True, null=True)
    ff = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PerformanceData'


class Product(models.Model):
    modelnumber = models.CharField(primary_key=True, max_length=255)
    productname = models.CharField(max_length=255, blank=True, null=True)
    celltechnology = models.CharField(max_length=255, blank=True, null=True)
    cellman = models.CharField(max_length=255, blank=True, null=True)
    numcells = models.IntegerField(blank=True, null=True)
    numcellsinseries = models.IntegerField(blank=True, null=True)
    numseriesstrings = models.IntegerField(blank=True, null=True)
    numdiodes = models.IntegerField(blank=True, null=True)
    productlength = models.FloatField(blank=True, null=True)
    productwidth = models.FloatField(blank=True, null=True)
    productweight = models.FloatField(blank=True, null=True)
    superstratetype = models.CharField(max_length=255, blank=True, null=True)
    superstrateman = models.CharField(max_length=255, blank=True, null=True)
    substratetype = models.CharField(max_length=255, blank=True, null=True)
    substrateman = models.CharField(max_length=255, blank=True, null=True)
    frametype = models.CharField(max_length=255, blank=True, null=True)
    frameadhesive = models.CharField(max_length=255, blank=True, null=True)
    encapsulanttype = models.CharField(max_length=255, blank=True, null=True)
    encapsulantman = models.CharField(max_length=255, blank=True, null=True)
    junctionboxtype = models.CharField(max_length=255, blank=True, null=True)
    junctionboxman = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Product'


class Service(models.Model):
    serviceid = models.CharField(db_column='serviceID', primary_key=True, max_length=255)  # Field name made lowercase.
    servicename = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    isfirequired = models.CharField(db_column='isFIrequired', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fifrequency = models.CharField(db_column='FIfrequency', max_length=255, blank=True, null=True)  # Field name made lowercase.
    standardid = models.ForeignKey('Teststandard', models.DO_NOTHING, db_column='standardID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Service'


class Testsequence(models.Model):
    sequence_id = models.CharField(db_column='sequence_ID', primary_key=True, max_length=255)  # Field name made lowercase.
    sequence_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestSequence'


class Teststandard(models.Model):
    standardid = models.CharField(db_column='standardID', primary_key=True, max_length=255)  # Field name made lowercase.
    standardname = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    publisheddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestStandard'


class User(models.Model):
    userid = models.CharField(db_column='userID', primary_key=True, max_length=255)  # Field name made lowercase.
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    jobtitle = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    officephone = models.IntegerField(blank=True, null=True)
    cellphone = models.IntegerField(blank=True, null=True)
    prefix = models.CharField(max_length=255, blank=True, null=True)
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='clientID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
