import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Azure Function Saludo procesó una petición.')
    
    try:
        nombre = None
        
        nombre = req.params.get('nombre')
        
        if not nombre:
            try:
                req_body = req.get_json()
                if req_body:
                    nombre = req_body.get('nombre')
            except ValueError:
                pass
        
        if nombre:
            from datetime import datetime, timezone
            
            respuesta = {
                "saludo": f"Hola, {nombre}. La función ha sido ejecutada de forma segura.",
                "nombre": nombre,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "metodo": req.method,
                "estado": "exitoso"
            }
            
            return func.HttpResponse(
                json.dumps(respuesta, ensure_ascii=False),
                status_code=200,
                mimetype="application/json",
                charset="utf-8"
            )
        else:
            error_response = {
                "error": "Parámetro 'nombre' es requerido",
                "descripcion": "Debes proporcionar un nombre como query parameter (?nombre=TuNombre) o en el body JSON ({\"nombre\": \"TuNombre\"})",
                "ejemplos": {
                    "GET": "/api/Saludo?nombre=Juan",
                    "POST": {
                        "nombre": "Juan"
                    }
                },
                "estado": "error"
            }
            
            return func.HttpResponse(
                json.dumps(error_response, ensure_ascii=False),
                status_code=400,
                mimetype="application/json",
                charset="utf-8"
            )
            
    except Exception as e:
        logging.error(f'Error procesando la petición: {str(e)}')
        
        error_response = {
            "error": "Error interno del servidor",
            "mensaje": str(e),
            "estado": "error"
        }
        
        return func.HttpResponse(
            json.dumps(error_response, ensure_ascii=False),
            status_code=500,
            mimetype="application/json",
            charset="utf-8"
        )
