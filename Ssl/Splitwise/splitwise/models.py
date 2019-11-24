from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from datetime import datetime    

class Friend(models.Model):
	person1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='person1')
	person2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='person2')
	money_owed = models.IntegerField(default = 0)

	def __str__(self):
		return self.person2.username

class Group(models.Model):
	group_name = models.CharField(max_length=30)
	no_transactions = models.IntegerField(default=0)
	members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership')

	def __str__(self):
		return self.group_name

class Membership(models.Model):
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	group = models.ForeignKey(Group, on_delete = models.CASCADE)
	money_owed = models.IntegerField(default=0)

class Transaction(models.Model):
	group = models.ForeignKey(Group, on_delete = models.CASCADE, null=True, blank=True)
	group_transaction_id = models.IntegerField(default = 0)
	lender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lender')
	borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='borrower')
	description = models.CharField(max_length=30)
	amount = models.DecimalField(default=0,decimal_places=2,max_digits=10)
	MOVIES = 'mv'
	FOOD = 'fd'
	TRAVEL = 'tr'
	ELECTRONICS = 'ee'
	MEDICAL = 'md'
	SHOPPING = 'sp'
	SERVICES = 'sv'
	OTHERS = 'ot'
	TAG_CHOICES= [
        (MOVIES, 'Movies'),
		(FOOD, 'Food'),
		(TRAVEL, 'Travel'),
		(ELECTRONICS, 'Electronics'),
		(MEDICAL, 'Medical'),
		(SHOPPING, 'Shopping'),
		(SERVICES, 'Services'),
		(OTHERS, 'Others')
    ]
	tag = models.CharField(
        max_length=2,
        choices=TAG_CHOICES
    )
	date = models.DateTimeField(default=datetime.now)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	#location = models.CharField(max_length=30, blank=True)
	#birth_date = models.DateField(null=True, blank=True)
	image = models.ImageField(upload_to='profile_image', blank=True, default="default_face.png")

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


