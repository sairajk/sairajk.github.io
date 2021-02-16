import cv2


def resize(img_path, target_size):
    img = cv2.imread(img_path)
    img_resized = cv2.resize(img, target_size, interpolation=cv2.INTER_LANCZOS4)
    save_path = img_path[:img_path.rfind(".")] + "_re.jpg"
    cv2.imwrite(save_path, img_resized)

    print(f"Resized image saved at: {save_path}")


if __name__ == "__main__":
    img_path = "./test_img.png"
    target_size = (160, 160)
    resize(img_path, target_size)
