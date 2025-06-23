from PIL import Image, ImageDraw, ImageFont

def add_text(im, text, topleft, size, colour):
    font = ImageFont.truetype("./fonts/FiraSans-Regular.ttf", size)
    draw =  ImageDraw.Draw(im)
    draw.multiline_text(topleft, text, font=font, fill = colour)
    return im


if __name__ == '__main__':
    with Image.open("./images./blossom.jpg") as im:
       im = add_text(im, "Hello world\n to see Yaah", (100, 100), 200, (255,255,255))
       im.save("./saved-images/Marina with.jpg")
       
       

    