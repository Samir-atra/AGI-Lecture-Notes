
from IPython.display import display, Image, Audio

import cv2  # We're using OpenCV to read video, to install !pip install opencv-python
import time
from openai import OpenAI
import os
import requests
import numpy as np

client = OpenAI(api_key="API_KEY")

vio = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while(True): 
    ret, frame = vio.read()
    cv2.imshow('frame', frame)  
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
vio.release() 

PROMPT_MESSAGES = [
    {
        "role": "user",
        "content": [
            "These are frames from a video that I want to upload. Generate a compelling description that I can upload along with the video.",
            "output.avi",
        ],
    },
]
params = {
    "model": "gpt-4o",
    "messages": PROMPT_MESSAGES,
    "max_tokens": 200,
}

result = client.chat.completions.create(**params)
print(result.choices[0].message.content)