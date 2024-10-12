import PySimpleGUI as sg
sg.theme("DarkBlue4")
sg.theme_text_color("#F5F5DC")
window = sg.Window(title="profile",
                   layout=[[sg.Text("FTI UNISKA")],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
                           [sg.Text("UNISKA MAB BANJARMASIN")]],
                    size=(500,200),
                    font=("Times",18))
window()
window.close()