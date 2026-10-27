# 🎯 AI Object Detection and Tracking Using YOLO

## 📌 Project Overview

**AI Object Detection and Tracking** is a computer vision application developed using Python, YOLO, OpenCV, and Streamlit. It detects objects in uploaded videos, draws bounding boxes around detected objects, and tracks them across video frames using object tracking algorithms.

The application provides an interactive web interface where users can upload a video, configure detection settings, view the processed video, and download the results.

It uses **YOLO11n** for object detection and supports **ByteTrack** and **BoT-SORT** for object tracking.

## 🎯 Project Objectives

- Develop an AI-based object detection system.
- Detect objects in video frames using YOLO.
- Track objects across consecutive frames.
- Display bounding boxes, labels, confidence scores, and tracking IDs.
- Implement ByteTrack and BoT-SORT tracking algorithms.
- Provide an option to detect people only.
- Display detection statistics and processing progress.
- Build a web interface using Streamlit.
- Allow users to download processed videos.

## ✨ Features

- 🎯 Real-time object detection on processed video frames.
- 🤖 YOLO11n object detection model.
- 📦 Bounding boxes around detected objects.
- 🏷️ Object labels and confidence scores.
- 🆔 Object tracking IDs.
- 🔄 ByteTrack and BoT-SORT algorithm selection.
- 🚶 Optional people-only detection.
- 🎚️ Adjustable detection confidence threshold.
- 📊 Frames processed, total detections, and unique tracking IDs.
- 🎬 Original and processed video previews.
- ⬇️ Downloadable processed video.
- 🌐 Interactive Streamlit interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| Ultralytics YOLO | Object detection and tracking |
| YOLO11n | Pretrained object detection model |
| OpenCV | Video reading, frame processing, and video writing |
| ByteTrack | Multi-object tracking |
| BoT-SORT | Alternative multi-object tracking algorithm |
| NumPy | Numerical operations used by computer vision libraries |
| Git and GitHub | Version control and project hosting |

## 📂 Project Structure

```text
AI-Object-Detection-Tracking/
│
├── app.py
├── requirements.txt
└── README.md
```

### File Descriptions

- **`app.py`** — Contains the Streamlit interface, YOLO model loading, video processing, object tracking, and output download functionality.
- **`requirements.txt`** — Lists the Python libraries required to run the application.
- **`README.md`** — Contains project documentation and setup instructions.

The pretrained `yolo11n.pt` model is downloaded automatically by Ultralytics when it is not already available locally and the environment has internet access.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/AI-Object-Detection-Tracking.git
```

### Step 2: Navigate to the Project Folder

```bash
cd AI-Object-Detection-Tracking
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

Create a file named `requirements.txt` and add:

```text
streamlit
opencv-python
ultralytics
```

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

**Note:** Use a Python version supported by your installed Ultralytics, OpenCV, and PyTorch dependencies.

### Step 5: Run the Application

Make sure your Python file is named `app.py`.

Run:

```bash
python -m streamlit run app.py
```

The application will open in your default web browser.

## 🧠 How the Project Works

### 1. Upload a Video

The user uploads a video in one of the supported formats:

- MP4
- AVI
- MOV
- MKV

The application saves the uploaded video temporarily for processing.

### 2. Load the YOLO Model

The application loads the pretrained YOLO11n model.

YOLO detects objects in individual video frames and predicts their bounding boxes, class labels, and confidence scores.

The model is cached using Streamlit's `st.cache_resource` to avoid repeatedly loading it during normal Streamlit reruns.

### 3. Configure Detection Settings

Users can configure:

- **Detection Confidence:** Sets the minimum confidence threshold for detections.
- **Tracking Algorithm:** Selects ByteTrack or BoT-SORT.
- **People Only:** Limits detection to the person class when enabled.

A higher confidence threshold generally reduces low-confidence detections but may miss some objects.

### 4. Process Video Frames

OpenCV reads the uploaded video frame by frame.

For each frame, the YOLO model detects objects and the selected tracking algorithm attempts to maintain object identities across frames.

The application uses:

```python
results = model.track(
    source=frame,
    persist=True,
    tracker=tracker_name,
    conf=confidence,
    classes=classes,
    verbose=False
)
```

The `persist=True` parameter helps maintain tracking state between consecutive frames.

### 5. Draw Bounding Boxes

The model annotates the frame with detected object information, including bounding boxes, class labels, confidence scores, and tracking IDs when available.

The annotated frames are displayed in Streamlit and written to the output video.

### 6. Generate Detection Statistics

After processing, the application displays:

- **Frames Processed:** Number of video frames processed.
- **Total Detections:** Total number of detections across all processed frames.
- **Unique Tracking IDs:** Number of distinct tracking IDs observed.

Total detections count objects across frames, not necessarily distinct physical objects. Tracking IDs may also change when tracking is interrupted.

### 7. Preview and Download the Output

The application creates an annotated MP4 video.

Users can preview the processed video in the browser and download it as:

```text
tracked_output.mp4
```

## 🔄 System Workflow

```text
        Upload Video
             |
             v
       OpenCV Video Reader
             |
             v
      Extract Video Frames
             |
             v
       YOLO Object Detection
             |
             v
      ByteTrack / BoT-SORT
             |
             v
    Draw Boxes, Labels and IDs
             |
             v
       Display Video Frames
             |
             v
      Save Annotated Video
             |
             v
      Show Detection Summary
             |
             v
       Download Output Video
```

## 📊 Detection Summary

After processing the video, the application displays three metrics.

| Metric | Description |
|---|---|
| Frames Processed | Total number of successfully processed video frames |
| Total Detections | Total detections recorded across all frames |
| Unique Tracking IDs | Number of distinct tracking IDs observed during processing |

These metrics provide a basic summary of the processing results. They do not, by themselves, measure detection accuracy or tracking quality.

## 🚀 How to Use the Application

1. Install the required Python libraries.
2. Run the application using Streamlit.
3. Upload a supported video file.
4. Select the detection confidence threshold.
5. Choose ByteTrack or BoT-SORT.
6. Enable **Detect People Only** if you only want to detect people.
7. Click **Start Detection and Tracking**.
8. Monitor the frame-processing progress.
9. Review the detection summary.
10. Preview the processed video.
11. Click **Download Processed Video** to save the result.

## ⚠️ Limitations

- Processing speed depends on video resolution, video length, and available hardware.
- CPU processing may be slower than GPU-accelerated processing.
- Detection accuracy depends on the pretrained model and video quality.
- Objects may be missed in blurry, dark, crowded, or obstructed scenes.
- Tracking IDs can change when objects disappear or tracking is interrupted.
- The current application processes uploaded videos rather than directly streaming a live webcam.
- The application uses a pretrained model and does not train a custom YOLO model.
- The generated MP4 video uses the OpenCV `mp4v` codec, which may not be supported by every browser or media player.

## 🔮 Future Improvements

- Add live webcam detection.
- Integrate Deep SORT or another tracking algorithm.
- Support custom-trained YOLO models.
- Add object counting by class.
- Display FPS and processing time.
- Add detection statistics charts.
- Support more input and output video formats.
- Improve error handling for unsupported codecs.
- Add region-based object counting.
- Deploy the application online.

## 🎓 Learning Outcomes

This project demonstrates practical experience with:

- Artificial Intelligence.
- Computer Vision.
- Object Detection.
- YOLO models.
- Multi-Object Tracking.
- OpenCV video processing.
- ByteTrack and BoT-SORT.
- Bounding box visualization.
- Streamlit web application development.
- Python dependency management.

## 👩‍💻 Author

**Zarfshan Attiq Khan**

GitHub: Add your GitHub profile link here.

## 📄 License

This project is intended for educational and learning purposes. Add an appropriate open-source license if you plan to distribute the project publicly.