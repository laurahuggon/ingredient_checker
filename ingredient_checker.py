import streamlit as st

# Define a function to check ingredients
def check_ingredients(product_type, ingredients):
    # Define lists of keywords to search for in the ingredients
    silicones = ["cone", "conol", "silane", "siloxane"]
    sulfates = ["sulfate", "sulfoacetate", "sulfo", "sulfo succinate"]
    butters = ["butter"]
    proteins = ["protein", "wheat", "keratin", "soy", "amino acids", "collagen", "milk", "casein", "oat flour", "rice", "amaranthus", "baobab"]
    buildups = ["peg-40 hydrogenated castor oil", "PEG 40 hydrogenated castor oil", "castor", "vp/va copolymer"]
    pore_cloggers = ["olive oil", "shea butter", "shea", "soja", "a & d additive", "acetvlated lanolin", "acetylated lanolin", "acetylated lanolin alcohol", "acetylated wool fat", "acetylated wool wax", "active soil complex", "adansonia digitata l.", "agar", "ahnfeltia concinna", "ahnfeltia concinna extract", "ahnfeltiopsis concinna extract", "alaria esculenta", "alaria esculenta extract", "alga bladderwrack", "algae", "algae extract", "algea", "algin", "alginate", "alginic acid", "almond oil", "amyl cinnamal", "andiroba seed oil", "aphanothece sacrum polysaccharide", "apricot", "apricot kernel oil", "apricot oil", "argan oil", "arthrospira plantensis", "ascophyllum", "ascophyllum nodosum", "ascophyllum nodosum extract", "asparagopsis armata extract", "astrocaryum murumuru seed butter", "avocado", "avocado butter", "avocado oil", "babassu oil", "baobab", "baobab oil", "baoboab", "basic red", "beef tallow", "beeswax", "bismuth", "bismuth oxychloride", "black kelp", "bladderwack", "blue algae", "blue green algae", "borage oil", "brazil nut oil", "brown algae", "bryopsis africana", "buriti oil", "butyl stearate", "butyrospermum parkii butter", "butyrospermum", "butyrospermum parkii", "butyrospermum parkii (shea) butter", "butyrospermum parkii (shea) butter extract", "c13-14 isoparaffin", "cacao seed butter", "camelina oil", "canola oil", "capea biruncinata var. denuda sonder", "capea biruncinata var. elongata sonder", "capric acid", "carageenan gum", "carageenan moss", "carastay c", "carrageenan", "carrageenan moss", "carrot seed oil", "caulerpa filiformis", "caulerpa lentillifera extract", "cera alba", "cera bianca", "cera flava", "cera olea", "ceteareth 20", "ceteareth-20", "ceteareth-6 olivate", "cetearyl alcohol & ceteareth 20", "cetearyl alcohol + ceteareth 20", "cetrimonium bromide", "cetyl acetate", "chaetomorpha linum (aerea) cladophora radiosa", "cherry seed oil", "cheru seed oil", "chlamydomonas reinhardtii extract", "chlorophyceae", "chondrus crispus", "chondrus crispus (aka irish moss or carageenan moss)", "chondrus crispus powder", "chullu (wild apricot) seed oil", "cladophora cf. subsimplex", "cladosiphon okamuranus extract", "coal tar", "cocoa butter", "coconut", "coconut alkanes", "coconut butter", "coconut extract", "coconut fruit", "coconut nucifera extract", "coconut oil", "cocos nucifera", "cocos nucifera (coconut) fruit extract", "cocos nucifera (coconut) oil", "cocos nucifera oil", "cocos nucifera seed butter", "codium fragile extract", "coenochloris signiensis extract", "colloidal sulfur", "corn", "corn oil", "cotton awws", "cotton awws oil", "cotton seed oil", "cottonseed oil", "cranberry seed oil", "creosote", "crithmum maritimum", "cupuacu butter", "cystoseira tamariscifolia extract", "d & c red", "d & c red # 17", "d & c red # 21", "d & c red # 3", "d & c red # 30", "d & c red # 36", "d & c red 17", "d & c red 19", "d & c red 21", "d & c red 27", "d & c red 3", "d & c red 30", "d & c red 33", "d & c red 36", "d & c red 4", "d & c red 40", "d & c red 6", "d & c red 7", "d & c red 9", "d-limonene", "d&c red #17", "d&c red #21", "d&c red #3", "d&c red #30", "d&c red #40", "date seed oil", "decyl oleate", "dhupa seed oil", "di (2 ethylhexyl) succinate", "dictyopteris membranacea", "dictyopteris polypodioides", "diisostearyl malate", "dilsea carnosa", "dilsea carnosa extract", "dioctyl malate", "dioctyl succinate", "disodium monooleamido", "disodium monooleamido peg 2- sulfosuccinate", "disodium monooleamido peg 2-sulfosuccinate", "dodecanoic acid", "dulse", "dunaliella salina extract", "durvillaea antarctica extract", "ecklonia", "ecklonia radiata", "enteromorpha compressa", "ethoxylated lanolin", "ethylhexyl palmitat", "eevening primrose oil", "flax oil", "flaxseed oil", "fucus vesiculosus", "glyceryl 3-diisostearate", "glyceryl stearate se", "glyceryl-3 diisostearate", "glycine soja (soybean) oil", "haslea ostrearia", "hexadecyl alcohol", "himanthalia elongate", "hydrolyzed wheat protein", "irish moss", "isoceteth-20", "isocetyl alcohol", "isocetyl stearate", "isodecyl oleate", "isononyl isononoanoate", "isopropyl isostearate", "isopropyl isosterate", "isopropyl lanolate", "isopropyl linolate", "isopropyl linoleate", "isopropyl myristate", "isopropyl neopentanoate", "isopropyl palmitate", "isostearate", "isostearic acid", "isostearyl", "isostearyl isostearate", "isostearyl neopentanoate", "jania rubens extract", "kapok oil", "kappaphycus", "kappaphycus alvarezii extract", "karanja oil", "karite", "kelp", "kousou ekisu", "kukui nut", "kukui nut oil", "kukui oil", "laminaria", "laminaria digitata", "laminaria digitata extract", "laminaria longicruris", "laminaria longicruris extract", "laminaria saccharina", "laminaria saccharina extract", "laminaria saccharina extract (laminaria saccharine)", "laminaria saccharine", "laneth 10", "lanolic acid", "lanolin", "lanolin alcohol", "lanolin oil", "laureth 12", "laureth 23", "laureth 4", "laureth 7", "laureth-23", "laureth-4", "lauric acid", "lauryl alcohol", "lauryl olivate", "lauryl sulfate", "linolate", "linseed", "linseed oil", "linum usitatissimum (linseed) seed oil", "liquor picis carbonis", "lithothamnium calcareum", "lithothamnium calcareum powder", "lola implexa", "lpc", "macadamia nut oil", "macroalgae", "macrocystis pyrifera (kelp) extract", "macrocystis pyrifera extract", "magnesium myristate", "mahua seed oil", "mangifera indica seed butter", "mango butter", "marine algae", "marula", "marula oil", "mastocarpus stellatus", "microcystis aeruginosa", "mineral oil", "mink oil", "monostearate", "moringa", "moringa oil", "moringa oleifera seed oil", "moss", "myreth 3 myristate", "myreth-3 myristate", "myristate", "myristic acid", "myristyl", "myristyl alcohol", "myristyl lactate", "myristyl myristate", "myristyl propionate", "myrtrimonium bromide", "nahor seed oil", "nasturtium officinale (watercress) flower/leaf extract", "neem oil", "neopentanoate", "norwegian kelp", "nymphaea alba flower extract", "octodidecyl stearoyl stearate", "octyl palmitate", "octyl stearate", "olea europaea fruit oil", "oleth-10", "oleth-20", "oleth-3", "oleth-3 phosphate", "oleth-5", "oleyl alcohol", "olive", "olive butter", "olive oil", "olive oil peg-7 esters", "padina pavonica", "padina pavonica extract", "palash oil", "palm kernel oil", "palm oil", "palm oil butter", "palmaria oalmarta extract (dulse)", "palmaria palmata extract", "palmaria palmate", "palmitic acid", "papaya seed oil", "parkii", "parrafin", "peach kernel oil", "peanut oil", "pecan oil", "peg 100 distearate", "peg 150 distearate", "peg-150 distearate", "peg 150 distearate", "peg 16 lanolin", "peg 2 sulfosuccinate", "peg 200 dilaurate", "peg 65", "peg 8 stearate", "peg-16 lanolin", "peg-200 dilaurate", "peg-8 stearate", "pelvetia canaliculata extract", "pentaerythrital", "pequot oil", "persea americana", "persea gratissima (avocado) oil", "petroleum", "pg caprylate/caprate", "pg dipelargonate", "pg monostearate", "phaeodactylum tricornutum extract", "phaeophyceae", "phytantriol", "phytessence wakame", "pilu oil", "pine nut oil", "pix carbonis", "plankton", "plankton extract", "polyglyceryl-2 isostearate", "polyglyceryl-3 diisostearate", "polyglyceryl-3 diiosostearate", "polyglyceryl-4 isostearate", "polyglyceryl-4-caprate", "polyglyceryl-diisostearate", "polyquanterium-4", "polysiphonia elongata extract", "porphyra", "porphyra umbilicalis", "porphyridium", "porphyridium cruentum", "porphyridium cruentum extract", "potassium chloride", "potassium cocoate", "potassium salt", "ppg 10 cetyl ether", "ppg 12", "ppg 2 myristyl ether propionate", "ppg 2 myristyl propionate", "ppg 5 ceteth 10 phosphate", "ppg ceteth 10 phosphate", "ppg-2 myristyl", "ppg-2 myristyl propionate", "pracaxi oil", "propylene glycol monostearate", "prunus dulcis oil", "pumpkin seed oil", "pyrene coal tar pitch", "rapeseed oil", "ratanjyat oil", "red algae", "red palm oil", "retinyl palmitate", "rhodophyceae extract", "rhodophyta", "ricebran oil", "rice bran oil", "rockweed", "sal seed oil", "sandalwood seed oil", "sapote oil", "sargassum", "sargassum filipendula extract", "sargassum fillpendula extract", "sargassum fusiforme extract", "sclerocarya birrea", "sclerocarya birrea seed oil", "sea fern", "sea grass", "sea mayweed", "sea whip", "sea whip extract", "seaweed", "sesame", "sesame oil", "sesame seed", "sesamum indicum", "shark liver oil", "shark squalene", "shea", "shea butter", "shea nut oil", "sheep alcohol", "simmondsia chinensis seed wax", "sles", "sls", "sodium alginate", "sodium carbomer", "sodium laurel sulfate", "sodium laureth sulfate", "sodium lauryl sulfate", "soil minerals", "soja", "solulan 16", "sorbitan laurate", "sova", "soy", "soy oil", "soy protein", "soybean", "soybean oil", "soybean oil", "sphacelaria", "spiraea ulmaria (meadowsweet) flower extract", "spirulina", "squalene", "starch", "stealkonium chloride", "steareth 10", "steareth 2", "steareth 20", "steareth-10", "stearic acid", "stearic acid tea", "stearyl heptanoate", "sulfated castor oil", "sulfosuccinate", "sulphated castor oil", "sunflower butter", "sweet almond butter", "sweet almond oil", "talc", "talcum", "tallow", "tamanu oil", "tea stearate", "tetradecyl myristate", "theobroma butter", "theobroma cocoa seed butter", "theobroma oil", "tribehenin", "triethanolamine", "triticum aestivum", "triticum vulgare", "tucuma butter", "turkey red oil", "ulva fasciata", "ulva lactuca", "ulva rhacodes", "undaria", "undaria pinnatifida", "vegetable gelatin", "vitamin a palmitate", "vitamin e oil", "vitellaria paradoxa", "wakame", "water soluble sulfur", "wheat", "wheat germ glyceride", "wheat germ oil", "wool alcohol", "wool fat", "xanthophyta", "xylene", "zea mays"]
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
                    "**This product does not contain silicones, sulfates, butters, proteins, or buildup-causing ingredients.**")
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