# Binaural

A Python package for generating binaural beats and other brainwave entrainment audio.

## Features

- Generate binaural beats with customizable frequencies
- Create isochronic tones
- Generate monaural beats
- Adjustable parameters (frequency, duration, amplitude, etc.)
- Support for carrier frequency modulation
- Smooth attack/decay envelopes to prevent audio artifacts
- Multiple output formats (WAV, MP3, etc.)
- Solfeggio frequencies support (UT, RE, MI, etc.)
- Optional carrier frequency modulation
- Customizable waveforms (sine, square, etc.)

## Installation

You can install the package via pip:

```bash
pip install binaural
```

## Quick Start

### Generate a Simple Binaural Beat

```python
from binaural import generate_binaural_beat

# Generate a 10Hz theta binaural beat at 200Hz base frequency
left, right = generate_binaural_beat(
    base_frequency=200,  # Base frequency in Hz
    beat_frequency=10,   # Desired beat frequency in Hz
    duration=5,          # Duration in seconds
)

# Save as WAV file
import scipy.io.wavfile as wavfile
import numpy as np
wavfile.write('binaural_beat.wav', 44100, np.vstack((left, right)).T)
```

### Create an Isochronic Tone

```python
from binaural import generate_isochronic_tone

# Generate a 10Hz isochronic tone at 200Hz
tone = generate_isochronic_tone(
    frequency=200,    # Tone frequency in Hz
    pulse_rate=10,    # Pulse rate in Hz
    duration=5        # Duration in seconds
)
```

### Generate a Monaural Beat

```python
from binaural import generate_monaural_beat

# Generate a 10Hz monaural beat
beat = generate_monaural_beat(
    frequency1=200,   # First frequency in Hz
    frequency2=210,   # Second frequency in Hz
    duration=5        # Duration in seconds
)
```

### Generate SolfeggioFrequency 

```python
from binaural import SolfeggioFrequency, generate_solfeggio_tone, mix_solfeggio_frequencies

# Generate a single UT (174 Hz) tone for healing
healing_tone = generate_solfeggio_tone(SolfeggioFrequency.UT, duration=5)

# Mix multiple frequencies
mixed = mix_solfeggio_frequencies(
    frequencies=[SolfeggioFrequency.UT, SolfeggioFrequency.SOL],
    duration=5,
    amplitudes=[0.5, 0.5]
)

# Create a binaural beat based on 432 Hz (SOL)
left, right = generate_solfeggio_binaural(
    SolfeggioFrequency.SOL,
    beat_frequency=7.83,  # Schumann resonance
    duration=5
)

```

### More

```python
from binaural import (
    SolfeggioFrequency, 
    generate_solfeggio_tone, 
    mix_solfeggio_frequencies, 
    generate_solfeggio_binaural,
    generate_binaural_beat,
    generate_isochronic_tone,
    generate_monaural_beat
)

# Generate a single UT (174 Hz) tone for healing
healing_tone = generate_solfeggio_tone(SolfeggioFrequency.UT, duration=5)

# Mix multiple frequencies
mixed = mix_solfeggio_frequencies(
    frequencies=[SolfeggioFrequency.UT, SolfeggioFrequency.SOL],
    duration=5,
    amplitudes=[0.5, 0.5]
)

# Create a binaural beat based on 432 Hz (SOL)
left, right = generate_solfeggio_binaural(
    SolfeggioFrequency.SOL,
    beat_frequency=7.83,  # Schumann resonance
    duration=5
)

# Generate a binaural beat with a base frequency of 200 Hz and a beat frequency of 10 Hz
left, right = generate_binaural_beat(
    base_frequency=200,
    beat_frequency=10,
    duration=5
)

# Generate an isochronic tone with a frequency of 10 Hz and a pulse rate of 2 Hz
isochronic_tone = generate_isochronic_tone(
    frequency=10,
    pulse_rate=2,
    duration=5
)

# Generate a monaural beat with frequencies of 200 Hz and 210 Hz
monaural_beat = generate_monaural_beat(
    frequency1=200,
    frequency2=210,
    duration=5
)

```

## Advanced Usage

### Binaural Beat with Carrier Frequency

```python
left, right = generate_binaural_beat(
    base_frequency=200,
    beat_frequency=10,
    duration=5,
    carrier_frequency=432,  # Add carrier frequency modulation
    attack=0.5,            # Fade in time in seconds
    decay=0.5              # Fade out time in seconds
)
```

## API Reference

### generate_binaural_beat

```python
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
    """Generate a binaural beat."""
```

See function docstrings for detailed parameter descriptions and usage.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.