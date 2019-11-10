from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Go Case DIP Challenge")

        # Declaring the variables that will be used
        self.name= StringVar()
        self.size= IntVar()
        self.coord_x= IntVar()
        self.coord_y= IntVar()

        # Creating labels to guide the user
        self.img_label = ttk.LabelFrame(self, text="Escolha a imagem")
        self.font_label = ttk.LabelFrame(self, text="Escolha a fonte")
        self.name_label = ttk.LabelFrame(self, text="Escolha o nome")
        self.coord_x_label = ttk.LabelFrame(self, text="Coordenada X")
        self.coord_y_label = ttk.LabelFrame(self, text="Coordenada Y")
        self.size_label = ttk.LabelFrame(self, text="Tamanho da fonte")
        self.save_label= ttk.LabelFrame(self, text="Salve o mockup")

        # Setting all the label's positions inside the grid
        self.img_label.grid(column=0, row=1, padx=20, pady=20)
        self.font_label.grid(column=0, row=2, padx=20, pady=20)
        self.name_label.grid(column=0, row=3, padx=20, pady=20)
        self.coord_x_label.grid(column=0, row=4, padx=20, pady=20)
        self.coord_y_label.grid(column=1, row=4, padx=20, pady=20)
        self.size_label.grid(column=0, row=5, padx=20, pady=20)
        self.save_label.grid(column=0, row=6, padx=20,pady=20)

        # Calling the function that creates the input buttons/entries
        self.inputs()

    # Generating all the buttons and text/number entries
    def inputs(self):
        self.btn_img = ttk.Button(self.img_label, text="procure o arquivo", command=self.choose_image)
        self.btn_img.grid(column=1, row=1)

        self.btn_font= ttk.Button(self.font_label, text="procure o arquivo", command= self.choose_font)
        self.btn_font.grid(column=1, row=2)

        self.entry_name = Entry(self.name_label, textvariable=self.name)
        self.entry_name.grid(column=1, row=3)

        self.entry_size = Entry(self.size_label, textvariable=self.size)
        self.entry_size.grid(column=1, row=4)

        self.entry_coord_x = Entry(self.coord_x_label, textvariable=self.coord_x)
        self.entry_coord_x.grid(column=1, row=5)

        self.entry_coord_y = Entry(self.coord_y_label, textvariable=self.coord_y)
        self.entry_coord_y.grid(column=2, row=5)

        self.btn_save= ttk.Button(self.save_label, text="salvar", command= self.generate_mockup)
        self.btn_save.grid(column=1, row=6)

    # Getting the image path through a file picker
    def choose_image(self):
        self.img_path = filedialog.askopenfilename(initialdir="./mockups", title="Select a file",
                                                   filetypes=(("jpg files", "*.jpg"),("jpg files", "*.jpeg")))
        self.label = ttk.Label(self.img_label, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.img_path)

    # Getting the font path through a file picker
    def choose_font(self):
        self.font_path = filedialog.askopenfilename(initialdir="./fonts", title="Select a font",
                                               filetypes=(("ttf files", "*.ttf"), ("all files", "*.*")))
        self.label = ttk.Label(self.font_label, text="")
        self.label.grid(column=1, row=3)
        self.label.configure(text=self.font_path)

    # Saving the final mockup
    def generate_mockup(self):
        # Reading and opening the base mockup image
        self.base = Image.open(self.img_path).convert('RGBA')

        # Creating a blank image for the text, initialized to transparent text color
        self.txt = Image.new('RGBA', self.base.size, (255, 255, 255, 0))

        # Getting the font using both the size and font path already setted
        self.font = ImageFont.truetype(self.font_path, self.size.get())

        # Getting a drawing context on the 'txt' blank image
        self.d = ImageDraw.Draw(self.txt)

        # Drawing the text with the coordinate and name inputs
        self.d.text((self.coord_x.get(), self.coord_y.get()), self.name.get(), font=self.font, fill=(255, 255, 255, 255))

        # Joining both images in one
        out = Image.alpha_composite(self.base, self.txt)

        # Showing the output
        out.show()

        # Saving the output
        out.save('mockup.jpg')

# Running the Root GUI App
if __name__ == '__main__':
    root = Root()
    root.mainloop()
