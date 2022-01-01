def get_starting_pitches(notes):
    starting_pitches = []
    for n in notes:
        if n.time == 0:
            starting_pitches.append(n.pitch)
        else:
            break
    return starting_pitches

def get_scale(starting_pitches):
    return round(sum(starting_pitches) / len(starting_pitches))

def get_scale_notes(scale):
    # W, W, H, W, W, W, H
    scale_increments = [2, 2, 1, 2, 2, 2, 1]
    curr_pitch = scale
    notes_in_scale = {curr_pitch}
    
    # getting piches in the scale lower than the curr_pitch
    is_past_pitch_lim = False
    while not is_past_pitch_lim:
        for i in reversed(scale_increments):
            curr_pitch -= i
            if curr_pitch < 21:
                is_past_pitch_lim = True
                break
            notes_in_scale.add(curr_pitch)
    
    # getting piches in the scale higher than the curr_pitch
    curr_pitch = scale
    is_past_pitch_lim = False
    while not is_past_pitch_lim:
        for i in scale_increments:
            curr_pitch += i
            if curr_pitch > 108:
                is_past_pitch_lim = True
                break
            notes_in_scale.add(curr_pitch)
            
    return notes_in_scale

def get_pitches_from_rgb(rgb):
    return [
        get_pitch_from_color(rgb[0]),
        get_pitch_from_color(rgb[1]),
        get_pitch_from_color(rgb[2])
    ]
    
def get_pitch_from_color(color):
    # want midi number to be between 21 and 108
    return round(color/255 * 87) + 21

def get_vol_from_intensity(intensity):
    return round(intensity/255 * 127)

def get_length_from_alpha(alpha):
    return 1