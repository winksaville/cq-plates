import cadquery as cq # type: ignore

bw = 200  # bead width
nd = 0.4  # Nozzle Diameter
mt = 0.05 # minimum thickness
dt = 0.05 # delta thickness
length = 50
width  = 20
gap = 5
count = bw / (width + gap)
plates = []

for i in range(0, int(count)):
    p = (
        cq.Workplane("XY", origin=(((i * (width + gap)) - (bw / 2)), 0, 0))
        .rect(width, length)
        .extrude(mt+(i*dt))
    )
    plates.append(p.val())

# Combine the objects so they all can be slected and exported to stl
all = cq.Compound.makeCompound(plates)
show_object(all)
