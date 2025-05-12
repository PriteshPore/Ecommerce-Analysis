import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title("E-commerce Data Analysis App")
    st.sidebar.title("Upload your Dataset")

    # Upload File section

    uploaded_file = st.sidebar.file_uploader("Upload a csv or Excel File",type=['csv'])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file,engine="openpyxl")

            st.sidebar.success("File uploaded successfully")

            st.subheader("Data Overview")
            st.write("**Fetching first five record from the Dataset**")
            st.dataframe(data.head())

            # Display Basic Information
            st.subheader("Basic Information")
            st.write("**Shape of the Data**",data.shape)
            st.write("**Columns in the dataset**",data.columns)
            st.write("**Missing values**",data.isnull().sum())

            # generate summary statistics
            st.subheader("Summary Statistics")
            st.write(data.describe())


            # Visualisation
            st.subheader("Visualizations")

            if 'Gender' in data.columns:
                st.write("**Gender Distribution**")
                fig,ax = plt.subplots()
                sns.countplot(data=data,x ='Gender',palette="Set2",ax=ax)
                ax.set_title("Gender Distribution")
                ax.set_xlabel("Gender")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
            
            if 'Purchase' in data.columns:
                if 'Gender' in data.columns:
                    st.write("**Distribution of Genderwise Purchase**")
                    purchase_gender = data.groupby('Gender')['Purchase'].sum()
                    fig,ax = plt.subplots()
                    purchase_gender.plot(kind='bar',color =['skyblue','orange'],ax=ax)
                    ax.set_title("Purchase by Gender")
                    ax.set_ylabel("Purchase Amount")
                    st.pyplot(fig)

            if 'Age' in data.columns:
                    st.write("**Distribution of Agewise Purchase")
                    purchase_age = data.groupby('Age')['Purchase'].sum()
                    fig,ax = plt.subplots()
                    purchase_age.plot(kind='bar',color='lightcoral',ax=ax)
                    ax.set_title("Total Purchase by Age")
                    ax.set_ylabel("Purchase")
                    st.pyplot(fig)
        except Exception as e:
            st.error(f"Error while loading file {e}")
    else:
        st.info("Please upload the dataset to get started!!")
if __name__ == "__main__":
    main()  

