# 🏗️ Assignment: The "Centurion" Robot Controller

**Objective**: Develop a decoupled hardware-control system that translates user-inputted joint angles into a calculated spatial position (End-Effector coordinates).

## 🛠️ The Tech Stack
- Backend: Python with FastAPI.
- Frontend: React (Vite preferred).
- Math Library: NumPy (for handling trigonometric operations).



## 📋 Phase 1: The "Digital Brain" (Backend)
Your backend must act as the "Motion Controller." It should not care about the UI; it only cares about the physics.
- Define the Schema: Create a data model that accepts three floating-point numbers representing angles ($\theta_1, \theta_2, \theta_3$) in degrees.
- The Kinematics Engine: Implement a function that calculates the $(x, y)$ position of the "hand."
- Constraint: Assume a 2-link planar arm for simplicity.
- Link Lengths: Link 1 ($L_1$) = 20 units, Link 2 ($L_2$) = 15 units.
- The Math: You must convert degrees to radians before using math.cos or np.cos.
- The API Endpoint: Create a POST route called /calculate that returns a JSON object containing the calculated $x$ and $y$ coordinates.
- CORS Security: Ensure your backend is configured to accept requests from your React development port (usually 5173).

## 🎨 Phase 2: The "Control Pendant" (Frontend)
Your frontend is the interface a technician would use to move the robot.
- The Input Suite: Create a dashboard with three distinct sliders.
- Range: Each slider should go from -180 to 180.
- State: Use React state to track these values in real-time.
- The Communication Hook: Use the useEffect hook or a "Submit" button to send the slider values to your FastAPI server every time a value changes.
- The Display: Create a "Coordinate Readout" section that displays the $x$ and $y$ values returned by the server.
- *Bonus*: Round the values to 2 decimal places for a professional look.

## 🧠 Phase 3: The "Engineering Challenge" (Logic)
To pass this assignment, you must solve a common robotics problem within your code:
- The Singularity Check: If the calculated $x$ and $y$ are $(0, 0)$ or the arm is perfectly straight, how does your math handle it?
- The Physical Limit: Hard-code a "Safety Zone" in FastAPI. If the user moves the slider to an angle that would make the robot hit its own "base" (e.g., $y < 0$), the API should return an error message instead of coordinates.

## 📥 Deliverable Requirements
To consider this project "complete," you should be able to:
- Move the $\theta_1$ slider on the browser.
- See the FastAPI terminal log the incoming request.
- See the $(x, y)$ coordinates on your React screen update instantly.