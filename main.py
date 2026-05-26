import pygame
import random
import math



pygame.init()
pygame.mixer.init()

song="D:\Music\DNB #1\SpotiMate.io - Operator - Extended Mix - Arcando.mp3"

from audio.analyzer import analyze_audio
data=analyze_audio(song)
print("Tempo:", data["tempo"])
print(data["beat_times"][:10])

Width, Height = 1000, 500
pygame.display.set_caption("Audio Reactive Visual Engine")

pygame.mixer.music.load(song)
pygame.mixer.music.play()  
screen = pygame.display.set_mode((Width, Height))

                
clock = pygame.time.Clock()
time = 0

class Particle:
    def __init__(self):
        self.x = random.randint(0, Width)
        self.y = random.randint(0, Height)

        self.size = random.randint(2, 6)

        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)

        self.color = (
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255),
        )

    def move(self,energy):
        self.x += self.speed_x * (1 + energy * 8)
        self.y += self.speed_y * (1 + energy * 8)

        if self.x <= 0 or self.x >= Width:
            self.speed_x *= -1

        if self.y <= 0 or self.y >= Height:
            self.speed_y *= -1

    def draw(self, pulse):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            int(self.size + pulse)
        )
    def lines():
        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):

                p1 = particles[i]
                p2 = particles[j]

                distance = math.sqrt(
                    (p1.x - p2.x) ** 2 +
                    (p1.y - p2.y) ** 2
                )

                if distance < 120:

                    pygame.draw.line(
                        screen,
                        (0, 255, 255),
                        (int(p1.x), int(p1.y)),
                        (int(p2.x), int(p2.y)),
                        1
                    )
        
        
particles = [Particle() for _ in range(150)]

pulse = 0

fade_surface = pygame.Surface((Width, Height))
fade_surface.set_alpha(50)
fade_surface.fill((5, 5, 15))


#rms stuff
def get_current_rms(current_time):

    closest_index = min(
        range(len(data["rms_times"])),
        key=lambda i: abs(data["rms_times"][i] - current_time)
    )

    return data["rms"][closest_index]



    
running = True
while running:
    clock.tick(60)
    
    current_time = pygame.mixer.music.get_pos() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.blit(fade_surface, (0, 0))

    pulse *= 0.9
    
    for beat in data["beat_times"]:
        if abs(current_time - beat) < 0.1:
            pulse = 8
            
    Particle.lines()
    
    #rms stuff
    current_time = pygame.mixer.music.get_pos() / 1000
    current_rms = get_current_rms(current_time)

    for particle in particles:
        particle.move(current_rms)
        particle.draw(pulse + current_rms * 8)

    pygame.display.flip()

    time += 0.03
    
    
    
    
    
  
    


pygame.quit()
    

