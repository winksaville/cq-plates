import cadquery as cq # type: ignore

nd = 0.4  # Nozzle Diameter
length = 50
width  = 20
gap = 5

p1 = (
    cq.Workplane("XY", origin=(-(width + gap), 0, 0))
    .rect(width, length)
    .extrude(nd/2)
)
#show_object(p1)

p2 = (
    cq.Workplane("XY", origin=(0, 0, 0))
    .rect(width, length)
    .extrude(nd)
)
#show_object(p2)

p3 = (
    cq.Workplane("XY", origin=(width + gap, 0, 0))
    .rect(width, length)
    .extrude(nd * 2)
)
#show_object(p3)


# Combine the objects so they all can be slected and exported to stl
#
# Note: you must use .val() otherwise the following generates
#       a "AttributeError: 'Workplane' object has no 'wapped'"
#   all = cq.Compound.makeCompound([p1, p2, p3])
all = cq.Compound.makeCompound([p1.val(), p2.val(), p3.val()])
show_object(all)
