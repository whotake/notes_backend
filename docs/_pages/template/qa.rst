.. _qa:

QA
==

We try to keep our quality standards high. So, we use different tools to make this possible.

First of all, we use `mypy <http://mypy-lang.org/>`_ for optional static typing.

We are also using `radon <https://github.com/rubik/radon>`_ and `xenon <https://github.com/rubik/xenon>`_ to measure code complexity and quality.


mypy
----

Running ``mypy`` is required before any commit:

.. code:: bash

    python -m mypy server

This will eliminate a lot of possible ``TypeError``s and other issues.
However, this will not make code 100% working. So, testing and reviewing is still required.

``mypy`` is configured via ``setup.cfg``.


Rules
-----

Here are our standards:

- A single block of code can not go below ``B`` mark
- A single module can not go below ``A`` mark
- Overall mark can not go below ``A`` mark

If your commit breaks this rule: well, the build won't succeed.


Running code analysis
---------------------

There are several metrics we use.

Cyclomatic Comlexity:

.. code:: bash

  radon cc . -a

Maintainability Index:

.. code:: bash

  radon mi .

And at last raw metrics:

.. code:: bash

  radon raw .


Running validation
------------------

If you would like to run QA by hand:

.. code:: bash

  xenon --max-absolute B --max-modules A --max-average A .

It will return status code ``0`` if everything is fine.
