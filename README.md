# Folder Sorter

Ordena una carpeta de archivos en subcarpetas, según su extensión. El archivo
`mappings.json` contiene  un mapa de extensiones y carpetas, para customizar el
ordenamiento.

## Ejecución

Para obtener ayuda sobre la ejecución del programa, podemos ejecutar:

```bash
$ python3 sorter.py -h
```

## Flatter

En conjunto con el *sorter*, se desarrolló un *flatter*. Este realiza el trabajo
inverso, mueve todos los archivos de los subdirectorios al directorio actual (y
elimina los subdirectorio una vez vacios)

Para obtener ayuda sobre su ejecución, nuevamente ejecutamos:

```bash
$ python3 flatter.py -h
```

## Formato Ordenamiento

El formato del archivo de ordenamiento es un JSON que contiene para cada
carpeta, el nombre de las extensiones que deberán ser movidas a dicha carpeta

```json
{
    "Imagenes": [
        ".jpeg",
        ".jpg",
        ...
    ],
    "Documentos": [
        ".pdf",
        ".pptx",
        ...
    ],
    ...
```

Si no se le pasa un archivo con este formato por parámetro, se utilizará el por
defecto, que se encuentra en la carpeta del script.
