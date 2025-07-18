from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).resolve().parent
    
    RAW_DATA_DIR = BASE_DIR / 'data' / 'raw'
    CLEAN_DATA_DIR = BASE_DIR / 'data' / 'meta_data'
    FRAMES_DIR = BASE_DIR / 'data' / 'frames'
    CLEAN_VID_DIR = BASE_DIR / 'data' / 'cleaned'

    # Accepted video file extensions (extend if needed)
    VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".m4v", ".webm"}
    MIN_WIDTH = 1280    
    TARGET_CODEC = 'mp4v' 
    TARGET_FPS = None      
    FRAME_EXT = ".png"                  
    JPEG_QUALITY = 95                   
