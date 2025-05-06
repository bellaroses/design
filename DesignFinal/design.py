from textx import metamodel_from_file
from PIL import Image, ImageDraw, ImageFont

design_mm = metamodel_from_file('/Users/isabellaking/CS Coursework/CS420/Design/DesignFinal/design.tx')

design_model = design_mm.model_from_file('/Users/isabellaking/CS Coursework/CS420/Design/DesignFinal/Sample Programs/BusinessCard.dx')


class Design:
    def HexToRGB(self, hexCode):
        hexCode = hexCode.replace("#", "")
        red = int(hexCode[0:2], 16)
        green = int(hexCode[2:4], 16)
        blue = int(hexCode[4:6], 16)
        return (red, green, blue)
    def designSize(self, type):
        match type:
            case "instagram post":
                return (1080, 1080)
            case "letter paper":
                return (2550, 3300)
            case "business card":
                return (1050, 600)
            case "email signature":
                return (600, 150)
            case default:
                "Error: Incorrect Design Type"

    # ADD COLOR ELEMENT LATER
    def text(self, textElement, draw, color):
        draw.text((textElement.width, textElement.height), textElement.text, color, ImageFont.truetype(textElement.font, textElement.size))
    def image(self, imageElement, canvas):
        image = Image.open(imageElement.file).resize((imageElement.side1, imageElement.side2))
        canvas.paste(image, (imageElement.height, imageElement.width))
    def shape(self, shapeElement, draw, color):
        if (shapeElement.type[1] == "rectangle"):
            draw.rectangle((shapeElement.width1,shapeElement.height1,shapeElement.width2,shapeElement.height2), fill=color)
        elif (shapeElement.type[1] == "rounded rectangle"):
            draw.rounded_rectangle((shapeElement.width1,shapeElement.height1,shapeElement.width2,shapeElement.height2), fill=color, radius=50)
        else:
            print(f"Error: Invalid shape type: {shapeElement.type}")
    
    def interpret(self, model):
        #HEADER
        designName = model.template.designName
        designType = self.designSize(model.template.designType)

        #Making the Canvas
        background_color = self.HexToRGB(model.template.background)
        canvas = Image.new("RGB", designType, background_color)
        draw = ImageDraw.Draw(canvas)

        #Element Creation Order
        layers = {}
        for w in model.template.layers:
                layers[w.layerNumber] = w.itemsInLayer
        order = list(layers.keys())
        order.sort()
        layers = {i: layers[i] for i in order}
        order = []
        for w in layers.values():
            for x in w:
                order.append(x)

        #Organize Colors
        colors = {}
        for w in model.template.groups:
            for x in w.itemsInGroup:
                colors[x] = self.HexToRGB(w.hexCode)

        # Orignial Element order
        elements = {}
        count = 0
        for w in model.template.elements:
            elements[w.label] = count
            count += 1
        

        #Add Elements in Layers
        for w in order:
            for x in elements.keys():
                if w == x:
                    index = elements[x]
                    color = ""
                    for y in colors:
                        if model.template.elements[index].label == y:
                            color = y
                    if model.template.elements[index].type == "text":
                        self.text(model.template.elements[index], draw, colors[color])
                    elif model.template.elements[index].type == "image":
                        self.image(model.template.elements[index], canvas)
                    else:
                        self.shape(model.template.elements[index], draw, colors[color])
        

        for c in model.commands:
            if c.__class__.__name__ == "PEEK":
                canvas.show()
            elif c.__class__.__name__ == "EXPORT":
                match c.file:
                    case "png":
                        file = model.template.designName + ".png"
                        canvas.save(file)
                    case "pdf":
                        file = model.template.designName + ".pdf"
                        canvas.save(file)
                    case "jpg":
                        file = model.template.designName + ".jpg"
                        canvas.save(file)
                    case default:
                        print("ERROR: Invalid file type. Please type \"png\", \"pdf\", or \"jpg\".")
            else:
                print("ERROR: Invalid Command")


            


design = Design()
design.interpret(design_model)