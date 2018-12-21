# ////////////////////////////////  DESCRIPTION  /////////////////////////////////#
#                                                                                 #
#     The file defines a method that cleans the terminal screen for better        #
#     formatting.       									                      #
#                                                                                 #
#/////////////////////////////////////////////////////////////////////////////////#


from os import system, name

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')