import sys
import os
import ctypes
from datetime import datetime

# Helper to show message box if something goes wrong (since we have no console)
def show_message(title, message, is_error=False):
    # 0 = OK button only
    # 0x10 = Icon Hand (Error)
    # 0x40 = Icon Information
    style = 0x10 if is_error else 0x40
    ctypes.windll.user32.MessageBoxW(0, message, title, style)

try:
    from PIL import ImageGrab, Image
except ImportError:
    show_message("Paste to JPG Error", "Pillow library not found.\nPlease run 'pip install Pillow' in terminal.", True)
    sys.exit(1)

def main():
    # Context menu passes current directory via "%V"
    if len(sys.argv) > 1:
        # The argument usually comes with quotes if there are spaces, strip just in case
        target_dir = sys.argv[1].strip('"')
    else:
        # Fallback to current working directory
        target_dir = os.getcwd()

    try:
        # Grab image from clipboard
        img = ImageGrab.grabclipboard()
        
        if isinstance(img, Image.Image):
            # Generate unique filename based on timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"paste_{timestamp}.jpg"
            file_path = os.path.join(target_dir, filename)
            
            # Save as JPEG
            # Convert to RGB to support removing alpha channel if present (PNG -> JPG)
            if img.mode in ("RGBA", "P"): 
                img = img.convert("RGB")
                
            # Save as JPEG with maximum quality
            # quality=100: Best quality, least compression
            # subsampling=0: 4:4:4 (no chroma subsampling), sharpest color details
            img.save(file_path, "JPEG", quality=100, subsampling=0)
            # Silent success - no console, no popup
            
        elif isinstance(img, list):
            show_message("Paste to JPG", "Clipboard contains files, not raw image data.\nPlease copy the image content (right-click image -> Copy) directly.", True)
        else:
            show_message("Paste to JPG", "Clipboard does not contain image data.", True)
            
    except Exception as e:
        show_message("Paste to JPG Error", f"Failed to save image:\n{str(e)}", True)

if __name__ == "__main__":
    main()
