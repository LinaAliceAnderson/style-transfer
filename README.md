# Style-Transfer
## Step 1: Generating Style Image
Initially, the code utilises Stable Diffusion to create a style image based on a user-provided prompt. This step is optional if a pre-generated style image named 'generated_image.png' exists in the same folder.
## Step 2: Applying Style
Next, the generated or provided style is applied to the content image, which should also be placed in the same folder. The code visualises the style transfer progress, allowing users to observe changes in real-time.
## Optional: Saving Progress
Optionally, users can choose to save intermediate images depicting the gradual style transfer process. These images can later be converted into a GIF using the provided script.

## Requirements
To execute this code, you will need:
- python 3
- torch
- torchvision
- diffusers
- transformers
- matplotlib
- pillow

## Disclaimer
The author bears no responsibility if this code or any part thereof breaks your computer or your dreams.
