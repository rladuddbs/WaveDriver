
world = []

def update():
    for o in world:
        o.update()
def render():
    for o in world:
        o.draw()

def add_object(o):
    world.append(o)

def remove_object(o):
    for o in world:
        o.remove(o)
        return
