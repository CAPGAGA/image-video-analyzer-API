# own
from utils.media_handlers import extract_frames, preprocess_image
from consts import MEDIA_PATH, TEMP_FILES
from db_utils.crud import create_result

# Third-part
import os
import glob
import asyncio
import json

async def analyze_video(request, video_name, db_file_id):

    video_path = os.path.join(MEDIA_PATH, video_name)
    temp_files_path = os.path.join(TEMP_FILES, video_name)

    # create temp folder
    if not os.path.exists(temp_files_path):
        os.makedirs(temp_files_path)

    # extract frames from video
    await extract_frames(video_path, temp_files_path, 1)

    frame_files = glob.glob(os.path.join(temp_files_path, 'frame_*.png'))
    frame_files.sort()

    # loop = asyncio.get_event_loop()
    # executor = ThreadPoolExecutor()

    tasks = [asyncio.create_task(preprocess_image(frame_file)) for frame_file in frame_files]
    process_images = await asyncio.gather(*tasks)

    tasks_analysis = [asyncio.create_task(request.app.ml_model(process_image)) for process_image in process_images]
    labels = await asyncio.gather(*tasks_analysis)

    print(labels)

    for frame_file in frame_files:
        os.remove(frame_file)

    return labels

