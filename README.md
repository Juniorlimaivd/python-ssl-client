# Python SSL Vision Client

[![PyPI version](https://badge.fury.io/py/sslclient.svg)](https://badge.fury.io/py/sslclient)
[![pypi supported versions](https://img.shields.io/pypi/pyversions/sslclient.svg)](https://pypi.python.org/pypi/sslclient)

Python client for [SSL Vision](https://github.com/RoboCup-SSL/ssl-vision) 



## Installation


From source:

```
git clone --recursive https://github.com/Juniorlimaivd/python-ssl-client.git
cd python-ssl-client
python setup.py install
```

From [PyPi](https://pypi.python.org/pypi/sslclient/) directly:

```
pip install sslclient
```

## Example

```Python
import sslclient

c = sslclient.client(ip='255.255.255.255', port=1234)

# Bind connection to port and IP for UDP Multicast
c.connect()

while True:
    #received decoded package
    data = c.receive()
    
    if data.HasField('geometry'):
        print(data.geometry)
    
    if data.HasField('detection'):
        print(data.detection)
```

The data packet may have detection or geometry data. Consult SSL Vision Docs to know when you will receive each type of package.

The formats of the geometry and detection data are de followings:


### `Detection Example`


```json
{
  "detection": {
    "frame_number": 377308,
    "t_capture": 13977.820277,
    "t_sent": 1505683703.172275,
    "camera_id": 1,
    "balls": [
      {
        "confidence": 0.930344820022583,
        "area": 78,
        "x": -14.979391098022461,
        "y": -12.432811737060547,
        "z": 0,
        "pixel_x": 276.5769348144531,
        "pixel_y": 225.73077392578125
      }
      "{... other balls ...}"
    ],
    "robots_yellow": [
      {
        "confidence": 0.930344820022583,
        "area": 78,
        "x": -14.979391098022461,
        "y": -12.432811737060547,
        "z": 0,
        "pixel_x": 276.5769348144531,
        "pixel_y": 225.73077392578125
      }
      "{... other yellow robots ...}"
    ],
    "robots_blue": [
      {
        "confidence": 0.930344820022583,
        "area": 78,
        "x": -14.979391098022461,
        "y": -12.432811737060547,
        "z": 0,
        "pixel_x": 276.5769348144531,
        "pixel_y": 225.73077392578125
      }
      "{... other blue robots ...}"
    ]
  }
}
```


### `Geometry Example` 

```json
{
  "field": {
    "field_length": 1500,
    "field_width": 1300,
    "goal_width": 100,
    "goal_depth": 40,
    "boundary_width": 3,
    "field_lines": [
      {
        "name": "TopTouchLine",
        "p1": {
          "x": -750,
          "y": 650
        },
        "p2": {
          "x": 750,
          "y": 650
        },
        "thickness": 10
      },
      "{... other field lines ...}"
    ],
    "field_arcs": [
      {
        "name": "CenterCircle",
        "center": {
          "x": 0,
          "y": 0
        },
        "radius": 150,
        "a1": 10,
        "a2": 0,
        "thickness": 10
      },
      "{... other field arcs ...}"
    ]
  },
  "calib": [
    {
      "camera_id": 0,
      "focal_length": 2.1379730701446533,
      "principal_point_x": 390,
      "principal_point_y": 290,
      "distortion": 0,
      "q0": -0.0780009999871254,
      "q1": -0.9969499707221985,
      "q2": 0.0014819999923929572,
      "q3": 0.0017130000051110983,
      "tx": -621141.125,
      "ty": -459652.8125,
      "tz": 3500,
      "derived_camera_world_tx": -542101.5625,
      "derived_camera_world_ty": 550669.6875,
      "derived_camera_world_tz": -0.6016282439231873
    },
    "{... other cameras ...}"
  ]
}
``` 