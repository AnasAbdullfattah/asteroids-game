import pygame
class Asteroid:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius,self.width )

    def update(self,dt):
        (self.velocity * dt)

