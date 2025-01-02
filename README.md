# Prueba tecnica
## Microservicio para cálculo de precios finales

Este servicio fue construido con FastAPI debido a su rapidez y facilidad para crear APIs robustas en Python. Utiliza Pydantic para la validación de datos y SQLAlchemy ORM para interactuar con la base de datos. Además, la aplicación está diseñada para ser contenerizada con Docker y desplegada en un cluster de Kubernetes en GKE.

### Software requerido

- Python >= 3.12
- Docker

### Configuración de entorno de desarrollo

Es recomendable que se utilice un entorno virtual (_virtual environment_) de Python para el desarrollo y ejecución del microservicio en un entorno local.

Para la ejecución de los siguientes comandos se asume el uso de Windows y de PowerShell. 

#### Python virtual environment

```PowerShell
PS C:\...\humblecoop-service> python -m venv <nombre de entorno virtual>
```

> Es convención usar `.venv` para nombrar todos los entornos virtuales que inicialicemos.

Se activa el entorno virtual y se agregan los modulos requeridos.

```PowerShell
PS C:\...\humblecoop-service> .\.venv\Scripts\activate
(venv) PS C:\...\humblecoop-service> pip install --upgrade pip
(venv) PS C:\...\humblecoop-service> pip install -r requirements.txt
```


### Ejecución sin Docker

#### Ejecución de FastAPI app

```PowerShell
(venv) PS C:\...\humblecoop-service> cd src
(venv) PS C:\...\humblecoop-service\src> uvicorn app.main:app
```

### Ejecución con Docker

```PowerShell
(venv) PS C:\...\humblecoop-service> docker build -t hamblecoop-service .
(venv) PS C:\...\humblecoop-service> docker run -d -p 8080:8080 hamblecoop-service
```

## Ruta del servicio
- **Sin docker**: `http://127.0.0.1:8000/`

- **En docker**: `http://localhost:8080/`

## Guía para usar el servicio

## Endpoints

### Ruta del swagger:
- **Swagger**: `/v1/docs`

### 1. Calcular precios
- **Endpoint**: `/calculate-prices`
- **Método HTTP**: `POST`
- **Descripción**: Calcula el precio final de un producto segun el descuento del provedor.
- **Esquema de Entrada**:
  ```json
    {
      "items": [
        {
          "sku": "string",
          "unitPrice": "float",
          "provider": "string"
        },
        {
          "sku": "string",
          "unitPrice": "float",
          "provider": "string"
        }
      ]
    }
  ```

- **Ejemplo de Entrada**:
  ```json
    {
      "items": [
          {
            "sku": "2626",
            "unitPrice": 29.0,
            "provider": "Provedor Z"
          },
          {
            "sku": "0896-a",
            "unitPrice": 24.5,
            "provider": "Provedor D"
          }
      ]
    }
   ```
- **Respuesta del servicio**:
    ```json
    {
      "items": [
        {
    	  "sku": "2626",
    	  "unitPriceWithDiscount": null,
    	  "error": "Provider 'Provedor Z' not found"
    	},
    	{
    	  "sku": "0896-a",
    	  "unitPriceWithDiscount": 18.375,
    	  "error": null
    	}
      ]
    }
    ```

## Ejecucion de los tests unitarios
```PowerShell
(venv) PS C:\...\humblecoop-service> pytest
```

## La base de datos en Sqlite contiene una tabla llamada providers y su contenido es el siguiente:

| id | provider_name   | discount  |
|----|-------------|-------|
| 1  | Proveedor F | 0.12  |
| 2  | Proveedor A | 0.10  |
| 3  | Proveedor B | 0.30  |
| 4  | Proveedor C | 0.15  |
| 5  | Proveedor D | 0.25  |
| 6  | Proveedor E | 0.50  |

## La rutas y los endpoints del servicio desplegado en Google Cloud son las siguientes:

* Ruta del servicio: https://humblecoop-service-233019416601.us-east1.run.app/

* Ruta del endpoint del calculo de precios: https://humblecoop-service-233019416601.us-east1.run.app/calculate-prices

* Ruta del swagger: https://humblecoop-service-233019416601.us-east1.run.app/v1/docs