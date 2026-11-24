# Proyecto Calculadora CI - Módulo Integración Continua

## Objetivo
Este proyecto es una API web construida en Python con Flask que permite realizar operaciones matemáticas y guardar un historial en una base de datos Redis. El sistema está diseñado para desplegarse mediante dos contenedores comunicados usando Docker Compose.

## Requisitos
- Docker Desktop instalado.

## Comandos para levantar el proyecto
Para construir y levantar los contenedores, ejecute en la raíz del proyecto:
\`\`\`bash
docker compose up --build
\`\`\`
La aplicación estará disponible en `http://localhost:5000`.

## Prueba de comunicación
Para probar que los contenedores se comunican, ejecute:
\`\`\`bash
curl.exe -X POST http://localhost:5000/operar -H "Content-Type: application/json" -d '{\"a\": 5, \"b\": 3, \"op\": \"suma\"}'
\`\`\`