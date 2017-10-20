import pygame

from config import *
from levels import Level_01
from player import Player
import platforms


class Game:
    def __init__(self):
        self.player = Player()
        self.screen = None

        # Create all the levels
        self.level_list = [Level_01(self.player)]

        # Set the current level
        current_level_no = 0
        self.current_level = self.level_list[current_level_no]

        self.active_sprite_list = pygame.sprite.Group()

        self.player.rect.x = 140
        self.player.rect.y = GROUND_HEIGHT - self.player.rect.height
        self.active_sprite_list.add(self.player)

        self.should_quit = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.display.set_caption("MetaPyWeek 24#")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        while not self.should_quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.should_quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print "Escape pressed, quitting game :("
                        self.should_quit = True

                    if event.key == pygame.K_LEFT:
                        self.player.go_left()
                    if event.key == pygame.K_RIGHT:
                        self.player.go_right()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.player.change_x < 0:
                        self.player.stop()
                    if event.key == pygame.K_RIGHT and self.player.change_x > 0:
                        self.player.stop()

            collided = pygame.sprite.spritecollide(self.player,
                                                   self.current_level.level_elements,
                                                   False)
            for element in collided:
                if isinstance(element, platforms.Platform):
                    self.player.rect.right = element.rect.left

                elif isinstance(element, platforms.Trampoline):
                    self.player.jump()

            self.active_sprite_list.update()

            # Update items in the level
            self.current_level.update()

            # If the player gets near the right side, shift the world left (-x)
            if self.player.rect.right >= 500:
                diff = self.player.rect.right - 500
                self.player.rect.right = 500
                self.current_level.shift_world(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if self.player.rect.left <= 120:
                diff = 120 - self.player.rect.left
                self.player.rect.left = 120
                self.current_level.shift_world(diff)

            self.current_level.draw(self.screen)
            self.active_sprite_list.draw(self.screen)

            self.clock.tick(60)
            pygame.display.flip()


def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
