import tkinter as tk
from predict import FIFA_player_predict 
import ctypes
 
def search_player():
    # get values from entry widgets
    pac = int(entry_pac.get())
    sho = int(entry_sho.get())
    pas = int(entry_pas.get())
    dri = int(entry_dri.get())
    defend = int(entry_def.get())
    phy = int(entry_phy.get())

    player_name = FIFA_player_predict(pac, sho, pas, dri, defend, phy)
    
    # Update label with player's name
    player_label.config(text="Player's Name: " + str(player_name))
    player_label.grid(row=0, column=3, rowspan=3, padx=50, pady=10, sticky="nsew")

# Create window
root = tk.Tk()

# Change the taskbar icon, app icon, title and size of the window
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
root.title("FIFA 21")
root.geometry("500x350+500+200")
root.config(background='#f0f0f0')
root.iconbitmap('.\images\icon_destop.ico')

# Create labels and entry widgets
tk.Label(root, text="PAC:", font=("Arial", 14), bg='#f0f0f0').grid(row=0, column=0, sticky="e", pady=5)
entry_pac = tk.Entry(root, font=("Arial", 12), width=10)
entry_pac.grid(row=0, column=1, pady=5)

tk.Label(root, text="SHO:", font=("Arial", 14), bg='#f0f0f0').grid(row=1, column=0, sticky="e", pady=5)
entry_sho = tk.Entry(root, font=("Arial", 12), width=10)
entry_sho.grid(row=1, column=1, pady=5)

tk.Label(root, text="PAS:", font=("Arial", 14), bg='#f0f0f0').grid(row=2, column=0, sticky="e", pady=5)
entry_pas = tk.Entry(root, font=("Arial", 12), width=10)
entry_pas.grid(row=2, column=1, pady=5)

tk.Label(root, text="DRI :", font=("Arial", 14), bg='#f0f0f0').grid(row=3, column=0, sticky="e", pady=5)
entry_dri = tk.Entry(root, font=("Arial", 12), width=10)
entry_dri.grid(row=3, column=1, pady=5)

tk.Label(root, text="DEF:", font=("Arial", 14), bg='#f0f0f0').grid(row=4, column=0, sticky="e", pady=5)
entry_def = tk.Entry(root, font=("Arial", 12), width=10)
entry_def.grid(row=4, column=1, pady=5)

tk.Label(root, text="PHY:", font=("Arial", 14), bg='#f0f0f0').grid(row=5, column=0, sticky="e", pady=5)
entry_phy = tk.Entry(root, font=("Arial", 12), width=10)
entry_phy.grid(row=5, column=1, pady=5)

# Create search button
search_button = tk.Button(root, text="Search", font=("Arial", 14), command=search_player, bg='#007bff', fg='white')
search_button.grid(row=6, column=0, columnspan=2, pady=10, padx=5, sticky="ew")

# Create label to show the result
player_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
player_label.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="w")

root.mainloop()

