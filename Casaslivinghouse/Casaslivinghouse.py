import reflex as rx
from .casa_detail import casa_detail_page
from .footer import footer
from .hero_section import hero_section
from .models import Casa
from .navbar import navbar_icons
from .quienes_somos import quienes_somos
from .state import State
from .testimonios import testimonios_section
from .como_comprar import como_comprar_section
from .whatsapp import whatsapp


def empty_state() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.icon("search-x", size=48, color="#94a3b8"),
            class_name="p-5 bg-slate-100 rounded-full",
        ),
        rx.heading("Sin resultados", size="5", class_name="text-slate-600 font-semibold"),
        rx.text(
            "Intenta ajustar los filtros de búsqueda",
            class_name="text-slate-400 text-sm",
        ),
        rx.button(
            rx.icon("refresh-cw", size=15),
            "Limpiar filtros",
            on_click=State.reset_filters,
            class_name="mt-2 px-4 py-2 border border-teal-500 text-teal-600 hover:bg-teal-50 rounded-xl text-sm font-medium transition-colors",
            variant="ghost",
            size="2",
        ),
        align="center",
        spacing="4",
        padding="5rem 2rem",
        width="100%",
    )


def loading_skeleton() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.spinner(size="3", color="teal"),
            rx.text("Cargando catálogo...", class_name="text-slate-500 text-sm"),
            align="center",
            spacing="3",
        ),
        padding="6rem",
        width="100%",
    )


def credito_feature(icono: str, titulo: str, descripcion: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(icono, size=22, color="#0d9488"),
                class_name="p-3 bg-teal-50 rounded-xl w-fit",
            ),
            rx.text(
                titulo,
                class_name="text-slate-800 font-bold text-base",
            ),
            rx.text(
                descripcion,
                class_name="text-slate-500 text-sm leading-relaxed",
            ),
            spacing="2",
            align_items="start",
        ),
        class_name="p-5 bg-white rounded-2xl border border-teal-100 shadow-sm hover:shadow-md hover:-translate-y-1 transition-all duration-200",
    )


def productos_credito_section():
    return rx.box(
        rx.box(
            # Header
            rx.vstack(
                rx.text(
                    "FINANCIAMIENTO",
                    class_name="text-teal-600 text-xs font-bold uppercase tracking-widest",
                ),
                rx.heading(
                    "Tu casa con crédito directo",
                    class_name="text-3xl md:text-4xl font-bold text-slate-900 text-center leading-tight",
                    size="8",
                ),
                rx.text(
                    "Sin banco, sin trámites complicados. Evaluamos tu caso de forma personalizada.",
                    class_name="text-slate-500 text-base text-center max-w-xl",
                ),
                spacing="3",
                align="center",
                class_name="mb-12",
            ),
            # Layout principal
            rx.flex(
                # Columna izquierda — card Crédito Directo
                rx.box(
                    rx.box(
                        rx.icon("banknote", size=44, color="white"),
                        class_name="p-4 bg-white/15 rounded-2xl w-fit mb-6",
                    ),
                    rx.heading(
                        "Crédito Directo",
                        class_name="text-white text-3xl font-black mb-2",
                    ),
                    rx.text(
                        "Financia tu casa directamente con nosotros, sin intermediarios bancarios.",
                        class_name="text-white/80 text-sm leading-relaxed mb-6",
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.icon("check-circle", size=16, color="white"),
                            rx.text("Pie + cuotas mensuales", class_name="text-white text-sm"),
                            spacing="2", align="center",
                        ),
                        rx.hstack(
                            rx.icon("check-circle", size=16, color="white"),
                            rx.text("Con o Sin DICOM", class_name="text-white text-sm"),
                            spacing="2", align="center",
                        ),
                        rx.hstack(
                            rx.icon("check-circle", size=16, color="white"),
                            rx.text("Evaluación personalizada", class_name="text-white text-sm"),
                            spacing="2", align="center",
                        ),
                        rx.hstack(
                            rx.icon("check-circle", size=16, color="white"),
                            rx.text("Compatible con subsidios habitacionales", class_name="text-white text-sm"),
                            spacing="2", align="center",
                        ),
                        spacing="3",
                        align_items="start",
                        class_name="mb-8",
                    ),
                    rx.link(
                        rx.button(
                            rx.icon("message-circle", size=16),
                            "Consultar ahora",
                            class_name="bg-white text-teal-700 hover:bg-teal-50 font-bold px-6 py-3 rounded-xl transition-all duration-200 shadow-md flex items-center gap-2",
                            size="3",
                        ),
                        href="https://wa.me/56930754516",
                        is_external=True,
                    ),
                    class_name="p-8 rounded-2xl flex flex-col",
                    style={
                        "background": "linear-gradient(135deg, #0f766e 0%, #0d9488 50%, #14b8a6 100%)",
                        "min_height": "100%",
                    },
                ),
                # Columna derecha — 4 feature cards
                rx.box(
                    credito_feature(
                        "shield-check",
                        "Sin DICOM",
                        "Evaluamos cada caso de forma flexible y personalizada, sin importar tu historial crediticio.",
                    ),
                    credito_feature(
                        "calculator",
                        "Pie + Cuotas Accesibles",
                        "Define el monto del pie y distribuye el saldo en cuotas mensuales adaptadas a tu presupuesto.",
                    ),
                    credito_feature(
                        "credit-card",
                        "Paga con Tarjeta",
                        "Acepta tarjetas de crédito y débito para el pago del pie inicial de tu vivienda.",
                    ),
                    credito_feature(
                        "map-pin",
                        "Proyectos Turísticos",
                        "Financia cabañas y construcciones para proyectos turísticos en el sur de Chile.",
                    ),
                    class_name="grid grid-cols-1 sm:grid-cols-2 gap-4",
                ),
                direction=rx.breakpoints(initial="column", lg="row"),
                gap="6",
                align="stretch",
            ),
            class_name="max-w-7xl mx-auto px-6 lg:px-8 py-16",
        ),
        class_name="w-full",
        style={"background": "linear-gradient(180deg, #f8fafc 0%, #f0fdfa 100%)"},
    )


def card_component(casa: Casa):
    return rx.box(
        # Imagen
        rx.box(
            rx.image(
                src=rx.cond(casa.imagen != "", casa.imagen, casa.url_imagen),
                alt=casa.modelo,
                width="100%",
                height="210px",
                object_fit="cover",
            ),
            rx.box(
                rx.badge(
                    "DISPONIBLE",
                    class_name="bg-emerald-500 text-white text-xs font-bold px-2.5 py-1 rounded-full shadow-sm",
                ),
                class_name="absolute top-3 left-3",
            ),
            rx.box(
                rx.badge(
                    f"#{casa.id}",
                    class_name="bg-black/50 text-white text-xs px-2 py-0.5 rounded-full backdrop-blur-sm",
                ),
                class_name="absolute top-3 right-3",
            ),
            class_name="relative overflow-hidden",
        ),

        # Contenido
        rx.vstack(
            # Nombre
            rx.heading(
                casa.modelo,
                class_name="text-base font-bold text-slate-800",
                size="4",
            ),

            # Specs
            rx.hstack(
                rx.hstack(
                    rx.icon("ruler", size=13, color="#14b8a6"),
                    rx.text(f"{casa.superficie_m2}m²", class_name="text-xs font-semibold text-slate-600"),
                    spacing="1",
                    align="center",
                ),
                rx.hstack(
                    rx.icon("bed", size=13, color="#14b8a6"),
                    rx.text(f"{casa.dormitorios} dorm", class_name="text-xs font-semibold text-slate-600"),
                    spacing="1",
                    align="center",
                ),
                rx.hstack(
                    rx.icon("bath", size=13, color="#14b8a6"),
                    rx.text(f"{casa.banos} baños", class_name="text-xs font-semibold text-slate-600"),
                    spacing="1",
                    align="center",
                ),
                spacing="4",
                class_name="bg-slate-50 rounded-xl px-3 py-2.5 w-full border border-slate-100",
                justify="center",
                width="100%",
            ),

            # Precio
            rx.vstack(
                rx.text("Precio", class_name="text-xs text-slate-400 uppercase tracking-widest"),
                rx.text(casa.precio_texto, class_name="text-2xl font-bold text-teal-600"),
                spacing="1",
                align_items="start",
                width="100%",
            ),

            spacing="4",
            class_name="p-4 w-full",
            align_items="start",
            flex="1",
        ),

        # Botón
        rx.box(
            rx.button(
                rx.icon("eye", size=14),
                "Ver Detalles",
                on_click=State.navigate_to_casa(casa.id),
                class_name="text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-white rounded-lg transition-all duration-200 w-full",
                size="2",
                width="100%",
            ),
            class_name="px-4 pb-4 w-full",
        ),

        class_name="bg-white rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 overflow-hidden border border-slate-100 hover:-translate-y-1 flex flex-col",
        width="100%",
    )


def casas_page():
    return rx.box(
        # Encabezado de sección
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.box(class_name="w-1 h-8 bg-teal-500 rounded-full"),
                    rx.heading(
                        "Catálogo de Casas Prefabricadas",
                        class_name="text-2xl md:text-3xl font-bold text-slate-800",
                    ),
                    spacing="3",
                    align="center",
                ),
                rx.text(
                    f"Descubre nuestros {State.total_casas} modelos disponibles con financiamiento directo",
                    class_name="text-slate-500 text-sm md:text-base",
                ),
                spacing="3",
                align_items="start",
                class_name="mb-8",
            ),
            class_name="max-w-7xl mx-auto px-6 lg:px-8 pt-12",
        ),

        # Barra de filtros
        rx.box(
            rx.box(
                rx.hstack(
                    rx.hstack(
                        rx.icon("search", size=17, color="#94a3b8"),
                        rx.input(
                            placeholder="Buscar por modelo o descripción...",
                            value=State.search_term_casas,
                            on_change=State.set_search_term_casas,
                            size="3",
                            class_name="border-none outline-none bg-transparent text-slate-700 placeholder-slate-400 flex-1 min-w-0",
                            variant="soft",
                        ),
                        class_name="flex-1 min-w-0",
                        spacing="3",
                        align="center",
                    ),
                    rx.divider(orientation="vertical", class_name="h-6 bg-slate-200"),
                    rx.text(
                        f"{State.filtered_casas_count} resultados",
                        class_name="text-sm text-slate-400 whitespace-nowrap font-medium",
                    ),
                    rx.button(
                        rx.icon("x", size=14),
                        "Limpiar",
                        on_click=State.reset_filters,
                        class_name="text-sm text-slate-500 hover:text-red-500 transition-colors rounded-lg px-3 py-1.5",
                        variant="ghost",
                        size="2",
                    ),
                    align="center",
                    spacing="4",
                    width="100%",
                ),
                class_name="bg-white rounded-2xl shadow-sm border border-slate-200 px-5 py-3 w-full max-w-2xl mx-auto",
            ),
            class_name="max-w-7xl mx-auto px-6 lg:px-8 mb-8",
        ),

        # Grid de casas
        rx.cond(
            State.is_loading,
            loading_skeleton(),
            rx.cond(
                State.data_loaded,
                rx.cond(
                    State.filtered_casas_count == 0,
                    empty_state(),
                    rx.box(
                        rx.box(
                            rx.foreach(
                                State.filtered_casas,
                                lambda casa: card_component(casa),
                            ),
                            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 pb-12 px-6 lg:px-8 max-w-7xl mx-auto",
                        ),
                        width="100%",
                    ),
                ),
                loading_skeleton(),
            ),
        ),

        class_name="w-full bg-slate-50 min-h-screen",
    )


def index() -> rx.Component:
    return rx.box(
        navbar_icons(),
        rx.box(hero_section(), id="inicio"),
        rx.box(quienes_somos(), id="nosotros"),
        testimonios_section(),
        productos_credito_section(),
        como_comprar_section(),
        rx.box(casas_page(), id="modelos"),
        rx.box(
            whatsapp(),
            class_name="fixed bottom-6 right-6 z-50",
        ),
        rx.box(footer(), id="contacto"),
        class_name="w-full",
    )


app = rx.App(
    style={
        "font_family": "Montserrat",
        "line_height": "1.6",
        rx.text: {
            "text_decoration": "none",
            "font_family": "Montserrat",
        },
        rx.heading: {
            "font_family": "Montserrat",
        },
        rx.link: {
            "text_decoration": "none",
        },
        rx.icon: {
            "text_decoration": "none",
        },
    },
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap",
        "/style.css",
    ],
)

app.add_page(
    casa_detail_page,
    route="/casa/[casa_id]",
    on_load=State.load_casa_detail,
    title="Detalle Modelo | Casas Living House",
    description="Ficha técnica del modelo de casa prefabricada Living House.",
)

app.add_page(
    index,
    on_load=State.load_casas,
    title="Casas Prefabricadas Living House | Chile",
    description="Empresa chilena especializada en casas prefabricadas de calidad. Catálogo de modelos con financiamiento directo sin evaluación DICOM.",
    meta=[
        {
            "name": "keywords",
            "content": "casas prefabricadas Chile, viviendas prefabricadas, Living House, Benhaus, casas modulares",
        },
        {
            "property": "og:title",
            "content": "Casas Prefabricadas Living House",
        },
        {
            "property": "og:description",
            "content": "Catálogo de casas prefabricadas con financiamiento directo sin evaluación DICOM.",
        },
        {"property": "og:type", "content": "website"},
    ],
)
