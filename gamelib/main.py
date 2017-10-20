from pygame.colordict import THECOLORS
import pygame

from config import *
from levels import Level_01
from player import Player
import coins
import platforms
import shmuel

DEBUG = False

class Game:
    def __init__(self):
        pygame.display.set_caption("MetaPyWeek 24#")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.font = pygame.font.SysFont("monospace", 15)

        self.player = Player()
        self.level_list = [Level_01(self.player)]

        current_level_no = 0
        self.current_level = self.level_list[current_level_no]
        self.player.level = self.current_level
        self.active_sprite_list = pygame.sprite.Group()

        self.player.rect.x = 140
        self.player.rect.y = GROUND_HEIGHT - self.player.rect.height
        self.active_sprite_list.add(self.player)

        self.active_rays = []

        self.shmuel = shmuel.Shmuel()

        self.should_quit = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        self.coin_count = 0

    def run(self):
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

                if event.type == pygame.MOUSEBUTTONUP:
                    new_tramp = platforms.Trampoline()
                    new_tramp.rect.center = event.pos
                    self.current_level.level_elements.add(new_tramp)

                    self.active_rays.append((new_tramp, 255))


            collided = pygame.sprite.spritecollide(self.player,
                                                   self.current_level.level_elements,
                                                   False)
            for element in collided:
                if isinstance(element, coins.Coin):
                    self.current_level.level_elements.remove(element)
                    self.coin_count += element.coin_value

            self.active_sprite_list.update()
            self.current_level.update()
            self.shmuel.update()

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

            #DRAW HERE:
            self.current_level.draw(self.screen)
            self.active_sprite_list.draw(self.screen)

            self.screen.blit(self.shmuel.image, self.shmuel.rect)
            label = self.font.render("Coins: %s" % self.coin_count, True, THECOLORS["brown"])
            self.screen.blit(label, (SCREEN_WIDTH / 2, 20))

            new_rays = []
            for obj, percent in self.active_rays:
                pygame.draw.line(
                    self.screen,
                    pygame.Color(255, 0, 0, percent),
                    self.shmuel.rect.bottomleft,
                    obj.rect.topright,
                    4
                )
                if percent > 0:
                    new_rays.append((obj, percent - 1))

            self.active_rays = new_rays

            dt = self.clock.tick(60)

            if DEBUG:
                print "Frame took: %s" % dt

            pygame.display.flip()


def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
