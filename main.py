# archivo principal
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import PlainTextResponse
from typing import Annotated
app = FastAPI()

@app.get("/hola")
async def prueba_root():
    return {"message": "Accediste al endpoint de prueba"}
####### 2.a) 
@app.get("/files")
async def buscar_archivos():
    carpeta = "files"

    # Verifica que la carpeta exista
    if not os.path.exists(carpeta):
        return {"error": f"La carpeta '{carpeta}' no existe."}

    # Lista solo los archivos dentro de la carpeta
    archivos = [
        f for f in os.listdir(carpeta)
        if os.path.isfile(os.path.join(carpeta, f))
    ]
    return {"archivos": archivos}

####### 2.b) 
@app.post("/files")
async def upload_file(
    file: Annotated[UploadFile, File(...)]
):
    # Asegurarte de que exista la carpeta "files"
    os.makedirs("files", exist_ok=True)

    # Ruta completa donde se va a guardar
    save_path = os.path.join("files", os.path.basename(file.filename))

    # Leer el contenido del archivo y escribirlo
    with open(save_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {"message": f"Archivo guardado como {save_path}", "size": len(content)}

####### 2.c)
@app.get("/files/{file_name}")
async def contenido_archivo(file_name):
    carpeta = "files"
    
    # Verifica que la carpeta exista
    if not os.path.exists(carpeta):
        return {"error": f"La carpeta '{carpeta}' no existe."}

    # Lista solo los archivos dentro de la carpeta
    archivo = os.path.join(carpeta, file_name)
        # Lee y devuelve el contenido del archivo como texto
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        return PlainTextResponse(content=contenido)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al leer el archivo: {e}")





