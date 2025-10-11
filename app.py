import streamlit as st
import pandas as pd

st.set_page_config(page_title="Diamond Price Calculator 💎", page_icon="💎", layout="centered")

st.title("💎 Diamond Price Per Carat Calculator")

st.markdown("""
Enter your diamond data below (Chavni, Weight, and Price per Carat).  
This app will calculate the **total weight** and **weighted average price per carat**.
""")

# Example data
example_data = {
    "chavni": [14, 11, 8, 6, 5, 2, -2],
    "price": [3500, 2500, 2800, 3800, 4000, 5000, 8000],
    "weight": [12.3, 13.16, 18.22, 22.33, 38.09, 3.04, 1],
}

# Create editable table
df = st.data_editor(pd.DataFrame(example_data), num_rows="dynamic", use_container_width=True)

if not df.empty:
    # Calculate weighted average
    df["total_value"] = df["weight"] * df["price"]
    total_value = df["total_value"].sum()
    total_weight = df["weight"].sum()

    if total_weight > 0:
        weighted_avg_price = total_value / total_weight
        st.success(f"**Total Weight:** {total_weight:.2f} carats")
        st.success(f"**Weighted Average Price per Carat:** ₹ {weighted_avg_price:,.2f}")
    else:
        st.warning("Please enter valid weights.")
else:
    st.info("Enter at least one row of data above to see results.")

st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
