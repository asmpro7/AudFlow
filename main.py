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
from playsound import playsound
from pathlib import Path
import json
class AudFlow(FlowLauncher):
    def query(self, query):
        base_dir = Path(__file__).resolve().parent
        Flow_launcher_main_dir = base_dir.parent.parent
        flow_settings_dir = Flow_launcher_main_dir / "Settings" / "Plugins" / "AudFlow" / "Settings.json"
        if os.path.exists(flow_settings_dir):
            with open(flow_settings_dir,"r") as f:
                settings=json.load(f)
        key=settings["execute_key"]
        output=[]
        try:
            if len(query.strip()) == 0:
                    
                    output.append({
                        "Title": f":en text to speech {key}",
                        "SubTitle": f"use: 'au :ar expresion {key}' to speak in arabic, after typing add '{key}' to run ",
                        "IcoPath": "Images/app.png"})
            else:
                 if len(query) > 3 and ":" in query[0]:                
                      lang=query[1:3]
                      query=query[3:]
                      if query.endswith(key):
                        output.clear()

                        myobj = gTTS(text=query, lang=lang, slow=False)
                        myobj.save("AudFlow.mp3")
                        
                        output.append({"Title": "Playing...","IcoPath": "Images/play.png"})
                        playsound("AudFlow.mp3")

                        
                        output.clear()
                        output.append({
                            "Title": "End",
                            "IcoPath": "Images/stop.png"})
                            
                        
                        
                      else:
                            output.append({
                            "Title": "Typing...",
                            "IcoPath": "Images/type.png"})

                       
                 else:

                    lang="en"
                      
                    if query.endswith(key):
                                    output.clear()

                                    myobj = gTTS(text=query, lang=lang, slow=False)
                                    myobj.save("AudFlow.mp3")

                                    

                                    output.append({"Title": "Playing...","IcoPath": "Images/play.png"})
                                    playsound("AudFlow.mp3")
                                    
                                    output.clear()
                                    output.append({
                                    "Title": "End",
                                    "IcoPath": "Images/stop.png"})
                                    
                    
                    elif not query.endswith(key):
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
        except :
            output.append({
                        "Title": "Check your connection",
                        "IcoPath": "Images/conn.png"})                               
        
             
        return output
   
if __name__ == "__main__":
    AudFlow()
