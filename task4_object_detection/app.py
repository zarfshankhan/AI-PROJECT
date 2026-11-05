import streamlit as st
import cv2
import os
import tempfile
import time
from ultralytics import YOLO

# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="AI Object Detection & Tracking",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Object Detection and Tracking")
st.write(
    "Upload a video to detect and track objects using YOLO "
    "and ByteTrack."
)

# =========================================
# LOAD YOLO MODEL
# =========================================

@st.cache_resource
def load_model():
    return YOLO("yolo11n.pt")


# =========================================
# SIDEBAR SETTINGS
# =========================================

st.sidebar.header("⚙️ Settings")

confidence = st.sidebar.slider(
    "Detection Confidence",
    min_value=0.10,
    max_value=0.90,
    value=0.35,
    step=0.05
)

tracker_name = st.sidebar.selectbox(
    "Tracking Algorithm",
    ["bytetrack.yaml", "botsort.yaml"]
)

people_only = st.sidebar.checkbox(
    "Detect People Only",
    value=False
)

# =========================================
# VIDEO UPLOAD
# =========================================

uploaded_video = st.file_uploader(
    "📹 Upload a Video",
    type=["mp4", "avi", "mov", "mkv"]
)

# =========================================
# PROCESS VIDEO
# =========================================

if uploaded_video is not None:

    st.success(f"Uploaded: {uploaded_video.name}")

    st.subheader("Original Video")

    st.video(uploaded_video)

    if st.button(
        "🚀 Start Detection and Tracking",
        type="primary"
    ):

        progress_bar = st.progress(0)
        status_text = st.empty()

        input_path = None
        output_path = None
        cap = None
        writer = None

        try:
            # Load model
            status_text.info("Loading YOLO model...")
            model = load_model()

            # Save uploaded video temporarily
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp4"
            ) as input_file:

                input_file.write(uploaded_video.getvalue())
                input_path = input_file.name

            # Create output file
            output_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp4"
            )

            output_path = output_file.name
            output_file.close()

            # Open video
            cap = cv2.VideoCapture(input_path)

            if not cap.isOpened():
                raise ValueError(
                    "Unable to open the uploaded video."
                )

            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(
                cap.get(cv2.CAP_PROP_FRAME_COUNT)
            )

            if fps <= 0 or fps > 120:
                fps = 25.0

            if width <= 0 or height <= 0:
                raise ValueError("Invalid video dimensions.")

            # Create output video writer
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")

            writer = cv2.VideoWriter(
                output_path,
                fourcc,
                fps,
                (width, height)
            )

            if not writer.isOpened():
                raise RuntimeError(
                    "Could not create the output video."
                )

            # Tracking settings
            classes = [0] if people_only else None

            frame_number = 0
            total_detections = 0
            unique_track_ids = set()

            # Display placeholders
            frame_display = st.empty()

            st.subheader("🔍 Detection Results")

            # Process every video frame
            while True:

                success, frame = cap.read()

                if not success:
                    break

                # Detect and track objects
                results = model.track(
                    source=frame,
                    persist=True,
                    tracker=tracker_name,
                    conf=confidence,
                    classes=classes,
                    verbose=False
                )

                result = results[0]

                # Draw bounding boxes, labels and tracking IDs
                annotated_frame = result.plot()

                # Count detections
                if result.boxes is not None:

                    total_detections += len(result.boxes)

                    if result.boxes.id is not None:

                        ids = (
                            result.boxes.id
                            .int()
                            .cpu()
                            .tolist()
                        )

                        unique_track_ids.update(ids)

                # Save annotated frame
                writer.write(annotated_frame)

                # Show processed frame in Streamlit
                rgb_frame = cv2.cvtColor(
                    annotated_frame,
                    cv2.COLOR_BGR2RGB
                )

                frame_display.image(
                    rgb_frame,
                    channels="RGB",
                    use_container_width=True
                )

                frame_number += 1

                # Update progress
                if total_frames > 0:

                    progress = min(
                        frame_number / total_frames,
                        1.0
                    )

                    progress_bar.progress(progress)

                    status_text.info(
                        f"Processing frame {frame_number} "
                        f"of {total_frames}..."
                    )

            # Release video resources
            cap.release()
            cap = None

            writer.release()
            writer = None

            progress_bar.progress(1.0)

            status_text.success(
                "Video processing completed successfully!"
            )

            # =====================================
            # RESULTS SUMMARY
            # =====================================

            st.subheader("📊 Detection Summary")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Frames Processed",
                frame_number
            )

            col2.metric(
                "Total Detections",
                total_detections
            )

            col3.metric(
                "Unique Tracking IDs",
                len(unique_track_ids)
            )

            # =====================================
            # DISPLAY PROCESSED VIDEO
            # =====================================

            st.subheader("🎬 Processed Video")

            with open(output_path, "rb") as video_file:

                video_bytes = video_file.read()

            st.video(video_bytes)

            # =====================================
            # DOWNLOAD OUTPUT
            # =====================================

            st.download_button(
                label="⬇️ Download Processed Video",
                data=video_bytes,
                file_name="tracked_output.mp4",
                mime="video/mp4",
                type="primary"
            )

        except Exception as error:

            st.error(f"An error occurred: {error}")

        finally:

            if cap is not None:
                cap.release()

            if writer is not None:
                writer.release()

            # Remove temporary files
            for path in [input_path, output_path]:

                if path and os.path.exists(path):

                    try:
                        os.remove(path)
                    except OSError:
                        pass

else:

    st.info(
        "Please upload a video file to start object detection."
    )

    st.markdown(
        """
        ### ✨ Project Features

        - 🎯 YOLO object detection
        - 📦 Bounding boxes and confidence scores
        - 🆔 Object tracking IDs
        - 🚶 Optional people-only detection
        - 📊 Detection statistics
        - 🎬 Processed video preview
        - ⬇️ Download processed video
        """
    )