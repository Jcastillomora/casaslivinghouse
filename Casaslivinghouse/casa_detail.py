import reflex as rx
from .footer import footer
from .navbar import navbar_icons
from .state import State
from .whatsapp import whatsapp

# ──────────────────────────────────────────────
# Contenido estático del Kit Inicial
# ──────────────────────────────────────────────

KIT_INCLUYE = [
    (
        "TECHUMBRE",
        [
            "Zinc 0,35 mm en diferentes medidas según modelo, caballetes de 40 cm de anchura y costaneras en 2x2 a 80 cm entre unas y otras.",
            "Fieltro asfáltico 10/40 en rollos como aislante de humedad (los lima hoyas se incluyen en los modelos que lo requieran).",
        ],
    ),
    (
        "CERCHAS",
        [
            'Cerchas en tabla de 1x5" con un espaciamiento de 1,0 mt entre una y otra.',
        ],
    ),
    (
        "PANELES INTERIORES",
        [
            "Paneles interiores en madera de 2x3, con pie derecho a 60 cm a eje y triple cadeneta altura de 2,42 mt.",
        ],
    ),
    (
        "PANELEX EXTERIORES",
        [
            "Paneles exteriores en madera de 2x3, con pie derecho a 60 cm a eje y triple cadeneta, fieltro asfáltico 10/40 como aislante de humedad y tinglado seco en cámara de 1x5 o 1x6.",
        ],
    ),
    (
        "EXTRAS",
        [
            "Tablas cepilladas de 1x4 en 2,5 mt para la unión entre paneles y sus encuentros.",
            "Perfil corta gotera galvanizado para inicio de panel.",
        ],
    ),
]

KIT_NO_INCLUYE = [
    "No incluye piso, puertas ni ventanas.",
    "No incluye forro por ninguna de sus caras en los paneles interiores.",
    "No incluye ningún tipo de aislante térmico.",
    "No incluye ningún tipo de tornillo o clavo.",
    "No incluye aleros ni tapacanes.",
]

KIT_ADICIONAL = [
    'Kit de ventanas (línea 15, incluye premarcos cepillados en tabla de 1x4")',
    "Kit de puertas (interior en terciado de 70 cm, exterior en pino o pino Oregón 80cm; incluye todos los marcos, no incluye chapas ni bisagras)",
    "Kit de piso (apoyos cemento 40 cm cada 1,5 mt, vigas centrales 2x6, cadenas en 2x4, terciado estructural 18mm, fieltro, fijaciones)",
    "Kit de cierre de aleros (tapacanes 1x8 y 1x4, listones 1x3 bruto, cortes de tinglado + 38 cm., fijaciones)",
]


# ──────────────────────────────────────────────
# Sub-componentes
# ──────────────────────────────────────────────


def back_bar() -> rx.Component:
    return rx.box(
        rx.box(
            rx.link(
                rx.hstack(
                    rx.icon("arrow-left", size=16, color="#475569"),
                    rx.text(
                        "Volver al catálogo",
                        class_name="text-sm text-slate-600 hover:text-teal-600 transition-colors font-medium",
                    ),
                    spacing="2",
                    align="center",
                ),
                href="/#modelos",
            ),
            rx.hstack(
                rx.icon("home", size=13, color="#94a3b8"),
                rx.text("/", class_name="text-xs text-slate-400"),
                rx.text(
                    State.current_casa.modelo,
                    class_name="text-xs text-slate-500 truncate max-w-xs",
                ),
                spacing="1",
                align="center",
            ),
            class_name="max-w-7xl mx-auto px-6 lg:px-8 flex items-center justify-between",
        ),
        class_name="w-full bg-white border-b border-slate-100 py-3",
    )


def hero_section_detail() -> rx.Component:
    return rx.box(
        # Imagen principal
        rx.box(
            rx.image(
                src=rx.cond(
                    State.current_casa.imagen != "",
                    State.current_casa.imagen,
                    State.current_casa.url_imagen,
                ),
                alt=State.current_casa.modelo,
                width="100%",
                height="100%",
                object_fit="cover",
                class_name="w-full h-full",
            ),
            rx.box(
                class_name="absolute inset-0 bg-gradient-to-t from-black/70 via-black/10 to-transparent",
            ),
            rx.box(
                rx.badge(
                    "DISPONIBLE",
                    class_name="bg-emerald-500 text-white text-xs font-bold px-3 py-1 rounded-full shadow-md",
                ),
                class_name="absolute top-4 left-4",
            ),
            class_name="relative w-full md:w-3/5 h-72 md:min-h-96 rounded-2xl overflow-hidden shadow-xl flex-shrink-0",
        ),

        # Panel de información
        rx.box(
            rx.box(
                rx.text(
                    State.current_casa.modelo,
                    class_name="text-3xl md:text-4xl font-bold text-slate-900 leading-tight",
                ),
                rx.hstack(
                    rx.icon("hash", size=14, color="#14b8a6"),
                    rx.text(
                        "Modelo ",
                        State.current_casa.id,
                        class_name="text-sm text-teal-700 font-semibold",
                    ),
                    spacing="1",
                    align="center",
                    class_name="mt-1",
                ),
                class_name="mb-5",
            ),
            rx.box(
                rx.text(
                    "Precio",
                    class_name="text-xs text-slate-400 uppercase tracking-widest font-medium",
                ),
                rx.text(
                    State.current_casa_precio_texto,
                    class_name="text-4xl font-bold text-teal-600",
                ),
                class_name="mb-5",
            ),
            rx.hstack(
                rx.hstack(
                    rx.icon("ruler", size=15, color="#14b8a6"),
                    rx.text(State.current_casa.superficie_m2, class_name="text-sm font-semibold text-slate-700"),
                    rx.text("m²", class_name="text-sm font-semibold text-slate-700"),
                    spacing="1", align="center",
                ),
                rx.box(class_name="w-px h-4 bg-slate-200"),
                rx.hstack(
                    rx.icon("bed", size=15, color="#14b8a6"),
                    rx.text(State.current_casa.dormitorios, class_name="text-sm font-semibold text-slate-700"),
                    rx.text("dorm.", class_name="text-sm font-semibold text-slate-700"),
                    spacing="1", align="center",
                ),
                rx.box(class_name="w-px h-4 bg-slate-200"),
                rx.hstack(
                    rx.icon("bath", size=15, color="#14b8a6"),
                    rx.text(State.current_casa.banos, class_name="text-sm font-semibold text-slate-700"),
                    rx.text("baños", class_name="text-sm font-semibold text-slate-700"),
                    spacing="1", align="center",
                ),
                class_name="bg-slate-50 rounded-xl px-4 py-3 border border-slate-100 mb-5 flex-wrap gap-y-2",
                spacing="3",
                align="center",
            ),
            rx.text(
                State.current_casa.descripcion,
                class_name="text-slate-600 leading-relaxed text-sm md:text-base mb-6",
            ),
            rx.flex(
                rx.link(
                    rx.button(
                        rx.icon("message-circle", size=16),
                        "Consultar por WhatsApp",
                        class_name="flex items-center gap-2 bg-teal-500 hover:bg-teal-600 text-white font-semibold text-sm rounded-xl px-6 py-3 transition-all duration-200 shadow-md",
                        size="3",
                    ),
                    href="https://wa.me/56930754516",
                    is_external=True,
                ),
                rx.cond(
                    State.current_casa.plano != "",
                    rx.link(
                        rx.button(
                            rx.icon("file-text", size=16),
                            "Ver Plano PDF",
                            class_name="flex items-center gap-2 bg-white border border-slate-300 hover:border-teal-500 hover:bg-teal-50 text-slate-700 hover:text-teal-700 font-semibold text-sm rounded-xl px-6 py-3 transition-all duration-200",
                            variant="ghost",
                            size="3",
                        ),
                        href=State.current_casa.plano,
                        is_external=True,
                    ),
                    rx.box(),
                ),
                class_name="flex flex-row items-center gap-4 flex-wrap mt-2",
            ),
            class_name="flex-1 pt-6 md:pt-0 md:pl-8",
        ),

        class_name="max-w-7xl mx-auto px-6 lg:px-8 flex flex-col md:flex-row items-start gap-0 py-10",
    )


def _bullet_item(text: str, color: str = "#14b8a6") -> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f"w-1.5 h-1.5 rounded-full mt-1.5 flex-shrink-0",
            background=color,
        ),
        rx.text(text, class_name="text-xs text-slate-600 leading-relaxed"),
        spacing="2",
        align="start",
        width="100%",
    )


def _x_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("x-circle", size=14, color="#ef4444"),
        rx.text(text, class_name="text-xs text-slate-600 leading-relaxed"),
        spacing="2",
        align="start",
        width="100%",
    )


def kit_incluye_column() -> rx.Component:
    section_items = []
    for title, bullets in KIT_INCLUYE:
        bullet_items = [_bullet_item(b) for b in bullets]
        section_items.append(
            rx.box(
                rx.text(
                    title,
                    class_name="text-xs font-bold text-slate-700 uppercase tracking-wide mb-2",
                ),
                rx.vstack(*bullet_items, spacing="1", align_items="start", width="100%"),
                class_name="mb-4",
                width="100%",
            )
        )

    return rx.box(
        rx.hstack(
            rx.icon("check-circle-2", size=16, color="#14b8a6"),
            rx.text(
                "¿Qué incluye un kit inicial?",
                class_name="text-sm font-bold text-slate-700",
            ),
            spacing="2",
            align="center",
            class_name="pb-3 border-b border-slate-200 w-full mb-4",
        ),
        *section_items,
        class_name="p-6 w-full",
    )


def kit_no_incluye_column() -> rx.Component:
    x_items = [_x_item(item) for item in KIT_NO_INCLUYE]
    return rx.box(
        rx.hstack(
            rx.icon("x-octagon", size=16, color="#ef4444"),
            rx.text(
                "¿Qué NO incluye?",
                class_name="text-sm font-bold text-red-600",
            ),
            spacing="2",
            align="center",
            class_name="pb-3 border-b border-slate-200 w-full mb-4",
        ),
        rx.vstack(*x_items, spacing="3", align_items="start", width="100%"),
        class_name="p-6 w-full",
    )


def kit_adicional_section() -> rx.Component:
    add_items = [_bullet_item(item, "#6b7280") for item in KIT_ADICIONAL]
    return rx.box(
        rx.hstack(
            rx.icon("plus-circle", size=16, color="#8b5cf6"),
            rx.text(
                "¿Qué puedes agregar como ADICIONAL a tu Kit Inicial?",
                class_name="text-sm font-bold text-slate-700",
            ),
            spacing="2",
            align="center",
            class_name="pb-3 border-b border-slate-200 w-full mb-4",
        ),
        rx.vstack(*add_items, spacing="3", align_items="start", width="100%"),
        class_name="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 mb-4",
    )


def kit_inicial_section() -> rx.Component:
    return rx.box(
        # Tarjeta principal: título + dos columnas
        rx.box(
            rx.box(
                rx.hstack(
                    rx.icon("package", size=20, color="#0f172a"),
                    rx.heading(
                        "¿Qué es un Kit Inicial?",
                        class_name="text-lg font-bold text-slate-900",
                        size="5",
                    ),
                    spacing="3",
                    align="center",
                    justify="center",
                ),
                class_name="bg-slate-100 border-b border-slate-200 px-6 py-4 text-center",
            ),
            rx.box(
                rx.box(
                    kit_incluye_column(),
                    class_name="flex-1 border-b md:border-b-0 md:border-r border-slate-100",
                ),
                rx.box(
                    kit_no_incluye_column(),
                    class_name="flex-1",
                ),
                class_name="flex flex-col md:flex-row",
            ),
            class_name="rounded-2xl overflow-hidden shadow-sm border border-slate-200 mb-6",
        ),

        # Adicionales
        kit_adicional_section(),

        # Servicios adicionales
        rx.box(
            rx.hstack(
                rx.icon("wrench", size=16, color="#0369a1"),
                rx.text(
                    "SERVICIOS ADICIONALES: INSTALACIÓN DE KIT Y CONSTRUCCIÓN DE RADIER O BASE EN APOYOS DE CEMENTO.",
                    class_name="text-xs font-bold text-slate-700 uppercase tracking-wide leading-relaxed",
                ),
                spacing="3",
                align="start",
            ),
            class_name="bg-blue-50 border border-blue-200 rounded-2xl px-5 py-4",
        ),

        class_name="w-full",
    )


def cta_contacto() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "¿Te interesa este modelo?",
                        class_name="text-2xl font-bold text-white",
                        size="6",
                    ),
                    rx.text(
                        "Cotiza ahora con financiamiento directo, con o sin DICOM.",
                        class_name="text-teal-100 text-sm",
                    ),
                    spacing="2",
                    align_items="start",
                ),
                rx.flex(
                    rx.link(
                        rx.button(
                            rx.icon("message-circle", size=18),
                            "Consultar por WhatsApp",
                            class_name="bg-white text-teal-700 hover:bg-teal-50 font-bold px-6 py-3 rounded-xl shadow-lg transition-all duration-200 text-sm flex items-center gap-2",
                            size="3",
                        ),
                        href="https://wa.me/56930754516",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(
                            rx.icon("phone", size=18),
                            "+56 9 3075 4516",
                            class_name="border-2 border-white/50 text-white hover:bg-white/10 font-semibold px-5 py-3 rounded-xl transition-all duration-200 text-sm flex items-center gap-2",
                            variant="ghost",
                            size="3",
                        ),
                        href="tel:+56930754516",
                    ),
                    class_name="flex-wrap gap-3 mt-4 md:mt-0",
                ),
                class_name="flex flex-col md:flex-row items-start md:items-center justify-between gap-4",
            ),
            class_name="max-w-7xl mx-auto px-6 lg:px-8 py-12",
        ),
        class_name="w-full bg-gradient-to-r from-teal-600 to-teal-500",
    )


def loading_detail() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.spinner(size="3", color="teal"),
            rx.text("Cargando modelo...", class_name="text-slate-500 text-sm"),
            align="center",
            spacing="3",
        ),
        class_name="py-32 w-full min-h-96",
    )


def not_found_detail() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.icon("search-x", size=48, color="#94a3b8"),
            rx.heading(
                "Modelo no encontrado",
                class_name="text-slate-600 font-semibold",
                size="5",
            ),
            rx.text(
                "El modelo que buscas no existe en el catálogo.",
                class_name="text-slate-400 text-sm",
            ),
            rx.link(
                rx.button(
                    rx.icon("arrow-left", size=15),
                    "Volver al catálogo",
                    class_name="mt-2 px-4 py-2 bg-teal-500 text-white rounded-xl text-sm font-medium flex items-center gap-2",
                    size="2",
                ),
                href="/#modelos",
            ),
            align="center",
            spacing="4",
        ),
        class_name="py-32 px-8 w-full min-h-96",
    )


# ──────────────────────────────────────────────
# Página principal de detalle
# ──────────────────────────────────────────────


def casa_detail_page() -> rx.Component:
    return rx.box(
        navbar_icons(),
        rx.box(back_bar(), id="detalle"),

        rx.cond(
            State.is_loading,
            loading_detail(),
            rx.cond(
                State.current_casa.id == 0,
                rx.cond(
                    State.data_loaded,
                    not_found_detail(),
                    loading_detail(),
                ),
                rx.box(
                    # Hero
                    rx.box(
                        hero_section_detail(),
                        class_name="w-full bg-white border-b border-slate-100",
                    ),

                    # Kit Inicial
                    rx.box(
                        rx.box(
                            rx.hstack(
                                rx.box(class_name="w-1 h-8 bg-teal-500 rounded-full"),
                                rx.heading(
                                    "Información del Kit Inicial",
                                    class_name="text-2xl font-bold text-slate-800",
                                    size="6",
                                ),
                                spacing="3",
                                align="center",
                                class_name="mb-8",
                            ),
                            kit_inicial_section(),
                            class_name="max-w-7xl mx-auto px-6 lg:px-8 py-12",
                        ),
                        class_name="w-full bg-slate-50",
                    ),

                    # CTA
                    cta_contacto(),

                    class_name="w-full",
                ),
            ),
        ),

        rx.box(
            whatsapp(),
            class_name="fixed bottom-6 right-6 z-50",
        ),
        footer(),
        class_name="w-full",
    )
