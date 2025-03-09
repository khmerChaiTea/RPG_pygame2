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

    def run(self):
        while self.running:
            self.handle_events()
            self.all_sprites.update()  # Player and other sprites update
            self.draw()
            self.clock.tick(FRAMERATE)

        pygame.quit()              
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.display_surface.fill(BG_COLOR)
        self.all_sprites.draw(self.display_surface)  # Draw all sprites
        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()