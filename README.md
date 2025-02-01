# Intermittent ZeroDivisionError in Python

This repository demonstrates a subtle and uncommon bug in Python related to implicit type coercion and its interaction with exception handling.  The `bug.py` file contains code that will sometimes raise a `ZeroDivisionError` and other times return 0. This occurs due to the order of evaluation and the conditions leading to the potential division by zero.

The `bugSolution.py` file provides a solution that handles the edge case gracefully and prevents the intermittent error.