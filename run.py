import sys
from src import start
import libtcodpy as libtcod

#Some setup
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

#Link to information about custom fonts:
#http://roguecentral.org/doryen/data/libtcod/doc/1.5.1/html2/console_set_custom_font.html?c=false&cpp=false&cs=false&py=true&lua=false
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	
#Initializing the window, important
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)

#Important for real-time rogue-like, can skip if turn-based
libtcod.sys_set_fps(LIMIT_FPS)

#Player position
playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

def main():
	#Keeps the game running
	while not libtcod.console_is_window_closed():
		#Good link for colors:
		#http://roguecentral.org/doryen/data/libtcod/doc/1.5.1/html2/color.html?c=false&cpp=false&cs=false&py=true&lua=false
		libtcod.console_set_default_foreground(0, libtcod.white)

		libtcod.console_put_char(0, playerx, playery, '@', libtcod.BKGND_NONE)
		
		#This needs to be at the end of the loop for refreshing the screen
		libtcod.console_flush()

		#Prevents several chars after each other and so on..
		libtcod.console_put_char(0, playerx, playery, ' ', libtcod.BKGND_NONE)

		#handle keys and exit game if needed
		exit = handle_keys()
		if exit:
			break


#function for pressed keys
#Information if other keys are preferred
#http://roguecentral.org/doryen/data/libtcod/doc/1.5.1/html2/console_keycode_t.html?c=false&cpp=false&cs=false&py=true&lua=false
def handle_keys():
    global playerx, playery

    key = libtcod.console_check_for_keypress()
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game

    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        playery -= 1
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        playery += 1
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        playerx -= 1
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        playerx += 1


if __name__ == '__main__':
    main()