from django.db import models


class Email(models.Model):
    name = models.CharField(max_length=90, verbose_name="Name")
    children =  models.CharField(max_length=90, verbose_name="Children")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    with_children = models.CharField(max_length=90, verbose_name="With children or not")
    email = models.CharField(max_length=90, verbose_name="Email")
    other_contacts = models.CharField(max_length=90, verbose_name="Other contacts")
    other_qwestion = models.CharField(max_length=200, verbose_name="Other qwestion")
    ip_address = models.TextField(max_length=100, null=True, verbose_name='Id')