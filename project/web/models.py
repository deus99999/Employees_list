from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    role_level = models.IntegerField(default=1)

    def __str__(self):
       return self.title


class Worker(MPTTModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    hire_date = models.DateField(default=timezone.now)
    position = models.ForeignKey(Role, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subordinates')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


# class Genre(MPTTModel):
#     name = models.CharField(max_length=50, unique=True)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#
#     class MPTTMeta:
#         order_insertion_by = ['name']
#
#
# class Position(MPTTModel):
#     position_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255, unique=True)
#     level = models.IntegerField()
#
#     def __str__(self):
#         return self.title
#
#
# # class Position(models.Model):
# #     position_id = models.AutoField(primary_key=True)
# #     title = models.CharField(max_length=255)
# #     level = models.IntegerField()
# #
# #     def __str__(self):
# #         return self.title
#
#
# class Employee(models.Model):
#     employee_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     hire_date = models.DateField(default=timezone.now)
#     position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True,)
#     manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
#     #parent = TreeForeignKey('self', on_delete=models.SET_NULL,
#                               #     blank=True, null=True, verbose_name="Руководитель", related_name='child')
#
#     def __str__(self):
#         return self.name
#
#
#     def __unicode__(self):
#         return self.name

    # class MPTTMeta:
    #     order_insertion_by = ['name']