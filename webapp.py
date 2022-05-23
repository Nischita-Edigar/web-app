# import libraries
import streamlit as st
import pandas as pd
import seaborn as sns

#1. Title and subheader
st.title("Data Analysis")
st.subheader("Data Analysis using streamlit and python")

#upload dataset
upload = st.file_uploader('upload your dataset in csv format')
if upload is not None:
    data=pd.read_csv(upload)
    
#3. show dataset
if upload is not None:
 if st.checkbox("preview Dataset"):
    if st.button("Head"):
        st.write(data.head())
    if st.button("Tail"):
        st.write(data.tail())
        
#4. Check datatype of each column
if upload is not None:
    if st.checkbox("Datatype of each column"):
        st.text("Data types")
        st.write(data.dtypes.astype(str))
        
#5.Find the shape of the dataset
if upload is not None:
    data_shape=st.radio("What Dimensiom do you want to check?",('Rows','Columns'))
    
    if data_shape=='Rows':
            st.text("Number of Rows:")
            st.write(data.shape[0])
            
    if data_shape=='Columns':
                st.text("Number of Columns:")
                st.write(data.shape[1])
                
#6. Find the null values in the dataset

if upload is not None:
   test=data.isnull().values.any()
   if test==True:
     if st.checkbox("Null values in the dataset"):            
        sns.heatmap(data.isnull())
        st.pyplot()
   else:
       st.success("No missing values found!!!")
            
#7. Find duplicate values in the datset

if upload is not None:
  test=data.duplicated().any()
  if test==True:
     st.warning("This data set contains some duplicate values")
     dup=st.selectbox("Do you want to remove duplicate values?", \
                      ("select one",'Yes','No'))
     if dup=='No':
         st.text("Ok No problem")
     if dup=='Yes':
         data=data.drop_duplicates()
         st.text("Duplicate values removed")
         
#8. Get overall statistics
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe())
         
 #9. About

if st.button("ABOUT APP"):
    st.text("Built with Streamlit") 
    st.text("Thans to Streamlit") 
#10. By
if st.button("By"): 
   st.success("Nischita Edigar")      
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            