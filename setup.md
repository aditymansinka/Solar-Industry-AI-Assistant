Here are the **Local Setup Instructions** for your **Solar Industry AI Assistant** project, formatted as requested:

---

# Local Setup Instructions

## 1. Prerequisites

* Python 3.13 installed (or your project's required Python version)
* Git (optional, if cloning from a repo)
* (Optional) Streamlit-compatible environment for running the app

---

## 2. Clone the Repository (Optional)

```bash
git clone https://github.com/aditymansinka/Solar-Industry-AI-Assistant.git
cd Solar-Rooftop-AI-Assistant
```

---

## 3. Create and Activate a Virtual Environment

On Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

On macOS/Linux (bash):

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

---

## 6. Notes

* Upload satellite rooftop images in `.jpg`, `.jpeg`, `.png`, or `.webp` formats.
* Internet is not required for basic functionality (as the analysis is simulated locally).
* If you encounter issues with image formats or rendering, ensure `Pillow` and `matplotlib` are properly installed.
* Sample input images may be found in the `Examples/` directory (if provided).


