class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        #initialising properties
        self.image =  image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.rect = self.image.get_rect()
        self.rect.x = (100)
        self.rect.y = (600)
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        # self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        # self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        #update screen for image and text
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text.rect)

    def checkForInput(self,position):
        #check for clicking button
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True 
        return False
    
    def changeColor(self, position):
        #check for hover over button / change color
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else: 
            self.text = self.font.render(self.text_input, True, self.base_color)