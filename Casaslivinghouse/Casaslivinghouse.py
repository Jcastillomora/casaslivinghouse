import reflex as rx
from .footer import footer
from .hero_section import hero_section
from .models import Casa
from .navbar import navbar_icons
from .state import State
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


def productos_credito_section():
    return rx.box(
        rx.box(
            rx.flex(
                # Columna izquierda – Crédito Directo
                rx.box(
                    rx.box(
                        rx.image(
                            src="https://images.unsplash.com/photo-1556912173-46c336c7fd55?w=600&q=80",
                            alt="Crédito directo para tu hogar",
                            width="100%",
                            height="280px",
                            object_fit="cover",
                            border_radius="1rem 1rem 0 0",
                        ),
                        rx.box(
                            rx.heading(
                                "Crédito Directo",
                                size="7",
                                color="#fff",
                                weight="bold",
                                margin_bottom="0.5rem",
                            ),
                            rx.heading(
                                "Todas nuestras casas prefabricadas disponibles",
                                size="5",
                                color="#fff",
                                weight="regular",
                                margin_bottom="1.5rem",
                                line_height="1.4",
                            ),
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("check-circle", size=16, color="#fff"),
                                    rx.text("Crédito directo pie + cuotas mensuales", color="#fff", size="3"),
                                    spacing="2", align="center",
                                ),
                                rx.hstack(
                                    rx.icon("check-circle", size=16, color="#fff"),
                                    rx.text("Con o Sin DICOM", color="#fff", size="3"),
                                    spacing="2", align="center",
                                ),
                                rx.hstack(
                                    rx.icon("check-circle", size=16, color="#fff"),
                                    rx.text("Sujeto a evaluación", color="#fff", size="3"),
                                    spacing="2", align="center",
                                ),
                                spacing="2",
                                align_items="start",
                                margin_bottom="1.5rem",
                            ),
                            rx.link(
                                rx.button(
                                    "Consultar ahora",
                                    rx.icon("arrow-right", size=18),
                                    size="3",
                                    background="#fff",
                                    color="#dc2626",
                                    border_radius="2rem",
                                    font_weight="600",
                                    cursor="pointer",
                                    _hover={
                                        "background": "#f1f5f9",
                                        "transform": "translateY(-2px)",
                                        "box_shadow": "0 10px 25px rgba(0,0,0,0.2)",
                                    },
                                    transition="all 0.3s ease",
                                ),
                                href="https://wa.me/56930754516",
                                is_external=True,
                            ),
                            background="linear-gradient(135deg, #dc2626 0%, #b91c1c 100%)",
                            padding="2rem",
                            border_radius="0 0 1rem 1rem",
                        ),
                        background="#fff",
                        border_radius="1rem",
                        box_shadow="0 10px 40px rgba(0,0,0,0.1)",
                        overflow="hidden",
                        transition="all 0.3s ease",
                        _hover={
                            "transform": "translateY(-6px)",
                            "box_shadow": "0 20px 60px rgba(0,0,0,0.15)",
                        },
                    ),
                    flex="1",
                ),

                # Columna derecha – Productos
                rx.box(
                    rx.flex(
                        # Benhaus BASE
                        rx.box(
                            rx.image(
                                src="https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=600&q=80",
                                alt="Benhaus Base",
                                width="100%",
                                height="180px",
                                object_fit="cover",
                                border_radius="1rem 1rem 0 0",
                            ),
                            rx.box(
                                rx.flex(
                                    rx.heading("benhaus", size="5", color="#1e293b", weight="bold"),
                                    rx.badge(
                                        "BASE",
                                        background="#fbbf24",
                                        color="#78350f",
                                        font_weight="bold",
                                        padding="0.25rem 0.75rem",
                                    ),
                                    align="center",
                                    gap="0.75rem",
                                    margin_bottom="0.75rem",
                                ),
                                rx.text(
                                    "Estructura básica lista para personalizar",
                                    color="#64748b",
                                    size="2",
                                    margin_bottom="0.75rem",
                                ),
                                rx.flex(
                                    rx.text("Desde ", color="#64748b", size="2"),
                                    rx.heading("$15.990.000", size="4", color="#0369a1", weight="bold"),
                                    align="center",
                                    gap="0.5rem",
                                ),
                                padding="1.25rem",
                            ),
                            background="#fff",
                            border_radius="1rem",
                            box_shadow="0 4px 20px rgba(0,0,0,0.08)",
                            overflow="hidden",
                            transition="all 0.3s ease",
                            cursor="pointer",
                            _hover={"transform": "translateY(-4px)", "box_shadow": "0 12px 35px rgba(0,0,0,0.12)"},
                        ),

                        # Benhaus SIP
                        rx.box(
                            rx.image(
                                src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80",
                                alt="Benhaus SIP",
                                width="100%",
                                height="180px",
                                object_fit="cover",
                                border_radius="1rem 1rem 0 0",
                            ),
                            rx.box(
                                rx.flex(
                                    rx.heading("benhaus", size="5", color="#1e293b", weight="bold"),
                                    rx.badge(
                                        "SIP",
                                        background="#f97316",
                                        color="#fff",
                                        font_weight="bold",
                                        padding="0.25rem 0.75rem",
                                    ),
                                    align="center",
                                    gap="0.75rem",
                                    margin_bottom="0.75rem",
                                ),
                                rx.text(
                                    "Tecnología SIP de alta eficiencia energética",
                                    color="#64748b",
                                    size="2",
                                    margin_bottom="0.75rem",
                                ),
                                rx.flex(
                                    rx.text("Desde ", color="#64748b", size="2"),
                                    rx.heading("$24.990.000", size="4", color="#0369a1", weight="bold"),
                                    align="center",
                                    gap="0.5rem",
                                ),
                                padding="1.25rem",
                            ),
                            background="#fff",
                            border_radius="1rem",
                            box_shadow="0 4px 20px rgba(0,0,0,0.08)",
                            overflow="hidden",
                            transition="all 0.3s ease",
                            cursor="pointer",
                            _hover={"transform": "translateY(-4px)", "box_shadow": "0 12px 35px rgba(0,0,0,0.12)"},
                        ),

                        direction=rx.breakpoints(initial="column", sm="row"),
                        gap="1.25rem",
                    ),

                    # CTA tarjeta
                    rx.box(
                        rx.flex(
                            rx.vstack(
                                rx.heading(
                                    "Paga tu casa con tarjeta de crédito o débito",
                                    size="4",
                                    color="#1e293b",
                                    weight="bold",
                                ),
                                rx.text(
                                    "Paga el pie con tu tarjeta y el saldo con crédito directo sin evaluación DICOM",
                                    color="#64748b",
                                    size="2",
                                ),
                                spacing="2",
                                align_items="start",
                                flex="1",
                            ),
                            rx.link(
                                rx.button(
                                    "Crédito Directo",
                                    rx.icon("calculator", size=16),
                                    size="3",
                                    background="linear-gradient(135deg, #0369a1 0%, #0284c7 100%)",
                                    color="#fff",
                                    border_radius="2rem",
                                    font_weight="600",
                                    cursor="pointer",
                                    _hover={"opacity": "0.9", "transform": "scale(1.04)"},
                                    transition="all 0.3s ease",
                                ),
                                href="https://wa.me/56930754516",
                                is_external=True,
                            ),
                            align="center",
                            justify="between",
                            gap="1rem",
                            direction=rx.breakpoints(initial="column", sm="row"),
                        ),
                        background="linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%)",
                        padding="1.25rem",
                        border_radius="1rem",
                        border="2px solid #bae6fd",
                        margin_top="1.25rem",
                    ),

                    flex="1",
                ),

                direction=rx.breakpoints(initial="column", lg="row"),
                gap="2rem",
                align="start",
            ),
            class_name="max-w-7xl mx-auto px-6 lg:px-8 py-12",
        ),
        class_name="w-full bg-white border-b border-slate-100",
    )


def card_component(casa: Casa):
    precio_texto = f"${casa.precio:,}".replace(",", ".")

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
            # Nombre y descripción
            rx.vstack(
                rx.heading(
                    casa.modelo,
                    class_name="text-base font-bold text-slate-800",
                    size="4",
                ),
                rx.text(
                    casa.descripcion,
                    class_name="text-sm text-slate-500 leading-relaxed line-clamp-2",
                ),
                spacing="2",
                align_items="start",
                width="100%",
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
                rx.text(precio_texto, class_name="text-2xl font-bold text-teal-600"),
                spacing="1",
                align_items="start",
                width="100%",
            ),

            spacing="4",
            class_name="p-4 w-full",
            align_items="start",
            flex="1",
        ),

        # Botones
        rx.hstack(
            rx.box(
                rx.cond(
                    casa.plano,
                    rx.link(
                        rx.button(
                            rx.icon("file-text", size=14),
                            "Ver Plano",
                            class_name="text-xs font-medium text-slate-600 border border-slate-200 hover:border-teal-400 hover:text-teal-600 hover:bg-teal-50 transition-all duration-200 rounded-lg",
                            variant="ghost",
                            size="2",
                            width="100%",
                        ),
                        href=casa.plano,
                        is_external=True,
                        width="100%",
                    ),
                    rx.button(
                        rx.icon("file-x", size=14),
                        "Sin Plano",
                        class_name="text-xs text-slate-300 cursor-not-allowed rounded-lg",
                        variant="ghost",
                        size="2",
                        disabled=True,
                        width="100%",
                    ),
                ),
                flex="1",
                width="100%",
            ),
            rx.box(
                rx.link(
                    rx.button(
                        rx.icon("message-circle", size=14),
                        "Consultar",
                        class_name="text-xs font-semibold bg-teal-500 hover:bg-teal-600 text-white rounded-lg transition-all duration-200",
                        size="2",
                        width="100%",
                    ),
                    href="https://wa.me/56930754516",
                    is_external=True,
                    width="100%",
                ),
                flex="1",
                width="100%",
            ),
            spacing="3",
            align="center",
            class_name="px-4 pb-4 w-full",
            width="100%",
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
        hero_section(),
        productos_credito_section(),
        casas_page(),
        rx.box(
            whatsapp(),
            class_name="fixed bottom-6 right-6 z-50",
        ),
        footer(),
        class_name="w-full",
    )


app = rx.App(
    style={
        "font_family": "Roboto",
        "line_height": "1.6",
        rx.text: {
            "text_decoration": "none",
            "font_family": "Roboto",
            "color": "#000000",
        },
        rx.heading: {
            "font_family": "Roboto",
        },
        rx.link: {
            "text_decoration": "none",
        },
        rx.icon: {
            "text_decoration": "none",
        },
    },
    stylesheets=[
        "/style.css",
    ],
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
