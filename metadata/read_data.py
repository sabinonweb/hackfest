import exif
import pydantic_core

def read_image():
    with open("./lib/lor.jpg", "rb") as image_file:
        image = exif.Image(image_file);
        return image;

def read_geolocation():
    image = read_image()
    if image.has_exif:
        return (image.gps_latitude, image.gps_longitude)
        
def read_model():
    image = read_image()
    if image.has_exif():
        return image.model

def read_metadata():
    image = read_image();
    if image.has_exif:
        image_metadata = image.get_all()
        print("Image Metdata: ", image_metadata)
        return image_metadata

read_metadata()  
