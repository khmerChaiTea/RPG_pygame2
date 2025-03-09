from settings import *

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, row, width, height, scale, colour):
        """ Extracts an image from the sprite sheet. """
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
        self.rect = self.image.get_frect(center = pos)
        self.player_image = SpriteSheet(self.image)
        
