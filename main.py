from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('RPG Adventure')
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.player = Player((400, 300), self.all_sprites)

        self.front_idle = [
            self.player.player_image.get_image(0, 0, 48, 48, 3, BLACK),
            self.player.player_image.get_image(1, 0, 48, 48, 3, BLACK),
            self.player.player_image.get_image(2, 0, 48, 48, 3, BLACK),
            self.player.player_image.get_image(3, 0, 48, 48, 3, BLACK),
            self.player.player_image.get_image(4, 0, 48, 48, 3, BLACK),
            self.player.player_image.get_image(5, 0, 48, 48, 3, BLACK),
        ]
        
        self.side_idle = [
            self.player.player_image.get_image(0, 1, 48, 48, 3, BLACK),
            self.player.player_image.get_image(1, 1, 48, 48, 3, BLACK),
            self.player.player_image.get_image(2, 1, 48, 48, 3, BLACK),
            self.player.player_image.get_image(3, 1, 48, 48, 3, BLACK),
            self.player.player_image.get_image(4, 1, 48, 48, 3, BLACK),
            self.player.player_image.get_image(5, 1, 48, 48, 3, BLACK),
        ]
        
        self.back_idle = [
            self.player.player_image.get_image(0, 2, 48, 48, 3, BLACK),
            self.player.player_image.get_image(1, 2, 48, 48, 3, BLACK),
            self.player.player_image.get_image(2, 2, 48, 48, 3, BLACK),
            self.player.player_image.get_image(3, 2, 48, 48, 3, BLACK),
            self.player.player_image.get_image(4, 2, 48, 48, 3, BLACK),
            self.player.player_image.get_image(5, 2, 48, 48, 3, BLACK),
        ]
        
        self.front_walk = [
            self.player.player_image.get_image(0, 3, 48, 48, 3, BLACK),
            self.player.player_image.get_image(1, 3, 48, 48, 3, BLACK),
            self.player.player_image.get_image(2, 3, 48, 48, 3, BLACK),
            self.player.player_image.get_image(3, 3, 48, 48, 3, BLACK),
            self.player.player_image.get_image(4, 3, 48, 48, 3, BLACK),
            self.player.player_image.get_image(5, 3, 48, 48, 3, BLACK),
        ]
        
        self.side_walk = [
            self.player.player_image.get_image(0, 4, 48, 48, 3, BLACK),
            self.player.player_image.get_image(1, 4, 48, 48, 3, BLACK),
            self.player.player_image.get_image(2, 4, 48, 48, 3, BLACK),
            self.player.player_image.get_image(3, 4, 48, 48, 3, BLACK),
            self.player.player_image.get_image(4, 4, 48, 48, 3, BLACK),
            self.player.player_image.get_image(5, 4, 48, 48, 3, BLACK),
        ]
        
        self.back_walk = [
            self.player.player_image.get_image(0, 5, 48, 48, 3, BLACK),
            self.player.player_image.get_image(1, 5, 48, 48, 3, BLACK),
            self.player.player_image.get_image(2, 5, 48, 48, 3, BLACK),
            self.player.player_image.get_image(3, 5, 48, 48, 3, BLACK),
            self.player.player_image.get_image(4, 5, 48, 48, 3, BLACK),
            self.player.player_image.get_image(5, 5, 48, 48, 3, BLACK),
        ]
        
        self.side_idle_left = [pygame.transform.flip(frame, True, False) for frame in self.side_idle]

        self.current_animation = self.front_idle
        self.current_frame = 0
        self.animation_speed = 150
        self.last_update = pygame.time.get_ticks()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.current_animation = self.side_idle
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.current_animation = self.front_idle
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    self.current_animation = self.side_idle_left
                elif event.key in (pygame.K_UP, pygame.K_w):
                    self.current_animation = self.back_idle
                    
    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.animation_speed:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.current_animation)

    def run(self):
        while self.running:
            self.handle_events()
            self.update_animation()
            self.all_sprites.update()
            self.draw()
            self.clock.tick(FRAMERATE)

        pygame.quit()

    def draw(self):
        self.display_surface.fill(BG_COLOR)
        self.display_surface.blit(self.current_animation[self.current_frame], (200, 200))
        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()