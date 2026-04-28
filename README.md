# Garbage Detection System
Advanced AI-powered garbage and litter detection system with YOLOE segmentation and custom model integration for comprehensive waste monitoring.

## Manual Installation

### Prerequisites Setup
```bash
# Install system dependencies
sudo apt update
sudo apt install cmake python3-dev python3-pip python3-venv

# Setup MQTT broker (if not already installed)
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt install mosquitto mosquitto-clients
sudo tee -a /etc/mosquitto/mosquitto.conf << EOF
listener 1883
protocol mqtt

listener 9001
protocol websockets

allow_anonymous true
EOF
sudo systemctl restart mosquitto
sudo systemctl enable mosquitto
```

### Application Setup
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install requirements
pip install -U pip
pip install -r requirements.txt

# Download required models
bash download_resources.sh
```

### Configuration
```bash
# Interactive configuration (recommended)
python configure.py

# Or manually edit config.json
# See detailed configuration guide below
```

#### Detailed Configuration Guide

The system uses a `config.json` file for all settings. Here's how to configure it for your specific setup:

##### Video Source Configuration

**For Demo/Testing (using local video files):**
```json
{
    "streams": [
        {
            "sn": "garbage235",
            "local_video": true,
            "video_source": "rtsp://admin:password@192.168.1.100:554/stream",
            "local_video_source": "demo/Garbage-2.mp4"
        }
    ]
}
```

**For Live Camera Feed:**
```json
{
    "streams": [
        {
            "sn": "garbage235",
            "local_video": false,
            "video_source": "rtsp://admin:your_password@192.168.8.150:554/Streaming/Channels/101",
            "local_video_source": "demo/Garbage-2.mp4"
        }
    ]
}
```

##### Key Configuration Parameters:

- **`local_video`**: 
  - Set to `true` to use demo video files for testing
  - Set to `false` to use live camera feed via RTSP
  
- **`video_source`**: 
  - **MUST UPDATE**: Replace with your actual camera's RTSP URL
  - Format: `rtsp://username:password@camera_ip:port/stream_path`
  - Example: `rtsp://admin:hajj1446@192.168.8.150:554/Streaming/Channels/101`
  
- **`local_video_source`**: 
  - Path to demo video file (used when `local_video: true`)
  - Default: `demo/Garbage-2.mp4`
  
- **`sn`**: 
  - Serial number/identifier for the monitoring zone
  - Change to match your area naming (e.g., "garage_area", "parking_lot", "clean_zone_1")

##### Multi-Instance Configuration

To monitor multiple areas simultaneously, add additional stream blocks:

```json
{
    "streams": [
        {
            "sn": "clean_zone_1",
            "local_video": false,
            "video_source": "rtsp://admin:password@192.168.8.150:554/Streaming/Channels/101",
            "local_video_source": "demo/Garbage-2.mp4"
        },
        {
            "sn": "clean_zone_2", 
            "local_video": false,
            "video_source": "rtsp://admin:password@192.168.8.151:554/Streaming/Channels/101",
            "local_video_source": "demo/Garbage-2.mp4"
        },
        {
            "sn": "parking_area",
            "local_video": true,
            "video_source": "rtsp://admin:password@192.168.8.152:554/Streaming/Channels/101", 
            "local_video_source": "demo/parking_test.mp4"
        }
    ]
}
```

##### Configuration Steps:

1. **Update RTSP URLs**: Replace `video_source` with your camera's actual RTSP URL
2. **Set Video Mode**: 
   - Use `"local_video": true` for testing with demo videos
   - Use `"local_video": false` for live camera feeds
3. **Customize Serial Numbers**: Update `sn` values to match your monitoring zones
4. **Add Multiple Streams**: Copy the stream block for each additional camera/area
5. **Verify Network Access**: Ensure cameras are accessible from the monitoring device

##### Important Notes:
- Each stream in the array represents one monitoring area/camera
- All streams will run simultaneously when the application starts
- RTSP URLs must be accessible from the device running the garbage detection system
- Test with demo videos first before switching to live camera feeds


### Running the Application
```bash
# Activate virtual environment
source venv/bin/activate

# Run with configuration file
python rknn_garbage.py config.json
```

## Configuration Options

### Stream Configuration
- **Demo Mode**: Uses local video files for testing
- **Live Mode**: Connects to RTSP camera streams  
- **Multi-Stream**: Monitor multiple cleaning areas simultaneously

### Detection Parameters
- **Person IOU Threshold**: Intersection over Union threshold for person detection (0.3)
- **Overlap IOU Threshold**: Threshold for overlapping detections (0.7)
- **Inference Interval**: Time between detection runs (300 seconds in production, 10 seconds for testing)
- **Heartbeat Interval**: System health monitoring frequency (30 seconds in production, 3 seconds for testing)
- **Data Send Interval**: Frequency of data transmission (300 seconds in production, 9 seconds for testing)
- **Frame Processing**: Configurable frame dimensions and JPEG quality for optimal performance

### Integration Settings
- **Data Send URL**: Endpoint for garbage monitoring reports
- **Heartbeat URL**: System health monitoring endpoint
- **Authentication**: Secure API communication with X-Secret-Key headers

## Background Service Management

The project includes systemd service integration for production deployment:

```bash


# Install as system service
sudo cp garbage-system.service /etc/systemd/system/garbage-system.service

sudo systemctl daemon-reload
sudo systemctl enable garbage-system.service
sudo systemctl start garbage-system.service

sudo systemctl status garbage-system.service

# Service management
sudo systemctl status garbage-system.service
sudo systemctl start garbage-system.service
sudo systemctl stop garbage-system.service
sudo systemctl restart garbage-system.service

# View logs
sudo journalctl -u garbage-system.service -f
```

## Project Structure
```
garbage-detection_release/
├── rknn_garbage.py              # Main application script
├── config.json                  # Configuration file
├── requirements.txt             # Python dependencies
├── garbage-system.service       # Systemd service file
├── download_resources.sh        # Model download script
├── export_rknn.py              # Model export utility
├── litter_trash.txt            # Custom inference labels
├── models/                      # RKNN model files
│   ├── yoloe-11l-seg_rknn_model
│   └── garbage-yolo11s_rknn_model
├── demo/                        # Demo videos and test files
│   └── Garbage-2.mp4
├── libraries/                   # Supporting libraries
└── config/                      # Configuration templates
    └── device/
        └── garbage202.json      # Example configuration file
```

## Model Information
- **YOLOE Segmentation Model**: Advanced segmentation for precise garbage detection (`yoloe-11l-seg_rknn_model`)
- **Garbage Detection Model**: Fine-tuned YOLO11s model for waste identification (`garbage-yolo11s_rknn_model`)
- **Target Platform**: RK3588 (Rockchip Neural Processing Unit)
- **Format**: RKNN optimized models for edge inference
- **Custom Labels**: Configurable detection classes via `litter_trash.txt`

## Dual Detection System
The system combines two powerful AI models:
1. **Garbage Detection Model**: Fine-tuned YOLO11s specifically for waste identification
2. **YOLOE Segmentation**: Advanced segmentation model with custom prompt-based detection using `litter_trash.txt`

This hybrid approach ensures comprehensive garbage detection across various scenarios.

## API Integration
The system integrates with external APIs for comprehensive monitoring:  
- **Garbage Monitoring**: Automated waste detection reporting
- **Health Monitoring**: System heartbeat and status updates
- **Authentication**: Secure API communication with X-Secret-Key headers

## Advanced Features

### Custom Label Configuration
Modify detection classes by editing the inference labels:

1. **Edit Labels**: Update `litter_trash.txt` with desired detection classes
2. **Export Model**: Run `python export_rknn.py` to generate new model
3. **Update Config**: Modify `config.json` to point to the new model

### Multi-Zone Monitoring
The system supports monitoring multiple cleaning areas:
- **garbage1**: Primary cleaning zone monitoring
- **garbage2**: Secondary cleaning zone monitoring  
- Each stream can be configured independently for RTSP or local video sources

## Troubleshooting

### Common Issues
1. **RKNN Model Loading**: Ensure models are downloaded via `./download_resources.sh`
2. **MQTT Connection**: Verify mosquitto service is running
3. **Camera Access**: Check RTSP URLs and network connectivity
4. **Permission Issues**: Ensure proper file permissions for service files
5. **Model Export**: Verify `litter_trash.txt` format before running `export_rknn.py`

### Debug Mode
Enable detailed logging by setting appropriate debug flags in config.json:
- Set `show: true` for visual debugging
- Set `draw: true` for detection visualization

### Log Files
- **Application Logs**: Check console output or journal logs for services
- **System Logs**: Use `journalctl` for systemd service debugging

## Development
For development and testing:
```bash
# Test with demo video
python rknn_garbage.py config.json

# Monitor in debug mode  
# Edit config.json and set: "show": true, "draw": true
```

## Performance Optimization
- **Inference Interval**: Adjust based on processing capability
- **Frame Processing**: Optimized for RK3588 NPU acceleration
- **Multi-threading**: Concurrent processing for multiple streams
- **Memory Management**: Efficient RKNN model loading and inference

## Detection Capabilities
- **Litter Detection**: Various types of waste and debris
- **Trash Classification**: Multiple garbage categories
- **Person Detection**: Human presence monitoring
- **Segmentation**: Precise object boundary detection
- **Real-time Processing**: Live camera feed analysis
