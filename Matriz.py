print("Matriz")
print()

def Matriz_String_Catch():
    print("Escreva os elementos da matriz cubica, separados apenas por espaços")
    matriz_string=input()
    return matriz_string

def List_Builder(_string):
    if _string[-1]!=" ":
        _string=_string+" "
    product=[]
    holder=""
    for letter in _string:
        try:
            int(letter)
            holder=holder+letter
        except ValueError:
            product.append(int(holder))
            holder=""
            
    return product

def Matriz_List_Generator(matriz_string):
    return List_Builder(matriz_string)


def Matriz_Type_Catch(matriz_file):
    print("Escreva a Quantidade de Linhas e Colunas dessa matriz, separados apenas por espaços")
    style_input=input()
    
    matriz_style=List_Builder(style_input)

    if matriz_style[0]*matriz_style[1]!=len(matriz_file):
        print("Você cometeu um erro, parabens!")
        print()
        return None
    else:
        return matriz_style


def Matriz_Builder(matriz_file, matriz_style):
    matriz_matriz, holder=[], []
    for index in range(len(matriz_file)):
        if index%matriz_style[1]==0 and index!=0:
            matriz_matriz.append(holder)
            holder=[]
        holder.append(matriz_file[index])
    if holder!=[]:
        matriz_matriz.append(holder)
            
    return matriz_matriz

class matriz:
    def __init__(self,string,file,style):
        if file==0:
            self.string=Matriz_String_Catch()
            self.file=Matriz_List_Generator(self.string)
            self.style=Matriz_Type_Catch(self.file)
            if self.style:
                self.filematriz=Matriz_Builder(self.file, self.style)
        else:
            self.string=None
            self.file=file
            self.style=style

    def show(self):
        max_line=self.style[0]
        max_column=self.style[1]
        for line in range(max_line):
            for column in range(max_column):
                print(self.file[max_column*line + column], end="")
                if column==max_column-1:
                    print()
                else:
                    print("", end="\t")

def Add_Matriz(list_matriz):                    
    x=matriz(0,0,0)
    while x.style==None:
        x=matriz(0,0,0)
    x.show()
    list_matriz.append(x)
    print("Matriz Adicionada!")
    return list_matriz

def Sum_Matriz(list_matriz):
    for index in range(len(list_matriz)):
        list_matriz[index].show()
        print("[",index,"]")

    print("Escolha o Número das matrizes que deseja somar, separado por espaços")
    index_sum_str=input()
    index_sum_list=List_Builder(index_sum_str)

    matriz_1=list_matriz[index_sum_list[0]]
    matriz_2=list_matriz[index_sum_list[1]]
    matriz_sum=[]

    if matriz_1.style == matriz_2.style:
        for index in range(len(matriz_1.file)):
            matriz_sum.append(matriz_1.file[index]+matriz_2.file[index])
        matriz_sum=matriz(False,matriz_sum,matriz_1.style)
        matriz_sum.show()
        
        print("Adicionar matriz a lista? (y/n)")
        choice=input()
        if choice=="y":
            list_matriz.append(matriz_sum)
            print("Matriz Adicionada!")
        else:
            print("Ok")
    else:
        print("Essas matrizes não são compatíveis para soma...")
    return list_matriz


def Multi_Matriz(list_matriz):
    pass
    

def main():
    list_matriz=[]
    while True:
        print("Opções:", "\t""\t", "Adicionar Matriz[1]", "\t", "Soma de Matriz[2]", "\t", "Multiplicação de Matriz[3]")
        choice=input()
        print()
        if choice=="1":
            list_matriz=Add_Matriz(list_matriz)
        elif choice=="2":
            list_matriz=Sum_Matriz(list_matriz)
        elif choice=="3":
            list_matriz=Multi_Matriz(list_matriz)

        print()


main()


#Determinante
#Multiplicação de Matrizes
#Error Detector Apurado
'''        Resposta Vazia
Uma virgula a menos
Bateu a cabeça no teclado
'''


