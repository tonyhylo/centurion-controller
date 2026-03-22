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
    singularity = CalculateSingularity(angles.theta2)

    if y < 0 or singularity > 0.1:
        if y < 0 :
            raise HTTPException(
                status_code=400, 
                detail="Collision Warning: Joint trajectory will collide with the floor (y < 0)."
            )
        else:
            raise HTTPException(
                status_code=400, 
                detail="Singularity Warning: Arm is fully extended or folded."
            )
    else:
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

def CalculateSingularity(theta2: float):
    L1 = 20
    L2 = 10
    theta2r = math.radians(theta2)

    return L1*L2*math.sin(theta2r)