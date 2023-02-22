import random 
class Editor():
    def password_limit(combo:list,limit:int):
        apropriate = []
        for line in combo:
            password = line.split(":")[1]
            if len(password)>=int(limit):
                apropriate.append(line.strip())
        
        return apropriate

    def password_hex(combo:list,hex:list):
        good = []
        for line in combo:
            password = line.split(":")[1]
            for character in password:
                if character in hex:
                    good.append(line.strip())
                    break
                else:
                    pass 
        return good
    
    
    def capture_remover(combo:list):
        newc = []
        for line in combo:
            try:
                user = line.split(":")[0]
                password = str(line.split(":")[1]).split(' ')[0]
                data = user.strip()+":"+password.strip()
                newc.append(data.strip())
            except:
                pass 

        return newc

    def domain_changer(combo:list,dom:str):
        newc = []
        try:
                for line in combo:
                    try:
                        user = line.split("@")[0]
                        password = line.split(":")[1]
                        new = user.strip()+dom.strip()+":"+password.strip()
                        newc.append(new.strip())
                    except:
                        pass
        except:
                pass
        return newc

    def reverser(combo:list):
        newc = []
        try:
                for line in combo:

                        usr = line.split(":")[0]
                        password = line.split(":")[1]
                        reversed=(f"{password.strip()}:{usr.strip()}")
                        newc.append(reversed.strip())
        except:
                pass 

        return newc

    def shuffle(combo:list):
        random.shuffle(combo)
        return combo

    def remove_dupes(combo:list):
        return list(set(list(combo)))

    def CLEANER(listt:list):
        random.shuffle(listt)
        nodupe = list(set(list(listt)))
        newlist = []
        for line in nodupe:
            if line == "" or line == " ":
                pass
            else:
                newlist.append(line.strip())
        return newlist

    def EP_TO_UP(combo:list):
        newcombo = []
        for line in combo:
            try:
                user = line.split("@")[0]
                password= line.split(":")[1]
                new=(f"{user.strip()}:{password.strip()}")
                newcombo.append(new.strip())
            except:
                pass
        return newcombo
        
    def lowercase_pass(combo:list):
        newc=[]
        
        for line in combo:
            password = line.split(":")[1]
            passowrd_low = password.lower()
            line = line.replace(password,passowrd_low)
            newc.append(line)
        return newc

    def upper_password(combo:list):
        newc=[]

        for line in combo:
            password = line.split(":")[1]
            passowrd_upper = password.upper()
            line = line.replace(password,passowrd_upper)
            newc.append(line)
        return newc 

class Extractors():

    def email_extracor(combo:list):
        newc = []
        for line in combo:
            try:
                email = line.split(":")[0]
                newc.append(email.strip())
            except:
                pass
        return newc
    
    def password_extracor(combo:list):
        newc = []
        for line in combo:
            try:
                email = line.split(":")[1]
                newc.append(email.strip())
            except:
                pass
        return newc


class Tools():

    def lq_to_hq(combo:list):
        listt = []
        for line in combo:
                        try:
                                listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"!"+"\n")
                                listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"123"+"\n")
                                listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"1"+"\n")
                                listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip().capitalize()+"\n")
                                listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip()+"!"+"\n")
                                listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip()+"123"+"\n")
                                listt.append(str(line.split(":")[0])+":"+str(line.split(":")[1]).strip()+"1"+"\n")
                                listt.append(line)
                        except:
                            pass


        try:
            random.shuffle(listt)
        except:
            pass
        return listt

    def add_prefix_to_password(combo:list,prefix):
        newc=[]
        for line in combo:
            password = line.split(":")[1]
            passowrd_prefix = str((str(prefix).strip()+str(password).strip())).strip() 
            line = line.replace(password,passowrd_prefix)
            newc.append(line)
        return newc
    
