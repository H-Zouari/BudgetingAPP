from django.db import models
from users.models import UserAccount

CARD_PROVIDERS = (
    ("Visa", "Visa"),
    ("MasterCard", "MasterCard"),
    ("American_Express", "American Express"),
    ("Discover", "Discover"),
    ("Interlink", "Interlink"),
    ("STAR", "STAR"),
    ("JCB", "JCB"),
)

SCHEDULE_TYPE = (
    ("Recurring", "Recurring"),
    ("One_time", "One time"),
)


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(primary_key=True, max_length=128)


class Currency(models.Model):
    currency_name = models.CharField(primary_key=True, max_length=10)


class Schedule(models.Model):
    schedule_type = models.CharField(
        max_length=32, choices=SCHEDULE_TYPE, default="One_time"
    )
    repeats_on = models.DateField(null=True)


class Account(models.Model):
    Name = models.CharField(max_length=255)
    EndingIn = models.SmallIntegerField()
    provider = models.CharField(
        max_length=30,
        choices=CARD_PROVIDERS,
        help_text="amount currently in the account stated",
    )

    Balance = models.BigIntegerField(help_text="amount currently in the account stated")

    Type = models.CharField(
        max_length=32, help_text="type of account e.g checking debit ..."
    )

    Added_on = models.DateField()
    is_active = models.BooleanField()
    user_email = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)


class Budget(models.Model):
    Name = models.CharField(max_length=128, unique=True)
    start_Date = models.DateField()
    target_Date = models.DateField()
    Budgeted_Amount = models.BigIntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)


class Income(models.Model):
    source = models.CharField(max_length=32)
    amount = models.BigIntegerField()
    date_received = models.DateTimeField()

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


class Payee(models.Model):
    PayeeID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    Last_trans_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Payment(models.Model):
    PaymentID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=128)
    Amount = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    Payee = models.ForeignKey(Payee, on_delete=models.CASCADE)
    Schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    Budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
