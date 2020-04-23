# ENTRADAS DE LA NEURONA
ent_x1 = 0
ent_x2 = 0

#SALIDA DESEADA
deseado = 0
#- - - - - - - -- - - -  -
# PESOS DE LA ENTRADAS
peso_w1 = 0.0
peso_w2 = 0.2

# UMBRAL DE ACTIVACION
umbral = 0.45

# COEFICIENTE DE APRENDIZAJE
coef_apren = 0.25

# FUNCION DE PROPAGACION
def funcion_propagacion():
  valor = (ent_x1 * peso_w1) + (ent_x2 * peso_w2) - umbral
  print("EL valor es: ",valor)

  if (valor >= 0):
    salida = 1
  else:
    salida = 0
  return(salida)
print("La salida obtenida es: ", funcion_propagacion())

# CALCULO DEL ERROR
def calculo_error():
  obtenido = funcion_propagacion()
  error =  deseado - obtenido
  print("El error es: ", error)
  print("")
  
  # CALCULANDO DELTA
  delta_1 = coef_apren * error * ent_x1
  delta_2 = coef_apren * error * ent_x2

  # NUEVOS PESOS
  _peso_w1 = peso_w1 + delta_1
  _peso_w2 = peso_w2 + delta_2
  print("Los nuevos pesos son: ",
        '\n',"w1 =", _peso_w1,
        '\n',"w2 =", _peso_w2)
  print("")

  # CALCULO DEL UMBRAL
  _umbral = umbral - (coef_apren * error)
  print("El nuevo umbral: ", _umbral)
print(calculo_error())