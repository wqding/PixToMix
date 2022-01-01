from midiutil.MidiFile import MIDIFile

import os
import sys
import random

import helper

C_M = 0

class Note:
    def __init__(self, midi_pitch, time, volume=100, duration=2):
        self.pitch = midi_pitch
        self.time = time
        self.volume = volume
        self.duration = duration


class Song:
    def __init__(self, notes=[Note(64, 0)], tempo=120, track=0, channel=0):
        # array of Note objects that make up a song
        self.notes = notes
        # the scale the song will be in
        self.starting_pitches = helper.get_starting_pitches(notes)
        self.scale = helper.get_scale(self.starting_pitches)
        # all notes belonging to that scale
        self.notes_in_scale = helper.get_scale_notes(self.scale)
        
        # midi stuff
        self.tempo = tempo
        self.track = track
        self.channel = channel
    
    # function to find the closest pitch thats in key given a pitch
    def shift_to_scale(self, pitch):
        if pitch in self.notes_in_scale:
            return pitch
        
        upper_pitch = pitch+1
        lower_pitch = pitch-1
        while upper_pitch <= 108 or lower_pitch >= 21:
            if upper_pitch in self.notes_in_scale and lower_pitch in self.notes_in_scale:
                return random.choice([lower_pitch, upper_pitch])
            elif upper_pitch in self.notes_in_scale:
                return upper_pitch
            elif lower_pitch in self.notes_in_scale:
                return lower_pitch
            
            upper_pitch += 1
            lower_pitch -= 1
            
        return pitch
        
    def output_to_file(self, track_name):
        midi_file = MIDIFile(1)
        
        midi_file.addTrackName(self.track, 0, track_name)
        for note in self.notes:
            note.pitch = self.shift_to_scale(note.pitch)
            midi_file.addNote(self.track, self.channel, note.pitch, note.time, note.duration, note.volume)
        
        file_path = os.path.join(sys.path[0], f"output/{track_name}_output.mid")
        with open(file_path, 'wb') as outf:
            midi_file.writeFile(outf)


