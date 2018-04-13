TikzBuilder
###########

..  include::   /references.inc
..  vim:ft=rst spell:

TikzBuilder_ is a Python application to build nice (IMHO) diagrams for my
Computer Architecture class. The underlying graphics engine used in this
project is the package TikZ_, part of the LaTeX system. TikZ_ is a powerful,
but complex graphics system capable of building a wide variety of publication
quality graphics images. The package is intended to generate images that are
merged into LaTeX documents. However, this project simply generates a single
PDF image that can be converted into other formats as needed. I routinely
convert them into PNG files to be displayed on the web. Later versions of this
package will create data files that can be included in conventional LaTeX_
documents.

Why TizBuilder?
***************

I began working on building my architecture diagrams using TikZ directly. My
first adventures with the package were a bit difficult, largely because the
capabilities of this package are huge, and they are matched by a documentation
file over 1000 pages in length. As the images got more complex, I found myself
digging deeper into the package, and in the end I was spending too much time
learning about the TikZ_ engine, and getting my diagrams done! (This is a
common problem when exploring new technologies!)

I decided that I knew enough about TikZ to build the images, but creating the
layout I wanted involved adjusting coordinates for a large number of graphics
objects. I needed a way to specify the objects I need to display in a simple
way.

I decided to define the image I want using a Json_ data file. TikzBuilder_
reads this file, then places the graphics components using the data stored in
the data file. The output is a conventional LaTeX_ document that is processed
by ``pdflatex``. The full power of TikZ_ is not exercised in this process, but
it suits my current needs, and TikzBuilder_ a tool that cab be extended if
needed.

Machine Data File
*****************


