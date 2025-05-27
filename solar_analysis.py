import random

def analyze_image(image):
    # Simulate dynamic usable space (in %)
    usable_space = random.randint(50, 90)

    # Estimate number of panels (assuming 1 panel per 5 sq.m)
    panel_count = usable_space // 5 + random.choice([0, 1, -1])

    # Simulate panel wattage options and orientation
    panel_wattage = random.choice([350, 400, 450])
    orientation = random.choice(["South-facing", "East-facing", "West-facing"])

    # Randomized ROI (years)
    roi = round(random.uniform(2.5, 6.5), 2)

    # Simulate energy source breakdown
    solar = random.randint(50, 80)
    grid = random.randint(0, 40 - (solar - 50))  # ensure total stays ~100
    battery = 100 - solar - grid

    summary = f"This rooftop has approximately {usable_space}% usable space for solar installation."
    recommendation = f"Install {panel_count} panels of {panel_wattage}W each. {orientation} recommended."

    energy_breakdown = {
        "Solar": solar,
        "Grid": grid,
        "Battery Storage": battery
    }

    return {
        "summary": summary,
        "recommendation": recommendation,
        "roi": roi,
        "energy_breakdown": energy_breakdown
    }
