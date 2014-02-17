# -*- coding: utf-8 -*-

from pyramid.view import view_config
from datetime import date
from random import randint

@view_config(route_name='home', renderer='templates/mytemplate.pt')

def my_view(request):
	# if request.method=="post":
	#	dia = request.POST["dia"]
	#	mes = request.POST["mes"]
	#	return ...
	# return ...
	dia = request.POST.get("dia")
	if not dia:
		return {"project":"zodiac",'date':'','name':'','selec':'z_band.jpg','phase':'mapa de les constel.lacions dels signes dels zodiacs'}
	mes = request.POST.get("mes")
	d = date(2013, int(mes), int(dia))
	z = []
	z.append([]) # data
	z.append([]) # nom del signe del zodiac
	z.append([]) # nom del fitxer amb la imatge
	z.append([]) # frases de les galetes de la sort
	z[0] = [date(d.year, 1, 21) ,date(d.year, 2, 20) ,date(d.year, 3, 22),date(d.year, 4, 21),date(d.year, 5, 22),date(d.year, 6, 22),date(d.year, 7, 23),date(d.year, 8, 23),date(d.year, 9, 23),date(d.year, 10, 23),date(d.year, 11, 23),date(d.year, 12, 23)]
	z[1] = ["aquari","pexios","aires","taure","geminis","cancer","lleo","verge","libra","escorpi","sagitari","capricorn"]
	z[2] = ["z_aquarius.jpg","z_pisces.jpg","z_aries.jpg","z_taurus.jpg","z_gemini.jpg","z_cancer.jpg","z_leo.jpg","z_virgo.jpg","z_libra.jpg","z_scorpio.jpg","z_sagittarius.jpg","z_capricorn.jpg"]
	z[3] = ["Has d'estar preparat per modificar els teus plans, pero els canvis son sempre per be.","Trobaras en la mirada dels altes el afecte que avui necessites. ","Una nova pagina romantica s'escriura davant els teus ulls inesperadament.","Veuras com el mirall et retorna un rostre precios i radiant.","Arribaras per diferents vies a la mateixa meta, pero no deixes de perseguir-la.","Mai dubtis d'enfrenar-te als problemes mes dificils. Ets valent.","No visquis prometent, compleix la teva paraula com mes aviat millor.","L'aigua fa flotar el vaixell, pero tambe pot enfonsar-lo.","Quant cerquis el que mes desitges, recorda fer el teu millor esforc.","Corregeix els teus defectes i decideix-te a comencar una nova vida.","Avui amb el teu gran cor il.luminaras la teva vida i la del demes.","Recorda sempre complir les promeses que et fas a tu mateix.","Somia, avui tot es possible: l'amor, diners i la fortuna.","Coneix-te, canvia el que no t'agrada, accepta el que no pots canviar.","Un dels teus somnis es realitzara, el mes precios.","Avui seras reconegut pels teus dons especials i aconseguiras ser felic per moltes hores.","Saps que es exactament el que necessites. Treballa en aixo i fer-ho materialitzar-se.","Avui provaras la teva capacitat de ser felic i cada accio sera una alegria.","La teva vida sera meravellosa i plena de detalls espectaculars.","Avui, tots els camins condueixen al exit mes increible."]
	n = z[1][len(z[1])-1]
	r = z[2][len(z[2])-1]
	for i in range(0,11):
	    if d >= z[0][i] and d < z[0][i+1]:
	    	n = z[1][i]
	        r = z[2][i]
	p = z[3][randint(0,len(z[3])-1)]
	return {"project":"zodiac",'date':d,'name':n,'selec':r,'phase':p}
