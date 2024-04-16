import tkinter as tk
from predict import FIFA_player_predict

def on_entry_click(event, entry_widget, input_text):
    """Function to handle click event on entry widget."""
    if entry_widget.get() == input_text:
        entry_widget.delete(0, tk.END)
        entry_widget.config(fg='black')

def on_focus_out(event, entry_widget, input_text):
    """Function to handle focus out event on entry widget."""
    if entry_widget.get() == '':
        entry_widget.insert(0, input_text)
        entry_widget.config(fg='grey')

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
    player_label.config(text="Player's Name: " + player_name)
    player_label.grid(row=0, column=3, rowspan=3, padx=50, pady=10, sticky="nsew")

# Create window
root = tk.Tk()

root.title("FIFA 21")
root.geometry("500x350+500+200")
root.config(background='#f0f0f0')
root.iconbitmap('.\images\icon_destop.ico')

# Create labels and entry widgets


tk.Label(root, text="PAC:", font=("Arial", 14), bg='#f0f0f0').grid(row=0, column=0, sticky="e", pady=5)
entry_pac = tk.Entry(root, font=("Arial", 12), width=10, fg='grey')
entry_pac.insert(0, 'PAC')
entry_pac.bind('<FocusIn>', lambda event, widget=entry_pac, text='PAC': on_entry_click(event, widget, text))
entry_pac.bind('<FocusOut>', lambda event, widget=entry_pac, text='PAC': on_focus_out(event, widget, text))
entry_pac.grid(row=0, column=1, pady=5)

tk.Label(root, text="SHO:", font=("Arial", 14), bg='#f0f0f0').grid(row=1, column=0, sticky="e", pady=5)
entry_sho = tk.Entry(root, font=("Arial", 12), width=10, fg='grey')
entry_sho.insert(0, 'SHO')
entry_sho.bind('<FocusIn>', lambda event, widget=entry_sho, text='SHO': on_entry_click(event, widget, text))
entry_sho.bind('<FocusOut>', lambda event, widget=entry_sho, text='SHO': on_focus_out(event, widget, text))
entry_sho.grid(row=1, column=1, pady=5)

tk.Label(root, text="PAS:", font=("Arial", 14), bg='#f0f0f0').grid(row=2, column=0, sticky="e", pady=5)
entry_pas = tk.Entry(root, font=("Arial", 12), width=10, fg='grey')
entry_pas.insert(0, 'PAS')
entry_pas.bind('<FocusIn>', lambda event, widget=entry_pas, text='PAS': on_entry_click(event, widget, text))
entry_pas.bind('<FocusOut>', lambda event, widget=entry_pas, text='PAS': on_focus_out(event, widget, text))
entry_pas.grid(row=2, column=1, pady=5)

tk.Label(root, text="DRI :", font=("Arial", 14), bg='#f0f0f0').grid(row=3, column=0, sticky="e", pady=5)
entry_dri = tk.Entry(root, font=("Arial", 12), width=10, fg='grey')
entry_dri.insert(0, 'DRI')
entry_dri.bind('<FocusIn>', lambda event, widget=entry_dri, text='DRI': on_entry_click(event, widget, text))
entry_dri.bind('<FocusOut>', lambda event, widget=entry_dri, text='DRI': on_focus_out(event, widget, text))
entry_dri.grid(row=3, column=1, pady=5)

tk.Label(root, text="DEF:", font=("Arial", 14), bg='#f0f0f0').grid(row=4, column=0, sticky="e", pady=5)
entry_def = tk.Entry(root, font=("Arial", 12), width=10, fg='grey')
entry_def.insert(0, 'DEF')
entry_def.bind('<FocusIn>', lambda event, widget=entry_def, text='DEF': on_entry_click(event, widget, text))
entry_def.bind('<FocusOut>', lambda event, widget=entry_def, text='DEF': on_focus_out(event, widget, text))
entry_def.grid(row=4, column=1, pady=5)

tk.Label(root, text="PHY:", font=("Arial", 14), bg='#f0f0f0').grid(row=5, column=0, sticky="e", pady=5)
entry_phy = tk.Entry(root, font=("Arial", 12), width=10, fg='grey')
entry_phy.insert(0, 'PHY')
entry_phy.bind('<FocusIn>', lambda event, widget=entry_phy, text='PHY': on_entry_click(event, widget, text))
entry_phy.bind('<FocusOut>', lambda event, widget=entry_phy, text='PHY': on_focus_out(event, widget, text))
entry_phy.grid(row=5, column=1, pady=5)

# Create search button
search_button = tk.Button(root, text="Search", font=("Arial", 14), command=search_player, bg='#007bff', fg='white')
search_button.grid(row=6, column=0, columnspan=2, pady=10, padx=5, sticky="ew")

# Create label to show the result
player_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
player_label.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="w")

root.mainloop()
