

import pygame as pg
from .. import tools
import os

class Viewer(tools.States):
    def __init__(self, screen_rect):
        tools.States.__init__(self)
        self.screen_rect = screen_rect
        self.options = ['Back']
        self.next_list = ['MENU']
        self.title, self.title_rect = self.make_text('Card Viewer', self.title_color, (self.screen_rect.centerx, 75), 150)
        self.pre_render_options()
        self.from_bottom = 500
        self.spacer = 75
        
        self.set_images()
        self.image = self.cards[0]
        self.image_rect = self.image.get_rect(center=self.screen_rect.center)
        
    def set_images(self):
        self.cards = []
        path = os.path.join(tools.Image.path, 'cards')
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith('.png'):
                    path = os.path.abspath(os.path.join(root, f))
                    self.cards.append(pg.image.load(path))
        
    def show_card(self):
        print(self.cards)
        
    def switch_card(self, num):
        ind = self.cards.index(self.image)
        ind += num
        if ind < 0:
            ind = len(self.cards)-1
        elif ind > len(self.cards)-1:
            ind = 0
            
        self.image = self.cards[ind]
        self.image_rect = self.image.get_rect(center=self.screen_rect.center)
        self.button_sound.sound.play()

    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key in [pg.K_LEFT, pg.K_a]:
                self.switch_card(-1)
            elif event.key in [pg.K_RIGHT, pg.K_d]:
                self.switch_card(1)
            
            elif event.key in [pg.K_UP, pg.K_w]:
                self.change_selected_option(-1)
            elif event.key in [pg.K_DOWN, pg.K_s]:
                self.change_selected_option(1)
                
            elif event.key == pg.K_RETURN:
                self.select_option(self.selected_index)
        self.mouse_menu_click(event)

    def update(self, now, keys):
        pg.mouse.set_visible(True)
        self.mouse_hover_sound()
        self.change_selected_option()

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.title,self.title_rect)
        screen.blit(self.image,self.image_rect)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            if i == self.selected_index:
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img,rend_rect)
            else:
                screen.blit(opt[0],opt[1])
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
