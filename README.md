# Ventas diarias 🏪
- Esta aplicación la desarrolle con el objetivo de ayudar a mi padre a la hora de sumar las ventas de cada dia en su comercio,
  tener que escribir cada venta en un papel y despues tener que sumar manualmente cada una era tedioso y propenso a errores

# Tecnologias utilizadas 💻
- Decidi volver a utilizar [Flet](https://flet.dev/) el framework de python para desarrollar aplicaciónes web modernas de manera rapida y facil, para poder centrarme
  mejor en el backend de la aplicación
- Utilice SQLite3 que viene por defecto con python, una base de datos liviana que combina bastante bien para aplicaciónes simples
- [Pandas](https://pandas.pydata.org/) Una libreria de python muy potente para la manipulacion de datos, en esa ocación la utilice
  para manipular la escritura y lectura de un archivo Excel
- [xlsxwrite](https://xlsxwriter.readthedocs.io/) un modulo de python para la creación y manipulación de archivos Excel

# Como funciona
- La idea principal de esta aplicación es poder cargar las ventas y verlas de manera ordenada, que sea lo mas intuitiva posible.
  Ofreciendo las opciones de poder seleccionar la categoria de venta (Impresion, Libreria, Cigarrillos, Varios) obviamente son opciones personalizadas para esta ocación, no es nada   
  general. Por otro lado tenes las opciones del metodo de pago (Efectivo o un cualquier medio virtual) y por ultimo el input para escribir el monto de la venta.
  Una vez enviados esos datos, se pueden visualizar en la tabla de manera odernada con las opciones de editar o eliminar cada fila
