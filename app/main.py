from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health():
    """Endpoint de salud para verificar que el servicio está funcionando."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

