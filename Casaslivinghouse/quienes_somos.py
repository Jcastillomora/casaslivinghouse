import reflex as rx


TEAM = [
    {
        "nombre": "Alexander Sáez Jorquera",
        "cargo": ["CEO", "Abogado"],
        "imagen": "/Alexander Saez.jpeg",
        "linkedin": "https://www.linkedin.com/in/alexander-s%C3%A1ez-jorquera-865b34149/",
        "whatsapp": "https://wa.me/56930754516",
    },
    {
        "nombre": "Juan Carlos García",
        "cargo": ["Agente Inmobiliario", "Post Venta y Cobranza"],
        "imagen": "/Juan Carlos Garcia.jpeg",
        "linkedin": "https://www.linkedin.com",
        "whatsapp": "https://wa.me/56962822333",
    },
]


def team_card(member: dict) -> rx.Component:
    return rx.vstack(
        # Foto circular con efectos
        rx.box(
            rx.image(
                src=member["imagen"],
                alt=member["nombre"],
                width="100%",
                height="100%",
                object_fit="cover",
                class_name="w-full h-full",
                style={
                    "object_position": "center 8%",
                    "filter": "brightness(0.95) contrast(1.08) saturate(1.15)",
                },
            ),
            # Overlay teal sutil
            rx.box(
                class_name="absolute inset-0 rounded-full pointer-events-none",
                style={
                    "background": "linear-gradient(135deg, rgba(20,184,166,0.12) 0%, rgba(13,148,136,0.08) 100%)",
                    "mix_blend_mode": "overlay",
                },
            ),
            rx.box(
                class_name="absolute inset-0 rounded-full pointer-events-none",
                style={
                    "background": "linear-gradient(180deg, rgba(255,255,255,0.08) 0%, transparent 50%)",
                },
            ),
            class_name="relative w-52 h-52 md:w-64 md:h-64 rounded-full overflow-hidden",
            style={
                "box_shadow": "0 0 0 4px rgba(20,184,166,0.4), 0 16px 48px rgba(20,184,166,0.15)",
            },
        ),

        # Nombre y cargo
        rx.vstack(
            rx.text(
                member["nombre"],
                class_name="text-slate-900 text-xl font-bold text-center",
            ),
            *(
                [rx.text(c, class_name="text-teal-600 text-sm font-semibold text-center tracking-wide")
                 for c in member["cargo"]]
                if isinstance(member["cargo"], list)
                else [rx.text(member["cargo"], class_name="text-teal-600 text-sm font-semibold text-center tracking-wide")]
            ),
            spacing="1",
            align="center",
        ),

        # Iconos sociales
        rx.hstack(
            rx.link(
                rx.box(
                    rx.icon("linkedin", size=18, color="#0d9488"),
                    class_name="p-2 rounded-lg border border-teal-200 hover:border-teal-500 hover:bg-teal-50 transition-all duration-200 cursor-pointer",
                ),
                href=member["linkedin"],
                is_external=True,
            ),
            rx.link(
                rx.box(
                    rx.icon("message-circle", size=18, color="#0d9488"),
                    class_name="p-2 rounded-lg border border-teal-200 hover:border-teal-500 hover:bg-teal-50 transition-all duration-200 cursor-pointer",
                ),
                href=member["whatsapp"],
                is_external=True,
            ),
            spacing="3",
            align="center",
        ),

        spacing="5",
        align="center",
    )


def quienes_somos() -> rx.Component:
    return rx.box(
        rx.box(
            # Encabezado
            rx.vstack(
                rx.text(
                    "QUIÉNES SOMOS",
                    class_name="text-teal-600 text-xs font-bold uppercase tracking-widest",
                ),
                rx.heading(
                    "Conoce nuestro equipo",
                    class_name="text-4xl md:text-5xl font-bold text-slate-900 text-center leading-tight",
                    size="8",
                ),
                rx.box(
                    rx.text(
                        "Somos una empresa del centro sur de Chile dedicada al desarrollo inmobiliario y al apoyo de las familias para conseguir el sueño de la casa propia, de la segunda vivienda o para la creación de proyectos turísticos donde la construcción de viviendas de calidad es nuestra mayor preocupación.",
                        class_name="text-slate-600 text-center leading-relaxed",
                    ),
                    rx.hstack(
                        rx.icon("heart", size=15, color="#0d9488"),
                        rx.text(
                            "Somos confianza y una empresa de inspiración cristiana de cara a la ciudadanía.",
                            class_name="text-teal-700 text-center font-semibold text-sm",
                        ),
                        spacing="2",
                        align="center",
                        justify="center",
                        class_name="mt-3",
                    ),
                    class_name="max-w-2xl",
                ),
                spacing="4",
                align="center",
                class_name="mb-16",
            ),

            # Tarjetas del equipo
            rx.flex(
                *[team_card(m) for m in TEAM],
                class_name="flex-col sm:flex-row items-center justify-center gap-16 md:gap-24",
            ),

            class_name="max-w-7xl mx-auto px-6 lg:px-8 py-20",
        ),
        class_name="w-full",
        style={
            "background": "linear-gradient(180deg, #ffffff 0%, #f0fdfa 50%, #ccfbf1 100%)",
        },
    )
