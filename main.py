from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
i=0
app = FastAPI()
# Esto crea una clase Producto
class Producto(BaseModel):
    nombre: str = Field(min_length=5)
    precio: float = Field(ge=0)
    stock: int = Field(ge=0,lt=51)
# Esto es un json útil para crear un objeto
datos = {
    "nombre": "Laptop",
    "precio": 15000,
    "stock": 5
}
# esto crea el objeto utilizando los datos
objeto = Producto(**datos)
objeto = Producto.model_validate(datos)

db = [objeto]
# saludo
@app.get("/")
def saludar():
    return {"mensaje": "hola desde mi api"}

# mostrar db
@app.get("/db")
def mostrar():
    return {"db": db}

@app.post("/crear")
def crear_producto(datos:Producto):
    nuevo_producto= {
        "id": i,
        **datos.model_dump()
    }
    db.append(nuevo_producto)
    i=i+1
    return {"mensaje": "elemento creado"}