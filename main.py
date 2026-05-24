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

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

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
        
        
particles = [Particle() for _ in range(120)]



running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((5, 5, 15))

    pulse = abs(math.sin(time)) * 8

    for particle in particles:
        particle.move()
        particle.draw(pulse)

    pygame.display.flip()

    time += 0.03
    
  
    


pygame.quit()
    

