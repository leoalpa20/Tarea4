# Tarea4

# Punto 1

Se adjunta PNG con la funcion modulada, se muestran los primeros 5 bits de la modulacion, para estar parte se uso un loop con un for y un if para asi asignar el valor de seno si es un uno y menos seno si se tiene un cero.

# Punto 2

Para calcular la potencia de la señal se usa la funcion de integracion trapeziodal de numpy, para lo cual se obtiene un valor de 0.499500049950005

# Punto 3

Se nos pide graficar nuevamente la funcion  pero con ruido añadido ya que asi se asemeja mas a un señal verdadera las cuales son altamente ruidosas, para esto se hace un rango de ruido en dB desde -2 a 3 como se nos pide y se grafica la funcion mas el ruido blanco guassiano que es obtenido con ayuda de numpy, se puede apreciar como es de esperarse que a medida que aumentan el nivel de ruido se distorsiona aun mas la señal e incluso si se coloca un nivel muy alto como 60 dB lo cual es demasiado la señal se pierde completamente y queda solamente ruido.

# Punto 4

Con ayuda del modulo signal se calcula el grafico de la potencial espectral de la señal, antes y despues del ruido, la cual varia considerablememte, se adjuntan los graficos.

# Punto 5

Para este punto se nos pide calcular el BER para lo que se obtiene un valro de cero para los 5 valores de SNR, si se prueba con valores de SNR mas altos se comienzan a obtener ya errores en elos bits, para que una señal se pueda consedirar buena, no se pueden perder mas de un bit cada diez mil, en teoria se esta cumplieando bien con este aspecto.

# Punto 6

Graficar BER contra SNR, lo cual es una linea recta para todos los valores de SNR pues BER es cero que es constante.
