from PIL import Image


"""
00 fragment_v2_2ca110b1-cf68-4dc2-8c2d-2d42b0c48c48.gif ^
00 fragment_v2_7d3faa25-9371-4373-8b1c-814c9bc3b046.gif s

02 fragment_v2_1c754b9c-6edd-41f8-b924-5eca909579d1.gif b
02 fragment_v2_5223ec41-703c-41cd-9ba9-7c0d7bad0a8f.gif m
02 fragment_v2_9010eff9-c33e-4ad9-b680-2067619ecfc6.gif 6
02 fragment_v2_eaf40e86-149c-4184-a22c-ca6970c8ce2a.gif I

"""

gif = '../GIFs/'+'fragment_v2_555a736b-38da-4af2-acc1-8407d9cb8124.gif'

im = Image.open(gif)
print(im.n_frames, gif)

for frame in range (0, im.n_frames):
    im.seek(frame)
    print(im.getpixel((25,25)), im.info['duration'])
    #im.show()