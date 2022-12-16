import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.components.menu import Menu

from dino_runner.components.element import Element

from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    GAME_SPEED = 20

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.running = False
        self.menu = Menu(self.screen)
        self.score = Element()
        self.death_count = Element()
        self.higest_score = Element()
        self.power_up_manager = PowerUpManager()
        

    def excute(self):
        self.running = True
        while self.running :
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.reset_game()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
       

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.power_up_manager.update(self)
        self.obstacle_manager.update(self)
        self.score.update()
        self.update_game_speed()

    
  
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw (self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.score.draw(self.screen)
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count.element == 0:
            self.menu.draw(self.screen ,"press any to start...")

        else:
            self.update_highest_score()
            self.menu.draw(self.screen, "GAME OVER, PRESS ANY KEY TO RESTART")
            self.menu.draw(self.screen, f"YOUR SCORE: {self.score.element}", half_screen_width, 350, )
            self.menu.draw(self.screen, f"HIGHTES SCORE:  {self.higest_score.element}", half_screen_width, 400, )
            self.menu.draw(self.screen, f"TOTAL DEATHS: {self.death_count.element}", half_screen_width, 450, )

        self.screen.blit(ICON, (half_screen_width -50, half_screen_height -140))

        self.menu.update(self)
    
    def update_game_speed(self):
        if self.score.element % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5


    def update_highest_score(self):
        if self.score.element > self.higest_score.element:
            self.higest_score.set_element(self.score.element)

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.score.reset()
        self.game_speed = self.GAME_SPEED
        self.player.reset()

    def draw_power_up_time(self):
        if self.player.has.power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks() / 1000), 2)
            if time_to_show >= 0:
                self.menu.draw(self.screen, f"{self.player.type.capitalize()}" "enabled for{time_to_show} seconds", 550, 100)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE


