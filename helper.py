def get_starting_pitches(notes):
    starting_pitches = []
    for n in notes:
        if n.time == 0:
            starting_pitches.append(n.pitch)
        else:
            break
    return starting_pitches

def get_scale(starting_pitches):
    # TODO: some shit
    return sum(starting_pitches) / len(starting_pitches)

def get_scale_notes(scale):
    return



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