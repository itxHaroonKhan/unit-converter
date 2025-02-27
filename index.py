import streamlit as st

def length_converter(value, from_unit, to_unit):
    # Conversion factors relative to meters (1 meter = X units)
    conversion_factors = {
        "meter": 1,
        "kilometer": 0.001,
        "centimeter": 100,
        "millimeter": 1000,
        "mile": 0.000621371,
        "yard": 1.09361,
        "foot": 3.28084,
        "inch": 39.3701,
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert to Celsius first if needed
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        celsius = value  # Already in Celsius

    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:
        return celsius

def main():
    st.title("📏🌡️ Unit Converter")
    st.sidebar.header("Configuration")
    conversion_type = st.sidebar.selectbox("Select conversion type",
                                         ["Length", "Temperature"])

    if conversion_type == "Length":
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("Enter value:", min_value=0.0, step=0.1)
            from_unit = st.selectbox("From unit", [
                "meter", "kilometer", "centimeter", "millimeter",
                "mile", "yard", "foot", "inch"
            ])
        with col2:
            to_unit = st.selectbox("To unit", [
                "meter", "kilometer", "centimeter", "millimeter",
                "mile", "yard", "foot", "inch"
            ])

        if st.button("Convert Length"):
            result = length_converter(value, from_unit, to_unit)
            st.success(f"**Result:** {value:.2f} {from_unit} = {result:.2f} {to_unit}")

    elif conversion_type == "Temperature":
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("Enter temperature:", step=0.1)
            from_unit = st.selectbox("From unit", ["Celsius", "Fahrenheit", "Kelvin"])
        with col2:
            to_unit = st.selectbox("To unit", ["Celsius", "Fahrenheit", "Kelvin"])

        if st.button("Convert Temperature"):
            result = temperature_converter(value, from_unit, to_unit)
            st.success(f"**Result:** {value:.2f}°{from_unit[0]} = {result:.2f}°{to_unit[0]}")

if __name__ == "__main__":
    main()
