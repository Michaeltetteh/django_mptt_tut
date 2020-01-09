from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# import mptt
# from django.contrib.auth.models import Group
# from mptt.fields import TreeForeignKey

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # add a parent foreign key
    # parent = TreeForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True).contribute_to_class(Group, 'parent')
    # mptt.register(Group,order_insertion_by=['name'])
    
    class MPTTMeta:
        order_insertion_by = ['name']





