import winreg
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def uninstall_context_menu():
    # Registry path used in installation
    key_path = r"Directory\Background\shell\PasteToJPG"
    
    print("Attempting to uninstall 'Paste to JPG' context menu...")
    
    if not is_admin():
        print("\n[!] WARNING: This script usually requires Administrator privileges to modify the registry.")
        print("If it fails, please run this script as Administrator.")
    
    try:
        # Connect to HKEY_CLASSES_ROOT
        root = winreg.HKEY_CLASSES_ROOT
        
        # WinReg DeleteKey cannot delete keys with subkeys.
        # We must delete the 'command' subkey first.
        try:
            # Try to open the key to verify it exists
            key = winreg.OpenKey(root, key_path, 0, winreg.KEY_READ)
            winreg.CloseKey(key)
            
            # Delete 'command' subkey
            try:
                winreg.DeleteKey(root, key_path + r"\command")
                print(f" - Deleted subkey: {key_path}\\command")
            except FileNotFoundError:
                pass # Subkey might be missing, proceed
            
            # Delete the main key
            winreg.DeleteKey(root, key_path)
            print(f" - Deleted key: {key_path}")
            
            print("\n[SUCCESS] Context menu item removed successfully.")
            
        except FileNotFoundError:
            print(f"\n[INFO] The key '{key_path}' was not found. It may have already been uninstalled.")
            
    except PermissionError:
        print("\n[ERROR] Permission denied. Access is denied to the registry.")
        print("Please right-click this script and select 'Run as Administrator'.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    uninstall_context_menu()
    # Pause to let user read output
    input("\nPress Enter to exit...")
