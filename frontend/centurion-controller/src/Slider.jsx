import * as React from "react";
import Box from "@mui/material/Box";
import Stack from "@mui/material/Stack";
import Slider from "@mui/material/Slider";
import Grid from "@mui/material/Grid";

const MIN = -180;
const MAX = 180;
const marks = [
  {
    value: MIN,
    label: "-180",
  },
  {
    value: 0,
    label: "0",
  },
  {
    value: MAX,
    label: "180",
  },
];

export default function ContinuousSlider() {
  const [angles, setAngles] = React.useState({
    theta1: 0,
    theta2: 0
  })

  React.useEffect(() => {
    sendDataToRobot(angles);
  }, [angles])



  async function sendDataToRobot(angles) {
    const url = "http://localhost:8000/calculate";
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(angles),
    });
  }

  return (
    <Box sx={{ width: 500 }}>
      <Grid container spacing={5} sx={{ alignItems: "center" }}>
        <Grid>Joint 1</Grid>
        <Grid size="grow">
          <Slider
            sx={{
              "& .MuiSlider-markLabel": {
                color: "white", // The text inside the bubble
              },
            }}
            name="theta1"
            min={-180}
            max={180}
            value={angles.theta1}
            marks={marks}
            valueLabelDisplay="on"
            onChange={(e, val) => setAngles({...angles,"theta1": Number(val)})}
          />
        </Grid>
      </Grid>
      <Grid container spacing={5} sx={{ alignItems: "center" }}>
        <Grid>Joint 2</Grid>
        <Grid size="grow">
          <Slider
            sx={{
              "& .MuiSlider-markLabel": {
                color: "white", // The text inside the bubble
              },
            }}
            name="theta2"
            min={-180}
            max={180}
            value={angles.theta2}
            marks={marks}
            valueLabelDisplay="on"
            onChange={(e, val) => setAngles({...angles, "theta2": Number(val)})}
          />
        </Grid>
      </Grid>
      <div>
        theta1: {angles.theta1}
      </div>
      <div>
        theta2: {angles.theta2}
      </div>
    </Box>
  );
}
