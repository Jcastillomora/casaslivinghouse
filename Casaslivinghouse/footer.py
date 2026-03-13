import reflex as rx


def loading_card() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                "Somos Casas Living House",
                font_weight="bold",
                class_name="sm:text-xs md:text-base lg:text-lg text-white",
            ),
            rx.box(
                rx.text("Gracias a Dios", class_name="word"),
                rx.text("", class_name="word"),
                class_name="words",
            ),
            class_name="loader",
        ),
        class_name="card_loader w-full text-center",
    )


def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="3"),
        href=href,
        class_name="text-slate-400 hover:text-teal-400 transition-colors duration-200",
    )


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Casa Matriz – Temuco",
            size="4",
            weight="bold",
            as_="h3",
            class_name="text-slate-500 mb-2",
        ),
        rx.box(
            rx.html(
                """<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d925.2100535091267!2d-72.59130711404337!3d-38.740231196906635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9614d3ddfd0f408d%3A0x77568596c6b5195d!2sArturo%20Prat%20696%2C%20Of%20316%2C%204792393%20Temuco%2C%20Araucan%C3%ADa!5e0!3m2!1ses-419!2scl!4v1772550902416!5m2!1ses-419!2scl' width="200" height="200" style="border:0;border-radius:0.75rem;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""",
            ),
            class_name="sm:flex sm:justify-center sm:items-center",
        ),
        rx.hstack(
            rx.icon("map-pinned", size=20, color="crimson"),
            rx.text(
                "Arturo Prat N° 696, oficina 316, Temuco",
                class_name="text-slate-400 text-sm",
            ),
            spacing="2",
            align="center",
        ),
        spacing="4",
        flex_direction="column",
        class_name="sm:flex sm:justify-center sm:items-center",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Sucursal – La Unión",
            size="4",
            weight="bold",
            as_="h3",
            class_name="text-slate-500 mb-2",
        ),
        rx.box(
            rx.html(
                """<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3045.6789268958078!2d-72.5969385!3d-40.238440499999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f10.0!3m3!1m2!1s0x96166b0d928567ad%3A0x5a7a5fd2914d1d11!2sCasas%20Prefabricadas%20Living%20House!5e0!3m2!1ses!2scl!4v1755174836639!5m2!1ses!2scl!' width="200" height="200" style="border:0;border-radius:0.75rem;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""",
            ),
            class_name="sm:flex sm:justify-center sm:items-center",
        ),
        rx.hstack(
            rx.icon("map-pinned", size=20, color="crimson"),
            rx.text(
                "Ruta T 75 KM 35 Sector Puerto Nuevo, La Unión",
                class_name="text-slate-400 text-sm",
            ),
            spacing="2",
            align="center",
        ),
        spacing="4",
        flex_direction="column",
        class_name="sm:flex sm:justify-center sm:items-center",
    )


def social_link(image: str, href: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width="28px",
            height="28px",
            alt=alt,
            class_name="opacity-70 hover:opacity-100 transition-opacity duration-200",
        ),
        href=href,
        is_external=True,
    )


def socials() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Síguenos",
            size="3",
            weight="bold",
            class_name="text-slate-500 uppercase tracking-wider text-xs mb-1",
        ),
        rx.hstack(
            rx.vstack(
                rx.text("TikTok", class_name="text-slate-500 text-xs"),
                social_link(
                    "/tik tok.png",
                    "https://www.tiktok.com/@casaslivinghouse?lang=es",
                    "TikTok",
                ),
                align="center",
                spacing="1",
            ),
            rx.vstack(
                rx.text("Facebook", class_name="text-slate-500 text-xs"),
                social_link(
                    "/facebook.png",
                    "https://www.facebook.com/casas.living.house.casasprefabricadas/",
                    "Facebook",
                ),
                align="center",
                spacing="1",
            ),
            rx.vstack(
                rx.text("Instagram", class_name="text-slate-500 text-xs"),
                social_link(
                    "/instagram.png",
                    "https://www.instagram.com/casasprefabricadaslivinghouse/",
                    "Instagram",
                ),
                align="center",
                spacing="1",
            ),
            spacing="6",
        ),
        spacing="3",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.box(
            # Main grid
            rx.flex(
                # Brand + socials
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src="/casaslivinghouse.jpg",
                            width="50px",
                            height="50px",
                            border_radius="50%",
                            object_fit="cover",
                            class_name="ring-2 ring-teal-500/40",
                        ),
                        loading_card(),
                        align_items="center",
                        spacing="3",
                    ),
                    rx.text(
                        "Empresa del centro sur de Chile dedicada al desarrollo inmobiliario y al sueño de la casa propia.",
                        class_name="text-slate-400 text-sm leading-relaxed max-w-xs",
                    ),
                    socials(),
                    spacing="5",
                    align_items="start",
                ),
                footer_items_1(),
                footer_items_2(),
                justify="between",
                spacing="8",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(class_name="bg-slate-700/50 my-8"),
            # Bottom bar
            rx.flex(
                rx.text(
                    "© 2026 Casas Prefabricadas Living House — Todos los derechos reservados",
                    class_name="text-slate-500 text-sm text-center",
                ),
                justify="center",
                width="100%",
            ),
            class_name="max-w-7xl mx-auto px-6 lg:px-8 py-12",
        ),
        width="100%",
        class_name="bg-[#5eead4] border-t border-slate-800",
    )
