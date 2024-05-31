import streamlit as st

# Define a function to check ingredients
def check_ingredients(product_type, ingredients):
    # Define lists of keywords to search for in the ingredients
    silicones = ["cone", "conol", "silane", "siloxane"]
    sulfates = ["sulfate", "sulfonate", "sulfoacetate", "sulfo", "sulfo succinate"]
    butters = ["butter"]
    protein = ["protein", "wheat protein", "keratin", "soy protein", "amino acids", "collagen", "milk protein",
               "casein", "oat flour", "rice protein", "amaranthus", "baobab"]
    amber_ingredients = ["behentrimonium methosulfate"]

    # Initilise lists to store found ingredients
    found_silicones = []
    found_sulfates = []
    found_butters = []
    found_protein = []
    found_amber = []

    # Split the input string into individual ingredients
    original_ingredients_list = [ingredient.strip() for ingredient in ingredients.split(",")]
    # Convert input string to lowercase for case-insensitive matching
    ingredients_list_lower = [ingredient.lower() for ingredient in original_ingredients_list]

    # Loop through each ingredient to check for keywords
    for ingredient_lower, ingredient in zip(ingredients_list_lower, original_ingredients_list):
        # Check if any silicone keyword is in the ingredient
        if any(silicone in ingredient_lower for silicone in silicones):
            found_silicones.append(ingredient)
        # Check for special handling if the product type is Haircare
        if product_type == "Haircare":
            if ingredient_lower in amber_ingredients:
                found_amber.append(ingredient)
            elif any(sulfate in ingredient_lower for sulfate in sulfates):
                found_sulfates.append(ingredient)
            if any(butter in ingredient_lower for butter in butters):
                found_butters.append(ingredient)
            if any(protein in ingredient_lower for protein in protein):
                found_protein.append(ingredient)

    # Return lists of found ingredients and the original list
    return found_silicones, found_sulfates, found_butters, found_protein, found_amber, original_ingredients_list

# Initialize session state variables for Steamlit
if 'product_type' not in st.session_state:
    st.session_state.product_type = "Skincare"
if 'ingredients' not in st.session_state:
    st.session_state.ingredients = ""
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Streamlit interface setup
st.title("Ingredient Checker")

# Functions to handle submit and reset actions
def submit_action():
    st.session_state.submitted = True

def reset_action():
    st.session_state.submitted = False
    st.session_state.product_type = "Skincare"
    st.session_state.ingredients = ""

# Create the product type selection box
st.session_state.product_type = st.selectbox("Type of product:", ["Skincare", "Makeup", "Haircare"],
                                             index=["Skincare", "Makeup", "Haircare"].index(
                                                 st.session_state.product_type))
# Create the text area for entering ingredients
st.session_state.ingredients = st.text_area("Enter ingredients (separated by commas):", st.session_state.ingredients)

# Create the Submit and Reset buttons
col1, col2 = st.columns([1, 0.115])
with col1:
    st.button("Submit", on_click=submit_action)
with col2:
    st.button("Reset", on_click=reset_action)

# Process the input when the form is submitted
if st.session_state.submitted:
    ingredients = st.session_state.ingredients
    if ingredients:
        found_silicones, found_sulfates, found_butters, found_protein, found_amber, ingredients_list = check_ingredients(
            st.session_state.product_type, ingredients)

        # Highlight the found ingredients
        highlighted_ingredients = []
        for ingredient in ingredients_list:
            if ingredient in found_amber:
                highlighted_ingredients.append(f"<span style='background-color: #fff1b6'>{ingredient}</span>")
            elif ingredient in found_silicones or ingredient in found_sulfates or ingredient in found_butters or ingredient in found_protein:
                highlighted_ingredients.append(f"<span style='background-color: #ffcccb'>{ingredient}</span>")
            else:
                highlighted_ingredients.append(ingredient)

        # Display the highlighted ingredient list
        st.markdown("### Ingredient List:")
        st.markdown(", ".join(highlighted_ingredients), unsafe_allow_html=True)

        # Display the appropriate message based on the found ingredients
        if st.session_state.product_type == "Haircare":
            if found_silicones and found_sulfates and found_butters and found_protein:
                st.markdown("**This product contains silicones, sulfates, butters, and protein.**")
            elif found_silicones and found_sulfates and found_butters:
                st.markdown("**This product contains silicones, sulfates, and butters.**")
            elif found_silicones and found_sulfates and found_protein:
                st.markdown("**This product contains silicones, sulfates, and protein.**")
            elif found_silicones and found_butters and found_protein:
                st.markdown("**This product contains silicones, butters, and protein.**")
            elif found_sulfates and found_butters and found_protein:
                st.markdown("**This product contains sulfates, butters, and protein.**")
            elif found_silicones and found_sulfates:
                st.markdown("**This product contains silicones and sulfates.**")
            elif found_silicones and found_butters:
                st.markdown("**This product contains silicones and butters.**")
            elif found_silicones and found_protein:
                st.markdown("**This product contains silicones and protein.**")
            elif found_sulfates and found_butters:
                st.markdown("**This product contains sulfates and butters.**")
            elif found_sulfates and found_protein:
                st.markdown("**This product contains sulfates and protein.**")
            elif found_butters and found_protein:
                st.markdown("**This product contains butters and protein.**")
            elif found_silicones:
                st.markdown("**This product contains silicones.**")
            elif found_sulfates:
                st.markdown("**This product contains sulfates.**")
            elif found_butters:
                st.markdown("**This product contains butters.**")
            elif found_protein:
                st.markdown("**This product contains protein.**")
            else:
                st.markdown("**This product is silicone-, sulfate-, butter-, and protein-free.**")
        else:
            if found_silicones:
                if any(ingredient in found_silicones for ingredient in ingredients_list[:5]):
                    st.markdown("**This product contains silicones - it is silicone-based.**")
                else:
                    st.markdown("**This product does not contain silicone within the first five ingredients - it is water-based.**")
            else:
                st.markdown("**This product does not contain silicone - it is water-based.**")
    else:
        st.write("Please enter some ingredients.")

# streamlit run ingredient_checker.py