import datetime 
def season_events(number_of_month): 
    months = ('January','February','March','April','May','June','July','August','September','October','November','December') 
 
    if number_of_month > 12: 
        return "Month number" 
    elif number_of_month == 12 or number_of_month <= 2: 
        return "You were born in " + months[number_of_month-1] + ", when white snow fell outside the window." 
    elif number_of_month > 2 and number_of_month <= 5: 
        return "You were born in " + months[number_of_month-1] + ", when birds sang beautiful songs." 
    elif number_of_month > 5 and number_of_month <= 8: 
        return "You were born in " + months[number_of_month-1] + ", when the sun shone brighter than ever." 
    else: 
        return "You were born in " + months[number_of_month-1] + ", when the harvest was incredible." 
 
month_number = int(input("Month number: ")) 
print(season_events(month_number)) 
 
