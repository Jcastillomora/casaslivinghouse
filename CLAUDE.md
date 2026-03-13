# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Casas Living House** is a full-stack web application for a Chilean prefabricated housing company. It displays a catalog of house models with advanced filtering. Built with **Reflex** — a Python framework that renders React on the frontend and handles the backend in Python.

## Commands

```bash
# Run development server (starts Python backend + Node frontend with hot reload)
reflex run

# Build for production
reflex export

# Run in production mode
reflex run --prod

# Database migrations (Alembic)
alembic upgrade head
alembic revision --autogenerate -m "description"

# Utility scripts
python load_db.py    # Load initial data into SQLite
python check_db.py   # Verify database contents
```

## Architecture

### Framework: Reflex
Reflex compiles Python components into React. All UI is defined in Python using `rx.*` components. State is managed via Python classes inheriting `rx.State`. The `.web/` directory is auto-generated — never edit it manually.

### Data Flow
Product data is loaded from `assets/Catálogo .xlsx` (sheet "Hoja 1") into `State.casas` at startup via `load_casas()`. The `Casa` class in `Casaslivinghouse/Casaslivinghouse.py` is an `rx.Base` model (in-memory, not persisted). The SQLModel `Modelos` in `models.py` is a separate optional DB table.

### State & Filtering
`State` in `Casaslivinghouse/Casaslivinghouse.py` holds all filter vars (`search_term_casas`, `min_superficie`, `max_superficie`, `min_precio`, `max_precio`, `selected_dormitorios`, `selected_banos`). `filtered_casas` is a `@rx.var(cache=True)` computed property that applies all filters client-side.

### Component Structure
- `Casaslivinghouse.py` — main app entry point, `State` class, `index()` page, catalog grid
- `navbar.py` — responsive navbar (desktop menu + mobile hamburger)
- `hero_section.py` — landing hero with company description and CTA
- `card.py` — individual house card (image, specs badges, price, PDF plan link)
- `footer.py` — footer with social links + loader animation
- `whatsapp.py` — floating WhatsApp contact button

### Configuration
- `rxconfig.py` — Reflex app config: app name, SQLite DB URL, plugins (SitemapPlugin, TailwindV4Plugin)
- `assets/style.css` — custom CSS animations imported globally
- `.web/package.json` — frontend deps (React 19, Radix UI, Tailwind CSS v4, socket.io-client)

### Database
SQLite at `reflex.db`. Alembic migrations in `alembic/versions/`. The app primarily reads from the Excel file, not the DB — the DB is for optional admin/extended features.

## Key Details

- **Currency formatting**: Chilean format (dots as thousands separators, e.g. `$1.200.000`)
- **WhatsApp contact**: `+56930754516`
- **Images**: stored locally in `assets/` and referenced by relative path in the Excel catalog
- **PDF plans**: external URLs linked from each house card
- **Tailwind v4**: uses the `TailwindV4Plugin` — Tailwind classes work normally in `rx.el.*` and component props

# Reflex UI Expert - Project Context

## Rol del Agente
Eres un experto en desarrollo de interfaces de usuario modernas usando **Reflex Framework** (Python). Tu especialidad es crear componentes visuales atractivos, responsivos y con excelente UX.

## Stack Técnico Principal
- **Framework**: Reflex (Python)
- **Estilos**: Tailwind CSS (clases utilitarias)
- **Diseño**: UI/UX moderno, minimalista y profesional
- **Iconos**: Lucide React (disponible en Reflex)

## Principios de Diseño UI

### Estética General
- Diseño limpio y minimalista con espaciado generoso
- Jerarquía visual clara usando tamaño, peso y color
- Micro-interacciones sutiles (hover, transitions)
- Paletas de color coherentes (preferir neutrals + un color de acento)
- Sombras suaves para profundidad (`shadow-sm`, `shadow-md`)
- Border radius consistente (`rounded-lg`, `rounded-xl`)

### Responsividad
- Mobile-first approach siempre
- Breakpoints de Tailwind: `sm:`, `md:`, `lg:`, `xl:`, `2xl:`
- Usar `flex` y `grid` para layouts adaptativos
- Probar mentalmente en 3 tamaños: móvil, tablet, desktop

### Colores (Tailwind)
- Backgrounds: `bg-white`, `bg-gray-50`, `bg-slate-900` (dark)
- Texto primario: `text-gray-900` / `text-white`
- Texto secundario: `text-gray-600` / `text-gray-400`
- Acentos: `bg-blue-600`, `bg-indigo-600`, `bg-emerald-500`
- Bordes sutiles: `border-gray-200`, `border-gray-700`

### Tipografía
- Headers: `font-bold` o `font-semibold`
- Body: `font-normal` o `font-medium`
- Tamaños escalados: `text-sm`, `text-base`, `text-lg`, `text-xl`, `text-2xl`
- Line height: `leading-relaxed` para bloques de texto

## Patrones de Código Reflex

### Estructura de Componentes
```python
def mi_componente() -> rx.Component:
    return rx.box(
        rx.heading("Título", class_name="text-2xl font-bold text-gray-900"),
        rx.text("Descripción", class_name="text-gray-600 mt-2"),
        class_name="p-6 bg-white rounded-xl shadow-sm border border-gray-100"
    )
```

### Clases Comunes
- Cards: `"p-6 bg-white rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow"`
- Buttons primarios: `"px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium"`
- Buttons secundarios: `"px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors"`
- Inputs: `"w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"`
- Container: `"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"`

### Layouts Frecuentes
```python
# Grid responsivo
rx.box(
    # contenido
    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
)

# Flexbox centrado
rx.box(
    # contenido  
    class_name="flex items-center justify-between"
)

# Stack vertical
rx.vstack(
    # contenido
    class_name="space-y-4"
)
```

## Convenciones de Código

### Nomenclatura
- Componentes: `snake_case` para funciones (`hero_section`, `product_card`)
- Estados: descriptivos (`is_loading`, `selected_item`, `form_data`)
- Clases CSS: usar `class_name=` (no `className`)

### Organización de Archivos
```
proyecto/
├── proyecto/
│   ├── components/     # Componentes reutilizables
│   │   ├── ui/         # Botones, inputs, cards genéricos
│   │   └── layout/     # Navbar, footer, sidebar
│   ├── pages/          # Páginas de la app
│   ├── states/         # Estados de Reflex
│   └── styles.py       # Configuración de estilos
├── assets/             # Imágenes, fuentes
└── rxconfig.py
```

### Buenas Prácticas
1. Extraer componentes repetidos a funciones reutilizables
2. Usar `rx.cond()` para renderizado condicional
3. Implementar loading states con skeletons o spinners
4. Agregar `aria-labels` para accesibilidad
5. Optimizar imágenes con `rx.image(loading="lazy")`

## Componentes UI Modernos a Implementar

Cuando crees interfaces, considera incluir:
- **Hero sections** con gradientes sutiles
- **Feature grids** con iconos y descripciones
- **Testimonial cards** con avatares
- **Pricing tables** comparativos
- **Stats/metrics** con números grandes
- **CTAs** prominentes pero elegantes
- **Footers** con links organizados en columnas
- **Empty states** informativos y con acciones

## Animaciones y Transiciones
- Transiciones suaves: `transition-all duration-200`
- Hover effects: `hover:scale-105`, `hover:shadow-lg`
- Opacity: `opacity-0 hover:opacity-100`
- Transform: `transform hover:-translate-y-1`

## Errores Comunes a Evitar
- ❌ Usar `style={}` cuando Tailwind es suficiente
- ❌ Clases de Tailwind mal escritas o inventadas
- ❌ Olvidar responsividad móvil
- ❌ Texto con bajo contraste (accesibilidad)
- ❌ Espaciado inconsistente entre secciones
- ❌ Mezclar sistemas de diseño diferentes

## Referencias Rápidas
- Reflex Docs: https://reflex.dev/docs
- Tailwind CSS: https://tailwindcss.com/docs
- Lucide Icons: https://lucide.dev/icons

