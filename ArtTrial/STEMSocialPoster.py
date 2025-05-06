from PIL import Image, ImageDraw, ImageFont

#creates poster
poster = Image.new("RGB", (2550, 3300), (231, 246, 255))

#allows you to draw on the canvas
draw = ImageDraw.Draw(poster)

#TEXT

#adds a font and size
title = ImageFont.truetype("/Users/isabellaking/CS Coursework/CS420/Design/Fonts/arial/ARIAL.TTF", 500)

#creates text
draw.text((600,100), "STEM", (166, 29, 46), font=title)
draw.text((400,500), "SOCIAL", (13, 58, 118), font=title)


draw.rounded_rectangle((380, 2260, 2200, 2600), fill=(13, 58, 118), radius=50)

time = ImageFont.truetype("/Users/isabellaking/CS Coursework/CS420/Design/Fonts/arial/ARIAL.TTF", 120)
draw.text((600,2300), "Wednesday, April 30th", "white", font=time)
draw.text((500,2425), "@ GMCS 405 from 4pm - 6pm", "white", font=time)

hook = ImageFont.truetype("/Users/isabellaking/CS Coursework/CS420/Design/Fonts/arial/ARIALBI.TTF", 100)
draw.text((300,2700), "Join us for a night of exciting networking \nopportunities and delicious refreshments!", (197, 36, 0), font=hook)

icon = (300,300)
computer = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/computer.jpg")
computer = computer.resize(icon)
poster.paste(computer, (250, 100))

pi = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/pi.jpg")
pi = pi.resize(icon)
poster.paste(pi, (2200, 500))

data = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/data.jpg")
data = data.resize(icon)
poster.paste(data, (2100, 100))

math = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/calculator.jpg")
math = math.resize(icon)
poster.paste(math, (100, 500))


draw.rectangle((0,3000,2550,3300), fill=(66, 165, 245))
draw.rectangle((0,3050,2550,3300), fill=(13, 58, 118))


mainGraphic = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/MainGraphic.jpg")
mainGraphic = mainGraphic.resize((1200,1200))
poster.paste(mainGraphic, (700, 1000))


sideGraphic = (550,550)
pizza = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/pizza.jpg")
pizza = pizza.resize(sideGraphic)
poster.paste(pizza, (1900, 1600))

chips = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/chips.jpg")
chips = chips.resize(sideGraphic)
poster.paste(chips, (50, 1100))

cookie = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/cookie.jpg")
cookie = cookie.resize(sideGraphic)
poster.paste(cookie, (0, 1700))

pepsi = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/pepsi.jpg")
pepsi = pepsi.resize(sideGraphic)
poster.paste(pepsi, (2000, 1000))


sdsu = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/SDSU.jpg")
#sdsu = sdsu.crop((0,300,0,300))
sdsu = sdsu.resize((270,270))
sdsu.show
poster.paste(sdsu, (2200, 3050))

acm = Image.open("/Users/isabellaking/CS Coursework/CS420/Design/Images/ACM.jpg")
acm = acm.resize((200,200))
poster.paste(acm, (50, 3075))

acm = ImageFont.truetype("/Users/isabellaking/CS Coursework/CS420/Design/Fonts/arial/ARIALBI.TTF", 60)
draw.text((300, 3115), "Association for \nComputing Machinery", "white", font=acm)


poster.save("image.jpg")