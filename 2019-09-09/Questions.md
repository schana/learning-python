# Questions from last week

1. Division changes between Python 2 and 3

    [PEP 238 -- Changing the Division Operator](https://www.python.org/dev/peps/pep-0238/)
    >The current division (/) operator has an ambiguous meaning for numerical arguments: it returns the floor of the mathematical result of division if the arguments are ints or longs, but it returns a reasonable approximation of the division result if the arguments are floats or complex. This makes expressions expecting float or complex results error-prone when integers are not expected but possible as inputs.

    > We propose to fix this by introducing different operators for different operations: x/y to return a reasonable approximation of the mathematical result of the division ("true division"), x//y to return the floor ("floor division"). We call the current, mixed meaning of x/y "classic division".

1. Float representation

    [Stack Overflow answer](https://stackoverflow.com/a/588014)

    Floating point numbers are stored in the computer as a combination of a **Significand** and an **Exponent**, generally following the [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754-2008_revision) standard.

    For example, `15000` could be represented as 
    >1.5 * 10<sup>4</sup>

    with the significant of 1.5 and the exponent of 4. Some numbers are unable to be represented exactly in this way, such as 1/3 in base 10, or 1/10 in base 2. They have to be approximated, which leaves room for error.

1. Socket programming

    The canonical beginner's guide: [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/html/single/bgnet.html)
