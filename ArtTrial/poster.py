from PIL import Image, ImageDraw, ImageFont
import cairo

poster = Image.new("RGB", (2550, 3300), (16, 33, 82))
draw = ImageDraw.Draw(poster)
arial = ImageFont.truetype("/Users/isabellaking/Downloads/arial/ARIAL.TTF", 300)
draw.text((300,500), "Join the ACM!", "white", font=arial)
draw.rectangle((0,2600,2550,3300), fill=(153, 209, 255))
draw.rectangle((0,3000,2550,3300), fill=(71, 137, 191))
logo = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/ArtTrial/ACMLogo.png")
logo = logo.resize((200,200))
poster.paste(logo, (100, 3100))
poster.show()