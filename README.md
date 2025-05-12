# 🎯 Analytical Geometry – Python Turtle Visualization

**CPSC 231 – Introduction to Computer Science I**
**Assignment 1 – Fall 2021**
Author: Ryan Loi

---

## 📝 Project Overview

This assignment involved creating a **graphical Python program** using the `turtle` and `math` libraries to visualize analytical geometry concepts—specifically the intersection of a line and a circle.

The program runs in a graphical window (800x600 pixels), takes **user input**, draws **coordinate axes**, a **circle**, and a **line**, and uses mathematical calculations to **determine and display intersection points**.

---

## 🧩 Program Features

* Renders a **graphical window** using the `turtle` library
* Draws **X and Y axes** centered in the window
* Accepts **7 user inputs** to define:

  * Center of the circle `(xc, yc)`
  * Radius `r`
  * Line start `(x1, y1)` and end `(x2, y2)` coordinates
* Calculates intersection(s) using **analytical geometry and the quadratic formula**
* Draws:

  * The **circle in red**
  * The **line in blue**
  * **Green circles** at each valid intersection
  * A **"No Intersect!"** message if applicable

---

## 📐 Analytical Calculations

Uses the following formulas to determine intersection points:

### Quadratic Parameters:

```python
a = (x2 - x1)^2 + (y2 - y1)^2
b = 2 * ((x1 - xc)(x2 - x1) + (y1 - yc)(y2 - y1))
c = (x1 - xc)^2 + (y1 - yc)^2 - r^2
```

### Quadratic Formula:

```python
alpha = (-b ± sqrt(b^2 - 4ac)) / (2a)
```

### Intersection Coordinates:

```python
x = (1 - alpha) * x1 + alpha * x2
y = (1 - alpha) * y1 + alpha * y2
```

Only intersection points where `0 ≤ alpha ≤ 1` are drawn.

---

## 🔁 Bonus Feature

Includes a **looped mode** where users can:

* Continue entering new line segments
* Draw each line on the same window without clearing previous elements
* Accumulate and print the **total number of intersection points** after each new line

---

## ⚙️ Functionality Overview

### ✅ Key Programming Concepts Applied

| Concept               | Description                                                             |
| --------------------- | ----------------------------------------------------------------------- |
| **Constants**         | Used for window size, axis position, etc. to avoid magic numbers        |
| **User Input**        | 7 values are cast to proper types using `input()` and `int()`/`float()` |
| **Turtle Graphics**   | Used to draw the coordinate system, circle, line, and intersection dots |
| **Math Library**      | Used for power and square root operations                               |
| **Conditional Logic** | Used to determine the number of intersection points                     |
| **Quadratic Solving** | Applied to find intersection locations based on geometric principles    |
| **Looping (Bonus)**   | Allows user to add more lines interactively                             |

---

## 🚀 How to Run

Make sure you have **Python 3.6.8 or later** installed, then cd into the root directory.

```bash
python3 AnalyticalGeometry.py
```

Follow the terminal prompts to:

1. Enter the circle's center and radius
2. Enter the line's start and end points
3. View the drawing and results in the graphics window

---

## 📸 Demo Screenshot

Here’s a screenshot of the Program in action:

![Screenshot](https://imgur.com/m4Cfzb4.png)

---

## 🧠 Learning Outcomes

* Gained experience with **Python basics**: variables, input, conditionals, expressions
* Practiced **graphical programming** using the `turtle` module
* Applied **analytical geometry and math problem solving**
* Learned to visualize complex calculations through coding
* Reinforced debugging and modular code design through constants and comments