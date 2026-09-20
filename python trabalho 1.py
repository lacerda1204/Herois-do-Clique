#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Heróis do Clique"
FPS = 30

# Objetos
background = Actor('background')
enemy = Actor('enemy', (400, 230))
bonus_1 = Actor("bonus", (100, 100))
bonus_2 = Actor("bonus", (100, 200))

# Variáveis
count = 0
hp = 50
damage = 1
price1 = 15
price2 = 200

# Desenhando os gráficos
def draw():
    background.draw()
    enemy.draw()
    screen.draw.text(hp, center=(400, 130), color="
#DC143C", fontsize = 30, background="
#FFE4B5")
    screen.draw.text(count, center=(570, 30), color="black", fontsize = 30)
    # Bônus
    bonus_1.draw()
    screen.draw.text("1 de dano a cada 2s", center=(100, 80), color="black", fontsize = 20)
    screen.draw.text(price1, center=(100, 110), color="black", fontsize = 20)
    bonus_2.draw()
    screen.draw.text("5 pontos a cada 2s", center=(100, 180), color="black", fontsize = 20)
    screen.draw.text(price2, center=(100, 210), color="black", fontsize = 20)

# Funções dos bônus
def for_bonus_1():
    global hp
    hp -= 1

def for_bonus_2():
    global count
    count += 5

# Processando os cliques
def on_mouse_down(button, pos):
    global count, damage, hp
    if button == mouse.LEFT:
        # Clicando no objeto
        if enemy.collidepoint(pos):
            count += 1
            hp -= damage
            enemy.y = 200
            animate(enemy, tween='bounce_end', duration=0.5, y=230)
        # Clicando no bonus_1
        if bonus_1.collidepoint(pos):
             if count >= price1:
                  schedule_interval(for_bonus_1, 2)
                  count -= price1
        # Clicando no bonus_2
        if bonus_2.collidepoint(pos):
            if count >= price2:
                schedule_interval(for_bonus_2, 2)
                count -= price2