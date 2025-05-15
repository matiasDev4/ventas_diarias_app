# Ventas diarias 🏪
- Esta aplicación la desarrolle con el objetivo de ayudar a mi padre a la hora de sumar las ventas de cada dia en su comercio,
  tener que escribir cada venta en un papel y despues tener que sumar manualmente cada una era tedioso y propenso a errores

# Tecnologias utilizadas 💻
- [Flet](https://flet.dev/) Framework de Python para desarrollar aplicaciones web modernas de forma rápida y sencilla. Lo elegí para poder centrarme en la lógica del backend sin 
  complicarme con el frontend.
- Utilice SQLite3 Base de datos ligera integrada en Python. Ideal para aplicaciones simples y sin necesidad de instalar motores externos.
- [Pandas](https://pandas.pydata.org/) Librería poderosa para manipulación y análisis de datos. En este proyecto la usé para manejar la lectura y escritura de archivos Excel.
- [xlsxwrite](https://xlsxwriter.readthedocs.io/) Módulo especializado en la creación y edición de archivos Excel, complementando a Pandas para un mayor control sobre la         
  exportación.



https://github.com/user-attachments/assets/b99c3a34-f415-4be9-a789-7e78f0e56e65

> [!IMPORTANT]
> En caso de tener un antivirus, añadir la aplicacion a la lista de excepciones. De cualquier manera podes ver el video de ejemplo

[Descarga el ejecutable](https://github.com/matiasDev4/ventas_diarias_app/releases/download/1.0.0/ventas.exe)

# ¿Cómo funciona? ⚙️
La aplicación permite cargar ventas de forma rápida y ordenada, con una interfaz intuitiva. Las funcionalidades principales incluyen:

- Registro de ventas con selección de:

  - Categoría: Impresión, Librería, Cigarrillos, Varios (personalizadas para este proyecto).

  - Método de pago: Efectivo o medios virtuales.

  - Monto de la venta.

![ventas_diarias](https://github.com/user-attachments/assets/d7877d10-9c55-4024-90b7-c51c65fa54bc)


Visualización en tabla: Las ventas ingresadas se muestran en una tabla ordenada, con opciones para editar o eliminar cada fila.

- Botón "Nuevo día":

  - Limpia la tabla datos de la base de datos.

  - Guarda los totales del día en la tabla totales.

  - Exporta los datos a un archivo Excel ubicado en el Escritorio del sistema.
  
  - La base de datos se guarda automáticamente en el directorio APPDATA del sistema, garantizando persistencia sin intervención del usuario.

  ![ventas_excel](https://github.com/user-attachments/assets/f7914601-1a65-4e80-9d78-3fcff2e5859a)


# Clonacion del repositorio
- Instalar las dependecias de este proyecto
  ``pip install -r requirements.txt
  ``
- Corres la aplicacion con:
  ``flet run -d -r src/main.py
  ``
# Proximo objetivo
- Quiero llevar esta idea un paso más allá fusionándola con una aplicación POS desarrollada completamente desde cero. Si bien actualmente existen muchas soluciones POS en el   
  mercado, contar con una herramienta propia, personalizable y adaptada a las necesidades reales de un comercio representa un avance importante en mi trayectoria como desarrollador.
  El objetivo es crear un sistema que pueda ajustarse tanto a comercios específicos como también escalarse y ofrecerse a distintos negocios que necesiten una solución más accesible 
  y a medida, evitando la complejidad innecesaria de las plataformas genéricas.
