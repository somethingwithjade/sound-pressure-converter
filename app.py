# Streamlit frontend

import streamlit as st
from conversions import pascal_to_db, db_to_pascal, describe_db_level, REFERENCE_PRESSURE

st.title("Sound Pressure Level Converter (Pa ↔ dB SPL)")

conversion_type = st.selectbox(
    "Select conversion type:",
    ("Pascal → dB SPL", "dB SPL → Pascal")
)

# Input
if conversion_type == "Pascal → dB SPL":
    value = st.number_input(
        "Enter value in Pa:",
        min_value=0.0,
        format="%.6f",
        step=0.000001
    )
else:
    value = st.number_input(
        "Enter value in dB SPL:",
        min_value=0.0,
        format="%.3f",
        step=0.001
    )

# Action: only calculate when clicked
if st.button("Convert"):
    if conversion_type == "Pascal → dB SPL":
        if value <= 0:
            st.error("Sound pressure must be greater than 0 Pa to calculate dB SPL.")
        else:
            if value < REFERENCE_PRESSURE:
                st.warning("This value is below the hearing threshold of a person with normal hearing (20 μPa). The result may be negative and represents inaudible sound.")

            result = pascal_to_db(value)
            st.write(f"Result: {result:.2f} dB SPL")
            st.markdown(f"Description: {describe_db_level(result)}")

    else:
        result = db_to_pascal(value)
        st.write(f"Result: {result:.6f} Pa")

st.markdown("---")
st.markdown("This tool uses the standard reference pressure of 20 μPa (2×10⁻⁵ Pa).")
