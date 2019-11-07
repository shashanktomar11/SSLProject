from django.db import models

# Create your models here.
class Friend(models.Model):
	user_id = models.CharField(max_length=30)
	money_owed = models.IntegerField(default=0)
	CHOICES = [
		('You owe them', 'You owe them'),
		('They owe you', 'They owe you'),
	]
	who_owes_who = models.CharField(
		choices=CHOICES,
		max_length=20,
		default = 'They owe you'
	)

	def __str__(self):
		return self.user_id

class Group(models.Model):
	name = models.CharField(max_length=30)
	members = models.ManyToManyField(Friend, through='Membership')
	def __str__(self):
		return self.name

class Membership(models.Model):
	friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	money_owed = models.IntegerField(default = 0)
	CHOICES = [
		('You owe them', 'You owe them'),
		('They owe you', 'They owe you'),
	]
	who_owes_who = models.CharField(
		choices=CHOICES,
		max_length=20,
		default = 'They owe you'
	)
	def __str__(self):
		return self.friend.user_id + ' ' + self.group.name + ' ' + str(self.money_owed)

