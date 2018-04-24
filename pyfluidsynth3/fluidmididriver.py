class FluidMidiDriver():
    ''' Represents the FluidSynth midi driver object as defined in midi.h.

    This class is inspired by the FluidMidiDriver object from pyfluidsynth by MostAwesomeDude.

    Member:
    midi_driver -- The FluidSynth midi driver object (fluid_midi_driver_t).
    handle -- The handle to the FluidSynth library. Should be FluidHandle but a raw handle will
              probably work, too (FluidHandle).
    '''

    def __init__( self, handle, settings, router ):
        ''' Create a new FluidSynth midi driver instance using given handle and settings
        objects. '''
        self.handle = handle
        self.midi_driver = handle.new_fluid_midi_driver( settings.settings, handle.fluid_midi_router_handle_midi_event, router.midi_router )
        if self.midi_driver is None:
            print("Error creating Midi Driver!")

    def __del__(self):
        ''' Delete the midi driver. '''
        print("Killing Midi Driver.")
        self.handle.delete_fluid_midi_driver( self.midi_driver )