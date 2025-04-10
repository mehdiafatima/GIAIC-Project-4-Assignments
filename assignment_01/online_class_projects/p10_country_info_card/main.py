import streamlit as st 
import requests

def fetch_country_data(country_name):   
    url = f"https://restcountries.com/v3/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data["name"]["common"]
        capital = country_data.get("capital")[0]
        population = country_data.get("population")
        area = country_data.get("area")
        currencies = country_data.get("currencies")
        region = country_data.get("region")
        return name, capital, population, area, currencies, region
    
    else:
        return None
    

def main():
    st.title("Country Information App")
    
    country_name = st.text_input("Enter a country name:")

    if country_name:
        country_data = fetch_country_data(country_name)
        if country_data:
            name, capital, population, area, currencies, region = country_data
            st.subheader("Country Information")
            st.write(f"**Name:** {name}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**Population:** {population}")
            st.write(f"**Area:** {area} square kilometer")
            st.write(f"**Region:** {region}")
            st.write(f"**Currencies:** {currencies}")

        else:
            st.error("Country not found. Please try again.")


if __name__ == "__main__":
    main()            




            



        
        
    
    

