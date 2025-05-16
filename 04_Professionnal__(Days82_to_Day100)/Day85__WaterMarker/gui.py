import tkinter as tk
from tkinter import filedialog, messagebox, ttk, colorchooser
from PIL import ImageTk, Image
from watermark import add_text_watermark

class WatermarkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Watermarker")
        self.geometry("600x500")

        self.image_path = None
        self.watermarked = None
        self.font_color = "#FFFFFF"
        self.font_size = tk.IntVar(value=20)

        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(pady=10)

        tk.Button(self.controls_frame, text="Charger une image", command=self.load_image).pack(side=tk.LEFT, padx=5)
        self.entry = tk.Entry(self.controls_frame, width=20)
        self.entry.insert(0, "Votre filigrane")
        self.entry.pack(side=tk.LEFT, padx=5)

        self.position = tk.StringVar(value="bottom_right")
        ttk.Combobox(
            self.controls_frame,
            textvariable=self.position,
            values=["top_left", "top_right", "bottom_left", "bottom_right", "center"],
            width=12
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(self.controls_frame, text="Couleur texte", command=self.choose_color).pack(side=tk.LEFT, padx=5)
        tk.Label(self.controls_frame, text="Taille :").pack(side=tk.LEFT)
        tk.Spinbox(self.controls_frame, from_=10, to=100, textvariable=self.font_size, width=5).pack(side=tk.LEFT, padx=5)

        tk.Button(self.controls_frame, text="Appliquer", command=self.apply_watermark).pack(side=tk.LEFT, padx=5)
        tk.Button(self.controls_frame, text="Enregistrer", command=self.save_image).pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(self, width=500, height=350, bg="gray")
        self.canvas.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg")])
        if file_path:
            self.image_path = file_path
            self.display_image(Image.open(file_path))

    def display_image(self, pil_image):
        pil_image = pil_image.convert("RGB")
        pil_image.thumbnail((500, 350))
        self.tk_image = ImageTk.PhotoImage(pil_image)
        self.canvas.delete("all")
        self.canvas.create_image(250, 175, image=self.tk_image)

    def apply_watermark(self):
        if not self.image_path:
            messagebox.showwarning("Avertissement", "Veuillez d'abord charger une image.")
            return
        self.watermarked = add_text_watermark(
            self.image_path,
            self.entry.get(),
            self.position.get(),
            self.font_color,
            self.font_size.get()
        )
        self.display_image(self.watermarked)

    def save_image(self):
        if self.watermarked:
            path = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
            if path:
                self.watermarked.save(path)
        else:
            messagebox.showinfo("Info", "Aucune image à enregistrer.")

    def choose_color(self):
        color = colorchooser.askcolor(title="Choisissez une couleur")
        if color[1]:
            self.font_color = color[1]
