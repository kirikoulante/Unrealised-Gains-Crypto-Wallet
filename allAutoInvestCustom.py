from binance import Client
import datetime
from dateutil.relativedelta import relativedelta
import time


def get_auto_invest_BTC_lundi(arg_epoch_date):
	# date en epoch (en secondes)
	epoch_date = arg_epoch_date
	# convertir epoch en objet datetime
	date = datetime.datetime.fromtimestamp(epoch_date)
	# date d'aujourd'hui
	today = datetime.datetime.now()
	# nombre de secondes dans une semaine
	seconds_per_week = 604800
	# différence en secondes entre les deux dates
	delta = (today - date).total_seconds()
	# nombre de semaines entières entre les deux dates
	count = int(delta // seconds_per_week)
	# ajuster le nombre de semaines si nécessaire
	if date.weekday() == 0:
		count += 1
	# afficher le nombre de semaines entières
	print("Le nombre de semaines entières entre la date donnée et aujourd'hui est :", count)
	return count

def get_auto_invest_ETH_15th(arg_epoch_date):
	# date en epoch (en secondes)
	epoch_date = arg_epoch_date
	# convertir epoch en objet datetime
	date = datetime.datetime.utcfromtimestamp(epoch_date).replace(hour=0, minute=0, second=0, microsecond=0)
	# date d'aujourd'hui
	today = datetime.datetime.now()
	# initialiser le compteur de jours
	count = 0
	# initialiser l'objet datetime au 15ème jour du mois de la date de départ
	if date.day > 15:
		date = date.replace(day=1) + relativedelta(months=1)
	else:
		date = date.replace(day=15)
	# parcourir tous les 15ème jours de chaque mois entre la date de départ et aujourd'hui
	while date < today:
		# incrémenter le compteur de joursa	
		count += 1  
		# ajouter un mois complet à la date
		date += relativedelta(months=1)
		# passer au 15ème jour du mois suivant
		if date.day > 15:
			date = date.replace(day=1) + relativedelta(months=1)
		else:
			date = date.replace(day=15)
	# soustraire le nombre de jours en trop
	if date.day > 15:
		count -= date.day - 15
	# afficher le nombre de jours correspondant au 15ème jour de chaque mois
	print("Le nombre de jours correspondant au 15ème jour de chaque mois entre la date donnée et aujourd'hui est :", count)
	return count

def get_all_auto_invest(arg_epoch_date):
	total_btc = get_auto_invest_BTC_lundi(arg_epoch_date) * 15
	total_eth = get_auto_invest_ETH_15th(arg_epoch_date) * 25
	print("Total BTC = ", total_btc, " total ETH sans le 11 juillet = ", total_eth, " total global = ", total_eth+total_btc)
	return int(total_btc+total_eth+25)
