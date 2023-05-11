# -*- coding: utf-8 -*-
# made by Ahmed ElSaeed

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
from gtts import gTTS
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class AudFlow(FlowLauncher):
    def query(self, query):
        output=[]
        try:
            if len(query.strip()) == 0:
                    
                    output.append({
                        "Title": ":en text to speech |",
                        "SubTitle": "use: 'au :ar expresion |' to speak in arabic, after typing add '|' to run ",
                        "IcoPath": "Images/app.png"})
            else:
                 if len(query) > 3 and ":" in query[0]:                
                      lang=query[1:3]
                      query=query[3:]
                      if query[-1]=="|":
                        output.clear()

                        myobj = gTTS(text=query, lang=lang, slow=False)
                        myobj.save("AudFlow.mp3")
                        pygame.init()
                        pygame.mixer.music.load("AudFlow.mp3")
                        output.append({"Title": "Playing...","IcoPath": "Images/play.png"})
                        pygame.mixer.music.play()

                        while pygame.mixer.music.get_busy():
                            pygame.time.Clock().tick(10)
                        else:
                            output.clear()
                            output.append({
                                "Title": "End",
                                "IcoPath": "Images/stop.png"})
                            
                        
                        pygame.quit()
                      else:
                            output.append({
                            "Title": "Typing...",
                            "IcoPath": "Images/type.png"})

                       
                 else:

                    lang="en"
                      
                    if query[-1]=="|":
                                    output.clear()

                                    myobj = gTTS(text=query, lang=lang, slow=False)
                                    myobj.save("AudFlow.mp3")
                                    pygame.init()
                                    pygame.mixer.music.load("AudFlow.mp3")
                                    
                                    pygame.mixer.music.play()
                                    

                                    while pygame.mixer.music.get_busy():
                                        
                                        pygame.time.Clock().tick(10)
                                    else:
                                        output.clear()
                                        output.append({
                                        "Title": "End",
                                        "IcoPath": "Images/stop.png"})
                                    pygame.quit()
                    
                    elif query[-1] !="|":
                        output.append({
                        "Title": "Typing...",
                        "IcoPath": "Images/type.png"})
                         
        except ValueError:
            output.append({
                        "Title": "enter a valid language",
                        "IcoPath": "Images/error.png"})
          
        except IndexError:
            output.append({
                        "Title": ":en text to speech |",
                        "SubTitle": "use: 'au :ar expresion |' to speak in arabic, after typing add '|' to run ",
                        "IcoPath": "Images/app.png"})
        except pygame.error:
             pass
        except :
            output.append({
                        "Title": "Check your connection",
                        "IcoPath": "Images/conn.png"})                               
        
             
        return output
   
if __name__ == "__main__":
    AudFlow()
