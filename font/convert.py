import cairosvg
import os

OUTPUT_PATH = "png/"
INPUT_PATH = "svg_export/"

def convert_svg_to_png(svg_path, height):
    print(os.path.splitext(os.path.basename(svg_path)))
    cairosvg.svg2png(url=svg_path, 
                     write_to=OUTPUT_PATH + os.path.splitext(os.path.basename(svg_path))[0] + '.png',
                     output_height=height)

def convert_all_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            convert_svg_to_png(file_path, 60)
            
convert_all_files_in_folder(INPUT_PATH)