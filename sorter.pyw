import os

"""
Para utilizar, modificar las siguientes constantes a gusto.
CARPETA : La ruta de la carpeta que se debe ordenar
MAPA_DE_ARCHIVOS : Relaciona las extensiones de los archivos con la carpeta a la que deben pertenecer.
                   Para agregar una regla, se deben agregar de la forma (NOMBRE_CARPETA, (EXTENSIONES*))
DUPLICADOS : El nombre de la carpeta que contiene los archivos duplicados (por nombre)
"""


CARPETA = r"C:\Users\Julian\Downloads"
MAPA_DE_ARCHIVOS = (
    ("Imagenes", (".jpeg", ".jpg", ".png", ".ico")),
    ("Documentos", (".pdf", ".pptx", ".log", ".docx", ".txt")),
    ("Audio", (".mp3", ".wav")),
    ("Video", (".mp4", ".avi")),
    ("ZIPs", (".zip", ".rar", ".7z")),
    ("Ejecutables", (".msi", ".exe")),
    ("Torrents", (".torrent")),
    ("Jars", (".jar")),
    ("Paquetes de microsoft", (".msu", ".msi")),
    ("Codigo", (".py", ".c", ".h")),
)
DUPLICADOS = "Duplicados"


def mover(origen: str, destino: str) -> None:
    """
    Mueve el archivo de origen a destino.\n
    Si ya existe el archivo de destino, cambia el nombre agregando (n) al final.
    """

    nombre, extension = os.path.splitext(destino)

    i = 2
    while os.path.exists(destino):
        destino = nombre + " ({0})".format(i) + extension
        i += 1

    os.rename(origen, destino)


def obtener_categoria(extension: str) -> str:
    """
    Devuelve el nombre de la carpeta a la que pertence la extension pasada por parametro.\n
    Devuelve None si la extension es deconocida
    """

    for categoria in MAPA_DE_ARCHIVOS:
        if extension.lower() in categoria[1]:
            return categoria[0]


def ordenar_archivo(archivo: str) -> None:
    """
    Ordena el archivo en la carpeta correcta.\n
    Si es una carpeta, o si la extension es desconocida, no hace nada.
    """

    nombre, extension = os.path.splitext(archivo)

    if os.path.isdir(archivo):
        return

    categoria = obtener_categoria(extension)
    if categoria == None:
        print(f'"{archivo}" tiene una extension desconocida')
        return

    if not os.path.isdir(categoria):
        os.mkdir(categoria)

    if os.path.exists(os.path.join(CARPETA, categoria, archivo)):
        if not os.path.isdir(DUPLICADOS):
            os.mkdir(DUPLICADOS)
        mover(
            os.path.join(CARPETA, archivo), os.path.join(CARPETA, DUPLICADOS, archivo)
        )
        print(f'"{archivo}" se movio a la carpeta "{DUPLICADOS}"')
    else:
        mover(
            os.path.join(CARPETA, archivo),
            os.path.join(CARPETA, categoria, archivo),
        )
        print(f'"{archivo}" se movio a la carpeta "{categoria}"')


os.chdir(CARPETA)
for archivo in os.listdir():
    ordenar_archivo(archivo)
