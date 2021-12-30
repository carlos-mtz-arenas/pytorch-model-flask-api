
# acerca de

API para exponer un modelo para la clasificacion de imagenes

# pre requisitos

* python 3.X
* pip

# instalar

```
python3 -m pip install -r requirements.txt
```

# estructura

## iniciar la app

El archivo `startup.sh` sirve para inicializar la aplicacion, esto nos sirve para definir las variables de entorno que vamos a utilizar en nuestro ambiente. Asi que es posible ejecutarlo de la siguiente forma:

```
./startup.sh
```

Alternativamente, puedes ejecutar el archivo `main.py` directamente:

```
python3 ./src/main.py
```

## modelo

El modelo fue ignorado del repositorio, pero puedes incluirlo en `./src/model_meta/dog-trainer.h5` (hardcoded a ese nombre)

Tambien, el archivo `./src/model_meta/model_configuration.py` contiene una relacion de todas las clases que soportamos para nuestro modelo, asi que habria que adaptarlo para tu caso en especifico