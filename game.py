import tkinter as tk
import random

# Clase que representa el tablero del juego
class Tablero:
    def __init__(self, filas, columnas, num_obstaculos):
        self.filas = filas  # Número de filas del tablero
        self.columnas = columnas  # Número de columnas del tablero
        # Inicializa el tablero con ceros (vacío)
        self.tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.posicion_gato = (0, 0)  # Posición inicial del gato
        self.posicion_raton = (filas - 1, columnas - 1)  # Posición inicial del ratón
        self.tablero[0][0] = 1  # Marca la posición del gato en el tablero
        self.tablero[filas - 1][columnas - 1] = 2  # Marca la posición del ratón en el tablero
        self.generar_obstaculos(num_obstaculos)  # Genera obstáculos aleatorios

    def generar_obstaculos(self, num_obstaculos):
        """Genera obstáculos aleatorios en el tablero."""
        obstaculos_colocados = 0
        while obstaculos_colocados < num_obstaculos:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if self.tablero[fila][columna] == 0 and (fila, columna) not in [self.posicion_gato, self.posicion_raton]:
                self.tablero[fila][columna] = -1
                obstaculos_colocados += 1

    # Método para mover el gato a una nueva posición
    def mover_gato(self, nueva_posicion):
        self.tablero[self.posicion_gato[0]][self.posicion_gato[1]] = 0  # Limpia la posición anterior del gato
        self.posicion_gato = nueva_posicion  # Actualiza la posición del gato
        self.tablero[nueva_posicion[0]][nueva_posicion[1]] = 1  # Marca la nueva posición del gato

    # Método para mover el ratón a una nueva posición
    def mover_raton(self, nueva_posicion):
        self.tablero[self.posicion_raton[0]][self.posicion_raton[1]] = 0  # Limpia la posición anterior del ratón
        self.posicion_raton = nueva_posicion  # Actualiza la posición del ratón
        self.tablero[nueva_posicion[0]][nueva_posicion[1]] = 2  # Marca la nueva posición del ratón
    
    # Método que devuelve el estado actual del tablero
    def estado_actual(self):
        return self.tablero

# Clase que representa el juego del gato y el ratón
class JuegoGatoRaton(tk.Tk):
    def __init__(self):
        super().__init__()  # Inicializa la ventana principal
        self.title("Configuración del Juego del Gato y el Ratón")  # Título de la ventana
        self.filas = 5  # Número de filas del tablero por defecto
        self.columnas = 5  # Número de columnas del tablero por defecto
        self.num_obstaculos = 5  # Número de obstáculos por defecto
        self.crear_pantalla_configuracion()  # Crea la pantalla de configuración

    # Método para crear la pantalla de configuración
    def crear_pantalla_configuracion(self):
        self.pantalla_configuracion = tk.Frame(self)
        self.pantalla_configuracion.pack(padx=20, pady=20)
        
        # Entrada para el número de filas
        tk.Label(self.pantalla_configuracion, text="Número de filas:").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_filas = tk.Entry(self.pantalla_configuracion)
        self.entrada_filas.grid(row=0, column=1, padx=5, pady=5)
        self.entrada_filas.insert(0, str(self.filas))

        # Entrada para el número de columnas
        tk.Label(self.pantalla_configuracion, text="Número de columnas:").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_columnas = tk.Entry(self.pantalla_configuracion)
        self.entrada_columnas.grid(row=1, column=1, padx=5, pady=5)
        self.entrada_columnas.insert(0, str(self.columnas))

        # Entrada para el número de obstáculos
        tk.Label(self.pantalla_configuracion, text="Número de obstáculos:").grid(row=2, column=0, padx=5, pady=5)
        self.entrada_obstaculos = tk.Entry(self.pantalla_configuracion)
        self.entrada_obstaculos.grid(row=2, column=1, padx=5, pady=5)
        self.entrada_obstaculos.insert(0, str(self.num_obstaculos))

        # Botón para iniciar el juego
        boton_iniciar = tk.Button(self.pantalla_configuracion, text="Iniciar Juego", command=self.iniciar_juego)
        boton_iniciar.grid(row=3, column=0, columnspan=2, pady=10)

    # Método para iniciar el juego con las configuraciones seleccionadas
    def iniciar_juego(self):
        try:
            self.filas = int(self.entrada_filas.get())
            self.columnas = int(self.entrada_columnas.get())
            self.num_obstaculos = int(self.entrada_obstaculos.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
            return
        
        # Destruir la pantalla de configuración
        self.pantalla_configuracion.destroy()
        
        # Inicializar el tablero y la interfaz gráfica del juego
        self.tablero = Tablero(self.filas, self.columnas, self.num_obstaculos)
        self.celdas = [[None for _ in range(self.columnas)] for _ in range(self.filas)]
        self.title("Juego del Gato y el Ratón")
        self.crear_tablero()
        self.eleccion = None
        self.crear_pantalla_seleccion()

    # Método para crear la pantalla de selección de personaje
    def crear_pantalla_seleccion(self):
        self.pantalla_seleccion = tk.Toplevel(self)  # Crea una nueva ventana secundaria
        self.pantalla_seleccion.title("Selecciona tu personaje")  # Título de la ventana secundaria
        # Etiqueta con el mensaje de selección
        mensaje_label = tk.Label(self.pantalla_seleccion, text="¿Quieres ser el gato o el ratón?", padx=20, pady=20)
        mensaje_label.pack()  # Empaqueta la etiqueta en la ventana
        # Botón para seleccionar al gato
        boton_gato = tk.Button(self.pantalla_seleccion, text="Gato", command=lambda: self.iniciar_juego_personaje("gato"))
        boton_gato.pack(side="left", padx=20)  # Empaqueta el botón a la izquierda
        # Botón para seleccionar al ratón
        boton_raton = tk.Button(self.pantalla_seleccion, text="Ratón", command=lambda: self.iniciar_juego_personaje("raton"))
        boton_raton.pack(side="right", padx=20)  # Empaqueta el botón a la derecha

    # Método para iniciar el juego según la elección del usuario
    def iniciar_juego_personaje(self, eleccion):
        self.eleccion = eleccion  # Almacena la elección del usuario
        self.pantalla_seleccion.destroy()  # Cierra la ventana de selección
        self.bind("<KeyPress>", self.tecla_presionada)  # Asigna el evento de tecla presionada a un método
        if self.eleccion == "raton":  # Si el usuario eligió ser el ratón
            self.mover_gato_minimax()  # El gato se mueve primero usando el algoritmo Minimax
    
    # Método para crear la interfaz gráfica del tablero
    def crear_tablero(self):
        for i in range(self.filas):  # Itera sobre las filas
            for j in range(self.columnas):  # Itera sobre las columnas
                # Crea una celda con un borde
                celda = tk.Label(self, text="", width=4, height=2, borderwidth=2, relief="solid")
                celda.grid(row=i, column=j)  # Coloca la celda en la posición correspondiente
                self.celdas[i][j] = celda  # Almacena la celda en la matriz
        self.actualizar_tablero()  # Actualiza la interfaz gráfica del tablero
        # Añadir un botón de reinicio
        boton_reiniciar = tk.Button(self, text="Reiniciar", command=self.reiniciar_juego)
        boton_reiniciar.grid(row=self.filas, column=0, columnspan=self.columnas)

    # Método para reiniciar el juego
    def reiniciar_juego(self):
        self.tablero = Tablero(self.filas, self.columnas, self.num_obstaculos)
        self.actualizar_tablero()

    # Método para actualizar la interfaz gráfica del tablero
    def actualizar_tablero(self):
        for i in range(self.filas):  # Itera sobre las filas
            for j in range(self.columnas):  # Itera sobre las columnas
                if self.tablero.tablero[i][j] == 1:  # Si la celda contiene al gato
                    self.celdas[i][j].config(bg="orange")  # Colorea la celda de naranja
                elif self.tablero.tablero[i][j] == 2:  # Si la celda contiene al ratón
                    self.celdas[i][j].config(bg="gray")  # Colorea la celda de gris
                elif self.tablero.tablero[i][j] == -1:  # Si la celda contiene un obstáculo
                    self.celdas[i][j].config(bg="black")  # Colorea la celda de negro
                else:  # Si la celda está vacía
                    self.celdas[i][j].config(bg="white")  # Colorea la celda de blanco
    
    # Método para manejar el evento de tecla presionada
    def tecla_presionada(self, evento):
        if evento.keysym in ["Up", "Down", "Left", "Right"]:  # Si la tecla es una flecha
            if self.eleccion == "gato":  # Si el usuario controla al gato
                self.mover_gato(evento.keysym)  # Mueve al gato
                self.after(200, self.mover_raton_minimax)  # Espera 200 ms y mueve al ratón usando Minimax
            elif self.eleccion == "raton":  # Si el usuario controla al ratón
                self.mover_raton(evento.keysym)  # Mueve al ratón
                self.after(200, self.mover_gato_minimax)  # Espera 200 ms y mueve al gato usando Minimax
    
    # Método para mover al gato en la dirección especificada
    def mover_gato(self, direccion):
        movimientos = {  # Diccionario de movimientos posibles
            "Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)
        }
        dx, dy = movimientos[direccion]  # Obtiene el cambio en coordenadas
        nueva_posicion = (self.tablero.posicion_gato[0] + dx, self.tablero.posicion_gato[1] + dy)  # Calcula la nueva posición
        if self.posicion_valida(nueva_posicion):  # Si la nueva posición es válida
            self.tablero.mover_gato(nueva_posicion)  # Mueve al gato a la nueva posición
            self.actualizar_tablero()  # Actualiza la interfaz gráfica del tablero
            self.verificar_final_juego()  # Verifica si el juego ha terminado
    
    # Método para mover al ratón en la dirección especificada
    def mover_raton(self, direccion):
        movimientos = {  # Diccionario de movimientos posibles
            "Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)
        }
        dx, dy = movimientos[direccion]  # Obtiene el cambio en coordenadas
        nueva_posicion = (self.tablero.posicion_raton[0] + dx, self.tablero.posicion_raton[1] + dy)  # Calcula la nueva posición
        if self.posicion_valida(nueva_posicion):  # Si la nueva posición es válida
            self.tablero.mover_raton(nueva_posicion)  # Mueve al ratón a la nueva posición
            self.actualizar_tablero()  # Actualiza la interfaz gráfica del tablero
            self.verificar_final_juego()  # Verifica si el juego ha terminado
    
    # Método para mover al gato usando el algoritmo Minimax con poda alpha-beta
    def mover_gato_minimax(self):
        mejor_movimiento = None  # Variable para almacenar el mejor movimiento
        mejor_valor = float('inf')  # Inicializa el mejor valor a infinito positivo
        alpha = -float('inf')  # Inicializa alpha para la poda alpha-beta
        beta = float('inf')  # Inicializa beta para la poda alpha-beta
        depth = self.calcular_profundidad_dinamica(self.tablero.posicion_gato, self.tablero.posicion_raton)  # Calcula la profundidad dinámica
        for movimiento in self.obtener_movimientos_validos(self.tablero.posicion_gato):  # Itera sobre los movimientos válidos del gato
            valor = self.minimax(movimiento, self.tablero.posicion_raton, depth, False, alpha, beta)  # Calcula el valor del movimiento usando Minimax con poda alpha-beta
            if valor < mejor_valor:  # Si el valor es mejor que el mejor valor
                mejor_valor = valor  # Actualiza el mejor valor
                mejor_movimiento = movimiento  # Actualiza el mejor movimiento
        if mejor_movimiento:  # Si se encontró un mejor movimiento
            self.tablero.mover_gato(mejor_movimiento)  # Mueve al gato al mejor movimiento
            self.actualizar_tablero()  # Actualiza la interfaz gráfica del tablero
            self.verificar_final_juego()  # Verifica si el juego ha terminado
    
    # Método para mover al ratón usando el algoritmo Minimax con poda alpha-beta
    def mover_raton_minimax(self):
        mejor_movimiento = None  # Variable para almacenar el mejor movimiento
        mejor_valor = -float('inf')  # Inicializa el mejor valor a infinito negativo
        alpha = -float('inf')  # Inicializa alpha para la poda alpha-beta
        beta = float('inf')  # Inicializa beta para la poda alpha-beta
        depth = self.calcular_profundidad_dinamica(self.tablero.posicion_raton, self.tablero.posicion_gato)  # Calcula la profundidad dinámica
        for movimiento in self.obtener_movimientos_validos(self.tablero.posicion_raton):  # Itera sobre los movimientos válidos del ratón
            valor = self.minimax(self.tablero.posicion_gato, movimiento, depth, True, alpha, beta)  # Calcula el valor del movimiento usando Minimax con poda alpha-beta
            if valor > mejor_valor:  # Si el valor es mejor que el mejor valor
                mejor_valor = valor  # Actualiza el mejor valor
                mejor_movimiento = movimiento  # Actualiza el mejor movimiento
        if mejor_movimiento:  # Si se encontró un mejor movimiento
            self.tablero.mover_raton(mejor_movimiento)  # Mueve al ratón al mejor movimiento
            self.actualizar_tablero()  # Actualiza la interfaz gráfica del tablero
            self.verificar_final_juego()  # Verifica si el juego ha terminado
    
    # Método para calcular la profundidad dinámica basada en la distancia de Manhattan
    def calcular_profundidad_dinamica(self, pos1, pos2):
        if pos1 is None or pos2 is None:
            return 2  # Devuelve una profundidad por defecto si alguna posición es None
        distancia = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
        if distancia <= 2:
            return 4  # Profundidad mayor cuando están muy cerca
        elif distancia <= 4:
            return 3  # Profundidad media cuando están moderadamente cerca
        else:
            return 2  # Profundidad menor cuando están lejos
    
    # Método que implementa el algoritmo Minimax con poda alpha-beta
    def minimax(self, posicion_gato, posicion_raton, profundidad, es_maximizador, alpha, beta):
        if profundidad == 0 or posicion_gato == posicion_raton:  # Si la profundidad es 0 o el gato atrapó al ratón
            return self.evaluar_tablero(posicion_gato, posicion_raton)  # Retorna la evaluación del tablero
        
        if es_maximizador:  # Si el nodo es maximizador
            max_eval = -float('inf')  # Inicializa la mejor evaluación a infinito negativo
            for movimiento in self.obtener_movimientos_validos(posicion_raton):  # Itera sobre los movimientos válidos del ratón
                eval = self.minimax(posicion_gato, movimiento, profundidad - 1, False, alpha, beta)  # Calcula la evaluación del movimiento usando Minimax con poda alpha-beta
                max_eval = max(max_eval, eval)  # Actualiza la mejor evaluación
                alpha = max(alpha, eval)  # Actualiza alpha
                if beta <= alpha:  # Poda beta
                    break
            return max_eval  # Retorna la mejor evaluación
        else:  # Si el nodo es minimizador
            min_eval = float('inf')  # Inicializa la mejor evaluación a infinito positivo
            for movimiento in self.obtener_movimientos_validos(posicion_gato):  # Itera sobre los movimientos válidos del gato
                eval = self.minimax(movimiento, posicion_raton, profundidad - 1, True, alpha, beta)  # Calcula la evaluación del movimiento usando Minimax con poda alpha-beta
                min_eval = min(min_eval, eval)  # Actualiza la mejor evaluación
                beta = min(beta, eval)  # Actualiza beta
                if beta <= alpha:  # Poda alpha
                    break
            return min_eval  # Retorna la mejor evaluación
    
    # Método para evaluar el tablero
    def evaluar_tablero(self, posicion_gato, posicion_raton):
        """Evalúa el tablero en función de la distancia entre el gato y el ratón.
        
        Maximiza la distancia entre el gato y el ratón si el usuario controla al ratón,
        y minimiza la distancia si el usuario controla al gato.
        """
        if posicion_gato is None or posicion_raton is None:
            return 0  # Evaluación por defecto si alguna posición es None
        distancia = abs(posicion_gato[0] - posicion_raton[0]) + abs(posicion_gato[1] - posicion_raton[1])
        if self.eleccion == "gato":
            return -distancia
        else:
            return distancia
    
    # Método para obtener los movimientos válidos desde una posición dada
    def obtener_movimientos_validos(self, posicion):
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Lista de movimientos posibles
        movimientos_validos = []  # Lista para almacenar los movimientos válidos
        for dx, dy in movimientos:  # Itera sobre los movimientos posibles
            nueva_posicion = (posicion[0] + dx, posicion[1] + dy)  # Calcula la nueva posición
            if self.posicion_valida(nueva_posicion):  # Si la nueva posición es válida
                movimientos_validos.append(nueva_posicion)  # Agrega la nueva posición a los movimientos válidos
        return movimientos_validos  # Retorna los movimientos válidos
    
    # Método para verificar si una posición es válida
    def posicion_valida(self, posicion):
        x, y = posicion  # Obtiene las coordenadas de la posición
        return 0 <= x < self.filas and 0 <= y < self.columnas and self.tablero.tablero[x][y] in [0, 2]  # Verifica si las coordenadas están dentro del tablero y no hay un obstáculo

    # Método para verificar si el juego ha terminado
    def verificar_final_juego(self):
        if self.tablero.posicion_raton == self.tablero.posicion_gato:  # Si el gato atrapó al ratón
            self.mostrar_mensaje_fin("¡El gato atrapó al ratón!")  # Muestra un mensaje de fin del juego
    
    # Método para mostrar un mensaje de fin del juego
    def mostrar_mensaje_fin(self, mensaje):
        ventana_fin = tk.Toplevel(self)  # Crea una nueva ventana secundaria
        ventana_fin.title("Fin del Juego")  # Título de la ventana secundaria
        mensaje_label = tk.Label(ventana_fin, text=mensaje, padx=20, pady=20)  # Crea una etiqueta con el mensaje
        mensaje_label.pack()  # Empaqueta la etiqueta en la ventana
        boton_cerrar = tk.Button(ventana_fin, text="Cerrar", command=self.destroy)  # Crea un botón para cerrar el juego
        boton_cerrar.pack(pady=10)  # Empaqueta el botón en la ventana

# Código principal para iniciar el juego
if __name__ == "__main__":
    juego = JuegoGatoRaton()  # Crea una instancia del juego
    juego.mainloop()  # Inicia el bucle principal de la interfaz gráfica
