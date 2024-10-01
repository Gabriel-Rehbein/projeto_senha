import itertools
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Definindo os caracteres possíveis
caracteres_possiveis = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~"

# Função para tentar adivinhar a senha
def tentar_adivinhar_senha(senha, barra_progresso, status_label, tentativas=0):
    if tentativas == 0:
        total_combinacoes = len(caracteres_possiveis) ** len(senha)
    
    for tentativa in itertools.product(caracteres_possiveis, repeat=len(senha)):
        tentativa_senha = ''.join(tentativa)
        tentativas += 1

        # Atualiza a barra de progresso
        proporcao = tentativas / total_combinacoes
        barra_progresso['value'] = proporcao * 100
        status_label['text'] = f"Tentativa: {tentativa_senha} ({tentativas}/{total_combinacoes})"
        root.update()

        if tentativa_senha == senha:
            messagebox.showinfo("Sucesso", f"A senha foi descoberta: {tentativa_senha}")
            return

    # Para não travar a interface, usa-se `after`
    root.after(10, lambda: tentar_adivinhar_senha(senha, barra_progresso, status_label, tentativas))

# Função para iniciar a tentativa de descobrir a senha
def iniciar_tentativa():
    senha_usuario = entrada_senha.get()

    if len(senha_usuario) > 6:
        messagebox.showerror("Erro", "A senha é muito longa. Tente uma senha de até 6 caracteres.")
    elif len(senha_usuario) < 1:
        messagebox.showerror("Erro", "A senha não pode estar vazia.")
    else:
        barra_progresso['value'] = 0
        status_label['text'] = "Status: Aguardando..."
        tentar_adivinhar_senha(senha_usuario, barra_progresso, status_label)

# Criando a janela principal
root = tk.Tk()
root.title("Descobridor de Senhas")

# Criando o layout da GUI
tk.Label(root, text="Digite a senha (máx 6 caracteres):").pack(pady=10)
entrada_senha = tk.Entry(root)
entrada_senha.pack(pady=10)

barra_progresso = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
barra_progresso.pack(pady=10)

status_label = tk.Label(root, text="Status: Aguardando...")
status_label.pack(pady=10)

tk.Button(root, text="Iniciar", command=iniciar_tentativa).pack(pady=10)

# Iniciando o loop principal da janela
root.mainloop()
