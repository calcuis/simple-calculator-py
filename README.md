## simple-calculator

The provided Python code uses the Tkinter library to construct a simple graphical user interface (GUI) for a basic calculator application. Upon execution, it creates a window with the title "cal" and dimensions of 185x165 pixels.

The GUI consists of a label widget (label) that displays the current equation and its results. Users can input numbers (0-9) and common arithmetic operators (+, -, *, /) via buttons. Clicking these buttons triggers the `btn_click(number)` function, appending the corresponding digit or operator to the equation displayed in the label.

The "=" button performs the calculation, calling the `calculate()` function. This function uses Python's `eval()` to compute the result from the equation stored in equation_text. It handles syntax errors (`SyntaxError`) and arithmetic error (`ZeroDivisionError`) i.e., division by zero cases, gracefully, displaying appropriate error messages in the label.

The "clear" button resets both the equation and label to empty strings, allowing users to start fresh. Decimal point button is also included for convenience.

Overall, this code offers a basic but functional calculator GUI, enabling users to perform simple arithmetic calculations interactively.
