from blessed import *
import scripttools as st
import keygen
import communicator as cm
term = Terminal()
"""
print(term.red(" _______           _______  _______  _______  _______  _______  _______"))
print(term.orange("(  ___  )|\     /|(  ____ \(  ____ )(  ____ \(  ___  )(  ____ )(  ____ )"))
print(term.gold("| (   ) || )   ( || (    \/| (    )|| (    \/| (   ) || (    )|| (    )|"))
print(term.chartreuse("| |   | || |   | || (__    | (____)|| |      | |   | || (____)|| (____)|"))
print(term.aqua("| |   | |( (   ) )|  __)   |     __)| |      | |   | ||     __)|  _____)"))
print(term.deepskyblue2("| |   | | \ \_/ / | (      | (\ (   | |      | |   | || (\ (   | (      "))
print(term.purple("| (___) |  \   /  | (____/\| ) \ \__| (____/\| (___) || ) \ \__| )"))
print(term.maroon2("(_______)   \_/   (_______/|/   \__/(_______/(_______)|/   \__/|/\n\n"))
"""
print(term.gold(" _______           _______  _______  _______  _______  _______  _______"))
print(term.gold2("(  ___  )|\     /|(  ____ \(  ____ )(  ____ \(  ___  )(  ____ )(  ____ )"))
print(term.orange("| (   ) || )   ( || (    \/| (    )|| (    \/| (   ) || (    )|| (    )|"))
print(term.maroon1("| |   | || |   | || (__    | (____)|| |      | |   | || (____)|| (____)|"))
print(term.fuchsia("| |   | |( (   ) )|  __)   |     __)| |      | |   | ||     __)|  _____)"))
print(term.violet("| |   | | \ \_/ / | (      | (\ (   | |      | |   | || (\ (   | (      "))
print(term.mediumpurple("| (___) |  \   /  | (____/\| ) \ \__| (____/\| (___) || ) \ \__| )"))
print(term.slateblue("(_______)   \_/   (_______/|/   \__/(_______/(_______)|/   \__/|/\n\n"))
#prits communicator
print(term.seagreen1(" ____                                                                         __                   "))
print(term.aquamarine("/\  _`\                                                   __                 /\ \__                "))
print(term.mediumturquoise("\ \ \/\_\    ___     ___ ___     ___ ___   __  __    ___ /\_\    ___     __  \ \ ,_\   ___   _ __  "))
print(term.cyan2(" \ \ \/_/_  / __`\ /' __` __`\ /' __` __`\/\ \/\ \ /' _ `\/\ \  /'___\ /'__`\ \ \ \/  / __`\/\`'__\ "))
print(term.turquoise3("  \ \ \L\ \/\ \L\ \/\ \/\ \/\ \/\ \/\ \/\ \ \ \_\ \/\ \/\ \ \ \/\ \__//\ \L\.\_\ \ \_/\ \L\ \ \ \/ "))
print(term.turquoise4("   \ \____/\ \____/\ \_\ \_\ \_\ \_\ \_\ \_\ \____/\ \_\ \_\ \_\ \____\ \__/.\_\\\ \__\ \____/\ \_\ "))
print(term.deepskyblue4("    \/___/  \/___/  \/_/\/_/\/_/\/_/\/_/\/_/\/___/  \/_/\/_/\/_/\/____/\/__/\/_/ \/__/\/___/  \/_/ "))
print("\n\n welcome to overcorp communicator!")
while True:#simple menu
    """
    print("please choose an option:")
    print("1. Key generator")
    print("2. Com decoder/encoder")
    rsp=input("$> ")
    """
    rsp = st.Ilist(["question"],["Please choose an option"], [["Key generator","Com decoder/encoder"]])
    if rsp == 0:
        keygen.main()#calls the keygen main class to start generation
    elif rsp == 1:
        cm.start()#start the communicator