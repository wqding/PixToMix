import cv2

class ImageProcessor:
    def __init__(self, img_path, length=32, width=32):
        self.rgba = cv2.imread(img_path, cv2.IMREAD_UNCHANGED) # rgba
        self.gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # grayscale
        self.length = length
        self.width = width
        self.resized_rgba = cv2.resize(self.rgba, (self.length, self.width), interpolation = cv2.INTER_AREA)
        self.resized_gray = cv2.resize(self.gray, (self.length, self.width), interpolation = cv2.INTER_AREA)
        
    # wtf is fast fourier transfomr vs fourier transform?
    def get_fourier_transform(self):
        return
    
    

# a = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25],
# ]
# top, bot, left, right = 0, len(a)-1, 0, len(a[0])-1
# vert_dir = False
# while top <= bot and left <= right:
#     if vert_dir:
#         print("\ntop", top, "bot", bot)
#         for i in range(top, bot+1):
#             print("i", i)
#             print(a[i][right], a[bot-i+top][left])
#         right -= 1
#         left += 1
#     else:
#         print("\nleft", left, "right", right)
#         for j in range(left, right+1):
#             print("j", j)
#             print(a[top][j], a[bot][right-j+left])
#         bot -= 1
#         top += 1
#     vert_dir = not vert_dir