import reflex as rx

PASOS = [
    {
        "numero": "01",
        "titulo": "Elige tu modelo",
        "descripcion": "Navega por nuestro catálogo y elige el modelo que se adapta a tu terreno y presupuesto.",
        "icono": "home",
    },
    {
        "numero": "02",
        "titulo": "Solicita tu cotización",
        "descripcion": "Te enviamos una cotización detallada con precios, plazos y opciones de financiamiento.",
        "icono": "file-text",
    },
    {
        "numero": "03",
        "titulo": "Firmamos el contrato",
        "descripcion": "Acordamos los términos comerciales y firmamos el contrato de compraventa con garantías.",
        "icono": "file-check",
    },
    {
        "numero": "04",
        "titulo": "Fabricamos tu kit",
        "descripcion": "Iniciamos la fabricación de los paneles y la estructura de tu futura vivienda.",
        "icono": "hammer",
    },
    {
        "numero": "05",
        "titulo": "Despachamos a tu terreno",
        "descripcion": "Coordinamos el despacho de todos los materiales directamente a tu propiedad.",
        "icono": "truck",
    },
    {
        "numero": "06",
        "titulo": "Montamos tu hogar si contratas también este servicio adicional.",
        "descripcion": "Nuestro equipo realiza el montaje y en pocas semanas tienes tu casa lista para vivir.",
        "icono": "key",
    },
]


def paso_card(paso: dict) -> rx.Component:
    return rx.box(
        # Número decorativo de fondo
        rx.text(
            paso["numero"],
            class_name="absolute top-3 right-4 text-6xl font-black text-teal-100 leading-none select-none pointer-events-none",
        ),
        # Contenido
        rx.vstack(
            rx.box(
                rx.icon(paso["icono"], size=22, color="#0d9488"),
                class_name="p-3 bg-teal-50 rounded-xl w-fit",
            ),
            rx.text(
                paso["titulo"],
                class_name="text-slate-800 font-bold text-lg leading-snug",
            ),
            rx.text(
                paso["descripcion"],
                class_name="text-slate-500 text-sm leading-relaxed",
            ),
            spacing="3",
            align_items="start",
        ),
        class_name="relative p-6 bg-white rounded-2xl border border-teal-100 shadow-sm hover:shadow-md hover:-translate-y-1 transition-all duration-200 overflow-hidden",
    )


def como_comprar_section() -> rx.Component:
    return rx.box(
        rx.box(
            # Header
            rx.vstack(
                rx.text(
                    "PROCESO DE COMPRA",
                    class_name="text-teal-600 text-xs font-bold uppercase tracking-widest",
                ),
                rx.heading(
                    "¿Cómo comprar tu casa?",
                    class_name="text-3xl md:text-5xl font-bold text-slate-900 text-center leading-tight",
                    size="8",
                ),
                rx.text(
                    "En 6 simples pasos puedes tener la casa de tus sueños.",
                    class_name="text-slate-500 text-base text-center max-w-xl",
                ),
                spacing="4",
                align="center",
                class_name="mb-14",
            ),
            # Grid de pasos
            rx.box(
                *[paso_card(p) for p in PASOS],
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6",
            ),
            # CTA
            rx.box(
                rx.link(
                    rx.button(
                        rx.icon("message-circle", size=16),
                        "Iniciar el proceso por WhatsApp",
                        class_name="bg-teal-600 hover:bg-teal-500 text-white font-semibold px-8 py-3 rounded-xl transition-all duration-200 shadow-lg shadow-teal-500/20 flex items-center gap-2",
                        size="3",
                    ),
                    href="https://wa.me/56930754516",
                    is_external=True,
                ),
                class_name="flex justify-center mt-12",
            ),
            class_name="max-w-7xl mx-auto px-6 lg:px-8 py-20",
        ),
        width="100%",
        style={
            "background": "linear-gradient(180deg, #ffffff 0%, #f0fdfa 60%, #ccfbf1 100%)",
        },
    )
