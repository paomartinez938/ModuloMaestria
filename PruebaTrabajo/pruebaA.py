import tkinter

if __name__ == '_main_':
    window = tkinter.Tk()
    window.title("Calculadora de Temperatura")
    window.geometry('600x400')

    frame = tkinter.Frame(window)
    frame.pack() ##geometry manager, responsive

    #ingresa datos para generar cálculo
    input_frame = tkinter.LabelFrame(frame, text = "Datos Ingresados")
    input_frame.grid(row=0, column=0) #primera franja del grid

    temperatura_label = tkinter.Label(input_frame, text = "Temperatura")
    temperatura_label.grid(row=0, column=0)

    irradiancia_label = tkinter.Label(input_frame, text = "Irradiancia")
    irradiancia_label.grid(row=1, column=0)

    temperatura_input = tkinter.Entry(input_frame)
    temperatura_input.grid(row=0, column=1)

    irradiancia_input = tkinter.Entry(input_frame)
    irradiancia_input.grid(row=1, column=1)

     # ejemplo funcion de calculo
    def funcion_calculo():
        temperatura = int(temperatura_input.get())
        irradiancia = int(irradiancia_input.get())
        pMax_resultado["text"] = temperatura
        vMax_resultado["text"] = irradiancia

    # boton que ejecuta la funcion de calculo
    calcular_button = tkinter.Button(input_frame, text="Calcular", command=funcion_calculo)
    calcular_button.grid(row=2, column=0)

    # Muestra el resultado del cálculo
    resultado_frame = tkinter.LabelFrame(frame, text="Resultado")
    resultado_frame.grid(row=1, column=0)

    pMax_label = tkinter.Label(resultado_frame, text = "Pmax")
    pMax_label.grid(row=0, column=0)

    pMax_resultado = tkinter.Label(resultado_frame, text = "pMax ##")
    pMax_resultado.grid(row=0, column=1)

    vMax_label = tkinter.Label(resultado_frame, text = "Vmax")
    vMax_label.grid(row=1, column=0)

    vMax_resultado = tkinter.Label(resultado_frame, text = "vMax ##")
    vMax_resultado.grid(row=1, column=1)

    for widget in input_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    for widget in resultado_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    window.mainloop()