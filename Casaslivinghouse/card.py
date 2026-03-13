import reflex as rx
from .models import Casa
# from .Casaslivinghouse import State
from reflex_image_zoom import image_zoom

# def card_component(
#     image_src: str = "/img/card-top.jpg",
#     image_alt: str = "Sunset in the mountains",
#     title: str = "The Coldest Sunset",
#     description: str = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus quia, nulla! Maiores et perferendis eaque, exercitationem praesentium nihil.",
#     tags: list = None
# ) -> rx.Component:
#     """
#     Componente de tarjeta (card) reutilizable para Reflex.
    
#     Args:
#         image_src: URL de la imagen
#         image_alt: Texto alternativo para la imagen
#         title: Título de la tarjeta
#         description: Descripción del contenido
#         tags: Lista de etiquetas/tags
#     """
#     if tags is None:
#         tags = ["#photography", "#travel", "#winter"]
    
#     return rx.box(
#         # Imagen
#         image_zoom(
#             rx.image(
#                 src=image_src,
#                 alt=image_alt,
#                 class_name="w-full"
#             ),
#         ),
#         # Contenido principal
#         rx.box(
#             rx.box(
#                 title,
#                 class_name="font-bold text-xl text-gray-900"
#             ),
#             rx.text(
#                 description,
#                 class_name="text-gray-700 text-base py-4"
#             ),
#             rx.flex(
#                 rx.button(
#                     "Ver más",
#                     class_name="bg-cyan-500 hover:bg-cyan-800 text-white font-bold py-2 px-4 rounded-full",
#                 ),
#                 class_name="justify-end"
#             ),
#             class_name="px-6 py-4",
#             spacing="4",
#         ),
#         # Tags/Etiquetas
#         rx.box(
#             *[
#                 rx.text(
#                     tag,
#                     class_name="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
#                 )
#                 for tag in tags
#             ],
#             class_name="px-6 pt-4 pb-2"
#         ),
#         class_name="max-w-sm rounded overflow-hidden shadow-lg justify-center"
#     )


def card_component(casa: Casa):
    """Componente de card adaptado específicamente a tu Excel de catálogo"""
    
    # Formatear precio chileno
    precio_formateado = f"${casa.precio:,}".replace(",", ".")
    
    # Tags básicos con información clave
    tags_info = [
        f"{casa.superficie_m2}m²",
        f"{casa.dormitorios} dorm",
        f"{casa.banos} baños"
    ]
    
    return rx.card(
        rx.vstack(
            # ------------ Imagen de la casa -------------
            rx.image(
                src=casa.imagen,  # Usar la URL externa
                alt=casa.modelo,
                width="100%",
                height="200px",
                object_fit="cover",
                border_radius="0.5rem 0.5rem 0 0",
                fallback=rx.image(
                    src=casa.url_imagen,  # Fallback a imagen local
                    alt=casa.modelo,
                    width="100%",
                    height="200px",
                    object_fit="cover",
                ),
            ),
            
            # ------------ Información principal -------------
            rx.vstack(
                # Header con ID
                rx.hstack(
                    rx.badge(f"#{casa.id}", color_scheme="blue", size="1"),
                    rx.badge("DISPONIBLE", color_scheme="green", size="1"),
                    justify="between",
                    width="100%",
                ),
                
                # Nombre del modelo
                rx.heading(
                    casa.modelo,
                    class_name="text-lg font-semibold text-gray-600",
                    size="4",
                ),
                
                # Descripción
                rx.text(
                    casa.descripcion,
                    class_name="text-sm text-gray-600",
                    line_height="1.4",
                ),
                
                # Tags de especificaciones
                rx.hstack(
                    rx.foreach(
                        tags_info,
                        lambda tag: rx.badge(
                            tag,
                            size="2",
                            color_scheme="cyan",
                            class_name="font-medium",
                        )
                    ),
                    spacing="2",
                    wrap="wrap",
                    justify="center",
                ),
                
                # Precio destacado
                rx.text(
                    precio_formateado,
                    class_name="text-2xl font-bold text-green-600 mt-2",
                ),
                
                spacing="3",
                width="100%",
                padding="1rem",
            ),
            
            # ------------ Botones de acción -------------
            rx.hstack(
                # Botón ver plano
                rx.cond(
                    casa.plano,
                    rx.link(
                        rx.button(
                            rx.icon("file-text", size=16),
                            "Ver plano",
                            size="2",
                            width="33%",
                            cursor="pointer",
                            class_name="text-blue-600 border border-blue-600 hover:bg-blue-50",
                            background_color="transparent",
                        ),
                        href=casa.plano,
                        is_external=True,
                    )
                ),
                
                # Botón ver detalles
                rx.button(
                    rx.icon("eye", size=16),
                    "Detalles",
                    size="2",
                    width="33%",
                    cursor="pointer",
                    class_name="text-indigo-600 border border-indigo-600 hover:bg-indigo-50",
                    background_color="transparent",
                    on_click=lambda: rx.redirect(f"/casa/{casa.id}"),
                ),
                
                # Botón contactar
                rx.button(
                    rx.icon("phone", size=16),
                    "Contactar",
                    size="2",
                    width="34%",
                    cursor="pointer",
                    class_name="text-white hover:bg-purple-600",
                    background_color="#a280f6",
                    on_click=lambda: rx.redirect(f"/contacto/{casa.id}"),
                ),
                
                spacing="1",
                width="100%",
                padding="0 1rem 1rem 1rem",
            ),
            spacing="0",
        ),
        size="3",
        width="100%",
        max_width="22rem",
        box_shadow="lg",
        background_color="white",
        border_radius="0.5rem",
        overflow="hidden",
        class_name="m-2 hover:shadow-xl transition-all duration-300 hover:scale-105",
    )