# DigitalOcean App Platform — prueba de API FastAPI

Prueba completamente aislada de **CAJAS GABO**, Railway y otros proyectos.

## Contrato

- `GET /health` -> HTTP 200, `{"status":"ok"}`.
- No accede a datos, bancos, archivos ni bases de datos.

## Pruebas locales

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
uvicorn main:app --host 127.0.0.1 --port 8080
```

La URL de prueba es `http://127.0.0.1:8080/health`.

## DigitalOcean App Platform

La especificación se encuentra en `.do/app.yaml`. Configuración preparada:
una instancia de 512 MiB (`apps-s-1vcpu-0.5gb`), región `nyc`, conexión
propuesta al repositorio público de GitHub en `main`, y health check `/health`.

**No se despliega con solo publicar este código.** Crear la aplicación en
DigitalOcean requiere autorización expresa del titular, porque genera cargos.
DigitalOcean puede requerir vincular GitHub a App Platform incluso si el
repositorio es público. La acción de GitHub CI solo ejecuta pruebas y no
despliega ni crea servicios de pago.

## Controles

No agregar credenciales al repositorio. No modificar proyectos productivos.
Conservar esta prueba separada de CAJAS GABO.
