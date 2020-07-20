import requests

import colorama
from colorama import Fore, Back, Style        
import os
colorama.init()




print(Fore.RED + '''



/       \ /  |                          
$$$$$$$  |$$/   ______                  
$$ |  $$ |/  | /      \                 
$$ |  $$ |$$ |/$$$$$$  |                
$$ |  $$ |$$ |$$ |  $$/                 
$$ |__$$ |$$ |$$ |                      
$$    $$/ $$ |$$ |                      
$$$$$$$/  $$/ $$/                       
                                        
                                        
                                        
  ______                                
 /      \                               
/$$$$$$  |  _______   ______   _______  
$$ \__$$/  /       | /      \ /       \ 
$$      \ /$$$$$$$/  $$$$$$  |$$$$$$$  |
 $$$$$$  |$$ |       /    $$ |$$ |  $$ |
/  \__$$ |$$ \_____ /$$$$$$$ |$$ |  $$ |
$$    $$/ $$       |$$    $$ |$$ |  $$ |
 $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/ 
                                        


...............coded by https://github.com/restanse


''')
print(Style.RESET_ALL)    

url = input("enter site, like https://site.com/: ")


file = open("list.txt")
for line in file:
	
	link = url + line
	r = requests.get(link)
	if r.status_code == 200:
		print("found: " + link)

	
		





print("scanned")