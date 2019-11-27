# import pygame
# TIMER = 100
# player_time = 0 #how much time the player finish the game
# textclock = ''
# class Timer:
#     def count(self):
#         """
#         counter is for the number you start to countdown
#         text is the string version of the counter number
#         clock is the function to get time in pygame
#         player_time is the time save in the leaderboard
#         """
#         counter, textclock = TIMER, str(TIMER).rjust(3)
#         clock = pygame.time.Clock()
#         #The textfont of the number on the screen
#         font = pygame.font.Font(None, 40)
#         #put a userevent in the function every 1 second, 1000 means 1 sec
#         pygame.time.set_timer(pygame.USEREVENT, 1000)
#         while True:
#             for e in pygame.event.get():
#                 if e.type == pygame.USEREVENT:
#                     counter -= 1
#                     textclock = str(counter).rjust(3)
#                 if e.type == pygame.QUIT: break
#                 #condition that player win the game
#                 # if e.type == winthegame:
#                 #     player_time = TIMER - counter
#                 #     break
#                 else:
#                     screen.fill((255, 255, 255))
#                     #position of the clock
#                     screen.blit(font.render(textclock, True, (0, 0, 0)), (32, 48))
#                     pygame.display.flip()
#                     clock.tick(30)
#                     continue
#                 break
#
#
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# font = pygame.font.Font(None, 40)
# Timer.count(TIMER)
#
#
