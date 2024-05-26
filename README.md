# Style-Transfer
## Step 1: Generating Style Image
Initially, the code utilises Stable Diffusion to create a style image based on a user-provided prompt. This step is optional if a pre-generated style image named 'generated_image.png' exists in the same folder.
## Step 2: Applying Style
Next, the generated or provided style is applied to the content image, which should also be placed in the same folder. The code visualises the style transfer progress, allowing users to observe changes in real-time.
## Optional: Saving Progress
Optionally, users can choose to save intermediate images depicting the gradual style transfer process. These images can later be converted into a GIF using the provided script.

![30 iterations](https://github.com/LinaAliceAnderson/style-transfer/assets/29875475/063c11c2-468d-4b0d-8f59-e44bd1bb8830)  ![output](https://github.com/LinaAliceAnderson/style-transfer/assets/29875475/405c2d82-2c48-4195-84e1-eb05803a3c3e)


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
