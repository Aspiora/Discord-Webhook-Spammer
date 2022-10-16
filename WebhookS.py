print(f"""
                                                                                                 
 _    _      _     _                 _        _____                                           
| |  | |    | |   | |               | |      /  ___|                                          
| |  | | ___| |__ | |__   ___   ___ | | __   \ `--. _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
| |/\| |/ _ \ '_ \| '_ \ / _ \ / _ \| |/ /    `--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
\  /\  /  __/ |_) | | | | (_) | (_) |   <    /\__/ / |_) | (_| | | | | | | | | | | |  __/ |   
 \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\   \____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                   | |                                        
                                                   |_|                                        
                                          
                                   Developed By Aspiora
                                  Discord.gg/Aspiora#8733
""")

from dhooks import Webhook, Embed
import time
import os



webhookurl = Webhook(input("Webhook url gir: "))
delay = int(input("Delay gir: "))
embedm = int(input("Mesaj gir :"))



embed = Embed(
    description='',
    color=0x5CDBF0,
    timestamp='now'  
    )

image2 = 'İMG URL'
image1 = 'İMG URL'

embed.set_author(name='TEXT', icon_url=image1)
embed.add_field(name='TEXT ', value='TEXT')
embed.add_field(name='TEXT', value='TEXT')
embed.set_footer(text='TEXT', icon_url=image1)

embed.set_thumbnail(image1)
embed.set_image(image2)
while True:
    time.sleep(delay)
    webhookurl.send(embed=embed)

    webhookurl.send(embedm)
    print("""  

    //   ) )                             
   ((         ___       __      ___   /  
     \\     //___) ) //   ) ) //   ) /   
       ) ) //       //   / / //   / /    
((___ / / ((____   //   / / ((___/ /     ()

""")  