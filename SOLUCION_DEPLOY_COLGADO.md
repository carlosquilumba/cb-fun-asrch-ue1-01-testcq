Problema: Despliegue de Azure Function se queda colgado

Sintomas:
- El comando "func azure functionapp publish" se queda en "Deployment in progress, please wait..."
- Pasa mucho tiempo (mas de 10 minutos) sin completar
- Tienes que cancelar con Ctrl+C

Solucion 1: Verificar estado en Portal de Azure

1. Ve al Portal de Azure
2. Busca "Function App" y selecciona cb-fun-asrch-ue1-01-testcq
3. Ve a "Deployment Center" en el menu izquierdo
4. Revisa el estado del despliegue mas reciente
5. Busca errores o advertencias en los logs

Solucion 2: Verificar logs de compilacion

1. En la Function App, ve a "Log stream"
2. Busca errores relacionados con:
   - Dependencias faltantes
   - Errores de compilacion de Python
   - Problemas con requirements.txt
3. Revisa "Logs" en Deployment Center para detalles completos

Solucion 3: Problema con version de Python

Advertencia comun: "Local python version '3.13.7' is different from the version expected for your deployed Function App"

Opciones:

A) Cambiar Function App a Python 3.13 (si esta disponible):
   1. Ve a la Function App en el portal
   2. Ve a "Configuration" -> "General settings"
   3. Cambia "Stack" a Python 3.13
   4. Guarda los cambios
   5. Vuelve a desplegar

B) Usar Python 3.12 localmente:
   1. Instala Python 3.12
   2. Crea un entorno virtual con Python 3.12:
      python3.12 -m venv venv312
      venv312\Scripts\activate (Windows)
   3. Instala dependencias:
      pip install -r requirements.txt
   4. Despliega desde ese entorno

Solucion 4: Limpiar y reintentar

1. Espera 5 minutos despues de cancelar
2. Verifica en Deployment Center que no hay despliegues en progreso
3. Intenta desplegar de nuevo:
   func azure functionapp publish cb-fun-asrch-ue1-01-testcq

Solucion 5: Despliegue alternativo via Portal

Si el despliegue via CLI sigue fallando:

1. Crea un ZIP con todo el contenido de la carpeta cb-fun-asrch-ue1-01-testcq:
   - host.json
   - requirements.txt
   - Saludo/ (carpeta completa con function.json y __init__.py)
   - NO incluyas: local.settings.json, .gitignore, .python_packages, __pycache__

2. Ve a la Function App en el portal
3. Ve a "Deployment Center"
4. Selecciona "External Git" o "Local Git"
5. O ve a "Advanced Tools" (Kudu) -> "Zip Push Deploy"
6. Sube el ZIP manualmente

Solucion 6: Verificar conexion y dependencias

1. Verifica tu conexion a internet (puede ser lento)
2. Verifica que requirements.txt solo tenga:
   azure-functions
   azure-functions-worker
3. Elimina cualquier dependencia extra si las agregaste

Solucion 7: Usar Azure Functions Core Tools en modo verbose

Ejecuta con mas informacion:
   func azure functionapp publish cb-fun-asrch-ue1-01-testcq --verbose

Esto te dara mas detalles sobre donde se esta quedando atascado.

Notas importantes:

- El despliegue puede tardar 5-10 minutos normalmente
- Si pasa mas de 15 minutos, probablemente esta atascado
- La advertencia de version de Python NO impide el despliegue, pero puede causar problemas despues
- Siempre verifica los logs en el Portal de Azure para ver errores reales

