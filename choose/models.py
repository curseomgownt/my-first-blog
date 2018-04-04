from django.db import models
from django.contrib.auth.models import AbstractUser #добавлено

# Create your models here.

class User(AbstractUser):
	special_id = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='Идентификатор')

	status_special_id = models.BooleanField(default=False, verbose_name='Статус')

	start_period = models.DateTimeField(blank=True, null=True)

	end_period = models.DateTimeField(blank=True, null=True)

	inviter = models.OneToOneField('self',on_delete=models.CASCADE, blank=True,null=True, verbose_name='Инвайт')

	followers =  models.ForeignKey('self',on_delete=models.CASCADE, blank=True,null=True, related_name='User', verbose_name='Подписчики')

	tariff_name = models.OneToOneField('Tariff', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Тариф')

	balanse = models.IntegerField(default=0, verbose_name='Баланс')

	IP_adress = models.GenericIPAddressField(null=True, blank=True, verbose_name='IP' )


	def __str__(self):
		return '%s %s %s %s %s %s %s %s %s' %(self.special_id, self.status_special_id, self.start_period,
		 self.end_period, self.inviter, self.followers, self.tariff_name, self.balanse, self.IP_adress)


	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = ['username','special_id']




class Tariff(models.Model) :

	name = models.CharField(max_length=100, primary_key=True, verbose_name='Тариф')

	cost = models.IntegerField(verbose_name='Стоимость')

	period = models.IntegerField(verbose_name='Период')

	tariff_bonus = models.DecimalField( max_digits=3, decimal_places=2, verbose_name='Бонус')


	def __str__(self):
		return '%s %s %s %s' %(self.name, self.cost, self.period, self.tariff_bonus)





