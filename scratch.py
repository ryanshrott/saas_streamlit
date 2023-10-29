import requests
from PIL import Image
import io

def download_images(url_list):
    """Download images from the given list of URLs."""
    images = []
    for url in url_list:
        response = requests.get(url)
        if response.status_code == 200:  # If download is successful
            img = Image.open(io.BytesIO(response.content))
            images.append(img)
    return images

def create_collage(image_list, output_size=(1920, 1080)):
    """Create a grid collage from the given list of images."""
    
    # Calculate individual image size
    img_width = output_size[0] // 4  # 4 images per row
    img_height = int(img_width * (9 / 16))
    
    # Create an empty canvas
    collage = Image.new('RGB', output_size)
    
    # Paste each image onto the canvas
    x_offset, y_offset = 0, 0
    for img in image_list:
        img_resized = img.resize((img_width, img_height))
        collage.paste(img_resized, (x_offset, y_offset))
        
        x_offset += img_width
        if x_offset >= output_size[0]:  # Next row
            x_offset = 0
            y_offset += img_height
    
    # Save the collage
    collage.save('collage.jpg')
    print("Collage saved as collage.jpg")

if __name__ == "__main__":
    url_list = [
    "https://cache05.housesigma.com/Live/photos/FULL/1/519/W2523519.jpg?ea2a1969",
    "https://cache06.housesigma.com/Live/photos/FULL/2/519/W2523519_2.jpg?ea2a1969",
    "https://cache08.housesigma.com/Live/photos/FULL/3/519/W2523519_3.jpg?ea2a1969",
    "https://cache09.housesigma.com/Live/photos/FULL/4/519/W2523519_4.jpg?ea2a1969",
    "https://cache-e11.housesigma.com/Live/photos/FULL/5/519/W2523519_5.jpg?ea2a1969",
    "https://cache-e12.housesigma.com/Live/photos/FULL/6/519/W2523519_6.jpg?ea2a1969",
    "https://cache-e13.housesigma.com/Live/photos/FULL/7/519/W2523519_7.jpg?ea2a1969",
    "https://cache-e14.housesigma.com/Live/photos/FULL/8/519/W2523519_8.jpg?ea2a1969",
    "https://cache05.housesigma.com/Live/photos/FULL/9/519/W2523519_9.jpg?ea2a1969"
  ]
    images = download_images(url_list)
    create_collage(images)


"""

AsIs_LLM
: 
"no"
ConvenientLocation_LLM
: 
"no"
EcoFriendly_LLM
: 
"no"
ExtraSpaces_LLM
: 
"yes"
FirstTimeBuyerFriendly_LLM
: 
"yes"
FixerUpper_LLM
: 
"no"
InvestorReady_LLM
: 
"yes"
LargeGarage_LLM
: 
"no"
LuxuryFeatures_LLM
: 
"no"
ModernAppliances_LLM
: 
"yes"
ModernKitchen_LLM
: 
"yes"
MoveInReady_LLM
: 
"yes"
NearbyAmenities_LLM
: 
"no"
NewBuild_LLM
: 
"no"
OutdoorAmenities_LLM
: 
"yes"
OutdoorSpace_LLM
: 
"yes"
PrivateFeatures_LLM
: 
"yes"
RenovatedRecently_LLM
: 
"yes"
UltraLuxuriousRenovation_LLM
: 
"no""""