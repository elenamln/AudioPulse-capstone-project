# 🎧 AudioPulse Capstone Project 🎧

Welcome to the **AudioPulse Capstone Project**: a data analysis pipeline designed to collect, process, and analyze YouTube audio content to uncover audience trends and engagement patterns.

---

## Project Overview

This project aims to build the core data engineering pipeline that powers research and insights based on YouTube audio data.

---

## Features

- **YouTube Audio Collection:**  
  Collects videos featuring music, ambient sounds, podcasts, reviews, music sessions, and more.

- **Audio-Only Downloads:**  
  Extracts and downloads only the audio tracks from YouTube videos, ignoring the video stream.

- **Metadata Extraction:**  
  Gathers all available metadata (e.g., title, channel, views, likes, duration) for each audio track.

- **Data Processing & Organization:**  
  Cleans and organizes the raw data into structured CSV files optimized for downstream analysis.

- **Parallel Downloading:**  
  Utilizes parallel processing techniques to accelerate audio downloads, reducing overall runtime.

- **Robust Logging:**  
  Logs every download event, including successes and errors, to monitor the pipeline’s performance and troubleshoot issues.

- **Analytical Insights:**  
  Performs exploratory data analysis with Spark and Pandas to identify trends such as:
  - Top-performing audio tracks by views.
  - Average audio length.
  - Correlations between likes and views.
  
---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/audiopulse.git
   cd audiopulse
