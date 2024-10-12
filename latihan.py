import PySimpleGUI as sg
sg.theme("DarkBlue1")
sg.theme_text_color("#F0FFFF")
window = sg.Window(title="profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25))],
                           [sg.Text("NPM   : 2210010252")],
                           [sg.Text("Nama  : Anarki")],
                           [sg.Text("Kelas  : 5N Reg Pagi BJM")],
                           [sg.Text("Matkul : Pemrograman Visual")],
                           ],
                    size=(500,200),
                    font=("Times",16))
window()
window.close()