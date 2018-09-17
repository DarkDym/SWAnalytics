import json
from pymongo import MongoClient
import tkinter as tk

#-------declaração das variáveis globais---------------
mobs_id = []
mobs_name = []
mobs2_type = []
mobs2_elem = []
mobs2_comp = []
tst = []

#---------Função que cria dois lists de pesquisa de Mobs----------------- 
def createDictMob():
	with open('monsters.json','r') as ms:
		mob_D = json.load(ms)
	tamD = len(mob_D['unit_list'])
	global mobs_id
	global mobs_name
	mobs_id = []
	mobs_name = []
	for i in range(0,tamD):
		mobs_id.append(mob_D['unit_list'][i]['enety_id'])
		mobs_name.append(mob_D['unit_list'][i]['enety_name'])

#--------Função que abre o json de dados pessoais------------------
def openMJ():
	with open('DarkDym1-23705641.json','r') as sw:
		mob_data = json.load(sw)
	tam = len(mob_data['unit_list'])
	global mobs2_type
	global mobs2_elem
	global mobs2_comp
	mobs2_type = []
	mobs2_elem = []
	mobs2_comp = []
	for i in range(0,tam):
		mobs2_type.append(int(str(mob_data['unit_list'][i]['unit_master_id'])[0:3]))
		mobs2_elem.append(str(mob_data['unit_list'][i]['unit_master_id'])[3:5])
		mobs2_comp.append(int(str(mob_data['unit_list'][i]['unit_master_id'])))	

#---------Função que cria um list com os Mobs da conta---------------
def createMobOwn():
	tamx = len(mobs2_type)
	tamy = len(mobs_id)
	global tst
	tst = []
	lol = []
	aux = 0
	mobAux = []
	mobAux = sorted(mobs2_type)
	for i in range(0,tamx):
		for j in range(0,tamy):
			if (aux != mobAux[i]) :
				if (mobAux[i] == mobs_id[j]):
					tst.append(mobs_name[j])
					tst.append(mobs_id[j])
					for x in range(0,5):
						lol.append(0)
					tst.append(lol)
					lol = []
					aux = mobAux[i]			

#-----------Função que adiciona a quantidade de Mobs-----------------
def addMobOwn():
	tamx = len(mobs2_type)
	tamy = len(tst)
	cont = 0
	for i in range(0,tamx):
		for j in range(1,tamy,3):
			if (mobs2_type[i] == tst[j]) :
				if (mobs2_elem[i] == '01' or mobs2_elem[i] == '11') :
					tst[j+1][0] = tst[j+1][0] + 1
				elif (mobs2_elem[i] == '02' or mobs2_elem[i] == '12') :
					tst[j+1][1] = tst[j+1][1] + 1
				elif (mobs2_elem[i] == '03' or mobs2_elem[i] == '13') :
					tst[j+1][2] = tst[j+1][2] + 1
				elif (mobs2_elem[i] == '04' or mobs2_elem[i] == '14') :
					tst[j+1][3] = tst[j+1][3] + 1
				elif (mobs2_elem[i] == '05' or mobs2_elem[i] == '15') :
					tst[j+1][4] = tst[j+1][4] + 1
				else:
					print("WTF")

#-----------------------Conexão com o Banco de Dados MongoDB--------------------
def connect_Mongo():
	client = MongoClient("mongodb://DarkDym:Alfaromeuhp!1@sw0-shard-00-00-ntnmd.mongodb.net:27017,sw0-shard-00-01-ntnmd.mongodb.net:27017,sw0-shard-00-02-ntnmd.mongodb.net:27017/test?ssl=true&replicaSet=SW0-shard-0&authSource=admin&retryWrites=true",
		ssl = True)
	global db_mob	
	db_mob = client.tst

#-----------------------TESTE--------------------
	
#-----------------------TESTE--------------------

#-----------------------TELA--------------------
def cria_tela():
	class App(tk.Frame):
		def cria_teste(self, event):
			print("somente um teste de tela pra ver se funciona!")
			self.master.destroy()#fecha a tela!
		def destroi_teste(self):
			print("MORRA!")
			self.master.destroy()#fecha a tela!
				
		def __init__(self,  master):
			tk.Frame.__init__(self, master)
			dialog_frame = tk.Frame(self)
			dialog_frame.pack(padx=20,pady=25) 
			button_frame = tk.Frame(self)
			button_frame.pack(padx=15, pady=(0,15))
			self.pack()
			self.master.title("TESTE")
			#self.master.protocol('WM_DELETE_WINDOW',self.destroi_teste)
			self.master.bind('<Escape>',self.cria_teste)
			tk.Label(dialog_frame, text="ESTE É UM TESTE DE TELA!").pack()
			tk.Button(button_frame, text="OK", default='active',command=self.cria_teste).pack(side='right')
			tk.Button(button_frame, text="KO", command=self.destroi_teste).pack(side='right')
			pass
	root = tk.Tk()
	App(root)
	root.mainloop()

createDictMob()
openMJ()
createMobOwn()
#print(mobs_id)
#print(mobs_name)
#print(mobs2_type)
#print(mobs2_elem)
#print(mobs2_comp)
#mobs2_compS = sorted(mobs2_comp)
#print(mobs2_compS)	
#qt = []
#qnt = [0,0,0,0,0]
#qnt2 = [9,8,7,6,5]
#qt3 = []
#print(qt3)
#qt3.append(11)
# print(qt3)
# qt3.append(12)
# print(qt3)
# qt3.append(13)
# print(qt3)
# qt3.append(14)
# print(qt3)
# qt3.append(15)
# print(qt3)
# qt.append(qnt)
# print(qt)
# qt.append(qnt2)
# qt.append(qt3)
# print(qt)
# qt[0][0] = qt[0][0] + 90
# print(qt)
# print(tst)
addMobOwn()
cria_tela()
print(tst)


	
def insert_Aluno(nome,cpf,nasc,ingr,curso,fingr,aprov):
	result = db_mob.test.insert_one(
		{
			"Nome"		:	nome,
			"Ingresso"	:	ingr,
			"Forma de Ingresso"		:	fingr,
			"Curso"		:	curso,
			"CPF"		:	cpf,
			"Data Nasc"	:	nasc,
			"Histórico"	:	aprov
		})
	print(nome," inserido com sucesso!")

#connect_Mongo()
#for i in range(0,50):
#	insert_Aluno("Fulano"+str(i),i,i+1,i+2,"X"+str(i),"Y"+str(i),"S"+str(i))