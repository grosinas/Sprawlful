from PIL import Image
import os

def transpiler(pic1: str, pic2: str) -> Image:
    # Check if the input images exist
    if not os.path.exists(pic1):
        raise FileNotFoundError(f"The file {pic1} does not exist.")
    if not os.path.exists(pic2):
        raise FileNotFoundError(f"The file {pic2} does not exist.")

    # Open the images and convert them to RGBA
    img1 = Image.open(pic1).convert("RGBA")
    img2 = Image.open(pic2).convert("RGBA")
    
    # Check if the images have the same size
    if img1.size != img2.size:
        raise ValueError("Images must be the same size!")
    
    # Apply 50% opacity to the second image (img2)
    img2_with_opacity = img2.copy()
    data = img2_with_opacity.getdata()

    # Adjust the alpha channel to 50% opacity
    new_data = []
    for item in data:
        # item is a tuple (R, G, B, A)
        r, g, b, a = item
        new_data.append((r, g, b, int(a * 0.6)))  # 50% opacity
        
    img2_with_opacity.putdata(new_data)

    # Create a new image with transparency (RGBA) and paste the two images
    result = Image.new("RGBA", img1.size, (0, 0, 0, 0))
    result.paste(img1, (0, 0))  # Paste the first image
    result.paste(img2_with_opacity, (0, 0), img2_with_opacity)  # Paste the second image with 50% opacity
    
    # Save the resulting image to a file
    result.save(f"{pic1[:-4]}_merged.png", "PNG")
    
    # Return the resulting image
    return result
