# Environment specification

This document describes the software environments used to **develop**, **prepare stimuli**, and **run** the PsychoPy experiment for the auditory semantic 1-back fMRI pilot study.

---

## Operating system

* OS: Microsoft Windows 11 Home
* Version: 10.0.26100.26100

---

## PsychoPy (experiment runtime)

* PsychoPy version: **2023.2.3**
* Installation type: **Standalone**
* Launch mode: Builder / Runner GUI
* Python version used by PsychoPy: **3.8.10**

---

## Python (stimulus preparation & analysis)

* Python version: **3.12.10**
* Environment type: local system / virtual environment

---

## Text-to-Speech (offline stimulus generation)

Auditory word stimuli and baseline control sounds were generated offline using the **Piper TTS** engine.

- TTS engine: **Piper**
- Language: Polish
- Voice model: `pl_PL-gosia-medium`
- Format: ONNX

The following model files are required for stimulus generation but are **not included** in the repository due to size and licensing considerations:

- `stimuli_selection/models/piper/pl_PL-gosia-medium.onnx`
- `stimuli_selection/models/piper/pl_PL-gosia-medium.onnx.json`

The model can be obtained from the official Piper repository: Hugging Face `rhasspy/piper-voices` (Polish → pl_PL → gosia → medium).

---