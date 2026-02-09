import os
import sys
import winreg

def install_context_menu():
    # Registry path for "Directory Background" context menu
    reg_path = r"Directory\Background\shell\PasteToJPG"
    
    # 1. Get current python executable and script path
    # Use pythonw.exe to suppress console window
    python_dir = os.path.dirname(sys.executable)
    pythonw_exe = os.path.join(python_dir, "pythonw.exe")
    
    # Fallback to python.exe if pythonw.exe is not found (unlikely)
    if not os.path.exists(pythonw_exe):
        pythonw_exe = sys.executable

    # The script to run
    script_path = os.path.abspath("paste_image.py")
    
    # Check if script exists
    if not os.path.exists(script_path):
        print(f"Error: Could not find script at {script_path}")
        return False
        
    try:
        # 2. Create the main Key for the context menu item
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, reg_path)
        
        # 3. Set the display name
        winreg.SetValue(key, "", winreg.REG_SZ, "Paste as JPG Image")
        
        # 4. Set an icon (imageres.dll,-5301 looks like an image file)
        winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, "imageres.dll,-5301")
        
        # 5. Create the "command" subkey
        cmd_key = winreg.CreateKey(key, "command")
        
        # 6. Set the command to run
        # Use pythonw.exe for silent execution (no console window)
        command = f'"{pythonw_exe}" "{script_path}" "%V"'
        winreg.SetValue(cmd_key, "", winreg.REG_SZ, command)
        
        print("\nSuccessfully added 'Paste as JPG Image' to context menu!")
        print(f"Linked to script: {script_path}")
        print("\nNOTE: You can now right-click in any folder background and select 'Paste as JPG Image'.")
        return True
        
    except PermissionError:
        print("\nERROR: Admin privileges required to modify registry.")
        print("Please run this script as Administrator.")
        return False
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        return False

if __name__ == "__main__":
    install_context_menu()
    input("\nPress Enter to exit...")
