import gradio as gr
import replicate
import os
import tempfile
import requests
import base64
from io import BytesIO

# Print initial working directory
print(f"Initial working directory: {os.getcwd()}")

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    return None

def base64_to_temp_file(base64_string):
    if not base64_string:
        return None
    try:
        image_data = base64.b64decode(base64_string.split(',')[1])
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        temp_file.write(image_data)
        temp_file.close()
        return temp_file.name
    except Exception as e:
        print(f"Error creating temp file: {str(e)}")
        return None

def generate_image(prompt, aspect_ratio, image, prompt_strength, num_outputs, num_inference_steps, guidance, seed, output_format, output_quality, disable_safety_checker, go_fast, megapixels):
    try:
        input = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "num_outputs": num_outputs,
            "num_inference_steps": num_inference_steps,
            "guidance": guidance,
            "go_fast": go_fast,
            "megapixels": megapixels,
            "output_format": output_format,
            "output_quality": output_quality,
            "disable_safety_checker": disable_safety_checker
        }

        # Add optional parameters only if they are provided
        if image:
            input["image"] = image
        if prompt_strength is not None:
            input["prompt_strength"] = prompt_strength
        if seed is not None:
            input["seed"] = seed

        output = replicate.run(
            "black-forest-labs/flux-dev",
            input=input
        )

        # Download images and convert to base64
        base64_images = []
        for url in output:
            image_data = download_image(url)
            if image_data:
                base64_image = base64.b64encode(image_data.getvalue()).decode('utf-8')
                base64_images.append(f"data:image/png;base64,{base64_image}")
            else:
                base64_images.append("")
        
        # Convert base64 images to temporary files
        temp_files = [base64_to_temp_file(img) for img in base64_images]
        
        # Pad the list with None if less than 4 images are generated
        while len(temp_files) < 4:
            temp_files.append(None)
        
        return tuple(temp_files[:4])  # Return exactly 4 items (file paths or None) as a tuple
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return (None, None, None, None)  # Return 4 None values in case of an error

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(label="Prompt", value="black forest gateau cake spelling out the words \"FLUX DEV\", tasty, food photography, dynamic shot"),
        gr.Dropdown(["1:1", "16:9", "21:9", "3:2", "2:3", "4:5", "5:4", "3:4", "4:3", "9:16", "9:21"], label="Aspect Ratio", value="1:1"),
        gr.Image(label="Input Image (optional)", type="filepath"),
        gr.Slider(0, 1, value=0.8, step=0.01, label="Prompt Strength"),
        gr.Slider(1, 4, value=1, step=1, label="Number of Outputs"),
        gr.Slider(1, 50, value=28, step=1, label="Number of Inference Steps"),
        gr.Slider(0, 10, value=3, step=0.1, label="Guidance Scale"),
        gr.Number(label="Seed (optional)", precision=0),
        gr.Dropdown(["webp", "jpg", "png"], label="Output Format", value="webp"),
        gr.Slider(0, 100, value=80, step=1, label="Output Quality"),
        gr.Checkbox(label="Disable Safety Checker", value=False),
        gr.Checkbox(label="Go Fast", value=True),
        gr.Dropdown(["1", "0.25"], label="Megapixels", value="1"),
    ],
    outputs=[gr.Image(type="filepath") for _ in range(4)],
    title="FLUX DEV Image Generator",
    description="Generate images using the FLUX DEV model from Replicate"
)

if __name__ == "__main__":
    try:
        # Launch the interface with debugging enabled
        iface.launch(share=True, debug=True)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Clean up temporary files
        temp_dir = tempfile.gettempdir()
        for filename in os.listdir(temp_dir):
            if filename.endswith('.png'):
                file_path = os.path.join(temp_dir, filename)
                try:
                    os.unlink(file_path)
                except Exception as e:
                    print(f"Error deleting temporary file {file_path}: {str(e)}")
