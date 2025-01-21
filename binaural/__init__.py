
"""
Binaural - A Python package for generating binaural beats and brainwave entrainment.

This package provides tools for generating various types of audio-based brainwave 
entrainment, including binaural beats, monaural beats, and isochronic tones.
"""

from .core import (
    generate_binaural_beat,
    generate_isochronic_tone,
    generate_monaural_beat,
    generate_sine_wave,
    apply_envelope,
    generate_solfeggio_binaural,
    generate_solfeggio_tone,
    mix_solfeggio_frequencies,
    get_solfeggio_properties,
    SolfeggioFrequency
)

__version__ = "0.1.1"
__author__ = "Ishan Oshada"
__email__ = "ishan.kodithuwakku.offical@gmail.com"
__description__ = "A Python package for generating binaural beats and brainwave entrainment"

__all__ = [
    'generate_binaural_beat',
    'generate_isochronic_tone',
    'generate_monaural_beat',
    'generate_sine_wave',
    'apply_envelope',
    'generate_solfeggio_binaural',
    'generate_solfeggio_tone',
    'mix_solfeggio_frequencies',
    'get_solfeggio_properties',
    'SolfeggioFrequency'
]