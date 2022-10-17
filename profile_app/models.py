from django.db import models
from profile_app.common import MReference

class MProfile(models.Model):
    profile_id = models.BigIntegerField(primary_key=True)
    firstname = models.CharField(max_length=100,default="")
    lastname = models.CharField(max_length=100,default="")
    age = models.CharField(max_length=100,default="")
    address = models.CharField(max_length=100,default="")
    birthday = models.DateField(null=True,blank=True)
    reference_tablestatus_fk = models.ForeignKey(MReference, on_delete=models.PROTECT, related_name="minstructor_tablestatus", null=True,blank=True, default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    addedby_user_id = models.BigIntegerField(null=True,blank=True)
    updatedby_user_id = models.BigIntegerField(
        null=True,
        blank=True
    )
    date_updated = models.DateTimeField(
        null=True,
        blank=True,
        default=None
    )
          
    def __str__(self):
        return self.profile_id
