PROJECT

Se trata de un script desarrollado con objeto de simplificar la aplicación diaria de pyautogui para
automatizar tareas en la gestión diaria.

El programa permite ejecutar una ruta en la interfaz entre programas teniendo en cuenta una secuencia
de imágenes y teclas a almacenar en inputs.json y las carpetas de imágenes AccesoFundanet. En caso de
que una imagen en la que hacer click tenga varias alternativas posibles, para evitar que la aparición
de popups o disposiciones aleatorias de las ventanas interfieran en la ejecución correcta de la rutina 
de interfaz, se pueden crear nuevas carpetas AccesoFundanet+número en las que almacenar imágenes 
alternativas con el mismo nombre que la original de AccesoFundanet.

Para definir una ruta de imágenes en las que hacer clic/teclas que pulsar cada cierto tiempo se han 
de añadir en las carpetas AccesoFundanet y definir el inputs.json de la siguiente manera, teniendo
en cuenta que todos los números y valores deben estar entre comillas:

"Nombre de la rutina";{diccionario con los siguientes parámetros de configuración:}
	El resultado de la ejecución del programa será un archivo con el formato especificado en
	"outputformat" en la ruta definida para ello, con este nombre de la rutina y el día, hora,
	y minutos que se especifiquen.

	"activated":["1"] Para activar el ciclo con esa rutina o 0 para apagarlo,

	"clicksroute":[[],[]...] hace referencia en orden a una colección de listas compuestas de
		las siguientes opciones, consistentes en la ruta en la pantalla que seguirá el
		programa para exportar el archivo en el formato indicado en "outputformat":

		Si son imágenes en las que hacer click:
			[nombre del archivo de imagen, 
			si incluye inputs o no (0 ó 1), 
			cuántos clicks hay que hacer, 
			cuánto tiempo esperar después, 
			[el desplazamiento respecto de las posiciones x e y del centro de la imagen 
			para introducir el input en su caso], 
			y si se puede saltar el reconocimiento de la imagen o no]. 

		Si se trata de una combinación de teclas: 
			[0 para indicar que es una combinación de teclas, 
			si incluye inputs o no (0 ó 1), 
			[lista de listas 
				[tecla, si es keydown 1 si es keyup 0]...], 
			delay en tiempo tras la pulsación o levante de teclas,
			0 en todo caso,
			0 en todo caso]. 
	"inputs":[,] Lista de entradas para las imágenes/teclas que den acceso a inputs en los que 
		haya que escribir información, rutas de archivo para guardar...

	"outputformat":".xlsx" Por ejemplo, para guardar el archivo de salida en el formato correcto.

MODULES

El módulo principal a cargar desde otros archivos de python es Accesoimgs.py y este carga inputs.json
que especifica la ruta automatizada a ejecutar y el contenido de la carpeta "Accesoimgs" con los iconos
en los que hacer click de acuerdo con lo especificado en inputs.json.

CONTACT AND CONTRIBUTION

Este es un proyecto personal que no está abierto a contribuciones ahora mismo pero siéntete libre de 
compartir cualquier comentario, pregunta o sugerencia a través de javiercuartasmicieces@hotmail.com.

ACKNOWLEDGEMENTS

Los scripts fueron desarrollados utilizando especialmente la librería pyautogui, con objeto de 
simplificar su uso diario. El módulo está desarrollado en python (v3.7) con el IDLE Anaconda 
(proyecto personal).