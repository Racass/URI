import datetime

dia_1 = input()
hora_1 = input()
dia_2 = input()
hora_2 = input()

dia_1 = dia_1.replace("Dia ", "")
hora_1 = hora_1.replace(" : ", ":")
dia_2 = dia_2.replace("Dia ", "")
hora_2 = hora_2.replace(" : ", ":")

mes_1 = 1
mes_2 = 1
if(int(dia_1) > int(dia_2)):
    mes_2 = 2

data_1 = datetime.datetime(2019, int(mes_1), int(dia_1), int(hora_1[0:2]), int(hora_1[3:5]), int(hora_1[6:8]))
data_2 = datetime.datetime(2019, int(mes_2), int(dia_2), int(hora_2[0:2]), int(hora_2[3:5]), int(hora_2[6:8]))

data_fim = data_2 - data_1

dias_fim = str(data_fim.days)
horas_fim, remainder = divmod(data_fim.seconds, 3600)
mins_fim, seg_fim = divmod(remainder, 60)

print(str(dias_fim) + " dia(s)")
print(str(horas_fim) + " hora(s)")
print(str(mins_fim) + " minuto(s)")
print(str(seg_fim) + " segundo(s)")