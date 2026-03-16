import reflex as rx

VIDEOS = [
    {"src": "/testimonio1.mp4"},
    {"src": "/testimonio2.mp4"},
    {"src": "/testimonio3.mp4"},
    {"src": "/testimonio4.mp4"},
]


def video_card(v: dict) -> rx.Component:
    return rx.box(
        rx.el.video(
            rx.el.source(src=v["src"], type="video/mp4"),
            controls=True,
            preload="metadata",
            class_name="w-full h-auto block max-h-[320px] sm:max-h-none object-cover",
        ),
        class_name="rounded-2xl overflow-hidden bg-slate-900 shadow-xl transition-all duration-300",
        style={
            "box_shadow": "0 8px 32px rgba(0,0,0,0.6)",
            "_hover": {
                "box_shadow": "0 12px 40px rgba(20,184,166,0.25), 0 8px 32px rgba(0,0,0,0.6)",
                "transform": "translateY(-4px)",
            },
        },
    )


def testimonios_section() -> rx.Component:
    return rx.box(
        # Glow decorativo de fondo
        rx.box(
            class_name="absolute top-0 left-0 w-96 h-96 rounded-full pointer-events-none blur-3xl opacity-10",
            style={"background": "radial-gradient(circle, #14b8a6 0%, transparent 70%)"},
        ),
        rx.box(
            class_name="absolute bottom-0 right-0 w-80 h-80 rounded-full pointer-events-none blur-3xl opacity-8",
            style={"background": "radial-gradient(circle, #0f766e 0%, transparent 70%)"},
        ),

        # Contenido
        rx.box(
            # Header
            rx.box(
                rx.text(
                    "CLIENTES REALES",
                    class_name="text-teal-400 text-xs font-bold uppercase tracking-widest mb-4",
                ),
                rx.box(
                    rx.text(
                        "Familias que ya tienen ",
                        as_="span",
                        class_name="text-white",
                    ),
                    rx.text(
                        "su casa propia",
                        as_="span",
                        style={
                            "background": "linear-gradient(90deg, #14b8a6 0%, #2dd4bf 50%, #5eead4 100%)",
                            "background_clip": "text",
                            "-webkit-background-clip": "text",
                            "-webkit-text-fill-color": "transparent",
                        },
                    ),
                    class_name="text-3xl md:text-5xl font-bold leading-tight mb-4",
                ),
                rx.text(
                    "Mira lo que nuestros clientes dicen sobre su experiencia con Living House.",
                    class_name="text-slate-400 text-base mb-8 max-w-xl",
                ),
                rx.link(
                    rx.button(
                        rx.icon("message-circle", size=16),
                        "Contáctanos por WhatsApp",
                        class_name="bg-teal-600 hover:bg-teal-500 text-white font-semibold px-6 py-3 rounded-xl transition-all duration-200 shadow-lg shadow-teal-900/50 flex items-center gap-2 text-sm",
                        size="3",
                    ),
                    href="https://wa.me/56930754516",
                    is_external=True,
                ),
                class_name="mb-14",
            ),

            # Grid de videos
            rx.box(
                *[video_card(v) for v in VIDEOS],
                class_name="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-5",
            ),

            # Botón ver más
            rx.box(
                rx.link(
                    rx.button(
                        rx.image(
                            src="/tik tok.png",
                            width="20px",
                            height="20px",
                            alt="TikTok",
                        ),
                        rx.text("Ver más videos en TikTok"),
                        class_name="flex items-center gap-3 bg-white/10 hover:bg-white/20 border border-white/25 text-white font-semibold px-8 py-3 rounded-xl transition-all duration-200 text-sm",
                        size="3",
                    ),
                    href="https://www.tiktok.com/@casaslivinghouse?lang=es",
                    is_external=True,
                ),
                class_name="flex justify-center mt-10",
            ),

            class_name="relative z-10 max-w-7xl mx-auto px-6 lg:px-8 py-20",
        ),

        class_name="relative w-full overflow-hidden",
        style={"background": "linear-gradient(135deg, #0f766e 0%, #134e4a 45%, #115e59 100%)"},
    )
