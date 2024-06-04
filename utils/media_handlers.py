# Third-party
import subprocess
import cv2
import numpy as np
import os
import torchvision.transforms as transforms
from io import BytesIO
from PIL import Image


# extract frames from uploaded file
async def extract_frames(video_path, output_dir, fps=1):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f'fps={fps}',
        os.path.join(output_dir, 'frame_%04d.png')
    ]

    subprocess.run(command, check=True)

# preprocess extracted frames frames
async def preprocess_image(image_path):

    transform = transforms.Compose([
        transforms.Resize(size=224),
        transforms.CenterCrop(size=224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    with open(image_path, 'rb') as f:
        img = Image.open(BytesIO(f.read()))
        # Ensure the image is in RGB mode
        img = img.convert("RGB")
        img_tensor = transform(img).unsqueeze(0)
        np_image = img_tensor.numpy()
        # Change shape from [1, 3, 224, 224] to [1, 224, 224, 3]
        np_image = np.transpose(np_image, (0, 2, 3, 1))

    return np_image.astype(np.float32)