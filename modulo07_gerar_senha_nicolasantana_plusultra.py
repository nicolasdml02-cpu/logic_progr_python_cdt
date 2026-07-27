"""
===============================================================================
GERADOR DE SENHAS CYBERPUNK / IDE THEME (TKINTER + MESSAGEBOX)
===============================================================================
"""

import random
import string
import tkinter as tk
from tkinter import messagebox

# ==========================================
# PALETA DE CORES FORNECIDA + AJUSTES DE THEME
# ==========================================
COLOR_AZUL_ESC = "#3413ad"  # AE (Fundo da tela principal)
COLOR_AZUL_MED = "#11b0e4"  # AM (Bordas, seleções e destaques)
COLOR_AZUL_CLA = "#1f07fd"  # AC (Texto da senha / Highlights IDE)
COLOR_VERDE    = "#1c139e"  # V  (Botão Execute / Success)
COLOR_ROSA     = "#9000ff"  # R  (Acentos / Alertas e erros)
COLOR_AMARELO  = "#0252FF"  # A  (Botão Copy / Keywords)
COLOR_ACO      = "#00f7ff"  # B  (Fundo dos cards / Terminal)
COLOR_DARK_BG  = "#00A2FF"  # Fundo ultra escuro tipo IDE

# ==========================================
# LÓGICA DO SISTEMA
# ==========================================
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        
        if tamanho <= 0:
            messagebox.showwarning("⚠️ SYNTAX_WARNING", "O tamanho da senha deve ser maior que 0!")
            return
            
        if tamanho > 128:
            messagebox.showwarning("⚠️ OVERFLOW_WARNING", "Tamanho máximo recomendado é 128 caracteres.")
            return

        senha_caracteres = string.ascii_letters + string.digits + string.punctuation
        senha_gerada = ''.join(random.choice(senha_caracteres) for _ in range(tamanho))

        # Atualiza a senha e o nível de segurança
        var_senha.set(senha_gerada)
        atualizar_status_seguranca(tamanho)
        
    except ValueError:
        messagebox.showerror("❌ RUNTIME_ERROR", "Entrada inválida! Digite apenas números inteiros no parâmetro 'tamanho'.")

def copiar_senha():
    senha = var_senha.get()
    if senha and senha not in ["// Clique em EXECUTE", ""]:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo("✅ CLIPBOARD_SUCCESS", "Senha copiada com sucesso para a área de transferência!")
    else:
        messagebox.showwarning("⚠️ NULL_POINTER", "Nenhuma senha gerada para copiar!")

def atualizar_status_seguranca(tamanho):
    if tamanho < 8:
        lbl_status.config(text="[STATUS]: FRACO (WEAK_KEY)", fg=COLOR_ROSA)
    elif 8 <= tamanho < 14:
        lbl_status.config(text="[STATUS]: MEDIO (MODERATE_KEY)", fg=COLOR_AMARELO)
    else:
        lbl_status.config(text="[STATUS]: FORTE (HIGH_SECURITY)", fg=COLOR_VERDE)

# ==========================================
# CONSTRUÇÃO DA INTERFACE GRÁFICA (GUI IDE)
# ==========================================
janela = tk.Tk()
janela.title("DevKey Generator v2.0 - IDE Edition")
janela.geometry("520x520")
janela.configure(bg=COLOR_DARK_BG)
janela.resizable(False, False)

# --- CABEÇALHO ESTILO IDE / TERMINAL ---
top_bar = tk.Frame(janela, bg=COLOR_AZUL_ESC, height=35)
top_bar.pack(fill="x", side="top")

lbl_window_title = tk.Label(
    top_bar, 
    text=" ⚡ dev_password_generator.py - IDE Environment", 
    font=("Consolas", 10, "bold"), 
    bg=COLOR_AZUL_ESC, 
    fg=COLOR_AZUL_CLA
)
lbl_window_title.pack(side="left", padx=10, pady=5)

# --- CARD PRINCIPAL (TERMINAL / EDITOR DE CÓDIGO) ---
card = tk.Frame(janela, bg=COLOR_AZUL_ESC, bd=2, relief="solid")
card.pack(pady=20, fill="both", expand=True, padx=25)

# Header dentro do Card
card_header = tk.Frame(card, bg=COLOR_AZUL_MED)
card_header.pack(fill="x")

lbl_card_title = tk.Label(
    card_header, 
    text=" SYSTEM // PARAMETERS & CONFIGURATION ", 
    font=("Times new roman", 9, "bold"), 
    bg=COLOR_AZUL_MED, 
    fg="#FFFFFF"
)
lbl_card_title.pack(pady=4, anchor="w", padx=5)

# Conteúdo Interno do Card
inner_body = tk.Frame(card, bg=COLOR_ACO, padx=20, pady=20)
inner_body.pack(fill="both", expand=True)

# Linha 1: Input de tamanho com visual de variável
lbl_var = tk.Label(
    inner_body, 
    text="val length: int =", 
    font=("Times new roman", 11, "bold"), 
    bg=COLOR_ACO, 
    fg=COLOR_AMARELO
)
lbl_var.grid(row=0, column=0, sticky="w", pady=10)

entry_tamanho = tk.Entry(
    inner_body, 
    font=("Times new roman", 12, "bold"), 
    bg=COLOR_DARK_BG, 
    fg=COLOR_VERDE, 
    insertbackground=COLOR_VERDE,
    bd=2, 
    relief="solid",
    width=8,
    justify="center"
)
entry_tamanho.insert(0, "16")
entry_tamanho.grid(row=0, column=1, sticky="w", padx=10, pady=10)

# Linha 2: Terminal Output Box (Onde exibe a senha)
lbl_output = tk.Label(
    inner_body, 
    text="// GENERATED_KEY_OUTPUT:", 
    font=("Times new roman", 10, "bold"), 
    bg=COLOR_ACO, 
    fg=COLOR_AZUL_CLA
)
lbl_output.grid(row=1, column=0, columnspan=2, sticky="w", pady=(15, 5))

var_senha = tk.StringVar(value="// Clique em EXECUTE")
entry_senha = tk.Entry(
    inner_body, 
    textvariable=var_senha, 
    font=("Times new roman", 13, "bold"), 
    bg=COLOR_DARK_BG, 
    fg=COLOR_AZUL_CLA, 
    bd=2, 
    relief="solid",
    justify="center",
    state="readonly"
)
entry_senha.grid(row=2, column=0, columnspan=2, sticky="ew", ipady=10)

# Linha 3: Indicator Status
lbl_status = tk.Label(
    inner_body, 
    text="[STATUS]: WAITING_EXECUTION", 
    font=("Times new roman", 9, "bold"), 
    bg=COLOR_ACO, 
    fg="#888888"
)
lbl_status.grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 0))

inner_body.grid_columnconfigure(1, weight=1)

# --- CONTAINER DE BOTOES (ESTILO BARRA DE AÇÃO IDE) ---
btn_container = tk.Frame(janela, bg=COLOR_DARK_BG)
btn_container.pack(pady=(0, 25))

btn_gerar = tk.Button(
    btn_container, 
    text="▶ EXECUTE (Gerar)", 
    command=gerar_senha, 
    bg=COLOR_VERDE, 
    fg="#000000", 
    font=("Times new roman", 11, "bold"), 
    relief="flat",
    padx=20, 
    pady=10,
    activebackground=COLOR_AZUL_MED,
    activeforeground="#FFFFFF",
    cursor="hand2"
)
btn_gerar.pack(side="left", padx=10)

btn_copiar = tk.Button(
    btn_container, 
    text="📋 COPY_TO_CLIPBOARD", 
    command=copiar_senha, 
    bg=COLOR_AMARELO, 
    fg="#000000", 
    font=("Times new roman", 11, "bold"), 
    relief="flat",
    padx=20, 
    pady=10,
    activebackground=COLOR_ROSA,
    activeforeground="#FFFFFF",
    cursor="hand2"
)
btn_copiar.pack(side="left", padx=10)

# Rodapé
lbl_footer = tk.Label(
    janela, 
    text="UTF-8 | Python 3.x | Tkinter Engine", 
    font=("Times new roman", 8), 
    bg=COLOR_DARK_BG, 
    fg="#557788"
)
lbl_footer.pack(side="bottom", pady=5)

if __name__ == "__main__":
    janela.mainloop()