# 🎨 Hirst Dot Painting - Python Turtle Project  

## 📌 **Overview**  
This project is a **Python-based Turtle Graphics program** that generates a colorful **Hirst Dot Painting** using the `turtle` module. Inspired by **Damien Hirst’s dot paintings**, the script creates **100 randomly colored dots** arranged in a **10x10 grid**. The colors are selected from a predefined list, ensuring a visually appealing pattern.

## 🚀 **Features**  
✅ Generates a **grid of 100 dots** (10x10 format)  
✅ Uses **random colors** from a predefined color palette  
✅ **Turtle Graphics** ensures smooth rendering  
✅ **Fast execution** using `speed("fastest")`  
✅ Automatically closes the window on click  

## 🔧 **Technologies Used**  
- 🐍 **Python** (Core language)  
- 🖌️ **Turtle Graphics** (For drawing dots)  
- 🎲 **Random Module** (To randomly pick colors)  

## 🛠 **How the Code Works**  
1️⃣ **Set Up Turtle** → A turtle (`timmy`) is created with `penup()` to avoid unwanted lines.  
2️⃣ **Positioning the Turtle** → Moves to the starting point using `setheading()` and `forward()`.  
3️⃣ **Generating Dots** → Loops 100 times to create dots using `dot(size, color)`.  
4️⃣ **Row Shifting Logic** → Moves to the next row after every 10 dots.  
5️⃣ **Screen Exit** → The program waits for a user click to close the window.  

## 📌 **Python Concepts Used**  
✔ **Turtle Graphics** → For drawing and movement  
✔ **Loops (`for` loop)** → To generate multiple dots  
✔ **Functions (`random.choice()`)** → For selecting random colors  
✔ **Conditional Statements (`if` statement)** → To shift rows after every 10 dots  
✔ **Color Modes (`colormode(255)`)** → To support RGB colors  

## 🎨 **Preview of Output**  
The program generates a **grid of colorful dots**, mimicking a **Hirst painting**. The result is an abstract, artistic pattern! 🎨✨  

---

📌 **Feel free to fork the repo and experiment with different grid sizes, colors, and dot spacing!** 🚀

# 📜 **Code Explanation - Hirst Dot Painting (Python Turtle Graphics)**  

This project uses **Python's Turtle Graphics** to create a **Hirst-style dot painting**. If you're new to Python and Turtle, don't worry! I'll break down the code in a simple way so you can understand every step.  

---

## 🖥 **Step-by-Step Code Explanation**  

### 📌 **1. Importing Required Modules**  
```python
import turtle as turtle_module
import random  
```
- We import **turtle** (renaming it as `turtle_module` for clarity) to create graphics.  
- We also import **random** to pick random colors from a predefined color list.  

---

### 🎨 **2. Defining the Color Palette**  
```python
color_list = [(242, 243, 245), (230, 228, 224), (236, 241, 238), (241, 236, 240), (198, 159, 116), (70, 92, 129),
              (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), 
              (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), 
              (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), 
              (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8), 
              (181, 186, 213), (46, 72, 57), (168, 201, 212), (100, 137, 144)]
```
- This **list of tuples** contains **RGB color values** (Red, Green, Blue).  
- Each color is randomly picked to create a unique painting.  

---

### 🐢 **3. Setting Up the Turtle**  
```python
turtle_module.colormode(255)  # Enables RGB color mode (0-255)
timmy = turtle_module.Turtle()  # Create a turtle object named 'timmy'
timmy.speed("fastest")  # Set the speed to the fastest for quick drawing
timmy.penup()  # Lifts the pen to avoid drawing unnecessary lines
timmy.hideturtle()  # Hides the turtle cursor to keep the screen clean
```
- **`colormode(255)`** → Allows us to use RGB colors instead of predefined turtle colors.  
- **Creating the Turtle (`Turtle()`)** → The turtle (Timmy) will draw the dots.  
- **Setting Speed (`speed("fastest")`)** → Increases speed for instant drawing.  
- **Using `penup()`** → Ensures the turtle doesn’t draw lines when moving.  
- **`hideturtle()`** → Hides the turtle cursor for a clean output.  

---

### 📍 **4. Positioning the Turtle at the Starting Point**  
```python
timmy.setheading(225)  # Turn 225 degrees to move to the starting position
timmy.forward(300)  # Move back to start drawing from bottom left
timmy.setheading(0)  # Reset direction to face right
```
- Since the turtle starts in the center, we move it **down and left** to start drawing from the **bottom-left corner**.  
- Then, we **reset the direction to right** (so the turtle can move correctly in a grid pattern).  

---

### 🔄 **5. Creating the Dot Grid**  
```python
number_of_dots = 100  # Total dots (10 rows x 10 columns)

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(30, random.choice(color_list))  # Draw a dot with a random color
    timmy.forward(50)  # Move forward to place the next dot

    if dot_count % 10 == 0:  # After every 10 dots (1 full row), move up to the next row
        timmy.setheading(90)  # Turn to face upwards
        timmy.forward(50)  # Move up by 50 pixels
        timmy.setheading(180)  # Turn left
        timmy.forward(500)  # Move left to the start of the next row
        timmy.setheading(0)  # Reset direction to right
```
### 🔹 **How the Loop Works**  
1️⃣ **Loop runs 100 times** → Because we need **10 rows × 10 columns** (100 dots).  
2️⃣ **`timmy.dot(30, random.choice(color_list))`** → Creates a **30-pixel** dot in a **random color**.  
3️⃣ **`timmy.forward(50)`** → Moves **right** by **50 pixels** to leave space for the next dot.  
4️⃣ **New Row Logic**:  
   - Every **10th dot**, the turtle moves **up** (`90 degrees`)  
   - Moves **left** (`180 degrees`) by 500 pixels to align at the **next row’s starting point**  
   - Faces **right (`0 degrees`)** again for the next row  

---

### 🖥 **6. Keeping the Window Open**  
```python
screen = turtle_module.Screen()  # Get the screen object
screen.exitonclick()  # Waits for a click to close the window
```
- Without this, the window would **close immediately** after drawing the dots.  
- **`exitonclick()`** waits for a **mouse click** before closing the program.  

---

## 🔥 **Python Concepts Used in This Code**  
✅ **Turtle Graphics** → Used to create and position the turtle, draw dots, and move in a grid.  
✅ **Loops (`for` loop)** → Automates the process of drawing 100 dots.  
✅ **Random Module (`random.choice()`)** → Selects colors randomly from the predefined color list.  
✅ **Conditional Statements (`if` statement)** → Handles movement logic for new rows.  
✅ **Tuple & List Handling** → Stores and retrieves RGB color values efficiently.  

---

## 🏁 **Final Thoughts**  
This project is a **great way for beginners to learn Python, loops, and Turtle Graphics**! 🐢  
By modifying the **dot size, spacing, or color palette**, you can create **different artistic patterns**! 🎨  

---

📌 **Want to make it better?**  
- Try changing **dot size** (increase/decrease `timmy.dot(30, color)`).  
- Adjust **grid size** by modifying `number_of_dots`.  
- Experiment with **different colors** in `color_list`.  

---

## 🎯 **Conclusion**  
This **Hirst Dot Painting** Python project is a **fun and creative way to practice Python programming**!  
It teaches **loops, conditional statements, the Turtle module, and RGB colors** while making beautiful artwork!  

👉 **Fork the repo and try modifying it to create your own unique dot painting!** 🚀
