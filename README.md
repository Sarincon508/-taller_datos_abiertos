# 🇨🇴 Datos Abiertos de Colombia (Flutter)

[![Flutter](https://img.shields.io/badge/Flutter-3.47+-02569B?logo=flutter&logoColor=white)](https://flutter.dev/)
[![Dart](https://img.shields.io/badge/Dart-3.13+-0175C2?logo=dart&logoColor=white)](https://dart.dev/)
[![go_router](https://img.shields.io/badge/go__router-14.8+-00599C)](https://pub.dev/packages/go_router)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Aplicación móvil desarrollada en **Flutter** que consume la API pública oficial **[API Colombia](https://api-colombia.com/)**, implementando una arquitectura por capas limpia, navegación declarativa robusta con **go_router**, variables de entorno con **flutter_dotenv** y manejo integral de los estados de la aplicación (**Cargando**, **Éxito**, **Error con reintento**, y **Búsqueda vacía**).

---

## 📌 Tabla de Contenidos
1. [Descripción de la API y Endpoints Seleccionados](#-descripción-de-la-api-y-endpoints-seleccionados)
2. [Arquitectura y Estructura del Proyecto](#-arquitectura-y-estructura-del-proyecto)
3. [Rutas Implementadas con go_router](#-rutas-implementadas-con-go_router)
4. [Ejemplos de Respuesta JSON](#-ejemplos-de-respuesta-json)
5. [Manejo de Estados](#-manejo-de-estados)
6. [Capturas de Pantalla y Evidencias](#-capturas-de-pantalla-y-evidencias)
7. [Instalación y Ejecución](#-instalación-y-ejecución)
8. [Flujo GitFlow y Ramas](#-flujo-gitflow-y-ramas)
9. [Guía para Generar el Entregable en PDF](#-guía-para-generar-el-entregable-en-pdf)

---

## 🌐 Descripción de la API y Endpoints Seleccionados

- **Portal Base:** [https://api-colombia.com/](https://api-colombia.com/)
- **Documentación Swagger:** [https://api-colombia.com/swagger/index.html](https://api-colombia.com/swagger/index.html)
- **Base URL API v1:** `https://api-colombia.com/api/v1`

Se seleccionaron **4 endpoints** de alto valor informativo y visual:

| # | Endpoint | Path Base | Path Detalle | Descripción |
|---|---|---|---|---|
| **1** | **Departamentos** | `/api/v1/Department` | `/api/v1/Department/{id}` | Lista los 32 departamentos de Colombia, con su capital, población, superficie ($km^2$), cantidad de municipios y prefijo telefónico. |
| **2** | **Atracciones Turísticas** | `/api/v1/TouristicAttraction` | `/api/v1/TouristicAttraction/{id}` | Maravillas naturales, reservas ecológicas, parques y monumentos con galería fotográfica, coordenadas y ciudad asociada. |
| **3** | **Presidentes** | `/api/v1/President` | `/api/v1/President/{id}` | Mandatarios históricos de la república, periodos presidenciales, afiliaciones políticas y biografías completas. |
| **4** | **Platos Típicos** | `/api/v1/TypicalDish` | `/api/v1/TypicalDish/{id}` | Gastronomía tradicional colombiana, fotografía, desglose de ingredientes y departamento de origen. |

---

## 🏛 Arquitectura y Estructura del Proyecto

El proyecto sigue una separación rigurosa de responsabilidades basada en la estructura solicitada:

```
lib/
├── config/
│   └── environment.dart              # Gestión centralizada de variables (.env) y constantes
├── models/
│   ├── department_model.dart         # Modelo Department y CityCapital (fromJson / toJson)
│   ├── touristic_attraction_model.dart # Modelo TouristicAttraction y CitySummary
│   ├── president_model.dart          # Modelo President y formateadores de periodo
│   ├── typical_dish_model.dart       # Modelo TypicalDish y DepartmentSummary
│   └── dashboard_card_item.dart      # Metadatos para las tarjetas del Dashboard
├── routes/
│   └── app_router.dart               # Configuración GoRouter, rutas con nombre y parámetros
├── services/
│   └── api_colombia_service.dart     # Cliente HTTP unificado, validación de status codes y excepciones
├── themes/
│   └── app_theme.dart                # Paleta de colores Material 3, temas claro y oscuro
├── views/
│   ├── dashboard_view.dart           # Pantalla principal con cards de introducción
│   ├── departments/
│   │   ├── departments_list_view.dart # Listado con búsqueda en vivo y pull-to-refresh
│   │   └── department_detail_view.dart # Vista completa maestro-detalle
│   ├── attractions/
│   │   ├── attractions_list_view.dart
│   │   └── attraction_detail_view.dart
│   ├── presidents/
│   │   ├── presidents_list_view.dart
│   │   └── president_detail_view.dart
│   └── typical_dishes/
│       ├── typical_dishes_list_view.dart
│       └── typical_dish_detail_view.dart
├── widgets/
│   ├── custom_search_bar.dart        # Barra de búsqueda reutilizable con limpieza rápida
│   ├── dashboard_card.dart           # Card interactiva con gradientes y animaciones táctiles
│   ├── empty_view.dart               # Estado cuando no hay resultados de búsqueda
│   ├── error_view.dart               # Estado de error con código HTTP y botón reintentar
│   ├── image_with_fallback.dart      # Renderizado seguro de imágenes de red con placeholders
│   ├── info_chip.dart                # Chips visuales para atributos métricos
│   └── loading_view.dart             # Indicador de carga con mensaje contextual
└── main.dart                         # Punto de entrada, inicialización de dotenv y MaterialApp.router
```

### Paquetes Implementados:
- **`http`**: Realización de peticiones HTTP con timeouts y decodificación UTF-8.
- **`go_router`**: Navegación declarativa por rutas con nombres, subrutas y paso de parámetros `pathParameters` y objetos `extra`.
- **`flutter_dotenv`**: Carga de configuración desde archivo `.env`.
- **`intl`**: Formato y manejo de fechas y datos numéricos.

---

## 🚦 Rutas Implementadas con go_router

La navegación implementa el patrón **Maestro-Detalle** donde cada detalle puede cargarse directamente mediante su parámetro de ruta `:id` o aprovechar el objeto transferido en `extra` para una transición instantánea:

| Nombre de Ruta (`name`) | Ruta (`path`) | Parámetros | Vista Destino |
|---|---|---|---|
| `dashboard` | `/` | Ninguno | `DashboardView` |
| `departments` | `/departments` | Ninguno | `DepartmentsListView` |
| `department-detail` | `/departments/:id` | `:id` (int), `extra: Department?` | `DepartmentDetailView` |
| `attractions` | `/attractions` | Ninguno | `AttractionsListView` |
| `attraction-detail` | `/attractions/:id` | `:id` (int), `extra: TouristicAttraction?` | `AttractionDetailView` |
| `presidents` | `/presidents` | Ninguno | `PresidentsListView` |
| `president-detail` | `/presidents/:id` | `:id` (int), `extra: President?` | `PresidentDetailView` |
| `typical-dishes` | `/typical-dishes` | Ninguno | `TypicalDishesListView` |
| `typical-dish-detail` | `/typical-dishes/:id` | `:id` (int), `extra: TypicalDish?` | `TypicalDishDetailView` |

---

## 📄 Ejemplos de Respuesta JSON

### 1. Departamentos (`GET /api/v1/Department/1`)
```json
{
  "id": 1,
  "name": "Amazonas",
  "description": "Amazonas es uno de los treinta y dos departamentos que forman la República de Colombia...",
  "cityCapitalId": 1,
  "municipalities": 2,
  "surface": 109665,
  "population": 76589,
  "phonePrefix": "8",
  "cityCapital": {
    "id": 1,
    "name": "Leticia",
    "description": "Capital del departamento de Amazonas...",
    "surface": 5968,
    "population": 42280,
    "postalCode": "910001"
  }
}
```

### 2. Atracciones Turísticas (`GET /api/v1/TouristicAttraction/36`)
```json
{
  "id": 36,
  "name": "Hacienda Nápoles",
  "description": "Centro de entretenimiento familiar a espacio abierto ubicado en Puerto Triunfo, Antioquia...",
  "images": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/P%C3%B3rtico_Hacienda_N%C3%A1poles.JPG/800px-P%C3%B3rtico_Hacienda_N%C3%A1poles.JPG"
  ],
  "latitude": "5.887894",
  "longitude": "-74.6418",
  "city": {
    "id": 88,
    "name": "Puerto Triunfo"
  }
}
```

### 3. Presidentes (`GET /api/v1/President/3`)
```json
{
  "id": 3,
  "image": "https://upload.wikimedia.org/wikipedia/commons/d/db/Rafael_Nunez.JPG",
  "name": "Rafael",
  "lastName": "Núñez Moledo",
  "startPeriodDate": "1887-06-04",
  "endPeriodDate": "1888-08-07",
  "politicalParty": "Partido Nacional",
  "description": "Rafael Wenceslao Núñez Moledo fue un abogado, periodista y político colombiano..."
}
```

### 4. Platos Típicos (`GET /api/v1/TypicalDish/1`)
```json
{
  "id": 1,
  "name": "Bandeja Paisa",
  "description": "La bandeja paisa es uno de los platos más emblemáticos de Colombia...",
  "ingredients": "Frijoles, arroz, carne molida, chicharrón, huevo, plátano maduro, chorizo, arepa, aguacate.",
  "imageUrl": "https://apicolombiastorage.blob.core.windows.net/typicaldishes/1. Bandeja Paisa.jpg",
  "department": {
    "id": 2,
    "name": "Antioquia"
  }
}
```

---

## ⚡ Manejo de Estados

La aplicación implementa 4 estados clave en cada módulo:
1. **Cargando (`LoadingView`)**: Indicador circular animado con texto contextual del endpoint consultado.
2. **Éxito**: Renderizado mediante `ListView.builder` de alta eficiencia en memoria con tarjetas estilizadas y soporte para pull-to-refresh (`RefreshIndicator`).
3. **Error (`ErrorView`)**: Captura excepciones de red (`SocketException`), timeouts y errores HTTP (404, 500), visualizando el código de respuesta y un botón **Reintentar** que relanza la petición.
4. **Búsqueda Vacía (`EmptyView`)**: Notificación visual amigable cuando los filtros de texto no devuelven resultados.

---

## 📸 Capturas de Pantalla y Evidencias

| Dashboard (Home) | Listado con Búsqueda | Detalle de Registro |
|:---:|:---:|:---:|
| ![Dashboard](docs/screenshots/dashboard.png) | ![Listado](docs/screenshots/listado.png) | ![Detalle](docs/screenshots/detalle.png) |

| Estado de Carga | Estado de Error con Reintento | Búsqueda Sin Resultados |
|:---:|:---:|:---:|
| ![Carga](docs/screenshots/loading.png) | ![Error](docs/screenshots/error.png) | ![Vacío](docs/screenshots/empty.png) |

---

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Sarincon508/taller_datos_abiertos.git
   cd taller_datos_abiertos
   ```

2. **Verificar el archivo `.env`:**
   Asegúrese de que el archivo `.env` exista en la raíz del proyecto:
   ```env
   API_BASE_URL=https://api-colombia.com/api/v1
   APP_NAME="Datos Abiertos de Colombia"
   ```

3. **Obtener dependencias:**
   ```bash
   flutter pub get
   ```

4. **Ejecutar pruebas unitarias:**
   ```bash
   flutter test
   ```

5. **Iniciar la aplicación:**
   ```bash
   flutter run
   ```

---

## 🌿 Flujo GitFlow y Ramas

El repositorio sigue estrictamente el flujo de trabajo GitFlow:

- **`main`**: Rama principal de producción / estable.
- **`dev`**: Rama de integración y control de calidad.
- **`feature/taller_api_colombia`**: Rama de desarrollo de las funcionalidades del taller.

### Comandos de ciclo de vida Git:
```bash
# 1. Crear rama dev a partir de main
git checkout -b dev main

# 2. Crear rama feature a partir de dev
git checkout -b feature/taller_api_colombia dev

# 3. Realizar commits atómicos y semánticos
git commit -m "feat(models): implement data models for 4 endpoints"
git commit -m "feat(services): add ApiColombiaService with exception handling"
git commit -m "feat(routes): configure go_router master-detail routing"
git commit -m "feat(views): create Dashboard, ListView and Detail screens"
git commit -m "docs: add comprehensive README with API examples and architecture"

# 4. Pull Request e Integración a dev
git checkout dev
git merge --no-ff feature/taller_api_colombia -m "Merge pull request #1 from feature/taller_api_colombia to dev"

# 5. Integración final a main
git checkout main
git merge --no-ff dev -m "Merge branch 'dev' into main (v1.0.0 Release)"
```

---

## 📄 Guía para Generar el Entregable en PDF

Para entregar el documento solicitado en PDF:
1. Abra el archivo `docs/entregable_taller.html` en cualquier navegador web (Google Chrome, Edge, Brave).
2. Presione `Ctrl + P` (o `Cmd + P` en macOS).
3. Seleccione como destino **Guardar como PDF** (Save as PDF).
4. En **Márgenes**, seleccione **Predeterminado** o **Mínimo**, y marque la casilla **Gráficos de fondo**.
5. ¡Listo! Tendrá un documento formal de presentación con la portada, enlace a su repositorio, ramas, endpoints y descripción técnica.

---

### Desarrollado para la asignatura de Desarrollo Móvil.
- **Autor:** Samuel Rincón
- **Institución:** UCEVA
- **Año:** 2026
