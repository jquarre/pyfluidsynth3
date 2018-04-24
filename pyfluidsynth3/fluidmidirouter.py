class FluidMidiRouter():
    ''' Represents the FluidSynth midi router object as defined in midi.h.

    This class is inspired by the FluidMidiRouter object from pyfluidsynth by MostAwesomeDude.

    Member:
    midi_router -- The FluidSynth midi router object (fluid_midi_router_t).
    handle -- The handle to the FluidSynth library. Should be FluidHandle but a raw handle will
              probably work, too (FluidHandle).
    '''

    def __init__( self, handle, settings, synth ):
        ''' Create a new FluidSynth midi router instance using given handle and settings
        objects. '''
        self.handle = handle
        self.midi_router = handle.new_fluid_midi_router( settings.settings, handle.fluid_synth_handle_midi_event, synth.synth )
        if self.midi_router is None:
            print("Error creating Midi Router!")

    def __del__(self):
        ''' Delete the midi router. '''
        print("Killing Midi Router.")
        self.handle.delete_fluid_midi_router( self.midi_router )