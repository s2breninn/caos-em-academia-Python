import random
import matplotlib.pyplot as plt

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]

    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pegar_haltere(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso

    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]  # Se eles estiverem foram do lugar
        return round(len(num_caos) / len(self.porta_halteres) * 100, 2)

class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo #1 - Normal | 2 - Bagunceiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        listar_pesos = self.academia.listar_halteres()
        self.peso = random.choice(listar_pesos)
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)

        if self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)
        self.peso = 0

academia = Academia()

usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia)]
random.shuffle(usuarios)

list_caos = []
list_day = []
day = 0

for i in range(30):
    random.shuffle(usuarios)
    for user in usuarios:
        user.iniciar_treino()
    for user in usuarios:
        user.finalizar_treino()

    day += 1
    list_day.append(day)
    list_caos += [academia.calcular_caos()]

# Calculo média 30 dias
media_caos = round(sum(list_caos) / len(list_caos) * 100, 2)

# Plotar as barras
plt.bar(list_day, list_caos)

# Adicionar os valores nas barras
for i in range(len(list_day)):
    plt.text(list_day[i], list_caos[i], str(list_caos[i]), ha='center', va='bottom', fontsize=8)

# Configurações do gráfico
plt.title('Estatística com 2 pessoa desorganizada entre 12 em uma academia')
plt.xlabel('Dias')
plt.ylabel('Porcentagem')
plt.ylim(0, 100)

# Adicionar legenda personalizada
plt.text(0.5, -0.1, f'A média da probabilidade em que a academia estará desorganizada em 30 dias com 2 pessoas do tipo 2 e 10 do tipo 1 é de {media_caos}%', ha='center', va='center', fontsize=10, transform=plt.gca().transAxes)

plt.show()