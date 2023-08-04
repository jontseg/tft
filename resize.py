import os
import PySimpleGUI as sg
from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    image = Image.open(input_path)
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    resized_image.save(output_path)

sg.theme("LightBlue2")

layout = [
    [sg.Text("Folder Path:"), sg.InputText(key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Text("New Width:"), sg.InputText(key="-WIDTH-")],
    [sg.Text("New Height:"), sg.InputText(key="-HEIGHT-")],
    [sg.Button("Resize"), sg.Button("Exit")]
]

window = sg.Window("Image Resizer", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "Resize":
        folder_path = values["-FOLDER-"]
        new_width = int(values["-WIDTH-"])
        new_height = int(values["-HEIGHT-"])

        # Create a new folder for resized images
        output_folder = os.path.join(folder_path, "resized_images")
        os.makedirs(output_folder, exist_ok=True)

        # Process each image in the folder
        for filename in os.listdir(folder_path):
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                input_path = os.path.join(folder_path, filename)
                output_path = os.path.join(output_folder, filename)
                resize_image(input_path, output_path, new_width, new_height)

        sg.popup("Images resized successfully!", title="Success")

window.close()
