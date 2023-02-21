# Curso de Python: PIP y Entornos Virtuales

Para ejecutar cualquiera de los proyectos del presente repositorio, se ha de iniciar a través del siguiente comando para clonar el mismo:

```sh
git clone
```

## Game project

La carpeta **game** tiene el juego de *Piedra, Papel o Tijera*. Para su ejecución se necesita:
```sh
cd game
python main.py
```

## App project

La carpeta **app** contiene un generador de gráficas a través de *matplotlib* para la población mundial a través de los años. Para su ejecución se necesita:
```sh
cd app
python -m venv env
env/Scripts/activate
pip install -r requirements.txt
python main.py
```