import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image, ImageTk  # Importar Pillow para manejar la imagen

#We create an object of Tk class
window = tk.Tk()

#Size 2
Wide = 700
Height = 400
Size = str(Wide) + "x" + str(Height)
window.geometry(Size)

#Title
window.title('Scroll + Combo')
#Icon
window.iconbitmap('./Img/Crown.ico')

#Scrolled text
text = """La tecnología ha revolucionado innumerables aspectos de la vida cotidiana, y uno de los ámbitos en los que su impacto ha sido más evidente es la educación. Desde la introducción de herramientas digitales hasta el desarrollo de plataformas de aprendizaje en línea, 
el entorno educativo ha experimentado un cambio profundo que continúa evolucionando a pasos agigantados. Este fenómeno ha transformado no solo la manera en que los estudiantes acceden al conocimiento, 
sino también cómo se imparte, cómo se mide el rendimiento y cómo se concibe la educación misma.

Uno de los primeros hitos significativos en la evolución de la educación tecnológica fue la llegada de las computadoras a las aulas. En las décadas de 1980 y 1990, los centros educativos comenzaron a integrar computadoras personales en el proceso de enseñanza, 
lo que permitió a los estudiantes acceder a nuevos tipos de información, explorar programas interactivos y desarrollar habilidades tecnológicas que se volvieron esenciales en el mundo laboral. 
No obstante, la presencia de computadoras en las escuelas fue solo el comienzo de una transformación mucho más amplia.
El acceso a Internet y el posterior auge de las plataformas de aprendizaje en línea marcaron un nuevo capítulo en esta evolución. 

Internet abrió las puertas a un vasto universo de conocimientos, permitiendo a los estudiantes acceder a recursos educativos desde cualquier lugar y en cualquier momento. Esto cambió fundamentalmente el paradigma de la enseñanza, 
alejándose del modelo tradicional en el que el profesor era el guardián del conocimiento, hacia un enfoque en el que los estudiantes podían explorar el aprendizaje de manera autónoma. Con el tiempo, surgieron plataformas educativas en línea, como Coursera, 
edX, Khan Academy y muchas otras, que ofrecieron cursos en una amplia variedad de disciplinas, accesibles para cualquier persona con una conexión a Internet."""
scroll = scrolledtext.ScrolledText(window, width=60, height=15, wrap=tk.WORD)
scroll.insert(tk.INSERT, text)
scroll.grid(row=1,column=1)


#Combo box
data = [x*3 for x in range(20)]
combobox = ttk.Combobox(window, width=15, value=data)
combobox.grid(row=5, column=1, padx=15, pady=15)
combobox.current(3)
print(f'Showing the value of the combo to window start {combobox.get()}')

#Image on the button

#Cargar imagen con Pillow
img = Image.open('./Img/Homero.png')
image_tk = ImageTk.PhotoImage(img)
button = ttk.Button(window, image=image_tk)
button.grid(row=6, column=1)

# Evitar que la imagen sea recolectada por el Garbage Collector
button.image = image_tk


#Always put at the end
window.mainloop()