def add_time(start, duration, *optional):
    opt = ""
    for i in optional:
        opt = i

    s = start.split(" ")
    start_hours = s[0].split(":")
    d = duration.split(":")
    print(d)
    if d[0] == "0" and d[1] == "00":
        return start
    
    if s[1] == "AM":
        days = int(d[0])//24
        if days == 0:
            hour = int(start_hours[0]) + int(d[0])
            mint = int(start_hours[1]) + int(d[1])
            if mint >= 60 : 
                hour +=1
                mint = mint - 60
                if hour >= 12:
                    hour = hour -12
                    if mint < 10:
                        print("AM -1")
                        if hour == 0:
                            hour = 12
                            if opt != "":
                                return str(hour) + ":0" + str(mint) + " PM" + ", " + opt
                            else: 
                                return str(hour) + ":0" + str(mint) + " PM"
                        else:
                            if opt != "":
                                return str(hour) + ":0" + str(mint) + " PM" + ", " + opt
                            else: 
                                return str(hour) + ":0" + str(mint) + " PM"
                    else: 
                        print("AM -3")
                        return str(hour) + ":" + str(mint) + " PM"
                elif hour <12:
                    print("AM - 4")
                    if mint < 10:
                        
                        return str(hour) + ":0" + str(mint) + " AM"
                    else: 
                        return str(hour) + ":" + str(mint) + " AM"
        else:
            if int(d[0])%24 == 0:
                hour = int(start_hours[0]) 
            elif int(d[0])%24 != 0:
                 hour = int(start_hours[0]) + int(d[0])%24 
            print(hour)
            mint = int(start_hours[1]) + int(d[1])
            if mint >= 60 : 
                hour +=1
                mint = mint - 60
            
                if hour > 12:
                    hour = hour -12
                    print("AM - 5")
                    if mint < 10:
                        return str(hour) + ":0" + str(mint) + " AM"
                    else: 
                        return str(hour) + ":" + str(mint) + " AM"
                else:
                    print("AM - 6")
                    if mint < 10:
                        return str(hour) + ":0" + str(mint) + " PM"
                    else: 
                        return str(hour) + ":" + str(mint) + " PM"
                    
            else:
                if hour > 12:
                    hour = hour -12
                    print("AM - 7")
                    if mint < 10:
                        return str(hour) + ":0" + str(mint) + " PM"
                    else: 
                        return str(hour) + ":" + str(mint) + " PM"
                else:
                    print("AM - 8", opt)
                    if days == 1 :
                        print("AM - 8a", opt, days)
                  
                        if mint < 10 and opt == "":
                            return str(hour) + ":0" + str(mint) + " AM"   + " (next day)"
                        elif mint >= 10 and opt == "": 
                            return str(hour) + ":" + str(mint) + " AM" + " (next day)"
                        elif mint < 10 and opt != "":
                            return str(hour) + ":0" + str(mint) + " AM"   + " (next day)"
                        elif mint >= 10 and opt != "": 
                            return str(hour) + ":" + str(mint) + " AM," + " Sunday" + " (next day)"
                            
                    else:
                        print("AM - 8b", opt)
                        if mint < 10:
                            return str(hour) + ":0" + str(mint) + " AM"
                        else: 
                            return str(hour) + ":" + str(mint) + " AM"

    elif s[1] == "PM":
       
        days = int(d[0])//24
      
        if days == 0:
            print("aaya")
            hour = int(start_hours[0]) + int(d[0])
            mint = int(start_hours[1]) + int(d[1])
            if mint >= 60 : 
                hour +=1
                mint = mint - 60
                if hour > 12:
                    hour = hour -12
                    print("PM - 1")
                    if mint < 10:
                        return str(hour) + ":0" + str(mint) + " PM" 
                    else: 
                        return str(hour) + ":" + str(mint) + " PM" 
                else:
                    print("PM - 2")
                    if mint < 10:
                        return str(hour) + ":0" + str(mint) + " AM"
                    else: 
                        return str(hour) + ":" + str(mint) + " AM"
                    
            else:
                if hour > 12:
                    hour = hour -12
                    print("PM - 3")
                    if mint < 10:
                        return str(hour) + ":0" + str(mint) + " AM" + " (next day)"
                    else: 
                        return str(hour) + ":" + str(mint) + " AM" + " (next day)"
                else:
                    print("PM - 4")
                    if days == 0 and opt != "":
                        if mint < 10:
                            return str(hour) + ":0" + str(mint) + " PM," + " " + opt
                        else: 
                            return str(hour) + ":" + str(mint) + " PM," + " " + opt
                    else:
                        if mint < 10:
                            return str(hour) + ":0" + str(mint) + " PM"
                        else: 
                            return str(hour) + ":" + str(mint) + " PM"
    
        else:
            if int(d[0])%24 == 0:
                hour = int(start_hours[0]) 
            elif int(d[0])%24 != 0:
                 hour = int(start_hours[0]) + int(d[0])%24 
            print(hour)
            mint = int(start_hours[1]) + int(d[1])
            if mint >= 60 : 
                hour +=1
                mint = mint - 60
                days += 1
                if hour > 12:
                    
                    hour = hour -12
                    print("PM - 5")
                    if mint < 10:
                        return str(hour) + ":0" + str(mint) + " PM"
                    else: 
                        return str(hour) + ":" + str(mint) + " PM"
                else:
                    print("PM - 6")
                    if mint < 10 and opt == "":
                        return str(hour) + ":0" + str(mint) + " AM" + " (" + str(days) + " days later)"
                    elif mint >= 10 and opt == "": 
                        return str(hour) + ":" + str(mint) + " AM"
                    elif mint < 10 and opt != "":
                         return str(hour) + ":0" + str(mint) + " AM," + " Friday" + " (" + str(days) + " days later)"
                    elif mint >= 10 and opt == "": 
                        return str(hour) + ":" + str(mint) + " AM"
                    
            else:
                if hour > 12:
                    days += 1
                    hour = hour -12
                    print("PM - 7:", days, hour, mint, opt)
                    if mint < 10 and opt == "":
                        return str(hour) + ":0" + str(mint) + " AM" + " (" + str(days) + " days later)"
                    elif mint >= 10 and opt == "": 
                        return str(hour) + ":" + str(mint) + " AM" + " (" + str(days) + " days later)"
                    elif mint < 10 and opt != "":
                         return str(hour) + ":0" + str(mint) + " AM," + " Monday" + " (" + str(days) + " days later)"
                    elif mint >= 10 and opt != "": 
                        return str(hour) + ":" + str(mint) + " AM," + " Monday" + " (" + str(days) + " days later)"
                else:
                    print("PM - 8")
                    if mint < 10:
                        return str(hour) + ":0" + str(mint) + " PM"
                    else: 
                        return str(hour) + ":" + str(mint) + " PM"

