##OrdinarySpace by Jannik Giera
##If your C Drive usage is at 100%, this tool is a must have
##It can organize files, clear up space, debloat Windows etc

import os
import sys
import time
import shutil


exit = False

print("Ordinary Space by Jannik Giera")
print("It is recommended to run this program as an administrator!")

def organize_files():
    compressed_files = ["zip", "rar", "7z", "tar", "gz", "iso"] #Compressed files
    document_files = ["doc", "docx", "pdf", "txt", "ppt", "pptx", "xls", "xlsx"] #Document files
    image_files = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg"] #Image files
    music_files = ["mp3", "wav", "flac", "ogg", "wma", "aac"] #Music files
    video_files = ["mp4", "avi", "mkv", "mov", "wmv", "flac", "webm"] #Video files
    misc_files = ["exe", "msi"] #Miscellaneous files
    filespace = 0

    def move_file(src, dest):
        try:
            shutil.move(src, dest)
        except Exception as e:
            print(f"Could not move {src} to {dest}: {e}")

    ##Organize Desktop
    print("Organizing Desktop....")
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    for file in os.listdir(desktop):
        src = os.path.join(desktop, file)
        if os.path.isdir(src):
            continue
        if file.endswith(tuple(compressed_files)):
            dest = os.path.join(desktop, "Compressed Files")
        elif file.endswith(tuple(document_files)):
            dest = os.path.join(desktop, "Document Files")
        elif file.endswith(tuple(image_files)):
            dest = os.path.join(desktop, "Image Files")
        elif file.endswith(tuple(music_files)):
            dest = os.path.join(desktop, "Music Files")
        elif file.endswith(tuple(video_files)):
            dest = os.path.join(desktop, "Video Files")
        elif file.endswith(tuple(misc_files)):
            dest = os.path.join(desktop, "Miscellaneous Files")
        else:
            dest = os.path.join(desktop, "Miscellaneous Files")
        if not os.path.exists(dest):
            os.makedirs(dest)
        move_file(src, dest)
    print("Desktop organized")

    ##Organize Downloads
    print("Organizing Downloads....")
    downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    for file in os.listdir(downloads):
        src = os.path.join(downloads, file)
        if os.path.isdir(src):
            continue
        if file.endswith(tuple(compressed_files)):
            dest = os.path.join(downloads, "Compressed Files")
        elif file.endswith(tuple(document_files)):
            dest = os.path.join(downloads, "Document Files")
        elif file.endswith(tuple(image_files)):
            dest = os.path.join(downloads, "Image Files")
        elif file.endswith(tuple(music_files)):
            dest = os.path.join(downloads, "Music Files")
        elif file.endswith(tuple(video_files)):
            dest = os.path.join(downloads, "Video Files")
        elif file.endswith(tuple(misc_files)):
            dest = os.path.join(downloads, "Miscellaneous Files")
        else:
            dest = os.path.join(downloads, "Miscellaneous Files")
        if not os.path.exists(dest):
            os.makedirs(dest)
        move_file(src, dest)
    print("Downloads organized")

    ##Organize Documents
    print("Organizing Documents....")
    documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
    for file in os.listdir(documents):
        src = os.path.join(documents, file)
        if os.path.isdir(src):
            continue
        if file.endswith(tuple(compressed_files)):
            dest = os.path.join(documents, "Compressed Files")
        elif file.endswith(tuple(document_files)):
            dest = os.path.join(documents, "Document Files")
        elif file.endswith(tuple(image_files)):
            dest = os.path.join(documents, "Image Files")
        elif file.endswith(tuple(music_files)):
            dest = os.path.join(documents, "Music Files")
        elif file.endswith(tuple(video_files)):
            dest = os.path.join(documents, "Video Files")
        elif file.endswith(tuple(misc_files)):
            dest = os.path.join(documents, "Miscellaneous Files")
        else:
            dest = os.path.join(documents, "Miscellaneous Files")
        if not os.path.exists(dest):
            os.makedirs(dest)
        move_file(src, dest)
    print("Documents organized")

    ##Organize Pictures
    print("Organizing Pictures....")
    pictures = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
    for file in os.listdir(pictures):
        src = os.path.join(pictures, file)
        if os.path.isdir(src):
            continue
        if file.endswith(tuple(compressed_files)):
            dest = os.path.join(pictures, "Compressed Files")
        elif file.endswith(tuple(document_files)):
            dest = os.path.join(pictures, "Document Files")
        elif file.endswith(tuple(image_files)):
            dest = os.path.join(pictures, "Image Files")
        elif file.endswith(tuple(music_files)):
            dest = os.path.join(pictures, "Music Files")
        elif file.endswith(tuple(video_files)):
            dest = os.path.join(pictures, "Video Files")
        elif file.endswith(tuple(misc_files)):
            dest = os.path.join(pictures, "Miscellaneous Files")
        else:
            dest = os.path.join(pictures, "Miscellaneous Files")
        if not os.path.exists(dest):
            os.makedirs(dest)
        move_file(src, dest)
    print("Pictures organized")

    ##Organize Music
    print("Organizing Music....")
    music = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music')
    for file in os.listdir(music):
        src = os.path.join(music, file)
        if os.path.isdir(src):
            continue
        if file.endswith(tuple(compressed_files)):
            dest = os.path.join(music, "Compressed Files")
        elif file.endswith(tuple(document_files)):
            dest = os.path.join(music, "Document Files")
        elif file.endswith(tuple(image_files)):
            dest = os.path.join(music, "Image Files")
        elif file.endswith(tuple(music_files)):
            dest = os.path.join(music, "Music Files")
        elif file.endswith(tuple(video_files)):
            dest = os.path.join(music, "Video Files")
        elif file.endswith(tuple(misc_files)):
            dest = os.path.join(music, "Miscellaneous Files")
        else:
            dest = os.path.join(music, "Miscellaneous Files")
        if not os.path.exists(dest):
            os.makedirs(dest)
        move_file(src, dest)
    print("Music organized")

    ##Organize Videos
    print("Organizing Videos....")
    videos = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')
    for file in os.listdir(videos):
        src = os.path.join(videos, file)
        if os.path.isdir(src):
            continue
        if file.endswith(tuple(compressed_files)):
            dest = os.path.join(videos, "Compressed Files")
        elif file.endswith(tuple(document_files)):
            dest = os.path.join(videos, "Document Files")
        elif file.endswith(tuple(image_files)):
            dest = os.path.join(videos, "Image Files")
        elif file.endswith(tuple(music_files)):
            dest = os.path.join(videos, "Music Files")
        elif file.endswith(tuple(video_files)):
            dest = os.path.join(videos, "Video Files")
        elif file.endswith(tuple(misc_files)):
            dest = os.path.join(videos, "Miscellaneous Files")
        else:
            dest = os.path.join(videos, "Miscellaneous Files")
        if not os.path.exists(dest):
            os.makedirs(dest)
        move_file(src, dest)
    print("Videos organized")

    ##Calculate Space from the created folders on Desktop, Downloads, Documents, Pictures, Music, Videos that are previously created
    def get_folder_size(folder):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    folders = [
        os.path.join(desktop, "Compressed Files"),
        os.path.join(desktop, "Document Files"),
        os.path.join(desktop, "Image Files"),
        os.path.join(desktop, "Music Files"),
        os.path.join(desktop, "Video Files"),
        os.path.join(desktop, "Miscellaneous Files"),
        os.path.join(downloads, "Compressed Files"),
        os.path.join(downloads, "Document Files"),
        os.path.join(downloads, "Image Files"),
        os.path.join(downloads, "Music Files"),
        os.path.join(downloads, "Video Files"),
        os.path.join(downloads, "Miscellaneous Files"),
        os.path.join(documents, "Compressed Files"),
        os.path.join(documents, "Document Files"),
        os.path.join(documents, "Image Files"),
        os.path.join(documents, "Music Files"),
        os.path.join(documents, "Video Files"),
        os.path.join(documents, "Miscellaneous Files"),
        os.path.join(pictures, "Compressed Files"),
        os.path.join(pictures, "Document Files"),
        os.path.join(pictures, "Image Files"),
        os.path.join(pictures, "Music Files"),
        os.path.join(pictures, "Video Files"),
        os.path.join(pictures, "Miscellaneous Files"),
        os.path.join(music, "Compressed Files"),
        os.path.join(music, "Document Files"),
        os.path.join(music, "Image Files"),
        os.path.join(music, "Music Files"),
        os.path.join(music, "Video Files"),
        os.path.join(music, "Miscellaneous Files"),
        os.path.join(videos, "Compressed Files"),
        os.path.join(videos, "Document Files"),
        os.path.join(videos, "Image Files"),
        os.path.join(videos, "Music Files"),
        os.path.join(videos, "Video Files"),
        os.path.join(videos, "Miscellaneous Files")
    ]

    for folder in folders:
        if os.path.exists(folder):
            size = get_folder_size(folder)
            print(f"{folder} size: {size / (1024 * 1024):.2f} MB")
            filespace += size ##Add the size of the folder to the total size
        else:
            print(f"{folder} does not exist")

            ##Print the total size of the files
    print(f"Total size of files: {filespace / (1024 * 1024 * 1024):.2f} GB")

def clear_space():
    ##Clear Temp (Skip file or folder that is currently in use)
    print("Clearing Temp....")
    temp = os.path.join(os.environ['TEMP'])
    def delete_folder_contents(folder):
        total_deleted_size = 0
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(file_path)
                    os.remove(file_path)
                    total_deleted_size += file_size
                except Exception as e:
                    print(f"Could not delete {file_path}: {e}")
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path)
                except Exception as e:
                    print(f"Could not delete {dir_path}: {e}")
        return total_deleted_size

    deleted_size = delete_folder_contents(temp)
    print(f"Cleared Temp. Space saved: {deleted_size / (1024 * 1024):.2f} MB")

    ##Clear Prefetch
    print("Clearing Prefetch....")
    prefetch = os.path.join("C:\\Windows\\Prefetch")
    deleted_size = delete_folder_contents(prefetch)
    print(f"Cleared Prefetch. Space saved: {deleted_size / (1024 * 1024):.2f} MB")

    ##Clear Windows Update Cache
    print("Clearing Windows Update Cache....")
    windows_update_cache = os.path.join("C:\\Windows\\SoftwareDistribution\\Download")
    deleted_size = delete_folder_contents(windows_update_cache)
    print(f"Cleared Windows Update Cache. Space saved: {deleted_size / (1024 * 1024):.2f} MB")

    ##Clear Windows Error Reporting
    print("Clearing Windows Error Reporting....")
    windows_error_reporting = os.path.join("C:\\ProgramData\\Microsoft\\Windows\\WER")
    deleted_size = delete_folder_contents(windows_error_reporting)
    print(f"Cleared Windows Error Reporting. Space saved: {deleted_size / (1024 * 1024):.2f} MB")

    ##Clear Windows Temp
    print("Clearing Windows Temp....")
    windows_temp = os.path.join("C:\\Windows\\Temp")
    deleted_size = delete_folder_contents(windows_temp)
    print(f"Cleared Windows Temp. Space saved: {deleted_size / (1024 * 1024):.2f} MB")

    ##Clear Recycle Bin
    print("Clearing Recycle Bin....")
    os.system("rd /s /q C:\\$Recycle.Bin")
    print("Cleared Recycle Bin")

def debloat_windows():
    print("Debloating Windows...")
    # Remove unnecessary Windows apps
    apps_to_remove = [
        "Microsoft.3DBuilder",
        "Microsoft.BingWeather",
        "Microsoft.GetHelp",
        "Microsoft.Getstarted",
        "Microsoft.Messaging",
        "Microsoft.Microsoft3DViewer",
        "Microsoft.MicrosoftOfficeHub",
        "Microsoft.MicrosoftSolitaireCollection",
        "Microsoft.MicrosoftStickyNotes",
        "Microsoft.MixedReality.Portal",
        "Microsoft.Office.OneNote",
        "Microsoft.OneConnect",
        "Microsoft.People",
        "Microsoft.Print3D",
        "Microsoft.SkypeApp",
        "Microsoft.Wallet",
        "Microsoft.WindowsAlarms",
        "Microsoft.WindowsFeedbackHub",
        "Microsoft.WindowsMaps",
        "Microsoft.WindowsSoundRecorder",
        "Microsoft.Xbox.TCUI",
        "Microsoft.XboxApp",
        "Microsoft.XboxGameOverlay",
        "Microsoft.XboxGamingOverlay",
        "Microsoft.XboxIdentityProvider",
        "Microsoft.XboxSpeechToTextOverlay",
        "Microsoft.YourPhone",
        "Microsoft.ZuneMusic",
        "Microsoft.ZuneVideo",
        
        "Microsoft.Clipchamp",
        "Microsoft.LinkedInforWindows",

       
        "Microsoft.Office.Outlook"
    ]
    for app in apps_to_remove:
        os.system(f"powershell -Command \"Get-AppxPackage *{app}* | Remove-AppxPackage\"")
        print(f"Removed {app}")

    # Disable unnecessary Windows features
    features_to_disable = [
        "Internet-Explorer-Optional-amd64", 
        "Printing-XPSServices-Features"
    ]
    for feature in features_to_disable:
        os.system(f"dism /online /disable-feature /featurename:{feature}")
        print(f"Disabled {feature}")

    print("Windows debloated successfully.")

def show_c_drive_health():
    ##Show C Drive Health
    print("Showing C Drive Health....")
    os.system("wmic diskdrive get status")
    os.system("wmic diskdrive get statusinfo")
    os.system("wmic diskdrive get operationalstatus")

def blankStart(): #Disables all the start up programs that are not necessary by Windows
    print("This feature will disable all the start up programs that are not necessary by Windows")
    print("By disabling all the start up programs, it will make your computer boot faster and run faster")
    print("Do you want to continue? y/n")
    option = input("Option: ")
    if option == "y":
        try:
            # Corrected the PowerShell command with proper quote escaping
            os.system("""powershell -Command "Get-CimInstance Win32_StartupCommand | Where-Object { $_.Caption -notmatch 'Microsoft|Windows' } | ForEach-Object { Set-ItemProperty -Path HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run -Name $($_.Name) -Value '' }" """)

            print("All startup programs have been disabled.")
            print("Would you like to restart your computer to apply the changes? y/n")
            option = input("Option: ")
            if option == "y":
                os.system("shutdown /r /t 0")
            elif option == "n":
                print("Restart cancelled")
            else:
                print("Invalid option. Using n option")
        except Exception as e:
            print(f"An error occurred while disabling startup programs: {e}")
    elif option == "n":
        print("Blank start cancelled")
    else:
        print("Invalid option")


def schnazzell(): ##Fun Feature to make promo of my friend Schnazzell aka Lucas
    print("You curious about Schnazzell? y/n")
    option = input("Option: ")
    if option == "y":
        print("Opening all the Socials from Schnazzell")
        os.system("start https://www.twitch.tv/schnazzell")
        os.system("start https://www.youtube.com/@GuitaristMetallica")
        os.system("start https://x.com/General_Duck97?mx=2")
        os.system("start https://www.instagram.com/general_duck97")

    elif option == "n":
        print("You are missing out on Schnazzell. He motivated me to make this code")
    else:
        print("Invalid option")

def duplicatefilefinder(): ##Duplicate File Finder, goes through all the files in Desktop, Downloads, Documents, Pictures, Music, Videos and find the duplicate files.
    print("Finding files that are duplicates....")
    folders = [
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'),
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'),
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents'),
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures'),
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music'),
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')
    ]
    files = []
    duplicates = []
    for folder in folders:
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path):
                    files.append(file_path)
    for file in files:
        if files.count(file) > 1:
            duplicates.append(file)
    print("Duplicate files:")
    for duplicate in duplicates:
        print(duplicate)

    print("Would you like to delete the duplicate files? y/n")
    option = input("Option: ")
    if option == "y":
        for duplicate in duplicates:
            os.remove(duplicate)
            print(f"Deleted {duplicate}")
    elif option == "n":
        print("Duplicate files not deleted")
    else:
        print("Invalid option")


def largefilefinder(): #goes through all the files and folders in Desktop, Downloads, Documents, Pictures, Music, Videos and find the files that are larger than 500 MB or more
    print("Finding files that are larger than 500 MB....")
    folders = [
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'),
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'),
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents'),
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures'),
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music'),
        os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')
    ]
    for folder in folders:
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path):
                    if os.path.getsize(file_path) > 500 * 1024 * 1024:
                        print(f"{file_path} is larger than 500 MB")

    print("would you like to delete the files that are larger than 500 MB? y/n")
    option = input("Option: ")
    if option == "y":
        for folder in folders:
            for root, dirs, filenames in os.walk(folder):
                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    if os.path.isfile(file_path):
                        if os.path.getsize(file_path) > 500 * 1024 * 1024:
                            os.remove(file_path)
                            print(f"Deleted {file_path}")
    elif option == "n":
        print("Files that are larger than 500 MB not deleted")
    else:
        print("Invalid option")


def browsercachecleaner(): #Clears the cache of the browsers that are installed on the computer
    print("Clearing browser cache....")
    browsers = [
        os.path.join(os.environ['LOCALAPPDATA'], 'Google\\Chrome\\User Data\\Default\\Cache'),
        os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft\\Edge\\User Data\\Default\\Cache'),
        os.path.join(os.environ['LOCALAPPDATA'], 'Mozilla\\Firefox\\Profiles'),
        os.path.join(os.environ['LOCALAPPDATA'], 'BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache'),
        os.path.join(os.environ['APPDATA'], 'Opera Software\\Opera Stable\\Cache'),
        os.path.join(os.environ['APPDATA'], 'Opera Software\\Opera GX Stable\\Cache')
    ]

    for browser in browsers:
        if os.path.exists(browser):
            shutil.rmtree(browser)
            print(f"Cleared {browser}")
        else:
            print(f"{browser} does not exist")














while exit == False:
    print("Choose an option:")
    print("1. Organize files (That Includes Desktop, Downloads, Documents, Pictures, Music, Videos)")
    print("2. Clear up space (That Includes Temp, Prefetch, Windows Update Cache, Windows Error Reporting, Windows Temp, Recycle Bin)")
    print("3. Debloat Windows (That Includes Windows Apps, Windows Features, Windows Updates)")
    print("4. Show C Drive Health")
    print("5. Blank Start (Disables all the start up programs that are not necessary by Windows)")
    print("6. Schnazzell (Promo of my friend Schnazzell)")
    print("7. Duplicate File Finder")
    print("8. Large File Finder")
    print("9. Browser Cache Cleaner")
    print("10. Exit")

   
    option = input("Option: ")
    if option == "1":
        organize_files()
    elif option == "2":
        clear_space()
    elif option == "3":
        debloat_windows()
    elif option == "4":
        show_c_drive_health()
    elif option == "5":
        blankStart()
    elif option == "6":
        schnazzell()
    elif option == "7":
        duplicatefilefinder()
    elif option == "8":
        largefilefinder()
    elif option == "9":
        browsercachecleaner()
    elif option == "10":
        exit = True



        
    else:
        print("Invalid option")
