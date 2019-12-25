
class Line:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    # Presupposes that the line is 2D.
    def svg(self):
         return "<line x1={x1} y1={y1} x2={x2} y2={y2} " \
         "style=\"stroke:rgb(255,0,0);stroke-width:2\" />".format(
            x1=self.a.x, y1=self.a.y, x2=self.b.x, y2=self.b.y
         )
