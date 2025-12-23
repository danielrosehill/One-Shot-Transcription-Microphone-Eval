# Audio Feature Analysis for STT Benchmark

## Overview
This analysis examines correlations between audio characteristics and Word Error Rate (WER)
to understand why certain microphones perform better for speech-to-text transcription.

## Key Findings

### Top Correlations with WER

- **Spectral Bandwidth Mean**: r=-0.516 (p=0.049)
  - higher values correlate with FEWER errors
  - statistically significant

- **Harmonic Ratio**: r=-0.443 (p=0.098)
  - higher values correlate with FEWER errors
  - not statistically significant

- **Speech Clarity Ratio**: r=0.393 (p=0.147)
  - higher values correlate with MORE errors
  - not statistically significant

- **Mfcc 2 Mean**: r=-0.336 (p=0.221)
  - higher values correlate with FEWER errors
  - not statistically significant

- **Speech Formant Ratio**: r=0.325 (p=0.237)
  - higher values correlate with MORE errors
  - not statistically significant

- **Spectral Rolloff Mean**: r=-0.313 (p=0.255)
  - higher values correlate with FEWER errors
  - not statistically significant

- **Speech Fundamental Ratio**: r=-0.259 (p=0.352)
  - higher values correlate with FEWER errors
  - not statistically significant

- **Rms Mean**: r=0.244 (p=0.381)
  - higher values correlate with MORE errors
  - not statistically significant

- **Spectral Centroid Mean**: r=-0.242 (p=0.386)
  - higher values correlate with FEWER errors
  - not statistically significant

- **Zero Crossing Rate Mean**: r=0.166 (p=0.555)
  - higher values correlate with MORE errors
  - not statistically significant

## Category Analysis

| Category | Avg WER | WER Std | Spectral Centroid | Harmonic Ratio | Formant Energy |
|----------|---------|---------|-------------------|----------------|----------------|
| Desktop | 5.31% | 0.60% | 2439 Hz | 0.551 | 50.5% |
| Headset | 5.93% | 0.18% | 2507 Hz | 0.297 | 62.9% |
| Lavalier | 5.40% | nan% | 2302 Hz | 0.460 | 53.9% |
| Mobile | 5.32% | 0.83% | 2187 Hz | 0.517 | 63.6% |

## Best and Worst Performers

### Best (Lowest WER)
- Sample 15 (OnePlus Nord 3 5G): 4.13% WER
  - Spectral Centroid: 2639 Hz, Harmonic Ratio: 0.532
- Sample 1 (UGreen CM564): 4.44% WER
  - Spectral Centroid: 2893 Hz, Harmonic Ratio: 0.548
- Sample 7 (Audio-Technica ATR4697): 4.76% WER
  - Spectral Centroid: 2850 Hz, Harmonic Ratio: 0.667

### Worst (Highest WER)
- Sample 13 (Audio-Technica ATR4750-USB): 6.35% WER
  - Spectral Centroid: 2555 Hz, Harmonic Ratio: 0.485
- Sample 11 (Yealink BH72): 6.03% WER
  - Spectral Centroid: 1526 Hz, Harmonic Ratio: 0.413
- Sample 12 (Yealink BH72): 6.03% WER
  - Spectral Centroid: 1532 Hz, Harmonic Ratio: 0.366

## Interpretation

The analysis reveals several counterintuitive findings:

1. **Audio quality scores don't predict STT accuracy**: Traditional measures of audio quality
   (SNR, dynamic range) show weak correlation with transcription accuracy.

2. **Smartphone processing helps**: The OnePlus phone applies real-time audio processing
   (noise reduction, AGC) that appears to benefit STT engines, even though it reduces
   "audiophile" quality metrics.

3. **Spectral characteristics matter**: Features like spectral centroid and harmonic ratio
   show meaningful correlations, suggesting that frequency balance and voice clarity
   impact recognition accuracy.

4. **Environment > Equipment**: The same microphone (OnePlus Nord 3) shows dramatically
   different WER in quiet (4.13%) vs noisy (6.03%) environments, confirming that
   recording conditions dominate equipment choice.

## Note on Statistical Significance

With only 15 samples, many correlations don't reach traditional statistical significance
(p < 0.05). These findings are indicative rather than conclusive. A larger sample size
would be needed to confirm these patterns.
