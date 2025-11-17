Azure Function: cb-fun-asrch-ue1-01-testcq

Azure Function con la funcion Saludo que recibe un nombre y devuelve un saludo en formato JSON.

Estructura del Proyecto:

cb-fun-asrch-ue1-01-testcq/
- host.json
- local.settings.json
- requirements.txt
- .gitignore
- README.md
- Saludo/
  - function.json
  - __init__.py

Funcion: Saludo

Recibe un nombre por query parameter (GET) o en el body JSON (POST) y devuelve un saludo personalizado en formato JSON.

Ejemplo GET:
URL: https://cb-fun-asrch-ue1-01-testcq.azurewebsites.net/api/Saludo?nombre=Juan

Response JSON:
{
    "saludo": "Hola, Juan. La funcion ha sido ejecutada de forma segura.",
    "nombre": "Juan",
    "timestamp": "2025-01-17T10:30:00Z",
    "metodo": "GET",
    "estado": "exitoso"
}

Ejemplo POST:
URL: https://cb-fun-asrch-ue1-01-testcq.azurewebsites.net/api/Saludo
Body: {"nombre": "Maria"}

Response JSON:
{
    "saludo": "Hola, Maria. La funcion ha sido ejecutada de forma segura.",
    "nombre": "Maria",
    "timestamp": "2025-01-17T10:30:00Z",
    "metodo": "POST",
    "estado": "exitoso"
}

Despliegue:

Azure Functions Core Tools:

1. Navega a la carpeta del proyecto:
   cd cb-fun-asrch-ue1-01-testcq

2. Inicia sesion en Azure:
   az login

3. Despliega la funcion:
   func azure functionapp publish cb-fun-asrch-ue1-01-testcq

Visual Studio Code:

1. Instalar extension "Azure Functions" para VS Code
2. Abrir la carpeta cb-fun-asrch-ue1-01-testcq en VS Code
3. Iniciar sesion en Azure desde VS Code
4. Clic derecho en la carpeta y seleccionar "Deploy to Function App"
5. Seleccionar cb-fun-asrch-ue1-01-testcq

Desarrollo Local:

1. Navega a la carpeta del proyecto:
   cd cb-fun-asrch-ue1-01-testcq

2. Instalar dependencias:
   pip install -r requirements.txt

3. Ejecutar localmente:
   func start

La funcion estara disponible en: http://localhost:7071/api/Saludo?nombre=Juan

Configuracion:

local.settings.json:
Este archivo contiene configuraciones locales. NO subir a repositorio.

Para produccion, actualiza con la connection string del Storage Account:
- AzureWebJobsStorage: Connection string del Storage Account cbsaasrchue101testcq

host.json:
Configuracion global de la Function App. Este archivo SI se sube al repositorio y a Azure.

Notas:

- El nombre de la carpeta del proyecto (cb-fun-asrch-ue1-01-testcq) debe coincidir con el nombre de la Function App en Azure
- Todas las funciones deben estar en subcarpetas dentro del proyecto
- El archivo local.settings.json no debe subirse al repositorio (esta en .gitignore)
