import customtkinter
import page.default_graph as pd


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title('Optimochrone')
app.resizable(False, False)

# instance the default graph page
default_graph_frame = pd.default_graph(app) 

default_graph_frame.pack()

app.mainloop()