import runpod
import app
import os
from PIL import Image

def handler(event):
#   This function processes incoming requests to your Serverless endpoint.
#
#    Args:
#        event (dict): Contains the input data and request metadata
#       
#    Returns:
#       Any: The result to be returned to the client
    
    # Extract input data
    print(f"Worker Start")
    input = event['input']
    
    image_path = input.get('image')
    seed = input.get('seed', -1)
    ss_guidance_strength = input.get('ss_guidance_strength', 3)
    ss_sampling_steps = input.get('ss_sampling_steps', 50)
    slat_guidance_strength = input.get('slat_guidance_strength', 3)
    slat_sampling_steps = input.get('slat_sampling_steps', 6)
    
    app.initialize()
    
    # Validate image path
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        return
    
    try:
        # Load the image using Pillow
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error: Failed to load image '{image_path}': {e}")
        return
    
    _, mesh_path = app.generate_3d(
        image,
        seed,
        ss_guidance_strength,
        ss_sampling_steps,
        slat_guidance_strength,
        slat_sampling_steps
    )
    
    return mesh_path 

# Start the Serverless function when the script is run
if __name__ == '__main__':
    runpod.serverless.start({ 'handler': handler })
