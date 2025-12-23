# Microphone STT Benchmark - December 23, 2025

Point-in-time evaluation of microphone impact on speech-to-text accuracy.

## Evaluation Summary

| Parameter | Value |
|-----------|-------|
| **Date** | December 23, 2025 |
| **Total Samples** | 15 |
| **Reference Text** | 315 words |
| **STT Service** | OpenAI Whisper API (whisper-1) |
| **Methodology** | Single transcription service for consistency |

## Microphones Tested

| Category | Microphones |
|----------|-------------|
| Desktop | UGreen CM564, Samson Q2U, Audio-Technica ATR4697, Audio-Technica ATR4750-USB, Jabra Speak 510, Logitech C925e |
| Headset | Logitech H390, Yealink BH72 |
| Mobile | OnePlus Nord 3 5G |
| Lavalier | Maono Elf |

## Top 5 Rankings by Word Error Rate (WER)

| Rank | Microphone | Category | WER |
|------|------------|----------|-----|
| 1 | OnePlus Nord 3 5G | Mobile | 4.13% |
| 2 | UGreen CM564 | Desktop | 4.44% |
| 3 | Audio-Technica ATR4697 | Desktop | 4.76% |
| 4 | Samson Q2U | Desktop | 5.40% |
| 5 | OnePlus Nord 3 5G | Mobile | 5.40% |

## Category Averages

| Category | Avg Audio Quality Score | Avg WER |
|----------|------------------------|---------|
| Desktop | 71.7 | 5.31% |
| Headset | 81.3 | 5.93% |
| Mobile | 84.0 | 5.38% |
| Lavalier | 75.0 | 5.40% |

## Key Findings

- WER ranged from 4.13% to 6.35% across all samples
- Mobile phone (OnePlus Nord 3 5G) achieved both the best single-sample WER and highest audio quality scores
- Price did not strongly correlate with STT accuracy in this evaluation
- All microphones tested achieved acceptable WER (<7%) for speech-to-text applications

## Contents

### /pdfs
- `microphone-stt-benchmark.pdf` - Visual benchmark report with microphone images
- `spectrograms_collection.pdf` - Spectrograms for all audio samples

### /data
- `evaluation_results.json` - Complete evaluation data with rankings and scores
- `metadata.json` - Microphone specifications and recording metadata
- `audio_features.csv` - Extracted audio features for each sample
- `correlations.json` - Statistical correlations between audio features and WER
- `price_correlation.json` - Price vs. accuracy correlation analysis

### /analysis
- `spectrograms_ranked_by_wer.png` - All spectrograms ordered by WER performance
- `microphones-ranked-by-wer.png` - Microphone images ranked by WER
- `microphones-by-category.png` - Microphones grouped by category
- `microphones-grid.png` - Grid view of all microphones
- `infographic-wer-ranked.png` - Infographic summary
- `correlation_analysis.png` - Statistical correlation visualization
- `price_vs_wer_analysis.png` - Price vs. WER scatter plot

## Notes

This release captures the evaluation as of December 23, 2025. Future evaluations may include:
- Additional microphones
- Different STT services (local models, other cloud APIs)
- Varied recording conditions
