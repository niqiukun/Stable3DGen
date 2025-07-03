import runpod
import app

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
    
    image = input.get('image')
    seed = input.get('seed', -1)
    ss_guidance_strength = input.get('ss_guidance_strength', 3)
    ss_sampling_steps = input.get('ss_sampling_steps', 50)
    slat_guidance_strength = input.get('slat_guidance_strength', 3)
    slat_sampling_steps = input.get('slat_sampling_steps', 6)
    
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
