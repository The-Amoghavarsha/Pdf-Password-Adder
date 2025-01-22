# PDF Password Adder

This application allows you to add AES-256 encryption to your PDF files for enhanced security.

## Prerequisites

Ensure the following dependencies are installed:

1. **Python 3**: Required to run the script.
2. **Dependencies**: 
   - `python3-tk`: For GUI-based functionalities.
   - `qpdf`: For PDF processing.

### Installation Instructions

#### Debian-based Distributions (Ubuntu, Linux Mint, etc.)
Run the following command to install the required packages:
```bash
sudo apt install python3-tk qpdf
```

#### Other Linux Distributions
Use the package manager for your Linux distribution to install the required dependencies. Examples:

- **Fedora**:
  ```bash
  sudo dnf install python3-tkinter qpdf
  ```
- **Arch Linux**:
  ```bash
  sudo pacman -S python-tk qpdf
  ```

#### macOS
Install the dependencies using [Homebrew](https://brew.sh/):
```bash
brew install python-tk qpdf
```

#### Windows
1. Download and install **qpdf** from its [official releases page](https://github.com/qpdf/qpdf/releases).
2. Add the `qpdf` binary directory to your system's `PATH` environment variable:
   - Right-click on "This PC" or "My Computer" > Properties > Advanced system settings > Environment Variables.
   - Locate the `Path` variable, click Edit, and add the directory where `qpdf.exe` is located.
3. Install the Python dependency using `pip`:
   ```bash
   pip install tk
   ```

---

## Usage

After installing the dependencies, execute the script using the following command:

```bash
python3 pdf_password_adder.py
```

Once the script runs successfully, a **new AES-256 encrypted PDF file** will be generated, original file will be unaffected.
