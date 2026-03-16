import reflex as rx


def hero_stat(number: str, label: str, icon: str, bg: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.icon(icon, size=22, color="white"),
            class_name=f"w-12 h-12 rounded-full flex items-center justify-center flex-shrink-0 {bg}",
        ),
        rx.box(
            rx.text(number, class_name="text-2xl md:text-3xl font-black text-white leading-none"),
            rx.text(label, class_name="text-xs text-slate-400 mt-1 whitespace-nowrap"),
        ),
        class_name="flex flex-row items-center gap-3",
    )


def hero_section():
    return rx.box(
        # ── Hero principal ──────────────────────────────────────────────────
        rx.box(
            rx.box(
                rx.grid(
                    # Columna izquierda – texto
                    rx.vstack(
                        rx.box(
                            rx.hstack(
                                rx.icon("home", size=14, color="#5eead4"),
                                rx.text(
                                    "Casas Prefabricadas de Calidad",
                                    class_name="text-teal-300 text-sm font-medium",
                                ),
                                spacing="2",
                                align="center",
                            ),
                            class_name="bg-teal-500/15 border border-teal-500/30 px-3 py-1.5 rounded-full w-fit",
                        ),
                        rx.heading(
                            "Tu hogar, hecho realidad",
                            class_name="text-4xl md:text-5xl lg:text-6xl font-bold text-white leading-tight",
                        ),
                        rx.text(
                            "Somos Casas Prefabricadas Living House ¡Gracias a Dios! "
                            "Una empresa que te acompaña en cada uno de tus sueños.",
                            class_name="text-white/90 text-base md:text-lg leading-relaxed max-w-xl",
                        ),
                        rx.hstack(
                            rx.icon("heart", size=16, color="#5eead4"),
                            rx.text(
                                "Empresa de inspiración Cristiana, de confianza y cara a la ciudadanía.",
                                class_name="text-white/85 font-semibold text-sm md:text-base",
                            ),
                            spacing="2",
                            align="center",
                        ),
                        rx.hstack(
                            rx.button(
                                rx.hstack(
                                    rx.text("Ver Catálogo"),
                                    rx.icon("arrow-right", size=17),
                                    spacing="2",
                                    align="center",
                                ),
                                class_name="px-6 py-2.5 bg-teal-500 hover:bg-teal-400 text-white font-semibold rounded-xl transition-all duration-200 hover:scale-105 shadow-lg shadow-teal-500/30",
                                size="3",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("message-circle", size=17),
                                        rx.text("Contáctanos"),
                                        spacing="2",
                                        align="center",
                                    ),
                                    class_name="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white font-semibold rounded-xl transition-all duration-200 border border-white/20",
                                    size="3",
                                ),
                                href="https://wa.me/56930754516",
                                is_external=True,
                            ),
                            spacing="4",
                            wrap="wrap",
                        ),
                        spacing="6",
                        align_items="start",
                        class_name="py-10 lg:py-16",
                    ),
                    # Columna derecha – slider de imágenes
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.image(src="/volcan_osorno_137.jpg", alt="Casa Volcán Osorno 137m²"),
                                class_name="hero-slide-item",
                            ),
                            rx.box(
                                rx.image(src="/7lagos_108.jpg", alt="Casa 7 Lagos 108m²"),
                                class_name="hero-slide-item",
                            ),
                            rx.box(
                                rx.image(src="/foto_sección 1.jpg", alt="Casa Living House"),
                                class_name="hero-slide-item",
                            ),
                            rx.box(
                                rx.image(src="/puerto_octay_90.jpg", alt="Casa Puerto Octay 90m²"),
                                class_name="hero-slide-item",
                            ),
                            class_name="hero-slider-track",
                        ),
                        class_name="hero-slider-container shadow-2xl shadow-black/40",
                    ),
                    columns=rx.breakpoints(initial="1", md="2"),
                    gap="10",
                    class_name="items-center",
                ),
                class_name="max-w-7xl mx-auto px-6 lg:px-8",
            ),
            # Stats bar
            rx.box(
                rx.box(
                    rx.box(
                        hero_stat("20+", "Modelos disponibles", "building-2", "bg-purple-500/30"),
                        rx.box(class_name="w-px h-10 bg-white/20 hidden sm:block"),
                        hero_stat("5+", "Años de experiencia", "calendar", "bg-yellow-500/30"),
                        rx.box(class_name="w-px h-10 bg-white/20 hidden sm:block"),
                        hero_stat("100%", "Crédito Directo", "banknote", "bg-teal-500/30"),
                        rx.box(class_name="w-px h-10 bg-white/20 hidden sm:block"),
                        hero_stat("Sin DICOM", "Evaluación flexible", "shield-check", "bg-sky-500/30"),
                        class_name="flex flex-row items-center justify-center gap-6 md:gap-10 py-6",
                    ),
                    class_name="max-w-4xl mx-auto",
                ),
                class_name="stats-bar-animated border-t border-white/10 mt-4",
            ),
            class_name="bg-gradient-to-br from-slate-900 via-teal-950/80 to-slate-900",
        ),

        # ── Sección CTA ──────────────────────────────────────────────────────
        rx.box(
            rx.box(
                rx.vstack(
                    rx.text(
                        "No esperes más",
                        class_name="text-teal-600 font-semibold text-base md:text-lg text-center",
                    ),
                    rx.heading(
                        "Inicia el proceso con Casas Living House",
                        class_name="text-2xl md:text-4xl font-bold text-slate-800 text-center leading-snug",
                    ),
                    rx.text(
                        "Si cuentas con un diseño preliminar pero no sabes cómo continuar en el proceso de "
                        "construcción de tu nuevo hogar, nuestro equipo te guiará de manera clara y sencilla "
                        "en las etapas necesarias para concretar tu proyecto. Con Benhaus tendrás seguridad "
                        "y certeza en el desarrollo del proyecto.",
                        class_name="text-slate-600 text-center leading-relaxed max-w-3xl text-sm md:text-base",
                    ),
                    spacing="5",
                    align="center",
                    class_name="py-12 px-6",
                ),
                class_name="max-w-5xl mx-auto",
            ),
            class_name="bg-gradient-to-r from-teal-50 to-cyan-50 border-y border-teal-100",
        ),

        width="100%",
    )
