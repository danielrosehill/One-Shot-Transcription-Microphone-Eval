# Microphone Audio Samples for STT Evaluation

## Results (Single Transcription)

![alt text](device-images/composites/eval-20251223/infographic-wer-ranked.png)

![alt text](device-images/composites/eval-20251223/microphones-by-category.png)

A benchmark comparing how different microphones affect speech-to-text (STT) accuracy. All samples use the same ~2-minute reference text about coffee history, recorded in a consistent home office environment.

## Purpose

This repository evaluates which microphones produce the best results for speech-to-text transcription by testing:

1. **Word Error Rate (WER)** - Accuracy of transcription against ground truth
2. **Audio Quality Score** - Technical quality metrics relevant to voice/STT applications

## Methodology

All transcriptions performed using OpenAI Whisper API (whisper-1) in a single evaluation session on 2025-12-23 to ensure methodological consistency.

- **Reference Text**: 315 words about coffee history (~2 minutes spoken)
- **Recording Environment**: Home office, quiet acoustic conditions
- **Recording Software**: Audacity (default for most samples)
- **Transcription**: OpenAI Whisper API (whisper-1)
- **Metrics**: Word Error Rate (WER), Character Error Rate (CER), audio analysis via ffprobe

## Microphones Tested

| ID | Microphone | Type | Category | Connection | Notes |
|----|------------|------|----------|------------|-------|
| 1 | UGreen CM564 | USB Gooseneck | Desktop | USB-A | 30cm distance |
| 2 | Samson Q2U | Dynamic USB/XLR | Desktop | USB mini | 30cm distance |
| 3 | Logitech H390 | USB Headset | Headset | USB wired | Overhead mic |
| 4 | OnePlus Nord 3 5G | Smartphone built-in | Mobile | N/A | ASR HQ recording |
| 5 | OnePlus Nord 3 5G | Smartphone built-in | Mobile | N/A | Voicenotes.com (MP3) |
| 6 | Audio-Technica ATR4697 | Boundary Mic | Desktop | USB-A | 30cm distance |
| 7 | Audio-Technica ATR4697 | Boundary Mic | Desktop | USB-A | 80cm (long throw) |
| 8 | Jabra Speak 510 | USB Speakerphone | Desktop | USB | Conference device |
| 9 | Logitech C925e | Webcam built-in | Desktop | USB | 30cm distance |
| 10 | Maono Elf | Lavalier | Lavalier | USB-A | Wired lav |
| 11 | Yealink BH72 | Wireless Headset | Headset | USB Dongle | BT51 dongle |
| 12 | Yealink BH72 | Wireless Headset | Headset | Bluetooth | TP-Link UB500 |
| 13 | Audio-Technica ATR4750-USB | Condenser Gooseneck | Desktop | USB-A | Omnidirectional |
| 14 | OnePlus Nord 3 5G | Smartphone built-in | Mobile | N/A | Noisy (Mahane Yehuda) |
| 15 | OnePlus Nord 3 5G | Smartphone built-in | Mobile | N/A | Quiet (home office) |

## STT Evaluation Results

### Word Error Rate (WER) - Lower is Better

| Rank | ID | Microphone | Category | WER |
|------|-----|------------|----------|-----|
| 1 | 15 | OnePlus Nord 3 5G (quiet) | Mobile | **4.13%** |
| 2 | 1 | UGreen CM564 | Desktop | 4.44% |
| 3 | 7 | Audio-Technica ATR4697 (80cm) | Desktop | 4.76% |
| 4 | 2 | Samson Q2U | Desktop | 5.40% |
| 4 | 5 | OnePlus Nord 3 5G (MP3) | Mobile | 5.40% |
| 4 | 6 | Audio-Technica ATR4697 (30cm) | Desktop | 5.40% |
| 4 | 8 | Jabra Speak 510 | Desktop | 5.40% |
| 4 | 9 | Logitech C925e | Desktop | 5.40% |
| 4 | 10 | Maono Elf | Lavalier | 5.40% |
| 10 | 3 | Logitech H390 | Headset | 5.71% |
| 10 | 4 | OnePlus Nord 3 5G (HQ) | Mobile | 5.71% |
| 12 | 11 | Yealink BH72 (dongle) | Headset | 6.03% |
| 12 | 12 | Yealink BH72 (BT) | Headset | 6.03% |
| 12 | 14 | OnePlus Nord 3 5G (noisy) | Mobile | 6.03% |
| 15 | 13 | Audio-Technica ATR4750-USB | Desktop | 6.35% |

### Audio Quality Scores - Higher is Better

Quality score (0-100) based on technical audio metrics including SNR, dynamic range, clipping, and RMS levels.

| Rank | Microphone | Category | Quality Score |
|------|------------|----------|---------------|
| 1 | OnePlus Nord 3 5G (noisy) | Mobile | 89.0 |
| 2 | Yealink BH72 (dongle) | Headset | 85.0 |
| 2 | Yealink BH72 (BT) | Headset | 85.0 |
| 4 | OnePlus Nord 3 5G (HQ) | Mobile | 84.5 |
| 5 | OnePlus Nord 3 5G (MP3) | Mobile | 83.0 |
| 6 | Samson Q2U | Desktop | 80.0 |
| 6 | Jabra Speak 510 | Desktop | 80.0 |

### Category Summary

| Category | Avg Quality Score | Avg WER | Best Performer |
|----------|-------------------|---------|----------------|
| Desktop | 71.7 | 5.31% | UGreen CM564 (4.44%) |
| Mobile | 84.0 | 5.32% | OnePlus Nord 3 quiet (4.13%) |
| Lavalier | 75.0 | 5.40% | Maono Elf |
| Headset | 81.3 | 5.93% | Logitech H390 (5.71%) |

## Key Findings

1. **Best for STT Accuracy**: The OnePlus Nord 3 in a quiet environment achieved the lowest WER (4.13%), followed closely by the UGreen CM564 gooseneck (4.44%).

2. **Audio Quality vs WER Mismatch**: Higher audio quality scores don't directly correlate with better STT accuracy. The Yealink BH72 had the highest quality score (85) but only mid-range WER (6.03%).

3. **Environment Matters More Than Equipment**: The same OnePlus phone showed 4.13% WER in a quiet environment vs 6.03% in the noisy Mahane Yehuda market - a significant difference.

4. **Distance Affects Results**: The Audio-Technica ATR4697 boundary mic at 80cm outperformed the same mic at 30cm (4.76% vs 5.40%), possibly due to reduced proximity effects.

5. **Bluetooth Consistency**: Unlike some previous tests, both Yealink BH72 connection methods (dedicated dongle vs generic Bluetooth adapter) performed identically (6.03% WER).

6. **Most Microphones Perform Similarly**: The majority of microphones clustered around 5.40% WER, suggesting that for typical quiet office use, microphone choice has less impact than environmental factors.

## Repository Structure

```
.
├── samples/                    # Audio recordings (WAV/MP3)
├── text/                       # Reference text (coffee.txt)
├── metadata.json               # Recording metadata for each sample
├── evaluation_results.json     # Full evaluation data
├── evaluate.py                 # Evaluation script
├── device-images/
│   ├── originals/              # Microphone product photos
│   └── composites/             # Generated graphics
└── microphones/                # Detailed microphone documentation
```

## Downloads

- [PDF Report](device-images/composites/eval-20251223/microphone-stt-benchmark.pdf) - Complete visual benchmark report

## License

Audio samples and evaluation data provided for research and comparison purposes.
