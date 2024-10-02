# Replicate FLUX DEV Generator

This project is a Gradio app that utilizes the FLUX DEV model from Replicate to generate images based on text prompts. It provides an interactive web interface for easy image generation with various customizable parameters.

## Prerequisites

- Python 3.6+
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/PierrunoYT/replicate-flux-dev-generator.git
   cd replicate-flux-dev-generator
   ```

2. (Recommended) Create and activate a virtual environment:

   #### Windows
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   #### macOS and Linux
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Replicate API token:
   - Sign up for an account at [Replicate](https://replicate.com)
   - Obtain your API token from the dashboard

## Setting Environment Variables

#### Windows

You can use either `set` or `setx` to set environment variables:

- Using `set` (temporary, for current session only):
  ```
  set REPLICATE_API_TOKEN=your-api-token-here
  ```

- Using `setx` (permanent, requires restarting the command prompt):
  ```
  setx REPLICATE_API_TOKEN "your-api-token-here"
  ```
  After using `setx`, close and reopen your command prompt for the changes to take effect.

#### macOS and Linux

```
export REPLICATE_API_TOKEN=your-api-token-here
```

## Usage

The main script for the Gradio app is `flux_image_generator.py`. You can run it from the command line to start the web interface.

To launch the Gradio app:

```
python flux_image_generator.py
```

Once the app is running, you'll see a URL in the console. Open this URL in your web browser to access the Gradio interface.

In the Gradio interface, you can:

1. Enter a text prompt describing the image you want to generate.
2. Adjust various parameters:
   - Aspect Ratio: Choose from predefined aspect ratios
   - Input Image (optional): Upload an image for image-to-image generation
   - Prompt Strength: Adjust the strength of the prompt in image-to-image mode
   - Number of Outputs: Generate up to 4 images at once
   - Number of Inference Steps: Higher values may produce better quality but take longer
   - Guidance Scale: How closely the model should follow the prompt
   - Seed (optional): Set for reproducible generation
   - Output Format: Choose between webp, jpg, or png
   - Output Quality: Set the quality for jpg and webp outputs
   - Disable Safety Checker: Option to disable content filtering
   - Go Fast: Enable for faster predictions with optimized model
   - Megapixels: Choose between 1 or 0.25 megapixels for the generated image
3. Click "Submit" to generate the image(s).

The generated images will be displayed in the interface, and you can download them directly from there.

## Troubleshooting

- If you encounter a "ModuleNotFoundError", make sure you've activated the virtual environment (if used) and installed the required packages using pip.
- If you get an authentication error, check that you've correctly set the REPLICATE_API_TOKEN environment variable with your Replicate API token.
- For Windows users: 
  - If you're using PowerShell and the `set` command doesn't work, try using `$env:REPLICATE_API_TOKEN = "your-api-token-here"` instead.
  - If you've used `setx` to set the environment variable, remember to restart your command prompt for the changes to take effect.
- If the Gradio interface doesn't open automatically, try manually copying and pasting the URL from the console into your web browser.

## Contributing

Feel free to fork this repository and submit pull requests with any improvements or additional features you'd like to add to the Gradio app or the project in general.

## License

This project is open-source and available under the [MIT License](LICENSE).
