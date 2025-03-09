from settings import *

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, row, width, height, scale, colour):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        
        x = frame * width
        y = row * height

        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('characters', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=pos)
        self.player_image = SpriteSheet(self.image)

        self.direction = pygame.Vector2(0, 0)
        self.speed = 2

        # Animations
        self.front_idle = [self.player_image.get_image(i, 0, 48, 48, 3, BLACK) for i in range(6)]
        self.side_idle = [self.player_image.get_image(i, 1, 48, 48, 3, BLACK) for i in range(6)]
        self.back_idle = [self.player_image.get_image(i, 2, 48, 48, 3, BLACK) for i in range(6)]
        self.front_walk = [self.player_image.get_image(i, 3, 48, 48, 3, BLACK) for i in range(6)]
        self.side_walk = [self.player_image.get_image(i, 4, 48, 48, 3, BLACK) for i in range(6)]
        self.back_walk = [self.player_image.get_image(i, 5, 48, 48, 3, BLACK) for i in range(6)]

        self.side_idle_left = [pygame.transform.flip(frame, True, False) for frame in self.side_idle]
        self.side_walk_left = [pygame.transform.flip(frame, True, False) for frame in self.side_walk]

        self.current_animation = self.front_idle
        self.current_frame = 0
        self.animation_speed = 150
        self.last_update = pygame.time.get_ticks()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.direction.y = keys[pygame.K_DOWN] - keys[pygame.K_UP]

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def update_animation(self):
        # Determine the correct animation based on movement
        if self.direction.x > 0:
            self.current_animation = self.side_walk
        elif self.direction.x < 0:
            self.current_animation = self.side_walk_left
        elif self.direction.y > 0:
            self.current_animation = self.front_walk
        elif self.direction.y < 0:
            self.current_animation = self.back_walk
        else:
            if self.current_animation in (self.side_walk, self.side_walk_left):
                self.current_animation = self.side_idle if self.current_animation == self.side_walk else self.side_idle_left
            elif self.current_animation == self.front_walk:
                self.current_animation = self.front_idle
            elif self.current_animation == self.back_walk:
                self.current_animation = self.back_idle

        # Frame update logic
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.animation_speed:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_frame]  # Update the player's image

    def update(self):
        self.handle_input()
        self.move()
        self.update_animation()