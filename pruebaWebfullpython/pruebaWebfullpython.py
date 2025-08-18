import reflex as rx

class State(rx.State):
    """The app state."""

def index():
    return rx.container(
        # Fondo con gradiente
        rx.box(
            # Header con avatar y nombre
            rx.vstack(
                rx.spacer(height="40px"),
                
                # Avatar con efecto de hover
                rx.box(
                    rx.avatar(
                        src="/yo.jpeg", 
                        size="9",
                        radius="full"
                    ),
                    class_name="hover:scale-110 transition-transform duration-300",
                    border="4px solid",
                    border_color="blue.400",
                    border_radius="full",
                    padding="4px",
                    box_shadow="0 10px 25px rgba(0,0,0,0.2)"
                ),
                
                # Título principal
                rx.heading(
                    "Juan David López",
                    size="8",
                    color="gray.800",
                    text_align="center",
                    margin_top="20px"
                ),
                
                rx.text(
                    "Estudiante de Ingeniería de Sistemas y Computación",
                    size="4",
                    color="blue.600",
                    text_align="center",
                    font_weight="500"
                ),
                
                rx.text(
                    "Universidad del Quindío • 22 años",
                    size="2",
                    color="gray.600",
                    text_align="center"
                ),
                
                align="center",
                spacing="2"
            ),
            
            rx.spacer(height="30px"),
            
            # Tarjeta principal con descripción
            rx.card(
                rx.vstack(
                    rx.heading(
                        "Sobre mí",
                        size="5",
                        color="gray.800",
                        margin_bottom="15px"
                    ),
                    rx.text(
                        "¡Hola! Soy Juan David López, tengo 20 años y soy estudiante de ingeniería de sistemas y computación en la Universidad del Quindío. Actualmente estoy aprendiendo a programar con Python, tengo experiencia en Java back-end y bases de datos no relacionales. He creado esta aplicación web utilizando Reflex para mostrar mis habilidades.",
                        size="3",
                        line_height="1.6",
                        color="gray.700"
                    ),
                    align="start",
                    spacing="3"
                ),
                size="4",
                margin="20px 0",
                box_shadow="0 4px 15px rgba(0,0,0,0.1)",
                border="1px solid",
                border_color="gray.200"
            ),
            
            # Skills section
            rx.card(
                rx.vstack(
                    rx.heading(
                        "🛠️ Tecnologías",
                        size="4",
                        color="gray.800",
                        margin_bottom="15px"
                    ),
                    rx.hstack(
                        rx.badge("Python", color_scheme="blue", size="2"),
                        rx.badge("Java", color_scheme="orange", size="2"),
                        rx.badge("NoSQL", color_scheme="green", size="2"),
                        rx.badge("Reflex", color_scheme="purple", size="2"),
                        rx.badge("Backend", color_scheme="red", size="2"),
                        spacing="2",
                        wrap="wrap",
                        justify="center"
                    ),
                    spacing="3",
                    align="center"
                ),
                size="3",
                margin="20px 0",
                box_shadow="0 4px 15px rgba(0,0,0,0.1)",
                border="1px solid",
                border_color="gray.200"
            ),
            
            # Botones de acción
            rx.vstack(
                # Primer diálogo - Certificaciones
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(
                            "🏆 Ver Certificaciones",
                            size="4",
                            color_scheme="blue",
                            variant="solid",
                            width="250px",
                            class_name="hover:scale-105 transition-transform duration-200"
                        )
                    ),
                    rx.dialog.content(
                        rx.vstack(
                            rx.flex(
                                rx.heading("🏆", size="7"),
                                rx.heading("Mis Certificaciones", size="7", color="gray.800"),
                                align="center",
                                spacing="6"
                            ),
                            
                            rx.separator(),
                            
                            rx.text(
                                "Aquí puedes encontrar mi Certificado de Oracle",
                                size="3",
                                color="gray.600",
                                text_align="center"
                            ),
                            
                            rx.hstack(
                                rx.link(
                                    rx.button(
                                        "💼 Certificado backend",
                                        color_scheme="gray",
                                        size="4",
                                        width="200px"
                                    ),
                                    href="https://docs.google.com/document/d/1qmejh2R8CryGKfi-VQXgrpLkNCQwHHB2CFnLMIhsMtw/edit?usp=sharing",
                                    is_external=True
                                ),
                                rx.link(
                                    rx.button(
                                        "🐙 Certificado python",
                                        color_scheme="gray",
                                        size="4",
                                        width="200px",
                                    ),
                                    href="https://docs.google.com/document/d/1acNuxCPySM1ATrwSAxO15nn2eenXrhUJ0IT0r5cfziA/edit?usp=sharing",
                                    is_external=True
                                ),
                                rx.link(
                                    rx.button(
                                        "🐙 Certificado JavaScript",
                                        color_scheme="gray",
                                        size="4",
                                        width="200px",
                                    ),
                                    href="https://docs.google.com/document/d/1odrKUTNaIPEm55I_3vwSOxPNooVZk9bWPeIiSLZWmg0/edit?usp=sharing",
                                    is_external=True
                                ),
                                spacing="3",
                                justify="center"
                            ),
                            
                            
                            rx.separator(),
                            
                            rx.dialog.close(
                                rx.button(
                                    "Cerrar",
                                    color_scheme="red",
                                    variant="soft",
                                    size="2"
                                )
                            ),
                            
                            spacing="4",
                            align="center",
                            width="100%"
                        ),
                        max_width="1000px"
                    )
                ),
                
                # Segundo diálogo - Contacto
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(
                            "📞 Contáctame",
                            size="4",
                            color_scheme="green",
                            variant="solid",
                            width="250px",
                            class_name="hover:scale-105 transition-transform duration-200"
                        )
                    ),
                    rx.dialog.content(
                        rx.vstack(
                            rx.flex(
                                rx.heading("📞", size="6"),
                                rx.heading("¡Hablemos!", size="5", color="gray.800"),
                                align="center",
                                spacing="2"
                            ),
                            
                            rx.separator(),
                            
                            rx.text(
                                "¿Interesado en colaborar? ¡Conectemos!",
                                size="3",
                                color="gray.600",
                                text_align="center"
                            ),
                            
                            rx.vstack(
                                rx.link(
                                    rx.button(
                                        "💼 Mi LinkedIn",
                                        color_scheme="blue",
                                        size="4",
                                        width="150px"
                                    ),
                                    href="https://www.linkedin.com/in/juan-david-lopez-hernandez-2264b1261/",
                                    is_external=True
                                ),
                                rx.link(
                                    rx.button(
                                        "@ Mi Instagram",
                                        color_scheme="red",
                                        size="4",
                                        widht="150"
                                    ),
                                    href="https://www.instagram.com/juan.da312/",
                                    is_external=True
                                ),
                                rx.link(
                                    rx.button(
                                        "📂 Mis Proyectos",
                                        color_scheme="purple",
                                        size="4",
                                        width="150px"
                                    ),
                                    href="https://github.com/juan-david-lopez",
                                    is_external=True
                                ),
                                spacing="3",
                                align="center"
                            ),
                            
                            rx.separator(),
                            
                            rx.dialog.close(
                                rx.button(
                                    "Cerrar",
                                    color_scheme="red",
                                    variant="soft",
                                    size="2"
                                )
                            ),
                            
                            spacing="4",
                            align="center",
                            width="100%"
                        ),
                        max_width="400px"
                    )
                ),
                
                spacing="4",
                align="center",
                margin_top="30px"
            ),
            
            # Footer
            rx.center(
                rx.text(
                    "Diseñado con Reflex • 2025",
                    size="1",
                    color="gray.500",
                    margin_top="40px",
                    margin_bottom="20px"
                )
            ),
            
            align="center",
            spacing="4",
            width="100%"
        ),
        
        # Estilos del contenedor principal
        max_width="600px",
        margin="0 auto",
        padding="20px",
        min_height="100vh",
        style={
            "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        }
    )

def app():
    return rx.app(
        style={
            "font_family": "Inter, system-ui, sans-serif"
        }
    )

app = rx.App(
    style={
        "font_family": "Inter, system-ui, sans-serif"
    }
)
app.add_page(index, title="Juan David López - Portfolio")