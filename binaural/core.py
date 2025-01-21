"""Core functionality for binaural audio processing.

This module provides functions for generating binaural beats and related audio processing.
"""

import numpy as np
from typing import Tuple, Optional, Dict, List
from enum import Enum


def generate_sine_wave(
    frequency: float,
    duration: float,
    sample_rate: int = 44100,
    amplitude: float = 1.0
) -> np.ndarray:
    """
    Generate a sine wave.
    
    Args:
        frequency (float): Frequency of the sine wave in Hz
        duration (float): Duration of the signal in seconds
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
        amplitude (float, optional): Amplitude of the signal. Defaults to 1.0.
    
    Returns:
        np.ndarray: Array containing the sine wave samples
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return amplitude * np.sin(2 * np.pi * frequency * t)

def apply_envelope(
    signal: np.ndarray,
    attack: float = 0.1,
    decay: float = 0.1,
    sample_rate: int = 44100
) -> np.ndarray:
    """
    Apply an amplitude envelope (attack and decay) to a signal.
    
    Args:
        signal (np.ndarray): Input signal
        attack (float, optional): Attack time in seconds. Defaults to 0.1.
        decay (float, optional): Decay time in seconds. Defaults to 0.1.
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
    
    Returns:
        np.ndarray: Signal with envelope applied
    """
    total_samples = len(signal)
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    
    envelope = np.ones(total_samples)
    
    # Attack phase
    if attack_samples > 0:
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    
    # Decay phase
    if decay_samples > 0:
        envelope[-decay_samples:] = np.linspace(1, 0, decay_samples)
    
    return signal * envelope

def generate_binaural_beat(
    base_frequency: float,
    beat_frequency: float,
    duration: float,
    sample_rate: int = 44100,
    amplitude: float = 0.5,
    carrier_frequency: Optional[float] = None,
    attack: float = 0.1,
    decay: float = 0.1
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate a binaural beat.
    
    A binaural beat is an auditory illusion perceived when two slightly different 
    frequencies are presented separately to the left and right ear. The difference 
    between these frequencies creates the perceived beat.
    
    Args:
        base_frequency (float): Base frequency in Hz
        beat_frequency (float): Desired beat frequency in Hz
        duration (float): Duration of the signal in seconds
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
        amplitude (float, optional): Amplitude of the signal. Defaults to 0.5.
        carrier_frequency (float, optional): If provided, will modulate the binaural
            beat with this carrier frequency. Defaults to None.
        attack (float, optional): Attack time in seconds. Defaults to 0.1.
        decay (float, optional): Decay time in seconds. Defaults to 0.1.
    
    Returns:
        Tuple[np.ndarray, np.ndarray]: Left and right channel audio data
    
    Examples:
        >>> left, right = generate_binaural_beat(200, 10, 5)  # 5 seconds, 10Hz beat
        >>> # Save as wav file
        >>> import scipy.io.wavfile as wavfile
        >>> wavfile.write('binaural.wav', 44100, np.vstack((left, right)).T)
    """
    # Calculate frequencies for left and right channels
    left_freq = base_frequency
    right_freq = base_frequency + beat_frequency
    
    # Generate base signals
    left_channel = generate_sine_wave(left_freq, duration, sample_rate, amplitude)
    right_channel = generate_sine_wave(right_freq, duration, sample_rate, amplitude)
    
    # Apply carrier frequency if specified
    if carrier_frequency is not None:
        carrier = generate_sine_wave(carrier_frequency, duration, sample_rate, 1.0)
        left_channel *= carrier
        right_channel *= carrier
    
    # Apply envelope to avoid clicks and pops
    left_channel = apply_envelope(left_channel, attack, decay, sample_rate)
    right_channel = apply_envelope(right_channel, attack, decay, sample_rate)
    
    return left_channel, right_channel

def generate_isochronic_tone(
    frequency: float,
    pulse_rate: float,
    duration: float,
    sample_rate: int = 44100,
    amplitude: float = 0.5,
    duty_cycle: float = 0.5
) -> np.ndarray:
    """
    Generate an isochronic tone.
    
    Isochronic tones are regular beats of a single tone that are turned on and off 
    rapidly at regular intervals.
    
    Args:
        frequency (float): Frequency of the tone in Hz
        pulse_rate (float): Rate of pulsing in Hz
        duration (float): Duration of the signal in seconds
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
        amplitude (float, optional): Amplitude of the signal. Defaults to 0.5.
        duty_cycle (float, optional): Ratio of pulse on-time to period. Defaults to 0.5.
    
    Returns:
        np.ndarray: Audio data containing the isochronic tone
    """
    # Generate base tone
    tone = generate_sine_wave(frequency, duration, sample_rate, amplitude)
    
    # Generate pulse train
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    pulse_period = 1.0 / pulse_rate
    pulse = (t % pulse_period) < (pulse_period * duty_cycle)
    
    # Apply pulse train to tone
    return tone * pulse

def generate_monaural_beat(
    frequency1: float,
    frequency2: float,
    duration: float,
    sample_rate: int = 44100,
    amplitude: float = 0.5
) -> np.ndarray:
    """
    Generate a monaural beat.
    
    Monaural beats are created by combining two frequencies in a single channel,
    creating an amplitude modulation effect.
    
    Args:
        frequency1 (float): First frequency in Hz
        frequency2 (float): Second frequency in Hz
        duration (float): Duration of the signal in seconds
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
        amplitude (float, optional): Amplitude of the signal. Defaults to 0.5.
    
    Returns:
        np.ndarray: Audio data containing the monaural beat
    """
    wave1 = generate_sine_wave(frequency1, duration, sample_rate, amplitude)
    wave2 = generate_sine_wave(frequency2, duration, sample_rate, amplitude)
    
    return (wave1 + wave2) / 2

"""Core functionality for binaural audio processing and solfeggio frequencies.

This module provides functions for generating binaural beats, solfeggio frequencies,
and related audio processing capabilities.
"""
class SolfeggioFrequency(Enum):
    """Enumeration of Solfeggio frequencies and their healing properties."""
    UT = 174  # Healing - pain relief, tension reduction
    RE = 285  # Restoring - tissue and organ repair
    MI = 396  # Relieving - guilt, fear, grief transformation
    FA = 417  # Broadening - trauma release, change facilitation
    SOL = 432  # Connecting - universal harmony
    LA = 528  # Energizing - DNA repair, harmony
    SI = 639  # Balancing - relationships, cellular communication
    UT2 = 741  # Detoxing - cellular detox, mind cleansing
    RE2 = 852  # Awakening - spiritual order, intuition

def generate_sine_wave(
    frequency: float,
    duration: float,
    sample_rate: int = 44100,
    amplitude: float = 1.0
) -> np.ndarray:
    """
    Generate a sine wave.
    
    Args:
        frequency (float): Frequency of the sine wave in Hz
        duration (float): Duration of the signal in seconds
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
        amplitude (float, optional): Amplitude of the signal. Defaults to 1.0.
    
    Returns:
        np.ndarray: Array containing the sine wave samples
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return amplitude * np.sin(2 * np.pi * frequency * t)

def apply_envelope(
    signal: np.ndarray,
    attack: float = 0.1,
    decay: float = 0.1,
    sample_rate: int = 44100
) -> np.ndarray:
    """
    Apply an amplitude envelope (attack and decay) to a signal.
    
    Args:
        signal (np.ndarray): Input signal
        attack (float, optional): Attack time in seconds. Defaults to 0.1.
        decay (float, optional): Decay time in seconds. Defaults to 0.1.
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
    
    Returns:
        np.ndarray: Signal with envelope applied
    """
    total_samples = len(signal)
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    
    envelope = np.ones(total_samples)
    
    if attack_samples > 0:
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    
    if decay_samples > 0:
        envelope[-decay_samples:] = np.linspace(1, 0, decay_samples)
    
    return signal * envelope

def generate_solfeggio_tone(
    frequency: SolfeggioFrequency,
    duration: float,
    sample_rate: int = 44100,
    amplitude: float = 0.5,
    attack: float = 0.1,
    decay: float = 0.1
) -> np.ndarray:
    """
    Generate a Solfeggio frequency tone.
    
    Args:
        frequency (SolfeggioFrequency): Solfeggio frequency to generate
        duration (float): Duration of the signal in seconds
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
        amplitude (float, optional): Amplitude of the signal. Defaults to 0.5.
        attack (float, optional): Attack time in seconds. Defaults to 0.1.
        decay (float, optional): Decay time in seconds. Defaults to 0.1.
    
    Returns:
        np.ndarray: Audio data containing the Solfeggio tone
    """
    signal = generate_sine_wave(frequency.value, duration, sample_rate, amplitude)
    return apply_envelope(signal, attack, decay, sample_rate)

def generate_binaural_beat(
    base_frequency: float,
    beat_frequency: float,
    duration: float,
    sample_rate: int = 44100,
    amplitude: float = 0.5,
    carrier_frequency: Optional[float] = None,
    attack: float = 0.1,
    decay: float = 0.1
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate a binaural beat.
    
    Args:
        base_frequency (float): Base frequency in Hz
        beat_frequency (float): Desired beat frequency in Hz
        duration (float): Duration of the signal in seconds
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
        amplitude (float, optional): Amplitude of the signal. Defaults to 0.5.
        carrier_frequency (float, optional): Carrier frequency modulation. Defaults to None.
        attack (float, optional): Attack time in seconds. Defaults to 0.1.
        decay (float, optional): Decay time in seconds. Defaults to 0.1.
    
    Returns:
        Tuple[np.ndarray, np.ndarray]: Left and right channel audio data
    """
    left_freq = base_frequency
    right_freq = base_frequency + beat_frequency
    
    left_channel = generate_sine_wave(left_freq, duration, sample_rate, amplitude)
    right_channel = generate_sine_wave(right_freq, duration, sample_rate, amplitude)
    
    if carrier_frequency is not None:
        carrier = generate_sine_wave(carrier_frequency, duration, sample_rate, 1.0)
        left_channel *= carrier
        right_channel *= carrier
    
    left_channel = apply_envelope(left_channel, attack, decay, sample_rate)
    right_channel = apply_envelope(right_channel, attack, decay, sample_rate)
    
    return left_channel, right_channel

def generate_solfeggio_binaural(
    solfeggio_freq: SolfeggioFrequency,
    beat_frequency: float,
    duration: float,
    sample_rate: int = 44100,
    amplitude: float = 0.5,
    attack: float = 0.1,
    decay: float = 0.1
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate a binaural beat based on a Solfeggio frequency.
    
    Args:
        solfeggio_freq (SolfeggioFrequency): Base Solfeggio frequency
        beat_frequency (float): Desired beat frequency in Hz
        duration (float): Duration of the signal in seconds
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
        amplitude (float, optional): Amplitude of the signal. Defaults to 0.5.
        attack (float, optional): Attack time in seconds. Defaults to 0.1.
        decay (float, optional): Decay time in seconds. Defaults to 0.1.
    
    Returns:
        Tuple[np.ndarray, np.ndarray]: Left and right channel audio data
    """
    return generate_binaural_beat(
        solfeggio_freq.value,
        beat_frequency,
        duration,
        sample_rate,
        amplitude,
        None,
        attack,
        decay
    )

def mix_solfeggio_frequencies(
    frequencies: List[SolfeggioFrequency],
    duration: float,
    amplitudes: Optional[List[float]] = None,
    sample_rate: int = 44100,
    attack: float = 0.1,
    decay: float = 0.1
) -> np.ndarray:
    """
    Mix multiple Solfeggio frequencies together.
    
    Args:
        frequencies (List[SolfeggioFrequency]): List of Solfeggio frequencies to mix
        duration (float): Duration of the signal in seconds
        amplitudes (List[float], optional): List of amplitudes for each frequency.
            Defaults to None (equal amplitudes).
        sample_rate (int, optional): Sampling rate in Hz. Defaults to 44100.
        attack (float, optional): Attack time in seconds. Defaults to 0.1.
        decay (float, optional): Decay time in seconds. Defaults to 0.1.
    
    Returns:
        np.ndarray: Mixed audio signal
    """
    if amplitudes is None:
        amplitudes = [1.0 / len(frequencies)] * len(frequencies)
    
    if len(frequencies) != len(amplitudes):
        raise ValueError("Number of frequencies must match number of amplitudes")
    
    mixed_signal = np.zeros(int(sample_rate * duration))
    
    for freq, amp in zip(frequencies, amplitudes):
        tone = generate_solfeggio_tone(freq, duration, sample_rate, amp, 0, 0)
        mixed_signal += tone
    
    return apply_envelope(mixed_signal, attack, decay, sample_rate)

def get_solfeggio_properties(freq: SolfeggioFrequency) -> Dict[str, str]:
    """
    Get the healing properties associated with a Solfeggio frequency.
    
    Args:
        freq (SolfeggioFrequency): Solfeggio frequency enum value
    
    Returns:
        Dict[str, str]: Dictionary containing physical and mental benefits
    """
    properties = {
        SolfeggioFrequency.UT: {
            "physical": "Relieve pain and muscle tension",
            "mental": "Reduce misery, convey safety and love for organs"
        },
        SolfeggioFrequency.RE: {
            "physical": "Cure cuts, burns, and facilitate immune system",
            "mental": "Send instructions to repair damaged organs"
        },
        SolfeggioFrequency.MI: {
            "physical": "",
            "mental": "Heal guilt and doubt, eliminate fear, transform grief to joy"
        },

    }
    return properties.get(freq, {"physical": "", "mental": ""})
