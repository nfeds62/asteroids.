import pygame
from constants import *
from circleshape import *
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED
from shot import *



class Player(CircleShape):
    
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.time = 0

# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, direction, dt):
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.time > 0:
            self.time -= dt

        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(1, dt)

        if keys[pygame.K_w]:
            self.move(1, dt)
        if keys[pygame.K_s]:
            self.move(-1, dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
            

    def move(self, direction, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction
    
    def shoot(self):
        if self.time > 0:
            return
        shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = shot_direction * PLAYER_SHOOT_SPEED
        
        self.time = PLAYER_SHOOT_COOLDOWN
        self.shots_group.add(new_shot)
