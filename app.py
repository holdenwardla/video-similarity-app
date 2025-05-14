import streamlit as st
import os
import torch
import clip
from PIL import Image
from moviepy.editor import VideoFileClip
import numpy as np
import faiss
import matplotlib.pyplot as plt
import seaborn as sns

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Extract 1 frame per second
def extract_frames(video_path):
    clip_obj = VideoFileClip(video_path)
    duration = int(clip_obj.duration)
    frames = []
    for t in range(0, duration):
        frame
