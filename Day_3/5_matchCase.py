color=input("enter the color:")

match color :
    case "green":
        print("GO")
    case "Yellow":
        print("Look")
    case "Red":
        print("stop !")
    case _:
        print("Invalid Color")
