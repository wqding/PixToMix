import os
import sys
import Image
import Music

img_path = os.path.join(sys.path[0], "images/river.png")
processor = Image.ImageProcessor(img_path)



# processor = Image.ImageProcessor(img_path)
# processor.gen_MIDI_linear_traversal()
# processor.gen_MIDI_two_spiral_inward_traversal()