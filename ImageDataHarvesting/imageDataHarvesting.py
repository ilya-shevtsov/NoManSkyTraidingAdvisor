import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dayzi\AppData\Local\Tesseract-OCR\tesseract.exe'


def main():
    screenshot_name = "Buying.png"
    grayscale_screenshot = Image.open(screenshot_name).convert('LA')
    system_name = get_system_name(grayscale_screenshot)
    item_name = get_item_name(grayscale_screenshot)
    item_price = get_item_price(grayscale_screenshot)
    print(item_name, system_name, item_price)


# def getting_list_of_item(screenshot):
#     img_crop = crop_image(screenshot, left=1165, top=250, right_offset=320, bottom_offset=793)
#     for item in range(1):
#         left -


def get_system_name(screenshot):
    img_crop = crop_image(screenshot, left=310, top=940, right_offset=1100, bottom_offset=81)
    img_crop.save('temp_files/System_temp.png')
    img = cv2.imread('temp_files/System_temp.png')
    text = pytesseract.image_to_string(img)
    text = text.lstrip("-")
    text = text.lstrip()
    text = text[:-2]
    return text


def get_item_name(screenshot):
    img_crop = crop_image(screenshot, left=1165, top=255, right_offset=320, bottom_offset=791)
    # 2 img_crop = crop_image(screenshot, left=1165, top=355, right_offset=320, bottom_offset=681)
    # 3 img_crop = crop_image(screenshot, left=1165, top=455, right_offset=320, bottom_offset=571)
    # 4 img_crop = crop_image(screenshot, left=1165, top=555, right_offset=320, bottom_offset=459)
    # 5 img_crop = crop_image(screenshot, left=1165, top=655, right_offset=320, bottom_offset=349)
    img_crop.save('temp_files/Item_temp.png')
    img = cv2.imread('temp_files/Item_temp.png')
    text = pytesseract.image_to_string(img)
    text = text[:-2]
    return text


def get_item_price(screenshot):
    img_crop = crop_image(screenshot, left=1740, top=250, right_offset=-20, bottom_offset=780)
    img_crop.save('temp_files/Item_price_temp.png')
    img = cv2.imread('temp_files/Item_price_temp.png')
    text = pytesseract.image_to_string(img)
    try:
        text = int(text.replace(',', ''))
        text = int(text)
    except ValueError:
        img_crop = crop_image(screenshot, left=1750, top=250, right_offset=-20, bottom_offset=780)
        img_crop.save('temp_files/Item_price_temp.png')
        img = cv2.imread('temp_files/Item_price_temp.png')
        text = pytesseract.image_to_string(img)
        text = int(text)
    return text


def crop_image(screenshot, left, top, right_offset, bottom_offset):
    width = screenshot.width
    height = screenshot.height
    right = width - right_offset
    bottom = height - bottom_offset
    img_crop = screenshot.crop((left, top, right, bottom))
    return img_crop


if __name__ == '__main__':
    main()
