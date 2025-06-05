import tkinter #Importa a biblioteca tkinter
import tkinter.messagebox #Corrige um bug em que o tkinter.messagebox não era reconhecido

def binario_para_decimal(): #Cria a função para converter binário em decimal
    try: #Tenta:
        entrada_binaria = entry_binario.get() #Declarar a variável entrada_binaria a partir do valor da entrada do usuário.
        if not entrada_binaria: #Se não há entrada_binaria:
            tkinter.messagebox.showerror("Erro de Entrada", "Por favor, insira um número binário.") #Pop-up informando o erro e o motivo
            return

        valido = True #Declara a variável valido
        for caractere in entrada_binaria: #Verificação de todos os caracteres da variável entrada_binaria:
            if caractere != '0' and caractere != '1': #Se for encontrado um caractere diferente de 1 e 0:
                valido = False #valido recebe False
                break
        
        if not valido: #Se válido não for True:
            tkinter.messagebox.showerror("Erro de Formato", "Número binário inválido. Utilize apenas os dígitos 0 e 1.") #Pop-up informando o erro e o motivo
            return
            
        decimal_resultado = int(entrada_binaria, 2) #Declara o decimal resultado, a partir da conversão da entrada_binaria na base 2
        entry_decimal.delete(0, tkinter.END) #Exclui os valores preenchidos no número decimal
        entry_decimal.insert(0, str(decimal_resultado)) #Insere o numero binário que foi convertido
    except ValueError:
        tkinter.messagebox.showerror("Erro de Conversão", "Entrada binária inválida para conversão.") #Pop-up informando o erro e o motivo

def decimal_para_binario(): #Cria a função para converter decimal em binário
    try: #Tenta:
        entrada_decimal_str = entry_decimal.get() #Declarar a variável entrada_decimal_str a partir do valor da entrada do usuário.
        if not entrada_decimal_str: #Se não há entrada_decimal_str:
            tkinter.messagebox.showerror("Erro de Entrada", "Por favor, insira um número decimal.") #Pop-up informando o erro e o motivo
            return
        entrada_decimal = int(entrada_decimal_str) #Converte a variável de string para inteiro.
        if entrada_decimal < 0: #Se o número decimal for negativo:
            tkinter.messagebox.showerror("Erro de Valor", "Por favor, insira um número decimal (base 10) não negativo.") #Pop-up informando o erro e o motivo
            return
        binario_resultado = bin(entrada_decimal).replace("0b", "") #Declara o binario resultado, a partir da conversão da entrada_decimal e remove o "0b"
        entry_binario.delete(0, tkinter.END) #Exclui os valores preenchidos no número binário
        entry_binario.insert(0, binario_resultado) #Insere o numero decimal que foi convertido
    except ValueError:
        tkinter.messagebox.showerror("Erro de Formato", "Entrada decimal inválida. Por favor, insira um número inteiro.") #Pop-up informando o erro e o motivo

def limpar_campos():
    entry_binario.delete(0, tkinter.END)  #Exclui os valores preenchidos no número binário
    entry_decimal.delete(0, tkinter.END)  #Exclui os valores preenchidos no número decimal

janela = tkinter.Tk() # Cria a interface principal
janela.title("Conversor Binário(Base 2) <--> Decimal (Base 10)") #Insere um título à janela
janela.geometry("480x230") #Formata a janela pro tamanho 500x200
janela.resizable(True, True) #Permite que o usuário altere o tamanho da janela horizontalmente e verticalmente

cor_fundo = "#ecd3b3" #Declara a cor do fundo
cor_botao = "#45312c" #Declara a cor do botão
cor_texto_botao = "#ecd3b3" #Declara a cor do texto do botão
fonte_label = ("Arial", 10) #Declara a fonte dos textos
fonte_entry = ("Arial", 10) #Declara a fonte da entrada do usuário
fonte_botao = ("Arial", 10, "bold") #Declara a fonte do texto do botão

janela.configure(bg=cor_fundo) #Define o bg(background) como a cor_fundo

frame_binario = tkinter.Frame(janela, bg=cor_fundo) #Insere uma "moldura", uma área retangular à variável frame_binario
frame_binario.pack(pady=10) #Insere o frame_binario dentro da janela com um contorno de 10pixels verticalmente

label_binario = tkinter.Label(frame_binario, text=" Número Binário (Base 2):   ", font=fonte_label, bg=cor_fundo) #Insere texto dentro do frame_binario
label_binario.pack(side=tkinter.LEFT, padx=5) #Posiciona o texto o mais a esqueda possível da "moldura" com um contorno de 5px horizontais

entry_binario = tkinter.Entry(frame_binario, width=30, font=fonte_entry) #Cria uma espécie de input, com uma caixa de comprimeto de 30 caracteres, e específica a fonte do texto input
entry_binario.pack(side=tkinter.LEFT) #Posiciona o texto o mais a esqueda possível da "moldura" com um contorno de 5px horizontais

frame_decimal = tkinter.Frame(janela, bg=cor_fundo) #Insere uma "moldura", uma área retangular à variável frame_decimal
frame_decimal.pack(pady=10) #Insere o frame_decimal dentro da janela com um contorno de 10pixels verticalmente

label_decimal = tkinter.Label(frame_decimal, text="Número Decimal (Base 10):", font=fonte_label, bg=cor_fundo) #Insere texto dentro do frame_binario
label_decimal.pack(side=tkinter.LEFT, padx=5) #Posiciona o texto o mais a esqueda possível da "moldura" com um contorno de 5px horizontais

entry_decimal = tkinter.Entry(frame_decimal, width=30, font=fonte_entry,) #Cria uma espécie de input, com uma caixa de comprimeto de 30 caracteres, e específica a fonte do texto input
entry_decimal.pack(side=tkinter.LEFT) #Posiciona o texto o mais a esqueda possível da "moldura"

frame_botoes_conversao = tkinter.Frame(janela, bg=cor_fundo) #Insere uma "moldura" invisível, uma área retangular à variável frame_botoes_conversao
frame_botoes_conversao.pack(pady=15) #Insere o frame_botao_conversao dentro da janela com um contorno invisível de 10pixels verticalmente

botao_bin_para_dec = tkinter.Button( #Cria um botão
    frame_botoes_conversao, #Puxa as informações do frame
    text="Binário para Decimal →", #Insere texto ao frame
    command=binario_para_decimal, #Chama a função binario_para_decimal
    font=fonte_botao, #Informa a fonte
    bg=cor_botao, #Informa a cor do background
    fg=cor_texto_botao, #Informa a cor do texto
    width=20 #Informa o comprimeiro em caracteres
)
botao_bin_para_dec.pack(side=tkinter.LEFT, padx=10) #Insere o botão o mais a esqueda possível com contorno/espaçamento de 10px horizontalmente

botao_dec_para_bin = tkinter.Button( #Cria um botão
    frame_botoes_conversao, #Puxa as informações do frame
    text="← Decimal para Binário", #Insere texto ao frame
    command=decimal_para_binario, #Chama a função decimal_para_binario
    font=fonte_botao, #Informa a fonte
    bg=cor_botao, #Informa a cor do background
    fg=cor_texto_botao, #Informa a cor do texto
    width=20 #Informa o comprimeiro em caracteres
)
botao_dec_para_bin.pack(side=tkinter.LEFT, padx=10) #Insere o botão o mais a esqueda possível com contorno/espaçamento de 10px horizontalmente

botao_limpar = tkinter.Button( #Cria um botão
    janela, #Informa o local do botão
    text="Limpar Campos", #Insere texto ao frame
    command=limpar_campos, #Chama a função limpar_campos
    font=fonte_botao, #Informa a fonte
    bg="#ecd3b3", #Informa a cor do background
    fg= "#45312c", #Informa a cor do texto
    width=18 #Informa o comprimeiro em caracteres
)
botao_limpar.pack(pady=10) #Insere o botão o mais a esqueda possível com contorno/espaçamento de 10px verticalmente

creditos = tkinter.Frame(janela, bg=cor_fundo) #Insere uma "moldura", uma área retangular à variável creditos
creditos.pack(pady=10) #Insere o creditos dentro da janela com um contorno de 10pixels verticalmente

label_creditos = tkinter.Label(creditos, text="Autor: Dhavi Rodrigues", font=fonte_label, bg=cor_fundo) #Insere texto dentro do creditos
label_creditos.pack(side=tkinter.LEFT, padx=5) #Posiciona o texto o mais a esqueda possível da "moldura" com um contorno de 5px horizontais

janela.mainloop() #Mantem a janela aberta.