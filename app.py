from pathlib import Path
import streamlit as st
from PIL import Image, ImageDraw

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "hmcv.pdf"
profile_pic_path = current_dir / "assets" / "proimg.jpeg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hassam Rehan"
PAGE_ICON = ":wave:"
NAME = "Muhammad Hassam Rehan"
DESCRIPTION = """
 Data Analyst, Python and WordPress Developer 
"""
EMAIL = "hassam.rehank@gmail.com"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/profile.php?id=61556979432909",
    "LinkedIn": "https://www.linkedin.com/in/hassamrehan?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
    "GitHub": "https://github.com/hassamrehan222",
}

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)


# --- ROUND THE IMAGE ---
def round_image(image):
    # Create a mask to make the image round
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + image.size, fill=255)

    # Apply the mask to the image
    rounded_image = Image.new("RGBA", image.size)
    rounded_image.paste(image, (0, 0), mask=mask)

    return rounded_image


profile_pic = round_image(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")
st.write(
    """
- ✔️ MATRICULATION | Bahria Foundation School, Karachi | Graduated: 2018
- ✔️ INTERMEDIATE | Gov Dehli College, Karachi | Graduated: 2020
- ✔️ Bachelor in Computer Engineering | Bahria University, Karachi | Graduated: 2024
"""
)

# --- EXPERIENCE ---
st.write('\n')
st.subheader("Experience")
st.write(
    """
- ✔️ 4 Years Experience in Python Development
- ✔️ Strong hands-on experience and knowledge in Django 
- ✔️ Good understanding of SQL
- ✔️ Experience in WordPress
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, HTML 
- 📊 Data Analytics: Python Libraries
- 🗄️ Databases: SQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Internship | 10Coders**")
st.write("Nov 2023 - Jan 2024")
st.write(
    """
- ► Worked on a variety of web design projects using HTML, CSS, Bootstrap, and WordPress.
- ► Used clear communication and good design skills to consistently deliver well-made and effective solutions.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Artistics Milliners**")
st.write("May 2024 - June 2024")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data.
- ► Provided technical support and troubleshooting for hardware, software, and networking issues.
- ► Managed and maintained IT infrastructure, including servers, networks, and security systems.
"""
)

# --- PROJECTS ---
st.write('\n')
st.subheader("Projects")
st.write(
    """ 
- ► [E-commerce Website in Django](https://github.com/hassamrehan222/hassamrehan222-/blob/main/MyEcom.zip)
- ► [Tic Tac Toe Game](https://github.com/hassamrehan222/hassamrehan222-/blob/main/game.txt)
- ► [Cricket Web page Streamlit](https://github.com/hassamrehan222/hassamrehan222-/blob/main/cricket%20webpage.zip)
- ► [Text Utils Django Project](https://github.com/hassamrehan222/hassamrehan222-/blob/main/textutils.zip)
    """
)
