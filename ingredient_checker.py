import streamlit as st

# Define a function to check ingredients
def check_ingredients(product_type, ingredients):
    # Define lists of keywords to search for in the ingredients
    silicones = ["cone", "conol", "silane", "siloxane"]
    sulfates = ["sulfate", "sulfoacetate", "sulfo", "sulfo succinate"]
    butters = ["butter"]
    proteins = ["protein", "wheat", "keratin", "soy", "amino acids", "collagen", "milk", "casein", "oat flour", "rice", "amaranthus", "baobab"]
    buildups = ["peg-40 hydrogenated castor oil", "PEG 40 hydrogenated castor oil", "castor", "vp/va copolymer"]
    pore_cloggers = ["1-acetoxyhexadecane", "1-hexadecanol acetate", "1-hexadecanol", "acetic acid hexadecyl ester", "acetylated lanolin", "acetylated lanolin alcohol", "acetylated wool fat", "acetylated wool wax", "adansonia digitata l.", "agar", "ahnfeltiopsis concinna extract", "alaria esculenta extract", "alga bladderwrack", "algae", "algae extract", "algin", "alginate", "alginic acid", "algea", "aphanothece sacrum polysaccharide", "arthrospira plantensis", "ascophyllum nodosum extract", "asparagopsis armata extract", "baobab", "beeswax", "bismuth", "bryopsis africana", "butyl octadecanoate", "butyl stearate", "butyl stearic acid", "butyrospermum", "cacao seed butter", "capea biruncinata var. denuda sonder", "capea biruncinata var. elongata sonder", "carageenan gum", "carastay c", "caulerpa lentillifera extract", "caulerpa filiformis", "carrageenan", "carrageenan moss", "cera alba", "cera bianca", "cera flava", "cera olea", "cetearyl alcohol + ceteareth 20", "cetyl acetate", "chaetomorpha linum (aerea) cladophora radiosa", "chlamydomonas reinhardtii extract", "chlorella", "chlorophyceae", "chondrus crispus (aka irish moss or carageenan moss)", "cladophora cf. subsimplex", "cladosiphon okamuranus extract", "coal tar", "coco-caprate", "coco-caprylate", "cocoa butter", "coconut alkanes", "coconut butter", "coconut extract", "coconut nucifera extract", "coconut oil", "cocos nucifera oil", "cocos nucifera seed butter", "coenochloris signiensis extract", "colloidal sulfur", "cotton awws oil", "cotton seed oil", "corallina officinalis extract", "corn", "corn oil", "creosote", "cystoseira tamariscifolia extract", "d & c red # 17", "d & c red # 21", "d & c red # 3", "d & c red # 30", "d & c red # 36", "decyl oleate", "decyloleate", "dicotyledons succinate", "dictyopteris membranacea", "dictyopteris polypodioides", "diethylhexyl sodium sulfosuccinate", "diisooctyl succinate", "dilsea carnosa extract", "dodecanoic acid", "dodecoic acid", "dodecylic acid", "dunaliella salina extract", "duodecylic acid", "durvillaea antarctica extract", "ecklonia cava", "ecklonia cava extract", "ecklonia radiata", "enteromorpha compressa extract", "ethoxylated lanolin", "ethylhexyl palmitate", "ethylhexyl stearate", "eucheuma spinosum extract", "fucoxanthin", "fucus serratus", "fucus vesiculosus", "gamtae extract", "gelidiella acerosa extract", "gelidium amansii extract", "gigartina stellata extract", "glyceryl monostearate", "glyceryl stearate se", "glyceryl-3 diisostearate", "glycine soja oil", "glycine max", "gracilariopsis chorda extract", "haematococcus pluvialis extract", "haematococcus pluvialis", "haslea ostrearia extract", "hexadecanol acetate", "hexadecyl acetate", "hexadecyl alcohol", "himanthalia elongata extract", "hizikia fusiforme extract", "hydrogenated vegetable oil", "hydrolyzed rhodophycea extract", "hydrous magnesium silicate", "hypnea musciformis extract", "hypneaceae extract", "irish moss", "isocetyl alcohol", "isocetyl stearate", "isodecyl oleate", "isohexadecanol", "isohexadecyl alcohol", "isohexadecyl stearate", "isooctadecyl isooctadecanoate", "isopalmitic alcohol", "isopalmityl alcohol", "isopropyl isodecanoate", "isopropyl isostearate", "isopropyl linolate", "isopropyl myristate", "isopropyl palmitate", "isostearyl isostearate", "isostearyl neopentanoate", "jania rubens extract", "jojoba wax", "kappaphycus alvarezii extract", "karite", "kelp", "kousou ekisu", "laminaria", "laminaria digitata extract", "laminaria saccharina extract (laminaria saccharine)", "lanolin acetate", "lanolin alcohol acetate", "lanolin polyoxyethylene ether", "laureth-23", "laureth-4", "lauric acid", "laurostearic acid", "lcd", "linolate", "liquor carbonis detergens", "liquor picis carbonis", "lithothamnium calcareum powder", "lpc", "macroalgae", "macrocystis pyrifera extract", "mangifera indica seed butter", "mango butter", "marula", "marula oil", "methylsilanol mannuronate", "mink oil", "moss", "myristate", "myristic acid", "myristyl", "myristyl lactate", "myristyl myristate", "myristyl propionate", "n-hexadecyl alcohol", "n-hexadecyl ethanoate", "octadecanoic acid", "octadecyl heptanoate", "octyl palmitate", "octyl stearate", "oleth-3", "oleth-3 phosphate", "oleyl alcohol", "palmaria palmata extract", "palmityl acetate", "palmityl alcohol", "parkii", "peg 2 sulfosuccinate", "peg 2- sulfosuccinate", "peg 16 lanolin", "peg 200 dilaurate", "peg-75", "peg 8 stearate", "pelvetia canaliculata extract", "pes", "phaeodactylum tricornutum extract", "phaeophyceae", "pix carbonis", "pg monostearate", "pgms", "ppg-2 myristyl", "ppg 2 myristyl propionate", "ppg 2 myristyl ether propionate", "plankton", "polyethylene glycol 200", "polyethylene glycol dodecyl ether", "polyethylene glycol jojoba acid", "polyethylene glycol lauryl ether", "polyethylene glycol monododecyl ether", "polyethylene glycol stearate", "polyoxyethylene lauryl ether", "polysiphonia elongata extract", "polyglyceryl-3 diisostearate", "polyglyceryl-3-disostearate", "porphyra umbilicalis", "porphyridium", "porphyridium cruentum extract", "porphyridium polysaccharide", "potassium chloride", "potassium salt", "propanoic acid", "propylene glycol monostearate", "pyrene coal tar pitch", "red algae", "rhodophyta", "rhodophyceae extract", "sargassum filipendula extract", "sargassum fusiforme extract", "sclerocarya birrea", "sclerocarya birrea seed oil", "seaweed", "sea fern", "sesame", "sesamum indicum", "shark liver oil", "shark squalene", "shea", "shea butter", "sheep alcohol", "simmondsia chinensis seed wax", "sles", "slo", "sls", "sodium alginate", "sodium alkylethersulfate", "sodium docusate", "sodium dodecyl sulphate", "sodium laureth sulfate", "sodium lauryl ether sulfate", "sodium lauryl sulfate", "soja", "solulan 16", "sorbitan monooleate", "sorbitan oleate", "soy", "soybean", "soybean oil", "sphacelaria", "spirulina", "squalene", "steareth 10", "stearic acid tea", "stearyl heptanoate", "starch", "sulfated castor oil", "sulfated jojoba oil", "sulfosuccinate", "sulphated castor oil", "talc", "talcum", "tea stearate", "tetradecanoic acid", "tetradecyl lactate", "tetradecyl myristate", "tetradecyl propionate", "theobroma butter", "theobroma cocoa seed butter", "theobroma oil", "triticum aestivum", "triticum vulgare", "turkey red oil", "undaria pinnatifida", "ulva lactuca extract", "uva ursi extract", "vaseline", "vitamins c/e/squalene", "wool alcohols", "wool wax", "xanthan", "xanthan gum", "zinc oxide"]
    humectants = ["propolis extract", "honey extract", "glycerin", "sodium hyaluronate", "snail secretion filtrate", "betaine", "beta-glucan", "panthenol", "bambusa vulgaris extract", "allantoin"]
    anti_inflammatory = ["propolis extract", "honey extract", "panthenol", "snail secretion filtrate", "allantoin", "betaine", "centella asiatica", "madecassoside", "houttuynia cordata", "bamboo", "mugwort"]
    anti_microbials = ["propolis extract", "honey extract", "bamboo", "mugwort"]
    ceramides = ["ceramide", "sphinganine", "sphingosine", "palmitamide", "hexadecanamide"]
    peptides = ["peptide", "palmitoyl", "carnosine"]

    # Initilise lists to store found ingredients
    found_silicones = []
    found_sulfates = []
    found_butters = []
    found_proteins = []
    found_buildups = []
    found_pore_cloggers = []
    found_humectants = []
    found_anti_inflammatory = []
    found_anti_microbials = []
    found_ceramides = []
    found_peptides = []

    # Split the input string into individual ingredients
    original_ingredients_list = [ingredient.strip() for ingredient in ingredients.split(",")]
    # Convert input string to lowercase for case-insensitive matching
    ingredients_list_lower = [ingredient.lower() for ingredient in original_ingredients_list]

    # Loop through each ingredient to check for keywords
    for ingredient_lower, ingredient in zip(ingredients_list_lower, original_ingredients_list):
        # Check if any silicone keyword is in the ingredient
        if any(silicone in ingredient_lower for silicone in silicones):
            found_silicones.append(ingredient)
        # Check haircare-specific products
        if product_type == "Haircare":
            if any(sulfate in ingredient_lower for sulfate in sulfates) and not ingredient_lower.endswith("sulfonate"):
                found_sulfates.append(ingredient)
            if any(butter in ingredient_lower for butter in butters):
                found_butters.append(ingredient)
            if any(protein in ingredient_lower for protein in proteins):
                found_proteins.append(ingredient)
            if any(buildup in ingredient_lower for buildup in buildups):
                found_buildups.append(ingredient)
        # Check for pore-cloggers in skincare and makeup
        if product_type != "Haircare":
            if any(clogger in ingredient_lower for clogger in pore_cloggers):
                found_pore_cloggers.append(ingredient)
        # Check for skincare-specific ingredients
        if product_type == "Skincare":
            if ingredient_lower in humectants:
                found_humectants.append(ingredient)
            if ingredient_lower in anti_inflammatory:
                found_anti_inflammatory.append(ingredient)
            if ingredient_lower in anti_microbials:
                found_anti_microbials.append(ingredient)
            if any(ceramide in ingredient_lower for ceramide in ceramides):
                found_ceramides.append(ingredient)
            if any(peptide in ingredient_lower for peptide in peptides):
                found_peptides.append(ingredient)


    # Return lists of found ingredients and the original list
    return found_silicones, found_sulfates, found_butters, found_proteins, found_buildups, found_pore_cloggers, found_humectants, found_anti_inflammatory, found_anti_microbials, found_ceramides, found_peptides, original_ingredients_list

# Initialize session state variables for Steamlit
if 'product_type' not in st.session_state:
    st.session_state.product_type = "Skincare"
if 'ingredients' not in st.session_state:
    st.session_state.ingredients = ""
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Streamlit interface setup
st.title("Ingredient Checker")

# Functions to handle submit and clear actions
def submit_action():
    st.session_state.submitted = True

def clear_action():
    st.session_state.submitted = False
    st.session_state.ingredients = ""

# Create the product type selection box
st.session_state.product_type = st.selectbox("Type of product:", ["Skincare", "Makeup", "Haircare"],
                                             index=["Skincare", "Makeup", "Haircare"].index(
                                                 st.session_state.product_type))
# Create the text area for entering ingredients
st.session_state.ingredients = st.text_area("Enter ingredients (separated by commas):", st.session_state.ingredients)

# Create the Submit and Clear buttons
col1, col2 = st.columns([1, 0.115])
with col1:
    st.button("Submit", on_click=submit_action)
with col2:
    st.button("Clear", on_click=clear_action)

# Process the input when the form is submitted
if st.session_state.submitted:
    ingredients = st.session_state.ingredients
    if ingredients:
        found_silicones, found_sulfates, found_butters, found_proteins, found_buildups, found_pore_cloggers, found_humectants, found_anti_inflammatory, found_anti_microbials, found_ceramides, found_peptides, ingredients_list = check_ingredients(
            st.session_state.product_type, ingredients)

        # Highlight the found ingredients
        highlighted_ingredients = []
        for ingredient in ingredients_list:
            if ingredient in found_proteins:
                highlighted_ingredients.append(f"<span style='background-color: #43B347'>{ingredient}</span>")
            elif ingredient in found_silicones or ingredient in found_sulfates or ingredient in found_butters or ingredient in found_pore_cloggers or ingredient in found_buildups:
                highlighted_ingredients.append(f"<span style='background-color: #DE8F8D'>{ingredient}</span>")
            elif ingredient in found_humectants or ingredient in found_anti_inflammatory or ingredient in found_anti_microbials or ingredient in found_ceramides or ingredient in found_peptides:
                highlighted_ingredients.append(f"<span style='background-color: #43B347'>{ingredient}</span>")
            else:
                highlighted_ingredients.append(ingredient)

        # Display the highlighted ingredient list
        st.markdown(", ".join(highlighted_ingredients), unsafe_allow_html=True)

        # Display the appropriate message based on the found ingredients
        if st.session_state.product_type == "Haircare":
            if found_silicones:
                if len(found_silicones) == 1:
                    st.markdown(f"**This product contains 1 silicone:** {', '.join(found_silicones)}.")
                else:
                    st.markdown(
                        f"**This product contains {len(found_silicones)} silicones:** {', '.join(found_silicones)}.")

            if found_sulfates:
                if len(found_sulfates) == 1:
                    st.markdown(f"**This product contains 1 sulfate:** {', '.join(found_sulfates)}.")
                else:
                    st.markdown(
                        f"**This product contains {len(found_sulfates)} sulfates:** {', '.join(found_sulfates)}.")

            if found_butters:
                if len(found_butters) == 1:
                    st.markdown(f"**This product contains 1 butter:** {', '.join(found_butters)}.")
                else:
                    st.markdown(f"**This product contains {len(found_butters)} butters:** {', '.join(found_butters)}.")

            if found_proteins:
                if len(found_proteins) == 1:
                    st.markdown(f"**This product contains 1 protein:** {', '.join(found_proteins)}.")
                else:
                    st.markdown(
                        f"**This product contains {len(found_proteins)} proteins:** {', '.join(found_proteins)}.")

            if found_buildups:
                if len(found_buildups) == 1:
                    st.markdown(
                        f"**This product contains 1 product that may cause buildup:** {', '.join(found_buildups)}.")
                else:
                    st.markdown(
                        f"**This product contains {len(found_buildups)} products that may cause buildup:** {', '.join(found_buildups)}.")

            if not (found_silicones or found_sulfates or found_butters or found_proteins or found_buildups):
                st.markdown(
                    "**This product does not contain silicones, sulfates, butters, proteins, and buildup-causing ingredients.**")
        else:
            if found_silicones:
                if any(ingredient in found_silicones for ingredient in ingredients_list[:5]):
                    st.markdown("**This product contains silicones - it is silicone-based.**")
                else:
                    st.markdown("**This product does not contain silicone within the first five ingredients - it is water-based.**")
            else:
                st.markdown("**This product does not contain silicone - it is water-based.**")
            if found_pore_cloggers:
                if len(found_pore_cloggers) == 1:
                    st.write(f"**This product contains 1 pore-clogging ingredient:** {', '.join(found_pore_cloggers)}.")
                else:
                    st.write(
                        f"**This product contains {len(found_pore_cloggers)} pore-clogging ingredients:** {', '.join(found_pore_cloggers)}.")
        if st.session_state.product_type == "Skincare":
            if found_humectants:
                if len(found_humectants) == 1:
                    st.write(f"**This product contains 1 humectant:** {', '.join(found_humectants)}.")
                else:
                    st.write(
                        f"**This product contains {len(found_humectants)} humectants:** {', '.join(found_humectants)}.")
            if found_anti_inflammatory:
                if len(found_anti_inflammatory) == 1:
                    st.write(f"**This product contains 1 anti-inflammatory ingredient:** {', '.join(found_anti_inflammatory)}.")
                else:
                    st.write(
                        f"**This product contains {len(found_anti_inflammatory)} anti-inflammatory ingredients:** {', '.join(found_anti_inflammatory)}.")
            if found_anti_microbials:
                if len(found_anti_microbials) == 1:
                    st.write(f"**This product contains 1 antimicrobial ingredient:** {', '.join(found_anti_microbials)}.")
                else:
                    st.write(
                        f"**This product contains {len(found_anti_microbials)} antimicrobial ingredients:** {', '.join(found_anti_microbials)}.")
            if found_ceramides:
                if len(found_ceramides) == 1:
                    st.write(f"**This product contains 1 ceramide:** {', '.join(found_ceramides)}.")
                else:
                    st.write(
                        f"**This product contains {len(found_ceramides)} ceramides:** {', '.join(found_ceramides)}.")
            if found_peptides:
                if len(found_peptides) == 1:
                    st.write(f"**This product contains 1 peptide:** {', '.join(found_peptides)}.")
                else:
                    st.write(
                        f"**This product contains {len(found_peptides)} peptides:** {', '.join(found_peptides)}.")
    else:
        st.write("Please enter some ingredients.")

# streamlit run ingredient_checker.py