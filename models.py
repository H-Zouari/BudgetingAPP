from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    CategoryName = models.CharField(primary_key=True, max_length=128)


class Currency(models.Model):
    CurrencyName = models.CharField(primary_key=True, max_length=10)


class Schedule(models.Model):
    ScheduleID = models.IntegerField(primary_key=True)
    Type = models.CharField(max_length=32)


class UserAccount(AbstractUser):
    username = None
    email = models.EmailField("email adress", unique=True)
    # set below value
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    Country = models.CharField(max_length=32)
    LastloginDate = models.DateField()


class Account(models.Model):
    AccountID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    EndingIn = models.SmallIntegerField(unique=True)
    Balance = models.IntegerField()
    Type = models.CharField(max_length=32)
    Added_on = models.DateField()
    is_active = models.BooleanField()
    user_email = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


class Budget(models.Model):
    BudgetID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=128)
    StartDate = models.DateField()
    StartDate = models.DateField()
    BudgetAmount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


class Income(models.Model):
    IncomeID = models.IntegerField(primary_key=True)
    Source = models.CharField(max_length=32)
    Amount = models.IntegerField()
    DateReceived = models.DateField()

    AccountID = models.ForeignKey(Account, on_delete=models.CASCADE)
    Currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


class Payee(models.Model):
    PayeeID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    Last_trans_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


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
