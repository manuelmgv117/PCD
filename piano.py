import pygame
import os

# Inicializa pygame
pygame.init()

# Define el tamaño de la ventana
window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Piano Virtual")

# Define los colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define la fuente para el texto
font = pygame.font.Font(None, 36)

# Función para dibujar texto
def draw_text(surface, text, pos, color=BLACK):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

# Define las teclas del piano y sus notas correspondientes
keys = [
    {"key": pygame.K_a, "note": "Do", "color": WHITE, "rect": pygame.Rect(50, 100, 100, 200), "label": "A"},
    {"key": pygame.K_s, "note": "Re", "color": WHITE, "rect": pygame.Rect(150, 100, 100, 200), "label": "S"},
    {"key": pygame.K_d, "note": "Mi", "color": WHITE, "rect": pygame.Rect(250, 100, 100, 200), "label": "D"},
    {"key": pygame.K_f, "note": "Fa", "color": WHITE, "rect": pygame.Rect(350, 100, 100, 200), "label": "F"},
    {"key": pygame.K_g, "note": "Sol", "color": WHITE, "rect": pygame.Rect(450, 100, 100, 200), "label": "G"},
    {"key": pygame.K_h, "note": "La", "color": WHITE, "rect": pygame.Rect(550, 100, 100, 200), "label": "H"},
    {"key": pygame.K_j, "note": "Si", "color": WHITE, "rect": pygame.Rect(650, 100, 100, 200), "label": "J"},
]

# Carga los sonidos de las notas
sounds = {}
for key in keys:
    sound_path = f"sounds/{key['note']}.mp3"
    if os.path.isfile(sound_path):
        sounds[key["note"]] = pygame.mixer.Sound(sound_path)
    else:
        print(f"Error: No se encontró el archivo {sound_path}")

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            for key in keys:
                if event.key == key["key"]:
                    print(f"Tocando nota: {key['note']}")  # Agregado para depuración
                    sounds[key["note"]].play()

    # Dibuja las teclas
    window.fill((0, 0, 0))  # Limpia la ventana con el color de fondo
    for key in keys:
        pygame.draw.rect(window, key["color"], key["rect"])
        pygame.draw.rect(window, BLACK, key["rect"], 2)  # Dibuja el borde de la tecla
        # Dibuja el nombre de la nota y la tecla
        draw_text(window, key["note"], (key["rect"].x + 35, key["rect"].y + 80))
        draw_text(window, key["label"], (key["rect"].x + 35, key["rect"].y + 120))

    pygame.display.flip()  # Actualiza la ventana

pygame.quit()
