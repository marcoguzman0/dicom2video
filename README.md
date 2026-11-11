# dicom2video

Convertidor de secuencias de imágenes en video MP4, diseñado para trabajar con archivos PNG exportados desde estudios médicos o visualizadores como Weasis.

## Descripción

Este repositorio toma una carpeta de imágenes (`input/`) y genera un video en formato MP4 usando `ffmpeg`. La utilidad está pensada para casos donde los archivos están numerados secuencialmente, como:

- `00001.png`
- `00002.png`
- `00003.png`
- ...

Además, si las imágenes tienen sufijos adicionales como `imagen-axial.png`, la aplicación intenta limpiar el nombre eliminando el último segmento del estilo `-xxxx` para dejar una numeración ordenada antes de crear el video.

## Características

- Crea automáticamente las carpetas `input/` y `output/` si no existen.
- Renombra imágenes con sufijos no deseados para conservar la secuencia numérica.
- Genera un video MP4 usando `ffmpeg` con configuración estándar de compresión H.264.
- Incluye un menú simple de consola para elegir entre renombrar + generar video o salir.

## Requisitos

- Python 3.10 o superior
- `ffmpeg` instalado y disponible en el `PATH`

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/marcoguzman0/dicom2video.git
   cd dicom2video
   ```

2. Asegúrate de tener `ffmpeg` instalado:

   - Windows: descarga FFmpeg y agrega la carpeta `bin` al `PATH`.
   - Linux/macOS: usa el gestor de paquetes correspondiente o instala FFmpeg desde la documentación oficial.

3. Coloca las imágenes a convertir dentro de la carpeta `input/`.

## Uso

Ejecuta el programa:

```bash
python main.py
```

Se mostrará un menú:

1. `Rename images and generate video`
2. `Exit program`

### Opción 1

- Renombra las imágenes en `input/` para limpiar sufijos extra.
- Genera el video final en:

```text
output/output.mp4
```

### Opción 2

Sale del programa sin realizar cambios.

## Estructura del proyecto

```text
dicom2video/
├── main.py
├── utils.py
├── input/
│   ├── 00001.png
│   ├── 00002.png
│   └── ...
├── output/
│   └── output.mp4
├── .gitignore
└── README.md
```

## Cómo funciona

El flujo principal es:

1. `main.py` inicia la aplicación.
2. `utils.ensure_directories()` crea `input/` y `output/` si faltan.
3. `utils.main_menu()` presenta el menú interactivo.
4. `utils.rename_images()` renombra archivos `.png` según un patrón de sufijo y deja la secuencia ordenada.
5. `utils.generate_video()` ejecuta `ffmpeg` usando los archivos numerados como frames del video.

## Notas importantes

- El proyecto asume que los archivos de entrada están numerados en orden y que el nombre base puede reutilizarse.
- El video se genera con una tasa de 3 fps por defecto, aunque es posible ajustarla en la función `generate_video()`.
- La salida se guarda en `output/output.mp4`.

## Licencia

Este proyecto no especifica una licencia en el repositorio actual.
