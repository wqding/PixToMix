import Image
import Music
import helper

def linear_traversal(length, width, resized, resized_gray):
        time = 0    # start at the beginning
        notes = []
        for row in range(length):
            for col in range(width):
                curr_pitches = helper.get_pitches_from_rgb(resized[row][col])
                
                # TODO: add volume and duration
                notes.append(Music.Note(curr_pitches[0], time))
                notes.append(Music.Note(curr_pitches[1], time))
                notes.append(Music.Note(curr_pitches[2], time))
                
                # intensity = helper.get_vol_from_intensity(resized_gray[row][col])

                time += 1
                
        return notes
    
def two_spiral_inward_traversal(length, width, resized, resized_gray):
    time = 0
    notes = []
    
    top, bot, left, right = 0, length-1, 0, width-1
    vert_dir = False
    # TODO: add volume and duration
    while top <= bot and left <= right:
        if vert_dir:
            for i in range(top, bot+1):
                curr_pitches = helper.get_pitches_from_rgb(resized[i][right])
                notes.append(Music.Note(curr_pitches[0], time))
                notes.append(Music.Note(curr_pitches[1], time))
                notes.append(Music.Note(curr_pitches[2], time))
                
                curr_pitches = helper.get_pitches_from_rgb(resized[bot-i+top][left])
                notes.append(Music.Note(curr_pitches[0], time))
                notes.append(Music.Note(curr_pitches[1], time))
                notes.append(Music.Note(curr_pitches[2], time))
                time += 1
            right -= 1
            left += 1
        else:
            for j in range(left, right+1):
                # intensity1 = self.resized_gray[top][j]
                # intensity2 = self.resized_gray[bot][right-j+left]
                
                curr_pitches = helper.get_pitches_from_rgb(resized[top][j])
                notes.append(Music.Note(curr_pitches[0], time))
                notes.append(Music.Note(curr_pitches[1], time))
                notes.append(Music.Note(curr_pitches[2], time))
                
                curr_pitches = helper.get_pitches_from_rgb(resized[bot][right-j+left])
                notes.append(Music.Note(curr_pitches[0], time))
                notes.append(Music.Note(curr_pitches[1], time))
                notes.append(Music.Note(curr_pitches[2], time))
                time += 1
            bot -= 1
            top += 1
        
        vert_dir = not vert_dir
        
    return notes