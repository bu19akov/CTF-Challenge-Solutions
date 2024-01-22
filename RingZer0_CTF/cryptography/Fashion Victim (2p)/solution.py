from PIL import Image, ImageChops
import itertools
import os
import hashlib

def extract_frames(gif_path):
    frames = []
    with Image.open(gif_path) as img:
        if not img.is_animated:
            raise ValueError(f"The file {gif_path} is not an animated GIF.")

        frame_count = img.n_frames
        for frame in range(frame_count):
            img.seek(frame)
            frames.append(img.copy())
    return frames

def bitwise_and_all_combinations(frames):
    and_frames = []
    for frame1, frame2 in itertools.combinations(frames, 2):
        and_frame = ImageChops.logical_and(frame1.convert('1'), frame2.convert('1'))
        and_frames.append(and_frame)
    return and_frames

def hash_image(image):
    """Calculate the hash of an image file."""
    hash_md5 = hashlib.md5()
    with open(image, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Example usage
gif_path = './tv.gif'  # Replace with your GIF file path
frames = extract_frames(gif_path)
and_frames = bitwise_and_all_combinations(frames)

# Save the resulting images
output_folder = 'output_and_combinations'  # Replace with your desired output folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Save frames and calculate their hashes
hashes = {}
for i, frame in enumerate(and_frames):
    frame_path = f"{output_folder}/and_combination_{i}.png"
    frame.save(frame_path)
    frame_hash = hash_image(frame_path)
    if frame_hash in hashes:
        # Delete if duplicate
        os.remove(frame_path)
    else:
        hashes[frame_hash] = frame_path
