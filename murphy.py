from rocket import Rocket

rocket = Rocket('Murphy', 'Mark Williams')

print("This rocket is called " + rocket.name +
      ", and is owned by " + rocket.owner)

rocket.arm()
rocket.disarm()
rocket.launch()
