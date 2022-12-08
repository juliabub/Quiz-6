#The author's name is Julia Bub
import dbm
photo_category = dbm.open("categories", "c")
# photo_category["singer.png"] = "Taylor Swift performance"
# photo_category["color.png"] = "lavender is purple"
# photo_category["food.png"] = "my favorite food is pasta"

photo_category["singer.png"] = "Harry Styles is writing a song"
photo_category["color.png"] = "the sky is blue"
photo_category["food.png"] = "the ice cream melted"

for item in photo_category:
    print(item, photo_category[item])
