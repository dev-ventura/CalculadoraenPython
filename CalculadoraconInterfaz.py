#importando la biblioteca tkinter
import tkinter as tk
#me instancia un cuadro, recuerda colocar parentesis
root=tk.Tk()
#transmitir mensaje en la interfaz
mensaje=tk.StringVar()
ingresanumero1=tk.StringVar()
ingresanumero2=tk.StringVar()
resultadofinal=tk.StringVar()
def suma():
    nump=int(ingresanumero1.get())
    numq=int(ingresanumero2.get())
    res = nump + numq
    resultadofinal.set(res)
def resta():
    nump=int(ingresanumero1.get())
    numq=int(ingresanumero2.get())
    res=nump-numq
    resultadofinal.set(int(res))
def multiplicacion():
    nump=int(ingresanumero1.get())
    numq=int(ingresanumero2.get())
    res=nump*numq
    resultadofinal.set(int(res))
def division():
    nump=float(ingresanumero1.get())
    numq=float(ingresanumero2.get())
    res=nump/numq
    resultadofinal.set(float(res))
#Seran las dimensiones de nuestro recuadro interfaz
root.geometry('400x350')
#Prara colocar un titulo en nuestra interfaz
root.title('Calculadora')
#para colocar un fondo a nuestra interfaz
root.configure(bg='#000000')
#para darle color a las letras
tk.Label(root, text='Calculadora', bg='#000000', fg='#40FF00', font=('dotmatrix', 18)).place(x=110,y=20)
#Vamos a leer los datos
tk.Label(root, text='Ingresa el primer número:', bg='#000000', fg='#40FF00', font=('cantarell', 9)).place(x=40,y=80)
tk.Entry(root, textvariable=ingresanumero1).place(x=200,y=80)
tk.Label(root, text='Ingresa el segundo número:', bg='#000000', fg='#40FF00', font=('cantarell', 9)).place(x=40,y=120)
tk.Entry(root, textvariable=ingresanumero2).place(x=200,y=120)
tk.Label(root, text='Resultado Final:', bg='#000000', fg='#40FF00', font=('cantarell', 9)).place(x=40,y=160)
tk.Message(root, textvariable=resultadofinal).place(x=200,y=160)
#Voy creando mis botones para las distintas operaciones
tk.Button(root, text='Sumar', bd=1,  command=suma).place(x=40,y=220)
tk.Button(root, text='Restar', bd=1, command=resta).place(x=120,y=220)
tk.Button(root, text='Multiplicar', bd=1, command=multiplicacion).place(x=200,y=220)
tk.Button(root, text='Dividir', bd=1, command=division).place(x=300,y=220)
#una opcion de boton salir
tk.Button(root, text='Salir', bd=1, command=root.destroy).place(x=165,y=300)
#este hace que se ejecute el programa
root.mainloop()


