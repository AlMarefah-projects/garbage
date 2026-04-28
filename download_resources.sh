#!/bin/bash
# download_resources.sh
set -e

MODELS_DIR="models"
VIDEOS_DIR="demo"

# Model files and their Google Drive IDs
declare -A MODEL_FILES=(
    ["$MODELS_DIR/garbage-yolo11s_rknn_model/garbage-yolo11s-rk3588.rknn"]="1_qvgP0kTk-WG494wR3oWvqIviww1yT6Z"
    ["$MODELS_DIR/yoloe-11l-seg_rknn_model/yoloe-11l-seg-rk3588.rknn"]="1YAQRQGTdNstc9v2i_cYZGe8qT8LXEM8L"
)

declare -A VIDEO_FILES=(
    ["$VIDEOS_DIR/Garbage-2.mp4"]="1PnGnI5TE7qeLVBHmpYEPGnx70cbZ3e97"
)

# Ensure directories exist
for d in \
    "$MODELS_DIR/garbage-yolo11s_rknn_model" \
    "$MODELS_DIR/yoloe-11l-seg_rknn_model" \
    "$VIDEOS_DIR"
do
    mkdir -p "$d"
done

# Use python -m gdown for maximum compatibility
GDOWN="python3 -m gdown"

# Download models
echo "Checking and downloading model files..."
for file in "${!MODEL_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "Downloading $file ..."
        $GDOWN "https://drive.google.com/uc?id=${MODEL_FILES[$file]}" -O "$file"
        
    else
        echo "$file already exists. Skipping."
    fi
done

# Download videos
echo "Checking and downloading video files..."
for file in "${!VIDEO_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "Downloading $file ..."
        $GDOWN "https://drive.google.com/uc?id=${VIDEO_FILES[$file]}" -O "$file"
    else
        echo "$file already exists. Skipping."
    fi
done

echo "All resources checked/downloaded."