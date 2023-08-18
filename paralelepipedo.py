import turtle

# Configuración inicial
turtle.speed(1)  # Velocidad del dibujo (1 = lento, 10 = rápido)

# Dibujar el cuadrado
for _ in range(4):
    turtle.forward(100)  # Lado del cuadrado
    turtle.right(90)  # Girar 90 grados a la derecha

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.done()