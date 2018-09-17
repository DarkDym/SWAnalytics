import json
import monsters as MS

with open('DarkDym1-23705641.json','r') as SW:
	data = json.load(SW)

mob = []
qnt = []
qnt2 = [0,0,0,0,0]
tam = len(data['unit_list'])
x = 0
mob2 = []

for i in range(0,tam):
	mob2.append(int(str(data['unit_list'][i]['unit_master_id'])[0:3]))

mobs = []
mobs = sorted(mob2)
#flag = 0

print(mobs)
aux = 0

for i in range(0,tam):
	if (mobs[i] != aux):
		if (mobs[i] == 203):	
			mob.append("Mumia")
			qnt.append(qnt2)
			aux = mobs[i]
			#flag = 1
		elif (mobs[i] == 158):	
			mob.append("Imp Champion")
			qnt.append(qnt2)
			aux = mobs[i]
			#flag = 1
		else:
			mob.append("??? "+ str(mobs[i]))
			qnt.append(qnt2)
			aux = mobs[i]
			#flag = 0 
print(mob)
print(qnt)

tam2 = len(mob)
print("&&&&&&&&&&&"+str(tam2)+"&&&&&&&&&&&&&")
flag = 0
auxy = 0
#x = [1,1,1,1,1]
for i in range(0,tam):
	#print(int(str(data['unit_list'][i]['unit_master_id'])[0:3]))
	if (int(str(data['unit_list'][i]['unit_master_id'])[0:3]) == 203):  
		for y in range(0,tam2):
			#print("++++++++++++"+str(mob[y])+"+++++++++++++++++")
			if (mob[y] == "Mumia"):
				auxy = y					
				flag = 1
				#y = tam2*2
				print("@@@@@@@@@@@@@@@@"+str(auxy)+"@@@@@@@@@@@@@@@@@")
				print("@@@@@@@@@@@@@@@@"+str(mob[auxy])+"@@@@@@@@@@@@@@@@@")
				break
		if (int(str(data['unit_list'][i]['unit_master_id'])[3:5]) == 1):
			print("Água\n")
			print("-------------"+str(qnt[auxy][0])+"----------------")
			qnt[auxy][0] = qnt[auxy][0] + 1
			#mob[135][0] = mob[135][0] + 1
			print("-------------"+str(mob[auxy])+" | "+str(mob[auxy+1]) +" | "+ str(mob[auxy+1][0])+"----------------")
		elif(int(str(data['unit_list'][i]['unit_master_id'])[3:5]) == 2):
			print("Fogo\n")
			qnt[auxy][1] = str(int(qnt[auxy][1]) + 1)
			#mob[135][1] = mob[135][1] + 1
			print("-------------"+str(mob[auxy])+" | "+str(mob[auxy+1]) +" | "+ str(mob[auxy+1][1])+"----------------")
		elif(int(str(data['unit_list'][i]['unit_master_id'])[3:5]) == 3):
			print("Vento\n")
			qnt[auxy][2] = str(int(qnt[auxy][2]) + 1)
			#mob[135][2] = mob[135][2] + 1
			print("-------------"+str(mob[auxy])+" | "+str(mob[auxy+1]) +" | "+ str(mob[auxy+1][2])+"----------------")
		elif(int(str(data['unit_list'][i]['unit_master_id'])[3:5]) == 4):	
			print("Luz\n")
			qnt[auxy][3] = str(int(qnt[auxy][3]) + 1)
			#mob[135][3] = mob[135][3] + 1
			print("-------------"+str(mob[auxy])+" | "+str(mob[auxy+1]) +" | "+ str(mob[auxy+1][3])+"----------------")
		else:
			print("Dark\n")
			qnt[auxy][4] = str(int(qnt[auxy][4]) + 1)
			#mob[135][4] = mob[135][4] + 1	
			print("-------------"+str(mob[auxy])+" | "+str(mob[auxy+1]) +" | "+ str(mob[auxy+1][4])+"----------------")

#print("-------------"+str(mob[0])+" | "+str(mob[1]) +" | "+ str(mob[2][1])+"----------------")
print(mob)
print(qnt)			
