import pygame as pyg

#button class
class Button():
    # Input:
    #   font refers to the font used to help draw text
    #   text refers to the string value that will be displayed on button
    #   fc refers to the font color
    #   bg refers to the background color of the button
    #   border refers to border color of the button
    #   bd refers to border width
    #   pos refers to the position button is drawn at
    #   width refers to the width of the button
    #   height refers the height of the button
    #   pad refers to the padding space between border of button and text
    def __init__(self,
                 font,
                 text = None,
                 fc = 'black',
                 bg = 'white',
                 border = 'black',
                 bd = 2,
                 pos = (0, 0),
                 width = 80,
                 height = 50,
                 pad = (2, 2)):
        self.font = font
        self.text = text
        self.fc = fc
        self.bg = bg
        self.bd = bd
        self.border = border
        self.pos = pos
        self.rect = pyg.Rect(pos[0], pos[1], width, height)
        self.pad = pad

        self.clicked = False

    # Input:
    #   w refers to game window
    # Output:
    #   returns if button is clicked on
    def draw(self, w):
        # get mouse position and mouse pressed state
        mp = pyg.mouse.get_pos()
        mpr = pyg.mouse.get_pressed()

	# check mouseover and clicked conditions
        if self.rect.collidepoint(mp):
            if mpr[0] == 1 and self.clicked == False:
                self.clicked = True
        if mpr[0] == 0:
            self.clicked = False
	    
        # draw rectangle of button
        
        # inside rectangle
        pyg.draw.rect(w, self.bg, self.rect)
        
        # border of button
        pyg.draw.lines(w, self.border,True,[(self.rect.left,self.rect.top),(self.rect.right,self.rect.top),(self.rect.right,self.rect.bottom),(self.rect.left,self.rect.bottom)],self.bd)
        
        # blit text
        if self.text != None:
            c_text = self.font.render(str(self.text), 0, self.fc)
            w.blit(c_text, (self.pos[0]+self.pad[0], self.pos[1]+self.pad[1]))
        
        return self.clicked
                       

                          
