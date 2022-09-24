from pathlib import Path

import streamlit as st
from PIL import Image


# -- Path Settings --#
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



# -- GENERAL SETTINGS -- #
page_title = "Digital CV - Fabrício de Almeida"
page_icon = ":fire:"
name = "Fabrício de Almeida"
description = """Accountant with experience in tax and management, with a lot of interest for technology and data analysis. Focused and hardworking, my goal is work to guarantee the best decision possible to companies and society, using my data analysis skills.

"""
email = "fabriciotdalmeida@gmail.com"
social_media = {"Linkedin": "https://www.linkedin.com/in/fabr%C3%ADcio-teixeira-de-almeida-2b4b42164/?locale=en_US",
"Github": "https://github.com/fabzfta" }

st.set_page_config(page_title=page_title, page_icon= page_icon)

st.title("Be welcome!")

# -- LOAD CSS, PDF AND PROFILE PIC -- #

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


# -- HERO SECTION -- #
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label=" 💾 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write(":email: " , email)

# --- SOCIAL LINKS --- #
st.write("#")
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"[{platform}]({link})")


# -- EXPERIENCE AND QUALIFICATIONS -- #

st.write("#")
st.subheader("Experience & Qualifications")
st.write("""
    - ✔️ 5 years of experience with Financial Data Analysis
    - ✔️ Strong knowledge in Data Analysis tools as Excel and Python's Data Visualizations tools
    - ✔️ Good understanding of Accounting, Finance and Statistics
    - ✔️ Excelent team-player and displaying a strong sense of responsibility on every single task
""")

# -- SKILLS -- #

st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 💻 Programming: Python (Scikit-learn,Pandas, Django), SQL, Django
    - 📊 Data Visualization: Dash, Power BI,Plotly, Excel
    - 📚 Databases: Postgres, MySQL, AWS Athena, AWS Redshift
    - 📈 Finance Applications: MB365, Fortes accounting, Athena Accounting, Excel

    """
)

# --- WORK HISTORY -- #

st.write("#")
st.subheader("Job Experience")
st.write("---")

st.write("📊", "Data Analyst | Bluemetrics")
st.write("06/2022 - current")
st.write("""
 - 🔸 Using Finance knowledge, Sisense, SQL and relational database knowledge to analyze Commercial Real Estate data from companies and make it accurate in Sisense Dashboards. 
 - 🔸 Using Python to automate tasks and workflows, as well data conversion to guarantee its correct pattern for software.
 - 🔸 Using Python and Sisense to create internal Dashboards to make the data analysis workflow easier

""")

st.write("💻", "Junior Python Developer | MyIA")
st.write("02/2022 - 06/2022")
st.write("""
- 🔸 Used Python to develop technological solutions for companies.
- 🔸 Used Python to develop Back-End structures in software creations, with Django, Dash and Streamlit.
- 🔸 Used Python and SQL to create and manage software databases.

""")

st.write("📈", "Accounting Analyst | Controller Group")
st.write("12/2021 - 02/2022")
st.write("""
 - 🔸 Accounting reports generation using Excel and Athena Accounting Software.
 - 🔸 Finance data analisys using excel and Power BI.
 - 🔸 Customer service – direct contact with client.
 - 🔸 Accounting records registration and reconciliation.

""")

st.write("📈", "Finance Analyst | Atlantic Bridge")
st.write("11/2020 - 11/2021")
st.write("""
 - 🔸 Business financial management using slack and Trello for task management.
 - 🔸 Account receivables and payables using MB 365 Software.
 - 🔸 Internal Financial Data generation and analysis using Power BI.

""")



    


