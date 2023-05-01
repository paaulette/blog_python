# INSTRUCTIVO ENTREGA FINAL
Se deberá ingresar a la siguiente dirección: [127.0.0.1:8000/](http://127.0.0.1:8000/)
La cual mostrará la página inicial de la web

Vínculo para la demo: https://youtu.be/rAD3C_bGaTE

## NAVEGACIÓN EN LOS MENUES
Sobre el margen superior se encuentran las opciones:
-	Inicio
-	Acerca de mi 
-	Crear post 
-	Mi perfil 
-	Desloguear
-	Hola "nombre de usuario"

Se deberá hacer click a alguna de las opciones para ingresar e interactuar

### INICIO
Para poder visualizar esta página requiere un logueo.
Te lleva a la página principal con el listado de todos los posteos. 
En cada uno de esos posteos puede hacer click o pulsar “ver más”  para ver más información.
Los usuarios administradores pueden modificar o borrar los posteos. En caso de modificarlo se abre un formulario con los diferentes campos que se pueden modificar. En caso de borrarlo solicita la confirmación de que realmente se quiere eliminar el posteo en cuestión.

### ACERCA DE MI 
Para poder visualizar esta página requiere un logueo.
Se ingresa a una sección en la cual se puede leer un detalle de la historia del autos junto con el propósito de la página.

### CREAR POST 
Esta opción requiere un logueo con características de Admin para visualizarse y usarse.
Se ingresa a una sección en la cual se puede crear un nuevo posteo.

### DESLOGUEAR 
Esta opción requiere estar logueado para visualizarse y usarse.
Simplemente ejecuta un cierre de sesión informándolo.

### MI PERFIL 
Esta opción requiere un logueo para visualizarse y usarse.
Se ingresa a una sección en la cual se puede ver y modificar datos del usuario. Además se puede agregar una foto de avatar.

### INICIAR SESION u HOLA "NOMBRE DE USUARIO"
Esta opción requiere un logueo para visualizarse y usarse.
Al ingresar se leerá “iniciar sesión” se ingresa a una sección en la cual se puede iniciar sesión o crear un usuario nuevo. En caso de que el usuario ya este creado y logueado se ver “Hola 'nombre de usuario'”.
En el caso de crear un cliente se debe completar los campos:
-	Usuario
-	Mail 
-	Clave

En el caso de tener un usuario ya generado se debe ingresar con un mail y clave:
-	Usuario Admin: paula Clave: probando1234
-	Usuario standard: test Clave: probando1234

El usuario para http://127.0.0.1:8000/admin/
- Usuario: admin
- Clave: probando1234


## EXPLICACION DE LA DEMO EN VIDEO
Vínculo para la demo: https://youtu.be/rAD3C_bGaTE
El video comienza desde el log in. En donde se loguea el usuario “paula” el cual tiene permiso de administrador.
- Al ingresar se puede ver la página con los diferentes Posts cargados. 
- Se ingresa en el titulado “Ruta por la Costa Brava en coche …” donde se puede leer todo el post completo y se selecciona la opción “Editar post” 
- Se habilita un espacio con los campos posibles para modificar. Se cambia el nombre del post y se le agrega “EDITADO”. 
- Al hacer click en “Acerca de mi” se muestra una reseña del creador de la página.
- Al hacer click en “Mi perfil” se muestran: Nombre, Apellido, mail, Contraseña, descripción, web y el botón para subir un avatar. 
- Al hacer click en “Crear Post” se carga un post desde cero con Titulo, Subtitulo, texto e imagen. Al ir a inicio podemos visualizar que se cargó correctamente y luego al ingresar a leerlo completo indicamos la opción borrar. Esto nos lleva a una página en la que nos pide que confirmemos la acción de borrar el post. Al volver al inicio podemos comprobar que el post fue borrado correctamente. 
- Al hacer click en “Desloguear” se muestra una leyenda de que el deslogueo se realizó con exito.
- Se inicia sesión nuevamente con un perfil de “test” (no admin) en donde se puede ver que la opción “crear post” no se visualiza. Al hacer click en “Mi perfil” se muestran: Nombre, Apellido, mail, Contraseña, descripción, web y el botón para subir un avatar. Se prueba un cambio de avatar y luego se hace un deslogueo.
- Por último se crea un nuevo usuario “test2” con perfil no admin. Se confirma y luego se prueba el inicio de sesión de ese nuevo usuario para validar el correcto funcionamiento.