# ☀️ AI Powered Solar Rooftop Analyzer

An AI-powered Streamlit tool to analyze rooftop solar potential using satellite imagery. It simulates rooftop area usability, panel installation recommendations, ROI estimates, and energy source breakdown with visualizations.

---

## 🚀 Project Setup Instructions

### Prerequisites
- Python 3.10 or newer
- `pip` package manager

### Installation Steps

```bash
# 1. Clone the repository or unzip the project folder
cd clone https://github.com/aditymansinka/Solar-Industry-AI-Assistant.git
cd Solar-Rooftop-AI-Assistant

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit application
streamlit run app.py
```

**Notes:**  
- Supported image formats: `.jpg`, `.png`, `.jpeg`, `.webp`.  
- Ensure all required packages from `requirements.txt` are installed.

---

## ⚙️ Implementation Documentation

### Overview

This application simulates analysis of rooftop satellite imagery to provide solar panel installation suggestions and projected energy statistics.

### Main Components

1. **`solar_analysis.py`**  
   - `analyze_image(image)` simulates:
     - Usable rooftop area (50–90%).
     - Panel count and wattage recommendation.
     - ROI (2.5–6.5 years).
     - Energy source distribution (solar, grid, battery).
     - Returns result dictionary with summary and visual data.

2. **`image_utils.py`**  
   - `load_image()` — Loads image using PIL.  
   - `display_pie_chart()` — Displays energy source split with a pie chart.

3. **`app.py`**  
   - Streamlit-based UI:
     - Upload image.
     - Display image preview.
     - Button triggers analysis using `analyze_image`.
     - Displays ROI, recommendation, and pie chart of energy source breakdown.

### Technology Stack

- Python 3.10+  
- Streamlit  
- Pillow (image handling)  
- Matplotlib (visualization)

---

## 💡 Example Use Case

### Use Case: Assessing Rooftop for Solar Installation

**Scenario:**  
A user uploads a rooftop image to estimate solar potential.

**Sample Output:**

![Sample Output Screenshot](solar1.png)
![Sample Output Screenshot](solar2.png)
![Sample Output Screenshot](solar3.png)
![Sample Output Screenshot](solar4.png)

**Interpretation:**  
- Estimated 81% usable rooftop space.  
- Suggested 15 panels of 350W each.  
- Orientation: South-facing.  
- Estimated ROI: 6.45 years.  
- Solar contribution: 55%, Grid: 14%, Battery: 31%.

---

## 🔮 Future Improvement Suggestions

1. **Vision-based Rooftop Detection**  
   - Integrate AI/ML models (e.g., YOLOv8) for boundary detection.

2. **Map-Based Data Overlay**  
   - Include GIS layers using OpenStreetMap or Google Maps APIs.

3. **Exportable Reports**  
   - Enable PDF generation summarizing all output values.

4. **Net Metering & Incentives**  
   - Include economic policies and user-based incentive estimations.

5. **Mobile Optimization**  
   - Create mobile app version for on-site assessments.

---

## 📦 Project Deliverables

| Deliverable                  | Status |
|-----------------------------|--------|
| Complete codebase           | ✔️     |
| Analysis UI & output chart  | ✔️     |
| Sample run demonstration    | ✔️     |
| Setup guide & README        | ✔️     |

---



