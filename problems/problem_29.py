'''
    Diseñe un algoritmo que lea la hora actual del día HH:MM:SS y determine cuántas horas,
    minutos y segundos restan para culminar el día.
'''
def get_time_finish_day(day):
    
    day = 0

    if day == datetime.datetime.now ():
		
		return (day.strftime ('%d/%m/%Y %H:%M:%S'))
