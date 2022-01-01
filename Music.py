from midiutil.MidiFile import MIDIFile
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
        
    def output_midi_file(self, track_name):
        midi_file = MIDIFile(1)
        
        midi_file.addTrackName(self.track, self.time, track_name)
        for note in self.notes:
            midi_file.addNote(self.track, self.channel, note.pitch, note.time, note.duration, note.volume)
            
        self.output_midi_to_file(f"{track_name}_output.mid")


