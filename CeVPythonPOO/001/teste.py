import matplotlib.pyplot as plt
import numpy as np

# Seus Dados Experimentais
Mc = [234.8, 239.5, 242.1, 246.8, 249.7]
Vc = [129, 130, 136.5, 140, 142]

Mq = [240.0, 242.7, 245.7, 249.9]
Vq = [134, 137, 140, 144]

# Incertezas (1 g e 1 ml)
erro_M = 1
erro_V = 1

fig, ax = plt.subplots(figsize=(10, 7))

# Criando o fundo parecido com papel milimetrado
ax.grid(which='major', color='#999999', linestyle='-', alpha=0.5)
ax.grid(which='minor', color='#CCCCCC', linestyle=':', alpha=0.5)
ax.minorticks_on()

# Plotando os pontos com as barras de erro
ax.errorbar(Mc, Vc, xerr=erro_M, yerr=erro_V, fmt='o', color='blue', 
            label='Barra Circular (C)', capsize=4, markerfacecolor='white', markeredgecolor='blue')
ax.errorbar(Mq, Vq, xerr=erro_M, yerr=erro_V, fmt='s', color='red', 
            label='Barra Quadrada (Q)', capsize=4, markerfacecolor='white', markeredgecolor='red')

# Traçando as retas de ajuste (Método dos Mínimos Quadrados visual)
z_c = np.polyfit(Mc, Vc, 1)
p_c = np.poly1d(z_c)
ax.plot(Mc, p_c(Mc), 'b--', alpha=0.7)

z_q = np.polyfit(Mq, Vq, 1)
p_q = np.poly1d(z_q)
ax.plot(Mq, p_q(Mq), 'r--', alpha=0.7)

# Configurando os limites para aproveitar o papel (com quebra de eixo virtual)
ax.set_xlim(232, 252)
ax.set_ylim(126, 146)

# Títulos e legendas exigidos
ax.set_xlabel('Massa, M (g)', fontsize=12, fontweight='bold')
ax.set_ylabel('Volume, V (ml)', fontsize=12, fontweight='bold')
ax.set_title('Volume em função da Massa para o experimento de Empuxo', fontsize=14)
ax.legend(loc='upper left', framealpha=1)

plt.show()