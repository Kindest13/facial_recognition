def getColor(percentage):
    color = None
    
    if percentage > 60:
        color = (5, 185, 5)
    elif percentage > 40:
        color = (255, 0, 140)
    else:
        color = (185, 5, 5)

    return color
    