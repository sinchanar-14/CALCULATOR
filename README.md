# CALCULATOR

*COMPANY NAME*:MIRCO IT

*NAME*:SINCHANA R

*DOMAIN*:SOFTWARE DEVELOPER

*DURATION*: 4 WEEKS

The provided code implements a Premium Scientific Calculator using Python's Tkinter library, which is a standard GUI toolkit for creating desktop applications. The calculator is designed to perform both basic arithmetic and advanced scientific calculations, making it suitable for a wide range of users, from students to professionals.

### Key Components:

1. **Class Structure**: The `CalculatorApp` class encapsulates all functionalities and UI elements of the calculator. This object-oriented approach promotes modularity and ease of maintenance.

2. **User  Interface (UI)**: The UI is constructed using a grid layout, which organizes buttons and input fields neatly. The main components include:
   - An entry field for displaying input and results, styled with a large font for better visibility.
   - A toggle button for switching between dark and light themes, enhancing user experience based on preferences or lighting conditions.
   - A grid of buttons representing various mathematical functions, including trigonometric functions (sin, cos, tan), square root, logarithm, exponentiation, and basic arithmetic operations (addition, subtraction, multiplication, division).

3. **Button Functionality**: Each button is linked to a command that processes user input:
   - The equals button (`=`) evaluates the expression entered in the input field using Python's `eval` function, while ensuring safety by restricting access to built-in functions.
   - The clear button (`C`) resets the input field, and the backspace button (`⌫`) removes the last character.
   - Scientific functions are executed by converting the input to a float and applying the corresponding mathematical function from the `math` module. Error handling is implemented to manage invalid inputs, such as attempting to calculate the square root or logarithm of a negative number.

4. **Theme Management**: The calculator supports two themes—dark and light. The `apply_theme` method adjusts the background and foreground colors of the UI elements based on the selected theme, providing a visually appealing experience.

5. **Error Handling**: The application includes robust error handling to manage common issues, such as division by zero and invalid mathematical operations. When an error occurs, the calculator displays an appropriate message in the input field, guiding the user to correct their input.

6. **Execution**: The application is initiated in the `if __name__ == "__main__":` block, where a Tkinter root window is created, and the `CalculatorApp` class is instantiated. The window size is set to 400x550 pixels, providing ample space for the UI components.

### Conclusion:

Overall, this Premium Scientific Calculator is a well-structured and functional application that combines essential mathematical operations with advanced scientific capabilities. Its user-friendly interface, theme options, and error handling make it a versatile tool for anyone needing to perform calculations efficiently. The use of Tkinter ensures that the application is lightweight and easy to run on various platforms, making it accessible to a broad audience.

*OUTPUT*:<img width="290" alt="Image" src="https://github.com/user-attachments/assets/de7ad5a9-05ac-45f1-9a9c-f7b58cb1287b" />
