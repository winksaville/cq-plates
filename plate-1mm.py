import cadquery as cq # type: ignore

length = 90
width = 30
thickness = 1 
w = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(thickness)
)
show_object(w)
