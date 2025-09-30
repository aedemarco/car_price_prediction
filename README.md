# Predicción de Precios de Autos

## Objetivo del Proyecto y Alcance de la PoC

Este proyecto tiene como objetivo desarrollar un sistema de predicción de precios para automóviles utilizando técnicas de aprendizaje automático. El alcance de la Prueba de Concepto (PoC) consiste en entrenar y desplegar un modelo capaz de estimar el valor de un auto a partir de sus características, y se orienta a su despliegue en Google Cloud Platform (GCP).

## Instrucciones para Correr Localmente y Desplegar (Paso a Paso)

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/aedemarco/car_price_prediction.git
   cd car_price_prediction
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configurar variables de entorno necesarias (ver sección correspondiente).
4. Ejecutar los notebooks o scripts de entrenamiento y predicción.
5. Para desplegar en GCP, siga la documentación específica de despliegue (no incluida en este repositorio).

## Variables de Entorno y Manejo de Secretos

- No suba claves ni información sensible al repositorio.
- Utilice archivos `.env` o variables de entorno para configurar credenciales y endpoints.
- Ejemplo:
  ```
  API_KEY=su_clave_aqui
  ```

## Origen de los Datos

- Fuente: Dataset público de precios de autos (especifique el enlace si aplica).
- Licencia/permiso de uso: Asegúrese de cumplir con los términos de uso del dataset utilizado.

## Procedimiento de Anonimización o Generación de Datos Sintéticos

- Si se emplean datos reales con información sensible, se recomienda anonimizar identificadores personales.
- En caso de datos sintéticos, describa brevemente el método de generación.

## URL del Endpoint/API y Ejemplo de Request/Response

(https://car-price-app-337460867469.us-central1.run.app/)

## Diagrama de Arquitectura y Breve Explicación

- Arquitectura básica: Ingesta de datos -> Preprocesamiento -> Entrenamiento del modelo -> Despliegue/API para predicción.
- Utiliza notebooks de Jupyter y scripts Python para procesamiento y predicción.
- Despliegue pensado para GCP, pero adaptable a otros entornos cloud/locales.

## Versiones y Dependencias

- Ver archivo `requirements.txt` para dependencias de Python.
- Si se utiliza Docker, incluir un `Dockerfile` para la imagen del entorno.

## Licencia y Equipo/Miembros

- Licencia: No especificada.
- Equipo/miembros: [aedemarco](https://github.com/aedemarco), Butti Agustina, Carucci Florencia

## Declaración de Originalidad y Citación de Fuentes

- Todo el código y los notebooks son originales, salvo indicación en comentarios.
