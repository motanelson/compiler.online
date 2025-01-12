import tkinter as tk
import random

# Função para iniciar o jogo
def start_game():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 800, 600, fill="yellow")
    global player_position, goalkeeper_image
    player_position = 1  # Centro
    draw_player()
    canvas.create_text(400, 550, text="Use as teclas para escolher a direção: Esquerda, Cima (Centro), Direita", font=("Arial", 12))

# Função para desenhar o jogador e a bola
def draw_player():
    positions = {0: 200, 1: 400, 2: 600}
    canvas.create_oval(positions[player_position] - 20, 450, positions[player_position] + 20, 490, fill="blue", tag="player")
    canvas.create_oval(positions[player_position] - 10, 400, positions[player_position] + 10, 420, fill="white", tag="ball")

# Função para desenhar o goleiro
def draw_goalkeeper(position):
    positions = {0: 200, 1: 400, 2: 600}
    canvas.create_image(positions[position], 300, image=goalkeeper_image, tag="goalkeeper")

# Função para mover o jogador com base na tecla pressionada
def move_player(event):
    global player_position
    if event.keysym == "Left":
        player_position = 0  # Esquerda
    elif event.keysym == "Up":
        player_position = 1  # Centro
    elif event.keysym == "Right":
        player_position = 2  # Direita
    else:
        return
    canvas.delete("player", "ball", "goalkeeper")
    draw_player()
    shoot_ball()

# Função para "chutar" a bola e determinar se é gol
def shoot_ball():
    goalkeeper_position = random.randint(0, 2)
    draw_goalkeeper(goalkeeper_position)
    if goalkeeper_position != player_position:
        canvas.create_text(400, 300, text="GOOOL!", font=("Arial", 24), fill="green")
    else:
        canvas.create_text(400, 300, text="Defendido!", font=("Arial", 24), fill="red")
    canvas.create_text(400, 350, text="Pressione Baixo para jogar novamente", font=("Arial", 14))
    canvas.bind_all("<Down>", lambda event: start_game())

# Criando a interface gráfica
root = tk.Tk()
root.title("Jogo de Pênaltis")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Carregar a imagem do goleiro
goalkeeper_image = tk.PhotoImage(file="goalkeeper.png")

start_game()

root.bind_all("<Left>", move_player)
root.bind_all("<Up>", move_player)
root.bind_all("<Right>", move_player)

root.mainloop()
