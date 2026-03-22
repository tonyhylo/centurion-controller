# 🤖 2-DOF Kinematics Controller
> **A high-fidelity control pendant and digital twin for a two-link robotic arm.**

This project demonstrates a full-stack robotics application, bridging a **React/MUI** control interface with a **FastAPI** kinematics engine. It handles real-time coordinate calculation, mechanical safety constraints, and visualizes the arm's state.

![](./media/Recording%202026-03-21%20212742.gif)

---

## 🏗️ System Architecture

The system utilizes a **Coordinate-Request** pattern to ensure the "Digital Twin" in the browser perfectly mirrors the mathematical state in the backend.

| Layer | Technology | Responsibility |
| :--- | :--- | :--- |
| **Frontend** | React | Industrial Dashboard & Nested CSS Visualization |
| **UI Kit** | Material UI (MUI) | Precision Sliders & Real-time Telemetry Readout |
| **Backend** | Python / FastAPI | Kinematics Logic & Pydantic Data Validation |
| **Math** | NumPy / Trigonometry | Forward Kinematics (FK) & Singularity Monitoring |

---

## 🧠 Engineering Highlights

### 1. The Kinematic Chain (Digital Twin)
Rather than absolute positioning, the UI utilizes **Nested CSS Transforms**. By making `Link 2` a child of `Link 1` and using `transform-origin: left center`, the rotation of the "Shoulder" ($\theta_1$) naturally propagates through the "Elbow." This structural nesting mimics the physical constraints of a real mechanical assembly.  

### 2. Forward Kinematics Engine
The backend translates joint angles into Cartesian space ($x, y$) using a planar arm model:
- **X-Coordinate:** $L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2)$
- **Y-Coordinate:** $L_1 \sin(\theta_1) + L_2 \sin(\theta_1 + \theta_2)$

### 3. Industrial Safety Guards
The controller implements two critical safety checks before confirming any movement:
* **Collision Avoidance:** Automatically rejects any trajectory where $y < 0$ (Floor Collision).

![](./media/Screenshot%202026-03-21%20212434.png)

* **Singularity Monitoring:** Uses the Jacobian determinant ($|det(J)| = L_1 L_2 \sin(\theta_2)$) to identify "dead zones" where the arm loses a degree of freedom. If the arm is fully extended or folded, the server returns a `400 Bad Request` to alert the operator.

![](./media/Screenshot%202026-03-21%20212359.png)

---

## 🚀 Installation & Setup

### 1. Backend (Robot Brain)
```bash
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
````
### 2. Frontend (Control Pendant)

```bash
cd frontend
npm install
npm start
````