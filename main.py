import os
import sys
import Image
import Music
import Traversal

img_path = os.path.join(sys.path[0], "images/river.png")
processor = Image.ImageProcessor(img_path)

linear_trav_notes = Traversal.linear_traversal(processor.length, processor.length, processor.resized_rgba, processor.resized_gray)
two_spiral_inward_trav_notes = Traversal.two_spiral_inward_traversal(processor.length, processor.length, processor.resized_rgba, processor.resized_gray)

linear_trav_song = Music.Song(linear_trav_notes)
two_spiral_inward_trav_song = Music.Song(two_spiral_inward_trav_notes)

linear_trav_song.output_to_file("linear_traversal")
two_spiral_inward_trav_song.output_to_file("two_spiral_inward_traversal")
