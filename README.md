# Ingredient Checker

## Overview
This Python script is a Streamlit-based web application designed to help users analyse product ingredients for specific keywords. It highlights the presence of silicones, sulfates, butters, proteins, and other selected ingredients in cosmetic or personal care products.

## Features
1. **Product Type Selection:**
  - Users can choose between Skincare, Makeup, and Haircare products.
  - Different checks are applied based on the selected product type.

2. **Ingredient Analysis:**
  - Users input a comma-separated list of ingredients.
  - The app identifies and highlights unwanted ingredients based on defined categories:
    - Silicones: keywords like "cone," "conol," etc.
    - Sulfates: keywords like "sulfate," "sulfonate," etc. (Haircare-specific).
    - Butters: keywords like "butter" (Haircare-specific).
    - Proteins: keywords like "keratin," "amino acids," etc. (Haircare-specific).
    - Warning ingredients: specific keywords (Haircare-specific).

3. **Ingredient Highlighting:**
  - Unwanted ingredients are color-coded for easy identification.
    - Amber: warning ingredients.
    - Red: unwanted ingredients.

4. **Detailed Messages:**
  - For Haircare products, the app generates detailed messages about the composition (e.g., whether it contains silicones and sulfates).
  - For other products, the app determines if they are silicone-based or water-based.

5. **User Controls:**
  - `Submit` button processes the input and displays results.
  - `Reset` button clears the input and resets selections.

## Usage
1. Run the script using Streamlit:
```streamlit run ingredient_checker.py```
2. Select the product type.
3. Enter a comma-separated list of ingredients.
4. Click `Submit` to analyse the ingredients.
5. View the highlighted ingredient list and the detailed composition message.
6. Use `Reset` to clear the inputs and start over.

## Dependencies
  - Python 3.x
  - Streamlit: Install using pip install streamlit

## Example Input
Product Type: Haircare
Ingredients: "Water, Dimethicone, Sodium Lauryl Sulfate, Shea Butter, Hydrolyzed Keratin"
