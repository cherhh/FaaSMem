from PIL import Image
import time


def gray_scale(image, file_name):
    path = "gray-scale-" + file_name
    img = image.convert('L')
    img.save(path)
    return [path]


def image_processing(file_name, image_path):
    path_list = []
    start = time.time()
    with Image.open(image_path) as image:
        tmp = image
        # path_list += ops.flip(image, file_name)
        # path_list += ops.rotate(image, file_name)
        # path_list += ops.filter(image, file_name)
        path_list += gray_scale(image, file_name)
        # path_list += ops.resize(image, file_name)

    latency = time.time() - start
    return latency, path_list


def handler(handler_context):

    # Simulate download
    time.sleep(0)

    latency, path_list = image_processing('image.jpg', 'image.jpg')

    # Simulate upload
    time.sleep(0)


handler({})