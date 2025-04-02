import streamlit as st


#1- unit converter application
#2- input for unit converter application
#3- output given by unit converter application

# Inputs
#1- Value
#2- unit from conversion / which unit has to be converted
#3- unit to conversion

# value   unit_from  unit_to
# 2000      meters       kilometers


# Output
#converted value in preffered unit type

#              2.0/1.5
def convert_units(value: float, unit_from: str, unit_to: str ):
     print("value>>>", value)
     print("unit_from>>>",unit_from)
     print("unit_to>>>",unit_to)

     #1 kilometer = 1000 meters
     #1 meter + 0.001kilometer
     #1 kilogram = 1000 grams
     #1 gram = 0.001 kilogram
      # value in kilometer convert into meters
     if unit_from == "kilometers"  and  unit_to == "meters":
           #1.5  * 1000
           return value* 1000
     elif unit_from == "meters" and unit_to == "kilometers":
           #1 * 0.001 = 0.001 kilometer
           return value* 0.001
     elif unit_from == "kilograms"  and  unit_to == "grams":
           #2  * 1000 = 2000
           return value * 1000
     elif unit_from == "grams"   and  unit_to == "kilograms":
           return value * 0.001
     else :
           return" conversion is not supported kindly"
 

#result = output ki value
#result1 = convert_units(1.5, "kilometers","meters")
#print("the result in meter is", result1)
#result2 = convert_units(5000, "grams", "kilograms") 
#print("the value in kilogram is" , result2)



def main():
   st.title("unit converter")
   st.header("welcome to unit converter!")
   
   value = st.number_input("Enter the value that you want to convert:", min_value=0.0)
   unit_from = st.text_input("Enter the value that you want to convert from:(e.g. meters, kilometers, grams, kilometers)")
   unit_to = st.text_input("Enter the value that you want to convert toapp.py:(e.g. meters, kilometers, grams, kilometers)")

   if st.button("converter"):
        result = convert_units(value,unit_from, unit_to)
        st.write("convert value is:",result)


  # result = (convert_units ,  unit_from,unit_to)

   #print("welcome to unit converter!")

   #value = float (input ("Enter the value that you want to convert:")) #1  -> 1.00 -> 1.5
   #unit_to = input("unit of data after conversion (e.g. meters, kilometers, grams, kilograms)")
   #unit_from = input("current unit of data (e.g. meters, kilometers, grams, kilograms)")

   #print("value>>>", value)
   #print("unit_to>>>", unit_to)
   #print("unit_from>>>", unit_from)
   #result = convert_units(value,unit_from,unit_to)
   #print("ans ",result)
main()