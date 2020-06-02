from rocket import Rocket

rocket = Rocket('Murphy', 'Mark Williams', 1, 'inert')

print("This rocket is called " + rocket.name +
      ", and is owned by " + rocket.owner)

rocket.arm()
rocket.launch()
