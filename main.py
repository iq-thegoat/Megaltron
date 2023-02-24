import os 
import hashlib
import os.path as path
import time,sys
import tkinter.filedialog as fd
from yaspin import yaspin,Spinner
import colorama,random,datetime,socket
from ComboEditor.Editor import Editor
from discord import SyncWebhook
import ctypes

def send_to_webhook(webhook,message):
        webhook = SyncWebhook.from_url(webhook)
        webhook.send(message)

colorama.init()
colors = [colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN]

rc = random.choice(colors)
res = colorama.Fore.RESET

#GLOBALS
global NewList
global BigList
global FileNames
BigList = []
NewList = []
FileNames=[]
Folder_names = []

def writetofile(error:str):
    with open("erors.txt",'a',encoding='utf-8',errors='ignore')as e:
        e.write(error+"\n")

def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

Name = center("""

 /$$      /$$ /$$$$$$$$  /$$$$$$   /$$$$$$  /$$    /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$   /$$
| $$$    /$$$| $$_____/ /$$__  $$ /$$__  $$| $$   |__  $$__/| $$__  $$ /$$__  $$| $$$ | $$
| $$$$  /$$$$| $$      | $$  \__/| $$  \ $$| $$      | $$   | $$  \ $$| $$  \ $$| $$$$| $$
| $$ $$/$$ $$| $$$$$   | $$ /$$$$| $$$$$$$$| $$      | $$   | $$$$$$$/| $$  | $$| $$ $$ $$
| $$  $$$| $$| $$__/   | $$|_  $$| $$__  $$| $$      | $$   | $$__  $$| $$  | $$| $$  $$$$
| $$\  $ | $$| $$      | $$  \ $$| $$  | $$| $$      | $$   | $$  \ $$| $$  | $$| $$\  $$$
| $$ \/  | $$| $$$$$$$$|  $$$$$$/| $$  | $$| $$$$$$$$| $$   | $$  | $$|  $$$$$$/| $$ \  $$
|__/     |__/|________/ \______/ |__/  |__/|________/|__/   |__/  |__/ \______/ |__/  \__/
                                                                                          
                                                                                          
                                                                                          """)


def ErrorRemover(func):
    
    def wrapper(*args, **kwargs): 
        try:
            name = socket.gethostname()
            privateIp = socket.gethostbyname(socket.gethostname())
            func(*args, **kwargs)
        except Exception as E:
            try:
                msg = f"```TIME:{str(datetime.datetime.now())[:-7].replace(':','-')}\nERORR HAPPENED:{E}\nNAME:{name}\nPRIVATE IP: {privateIp}\nFUNC={str(func).split('at')[0]}```"
                with open("errors.txt", "a",errors="ignore") as errors:
                    errors.write(f"TIME:{str(datetime.datetime.now())[:-7].replace(':','-')}  ERORR HAPPENED:{E}\n")
            except:
                pass

    return wrapper


class delete:
    def __init__(self,filetype:str) -> None:
        self.filetype = filetype
        self.removed = []


    def filedeleter(self,folder_path:str):
        global NewList
        self.start = time.time()
        self.deleter(folder_path)
        os.system("cls")
        print(center(rc+Name))
        print(f"{rc}FilesRemoved{res}:{str(len(self.removed))}\n{rc}elapsed{res}:{str(int(time.time())-self.start)}")


    def deleter(self,folder_path:str):
        try:
            for file_or_folder in os.listdir(folder_path):
                try:
                    floder =path.join(folder_path ,file_or_folder)
                    if path.isfile(floder):
                        if path.splitext(floder)[1] == self.filetype:
                            os.remove(floder)
                            self.removed.append(floder)
                    elif path.isdir(floder):
                        try:
                            self.deleter(floder)
                        except Exception as e:
                            writetofile(e)
                            
                except Exception as e:
                            writetofile(e)
        except Exception as e:
                            writetofile(e)

class Scavanger:
    def __init__(self) -> None:
        pass
    
    def comboscavanger(self,folder_path:str) -> list:
        global NewList
        self.start = time.time()
        self.appender(folder_path)
        self.Count = len(BigList)
        self.filenames = FileNames
        self.foldernames = Folder_names 

        for line in BigList:
            try:
                try:
                    line = line.replace(",",":")
                    
                except Exception as e:
                            writetofile(e)

                if len(line.split(":")[0]) < 4 or len(line.split(":")[1]) <4:
                    pass
                
                else:
                    try:
                                line = line.replace(",",":")
                                
                    except Exception as e:
                            writetofile(e)
                    try:
                        line.split(":")[1]
                        NewList.append(line.strip())
                    except Exception as e:
                            writetofile(e)
                        
                        
            except Exception as e:
                            writetofile(e)
                    
            
        NewList = Editor.CLEANER(listt=NewList)
        os.system("cls")
        print(center(rc+Name))
        elapsed = float(time.time()) - float(self.start)  
        print(center(f"{res}[{rc}Scavanged Lines:{res}{self.Count}]\n[{rc}Scavanged Files:{res}{len(list(self.filenames))}]\n[{rc}FilesPerMinute:{res}{int((len(list(self.filenames))/elapsed)*60)}]\n[{rc}FoldersPerMinute:{res}{(int(len(list(self.foldernames))/elapsed)*60)}]\n[{rc}Scavanged Folders:{res}{int(len(list(self.foldernames)))}]\n[{rc}Time Elapsed:{res}{int(elapsed)} Seconds]\n[{rc}Developer:{res}IQTHEGOAT#0310]"))
        input("Press anything to save results")
        namy =  '[Combo - Scavanger - Email-Pass] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        namy2 =  '[Combo - Scavanger - User-Pass] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
        try:
            os.mkdir(os.getcwd()+"\\output")
        except:
            pass
        with open(f"{os.getcwd()}\\output\\{namy2}",'a',encoding="utf-8",errors="ignore")as e:
            with open(f"{os.getcwd()}\\output\\{namy}",'a',encoding="utf-8",errors="ignore")as a:
                for line in NewList:
                    try:
                        r = self.isUser(line)
                        if r[1] == True:
                            e.write(r[0]+"\n")
                        elif r[1] == False:
                            a.write(r[0]+'\n')
                    except:
                        pass
            
        #return BigList
        
    def Sorting(self,file:str,reversed:bool):
        with open(file,"r",encoding='utf-8',errors='ignore')as f:
            lst = f.readlines()
            lst = [s.replace('\n', '') for s in lst]
        if reversed:
            return sorted(lst,key=len,reverse=True)
        else:
            return sorted(lst,key=len,reverse=False)
    
    def appender(self,folder_path:str):
        try:
            for file_or_folder in os.listdir(folder_path):
                try:
                    floder =path.join(folder_path ,file_or_folder)
                    if path.isfile(floder):
                        if path.splitext(floder)[1] == ".txt" or path.splitext(floder)[1] == ".csv":
                            FileNames.append(path.splitext(floder)[0])
                            with open(floder,encoding='utf-8',errors='ignore') as f:
                                my_list = f.readlines()
                                my_list = [s.replace('\n', '') for s in my_list]
                                BigList.extend(my_list)
                    elif path.isdir(floder):
                        try:
                            Folder_names.append(path.splitext(floder)[0])
                            self.appender(floder)
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    
    def isUser(self,input_str:str):
        if ':' not in input_str:
            return None
        split_str = input_str.split(':')
        if '@' in split_str[0]:
            return [input_str, False]
        elif '@' in split_str[1]:
            return [f'{split_str[1]}:{split_str[0]}', False]
        elif split_str[0].isalpha() and split_str[1].isalpha():
            return [input_str, True]
        elif split_str[0].isalpha() and split_str[1].isdigit():
            return [f'{split_str[1]}:{split_str[0]}', True]
        else:
            return None

                

def getcombo(title="FILE"):
    try:
        fileo  = fd.askdirectory()
    except:
            fileo  = None
    return fileo

def getfile(title="FILE"):
    try:
        fileo  = fd.askopenfile(title=title,filetypes=[('Text files', '*.txt')]).name.replace('"','')
    except:
            fileo  = None
    return fileo

def get_hashtype(h):
    h_length = len(h)
    # Try to identify the hash type by looping over all hashlib algorithms
    for algorithm in hashlib.algorithms_guaranteed:
        hash_object = hashlib.new(algorithm)
        if h_length == hash_object.digest_size * 2:
            return algorithm
    return None





while True:
    try:
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("Megatron VER 2.0 Proggramed By:IQTHEGOAT#0310")
        print(rc+Name)
        CLI = f"{res}[{rc}1{res}] File Sorter\n[{rc}2{res}] Scavange Combos From Folder (csv,txt)\n{res}[{rc}3{res}]delete specefic file ext{res}\n[{rc}4{res}]Exit Tool"
        print(center(CLI))
        choice = input(center(f"\n{rc}D{res}ombo{rc}C{res}umper:"))
        scav = Scavanger()
        if int(choice) == 1:
            try:
                rev = input(center(f"\n\nreversed?:[{rc}y{res},{rc}n{res}]:"))
            except:
                rev = input(center(f"\n\nreversed?:[{rc}y{res},{rc}n{res}]:"))
            if rev.lower() == 'y':
                rev = True
            elif rev.lower() == 'n':
                rev = False
            r = scav.Sorting(getfile("File to be Sorted"),rev)
            namy =  '[Item - Sorter] {'+str(datetime.datetime.now())[:-7].replace(':','-')+'}.txt'
            try:
                    os.mkdir(os.getcwd()+"\\output")
            except:
                    pass
            with open(f"{os.getcwd()}\\output\\{namy}",'a',encoding="utf-8",errors="ignore")as a:
                for line in r:
                    a.write(line.strip()+'\n')

        elif int(choice) == 2:
            scav.comboscavanger(getcombo("Folder"))

        elif int(choice) == 3:
            try:
                r = input("what filetype:")
            except:
                r = input("what filetype:")
            deleter = delete(r)
            deleter.filedeleter(getcombo("Main-Folder"))

        elif int(choice) == 4:
            break
    except:
        pass
        
exit()
      