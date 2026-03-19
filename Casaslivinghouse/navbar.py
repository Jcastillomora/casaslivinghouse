import reflex as rx
from .footer import loading_card


class NavbarState(rx.State):
    menu_open: bool = False

    def toggle_menu(self):
        self.menu_open = not self.menu_open

    def close_menu(self):
        self.menu_open = False


def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
            class_name="text-white/90 hover:text-white transition-colors duration-200",
            spacing="2",
        ),
        href=url,
    )


def mobile_menu_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text, size="4", weight="medium"),
            class_name="text-white/90 hover:text-white transition-colors duration-200",
            spacing="3",
        ),
        href=url,
        on_click=NavbarState.close_menu,
        class_name="block w-full py-3 px-6 border-b border-teal-700/30 hover:bg-teal-700/30 transition-colors",
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
                        class_name="ring-2 ring-white/40 shadow-md",
                    ),
                    loading_card(),
                    align_items="center",
                    spacing="3",
                ),
                # Links
                rx.hstack(
                    navbar_icons_item("Inicio", "home", "/#inicio"),
                    navbar_icons_item("Nosotros", "users", "/#nosotros"),
                    navbar_icons_item("Modelos", "building-2", "/#modelos"),
                    navbar_icons_item("Contacto", "mail", "/#contacto"),
                    spacing="8",
                ),
                # CTA button
                rx.link(
                    rx.button(
                        rx.icon("phone", size=15),
                        "+56 9 3075 4516",
                        class_name="bg-white text-teal-700 hover:bg-teal-50 text-sm font-bold px-4 py-2 rounded-xl transition-all duration-200 flex items-center gap-2 shadow-md",
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
            rx.vstack(
                # Top bar: logo + hamburger
                rx.hstack(
                    rx.hstack(
                        rx.image(
                            src="/casaslivinghouse.jpg",
                            width="40px",
                            height="40px",
                            border_radius="50%",
                            object_fit="cover",
                            class_name="ring-2 ring-white/40",
                        ),
                        loading_card(),
                        align_items="center",
                        spacing="2",
                    ),
                    rx.box(
                        rx.cond(
                            NavbarState.menu_open,
                            rx.icon("x", size=22, color="white"),
                            rx.icon("menu", size=22, color="white"),
                        ),
                        on_click=NavbarState.toggle_menu,
                        class_name="p-2 rounded-lg hover:bg-white/15 transition-colors cursor-pointer",
                    ),
                    justify="between",
                    align_items="center",
                    width="100%",
                ),
                # Dropdown inline — same gradient, no overflow
                rx.cond(
                    NavbarState.menu_open,
                    rx.box(
                        mobile_menu_item("Inicio", "home", "/#inicio"),
                        mobile_menu_item("Nosotros", "users", "/#nosotros"),
                        mobile_menu_item("Modelos", "building-2", "/#modelos"),
                        mobile_menu_item("Contacto", "mail", "/#contacto"),
                        rx.link(
                            rx.hstack(
                                rx.icon("phone", size=18),
                                rx.text("+56 9 3075 4516", size="4", weight="medium"),
                                class_name="text-white/90 hover:text-white transition-colors duration-200",
                                spacing="3",
                            ),
                            href="https://wa.me/56930754516",
                            is_external=True,
                            on_click=NavbarState.close_menu,
                            class_name="block w-full py-3 px-6 hover:bg-teal-700/30 transition-colors",
                        ),
                        class_name="w-full border-t border-teal-700/30",
                    ),
                    rx.box(),
                ),
                spacing="0",
                width="100%",
            ),
        ),
        top="0",
        z_index="50",
        width="100%",
        class_name="px-4 py-3 border-b border-teal-700/30 shadow-lg",
        style={
            "background": "linear-gradient(135deg, #0d9488 0%, #14b8a6 60%, #0f766e 100%)",
        },
    )
