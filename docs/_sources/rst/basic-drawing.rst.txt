Basic Shape Drawing
*******************

A basic shape is defined using three lists:

    * points - the polygon to be drawn

    * pins - the shape coordinates (on the polygon) where basic pins are added

    * pins_t - same as above for "tall pins" on top/bottom of sloped shapes

These lists are drawn inside of a ``scope`` so they can all be shifted to some
specific coordinate.

The basic drawing scheme looks like this:

.   code-block:: python

    def draw(self)
        tex = []
        # draw pins first
        for p in range(len(self.pins)):
            if p == 0:
                tex.extend(

Drawing Pins
************

Although this is not typically seen in CPU diagrams, to assist in building our
simulator, we will show numbered pins on all parts. Eventually, these pins will
be colored to indicate input and output signal connections. We will not dela
with bi-directional signals at this time.

Pins are small numbered blocks on the side of each art. There ar two styles of
pins:

    * normal square pins for horizontal and vertical sides

    * "tall" pins that will be used on sloped shape sides

Pins are drawn first, then the shape ploygon is drawn. The polygon fill will
cover part of the tall pins to give a nuce look.

As part of the pin drawingprocess, the attach points are determined and
returned to be used when attaching wires to pins. Each pin has fourpossible
attach points, and side indicators are used to determine where the attach point
is, and how to shift the pin so it attaches to the shape side. For tall pins
the shift indicator is used to adjust the placement of the pin number.





    
