import reflex as rx
from .footer import loading_card


def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
            class_name="text-white hover:text-teal-400 transition-colors duration-200",
            spacing="2",
        ),
        href=url,
    )


def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
            class_name="text-slate-700 hover:text-teal-600 transition-colors",
        ),
        href=url,
    )


def navbar_icons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                # Logo
                rx.hstack(
                    rx.image(
                        src="/casaslivinghouse.jpg",
                        width="46px",
                        height="46px",
                        border_radius="50%",
                        object_fit="cover",
                        class_name="ring-2 ring-teal-500/40",
                    ),
                    loading_card(),
                    align_items="center",
                    spacing="3",
                ),
                # Links
                rx.hstack(
                    navbar_icons_item("Inicio", "home", "/#"),
                    navbar_icons_item("Nosotros", "users", "/#"),
                    navbar_icons_item("Modelos", "building-2", "/#"),
                    navbar_icons_item("Contacto", "mail", "/#"),
                    spacing="8",
                ),
                # CTA button
                rx.link(
                    rx.button(
                        rx.icon("phone", size=15),
                        "+56 9 3075 4516",
                        class_name="bg-teal-500 hover:bg-teal-400 text-white text-sm font-semibold px-4 py-2 rounded-xl transition-all duration-200 flex items-center gap-2 shadow-lg shadow-teal-500/20",
                        size="2",
                    ),
                    href="https://wa.me/56930754516",
                    is_external=True,
                ),
                justify="between",
                align_items="center",
                class_name="w-full px-8",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/casaslivinghouse.jpg",
                        width="40px",
                        height="40px",
                        border_radius="50%",
                        object_fit="cover",
                        class_name="ring-2 ring-teal-500/40",
                    ),
                    loading_card(),
                    align_items="center",
                    spacing="2",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.box(
                            rx.icon("menu", size=22, color="white"),
                            class_name="p-2 rounded-lg hover:bg-white/10 transition-colors cursor-pointer",
                        )
                    ),
                    rx.menu.content(
                        navbar_icons_menu_item("Inicio", "home", "/#"),
                        navbar_icons_menu_item("Nosotros", "users", "/#"),
                        navbar_icons_menu_item("Modelos", "building-2", "/#"),
                        navbar_icons_menu_item("Contacto", "mail", "/#"),
                        class_name="bg-[#5eead4]",
                    ),
                ),
                justify="between",
                align_items="center",
                width="100%",
            ),
        ),
        # position="sticky",
        top="0",
        z_index="50",
        width="100%",
        class_name="px-4 py-3 bg-[#5eead4] backdrop-blur-sm border-b border-white/10 shadow-xl",
    )
