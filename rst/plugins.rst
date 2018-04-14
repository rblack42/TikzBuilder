TikzBuilder Plugins
###################

:Ref: http://drunkenpython.org/tag/dispatcher.html

To make it easy to add new shaped to this tool, the individual shapes are
defined in a class with an associated handler that can be dropped into a single
``shapes`` directory. Here is an example program that uses this idea (adapter
from the reference above):

..  literalinclude::    code/test_plugins.py
    :linenos:
    :caption: test_plugins.py

To run this code, we create a ``shapes`` folder with this ``__init-_.py`` file:

..  literalinclude::    code/shapes/__init__.py
    :linenos:
    :caption: shapes/__init__.py

The magic in this file just populated the ``__all__ list with the names of all
Python files ending with ``.py``. Importing this package gives access to all
such files.

Here are the class files for each shape:

..  literalinclude::    code/shapes/ALu.py
    :linenos:
    :caption: shapes/ALU.py

..  literalinclude::    code/shapes/REG.py
    :linenos:
    :caption: shapes/REG.py

Here is an example of running this code

..  command-output::    python3 test_plugins.py ALU alu
    :cwd:   code

..  command-output::    python3 test_plugins.py REG pc
    :cwd:   code

