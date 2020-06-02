import rocket_class

rocket = Rocket("Murphy", "My first attempt at a big-boy rocket",
                "Mark Williams", 1, 0)

print("This rocket is called " + rocket.name +
      ", and is owned by " + rocket.owner)

rocket.arm()
rocket.launch()

print(rocket.launches)
