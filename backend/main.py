from pydantic import BaseModel
import numpy as np
import math
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Your React Dev Port
    allow_methods=["*"],
    allow_headers=["*"],
)

class JointAngles(BaseModel):
    theta1: float
    theta2: float


@app.post("/calculate")
async def get_coordinates(angles: JointAngles):
    x, y = CalculateKinematics(angles.theta1, angles.theta2)

    return {
        "x": round(x, 2),
        "y": round(y, 2),
        "Status": "Safe"
    }

def CalculateKinematics(theta1: float, theta2: float):
    L1 = 20
    L2 = 10
    theta1r = math.radians(theta1)
    theta2r = math.radians(theta2)
    #theta3d = theta3 * math.pi / 180

    x = L1 * math.cos(theta1r) + L2*math.cos(theta1r+theta2r)
    y = L1 * math.sin(theta1r) + L2*math.sin(theta1r+theta2r)

    return x, y