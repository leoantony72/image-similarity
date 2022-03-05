from PIL import Image
import imagehash


image1 = input("Enter Image Location :");
image2 = input("Enter Image Location :");

def image_hash(image1,image2):
    try:
        hasha = imagehash.whash(Image.open(image1))
        hashb = imagehash.whash(Image.open(image2))
    except FileNotFoundError:
        print("file not found")
        return

    hammingDistance = hasha - hashb
    # print(hammingDistance)
    if(hammingDistance == 0 ):
        print("Same Image")
        return
    if(hammingDistance <= 15):
        print(f"Image Is Similar, hamming distance = {hammingDistance}")
        return
    else:
        print("Image is not similar")  
        return  

image_hash(image1,image2)