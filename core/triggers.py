from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Payment, Income


@receiver(pre_save, sender=Payment)
def subtract_expense_from_account(sender, instance, *args, **kwargs):
    account = instance.account

    account.amount -= instance.amount
    account.save()


@receiver(post_save, sender=Income)
def add_income_to_account(sender, instance, created, **kwargs):
    if created:
        account = instance.source
        account.amount += instance.amount
        account.save()