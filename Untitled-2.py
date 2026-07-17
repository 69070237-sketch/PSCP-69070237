"""Color"""

color = input()
color2 = input()

mix = (color , color2)

if mix == ("Red" , "Yellow"):
    print("Orange")
elif mix == ("Red","Blue"):
    print("Violet")
elif mix == ("Yellow","Blue"):
    print("Green")
elif mix == ("Red","Red"):
    print("Red")
elif mix == ("Yellow","Yellow"):
    print("Yellow")
elif mix == ("Blue","Blue"):
    print("Blue")
elif mix == ("Blue","Red"):
    print("Violet")
elif mix == ("Yellow","Red"):
    print("Orange")
elif mix == ("Blue","Yellow"):
    print("Green")
else:
    print("Error")
