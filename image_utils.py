import cv2


def resize(img_path, target_size):
    img = cv2.imread(img_path)
    
    img = cv2.resize(img, target_size, interpolation=cv2.INTER_AREA)
    
    save_path = f"{img_path.rsplit('.', 1)[0]}_rsz.{img_path.rsplit('.', 1)[1]}"
    cv2.imwrite(save_path, img)
    print(f"Resized image saved at: {save_path}")


def center_pad(img_path, dim, pad_color=[255, 255, 255]):
    """
    Args:
        img: image to be center padded
        dim: image dimensions (height, width) [(y, x)] after padding
    """
    img = cv2.imread(img_path)
    h, w = img.shape[:2]
    if dim == -1:
        dim = (max(h, w), max(h, w))
    
    top = (dim[0] - h) // 2
    bottom = dim[0] - h - top
    left = (dim[1] - w) // 2
    right = dim[1] - w - left
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=pad_color)

    save_path = f"{img_path.rsplit('.', 1)[0]}_pad.{img_path.rsplit('.', 1)[1]}"
    cv2.imwrite(save_path, img)
    print(f"Padded image saved at: {save_path}")


if __name__ == "__main__":
    img_path = "./images/Proj-Lane_Det.jpg"
    # Resize
    target_size = (160, 160)
    resize(img_path, target_size)
    # Pad
    center_pad(img_path, (512, 512))
