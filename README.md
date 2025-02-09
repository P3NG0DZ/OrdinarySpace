# OrdinarySpace by Jannik Giera

OrdinarySpace is a powerful tool designed to help you manage and optimize your Windows system. Whether your C Drive usage is at 100% or you just want to organize your files, clear up space, or debloat Windows, this tool has got you covered.

## Features

- **Organize Files**: Automatically organizes files on your Desktop, Downloads, Documents, Pictures, Music, and Videos folders into categorized subfolders.
- **Clear Up Space**: Clears temporary files, prefetch data, Windows Update cache, Windows Error Reporting, and the Recycle Bin to free up space.
- **Debloat Windows**: Removes unnecessary Windows apps and disables unnecessary Windows features to optimize system performance.
- **Show C Drive Health**: Displays the health status of your C Drive.
- **Blank Start**: Disables unnecessary startup programs to speed up boot time.
- **Duplicate File Finder**: Finds and helps you delete duplicate files in your system.
- **Large File Finder**: Identifies files larger than 500 MB, allowing you to delete them if needed.
- **Browser Cache Cleaner**: Clears cache from popular browsers like Chrome, Edge, Firefox, Brave, and Opera.

## How to Run

### Running in Python

1. **Prerequisites**:
   - Ensure you have Python installed on your system.
   - Install the required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the Script**:
   - **Run as Administrator**: It is highly recommended to run the script with administrator privileges to ensure it has the necessary permissions to perform system operations.
   - Navigate to the project directory.
   - Run the script using Python with administrator rights:
     ```bash
     python main.py
     ```
     - On Windows, you can open Command Prompt or PowerShell as an administrator and then run the above command.

### Running as an Executable (EXE)

1. **Prerequisites**:
   - Ensure you have the `dist` directory in your project folder.
   - Locate the `OrdinarySpace.exe` file inside the `dist` directory.

2. **Running the Executable**:
   - **Run as Administrator**: Always run the executable with administrator privileges to ensure it can perform system-level operations.
   - Right-click the `OrdinarySpace.exe` file and select "Run as administrator".
   - Alternatively, you can run it from the command line with elevated privileges:
     ```bash
     ./dist/OrdinarySpace.exe
     ```
     - Open Command Prompt or PowerShell as an administrator and then run the above command.

## Troubleshooting

### Windows Defender Marks the EXE as a Virus

Windows Defender or other antivirus software might flag the executable as a potential threat due to its file manipulation capabilities. Here’s what you can do:

1. **Add an Exception**:
   - Open Windows Defender.
   - Go to "Virus & threat protection" > "Manage settings" > "Exclusions".
   - Add the `OrdinarySpace.exe` file or the entire `dist` directory as an exclusion.

2. **Verify the Source**:
   - Ensure that the executable was downloaded from a trusted source or built from the provided source code.

3. **Run as Administrator**:
   - Always run the executable with administrator rights to ensure it has the necessary permissions to perform system operations.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- **Schnazzell**: A special thanks to Schnazzell (Lucas) for motivating the creation of this tool. Check out his socials:
  - [Twitch](https://www.twitch.tv/schnazzell)
  - [YouTube](https://www.youtube.com/@GuitaristMetallica)
  - [Twitter](https://x.com/General_Duck97?mx=2)
  - [Instagram](https://www.instagram.com/general_duck97)

---

**Note**: Always run this tool with caution, especially when performing operations like file deletion or system debloating. Make sure to back up important data before proceeding. **Always run the tool as an administrator to ensure it has the necessary permissions to perform system-level operations.**