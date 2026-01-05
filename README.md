# Auditory semantic 1-back pilot

This repository contains a PsychoPy (Builder) experiment for a pilot fMRI study implementing an auditory semantic 1-back task with concrete, abstract, and baseline stimuli.

---

## Experiment overview

* **Modality:** auditory (spoken Polish words, TTS-generated)
* **Design:** block design
* **Conditions:**
  * Concrete words (CON)
  * Abstract words (ABS)
  * Auditory baseline (speech-shaped noise)
* **Task:** semantic 1-back comparison
* **Total duration:** ~10-12 minutes

---

## Stimuli preparation pipeline

Stimuli are generated and validated outside PsychoPy:

1. **Lexical selection and matching**

   * Concrete and abstract words selected from ANPW and SUBTLEX-PL
   * Extreme concreteness quantiles
   * Matching across conditions on:
     * word length
     * syllable count
     * lexical frequency (Zipf)
   * No item repetition across runs

2. **Statistical validation**

   * Automated reports comparing CON vs ABS within and across runs
   * Distribution plots and summary statistics
   * Outputs stored in `stimuli_selection/reports/`

3. **Audio generation of concrete and abstract words**

   * Offline TTS (Piper, Polish voice)
   * Fixed sampling rate and duration
   * Silence padding and RMS normalization

4. **Baseline noise generation**

   * Per-trial baseline stimuli of speech-shaped, band-limited noise derived from task stimuli
   * Counterbalanced use of CON/ABS source audio

---

## Repository structure

* `experiment/`
  PsychoPy Builder experiment (`.psyexp`) and task logic
* `experiment/resources/`
  * `audio/` - generated WAV files (CON, ABS, BASE)
  * `lists/` - trial lists used directly by PsychoPy
  * `instructions/` - task instructions for participants
* `stimuli_selection/`
  * `lexicons/` - source lexical databases
  * `models/` - offline models for TTS
  * `reports/` - statistical reports and figures
  * `scripts/` - notebooks for stimulus selection and generation
* `results/`- output data

---

## Requirements

* PsychoPy **2023.2.3** (standalone)
* Windows OS

---

## Running the experiment

Open the `.psyexp` file in PsychoPy Builder and run the experiment using PsychoPy standalone

---