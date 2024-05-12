import streamlit as st
from datetime import datetime
from fpdf import FPDF


# PDF generation function with improved margin and text wrapping
def create_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_left_margin(10)  # Set left margin
    pdf.set_right_margin(10)  # Set right margin

    # Define the width for multi_cell
    effective_page_width = pdf.w - 2 * pdf.l_margin

    # Loop through the data and add it to the pdf
    for key, value in data.items():
        # Use multi_cell for automatic text wrapping
        pdf.multi_cell(effective_page_width, 10, f"{key}: {value}", border=0, align='L')

    pdf_filename = "Track_Info.pdf"
    pdf.output(pdf_filename)
    return pdf_filename


# Title of the app
st.title('Track Information Manager')

# Creating form to input track details
with st.form("track_info_form"):
    st.subheader("Enter Track Details")
    track_name = st.text_input("Track Name", key="track_name")
    bpm = st.number_input("BPM", min_value=1, max_value=300, step=1, key="bpm")
    track_notes = st.text_area("Notes", key="track_notes")
    take_number = st.number_input("Take Number", min_value=1, step=1, key="take_number")
    time_of_day = st.time_input("Time of Day", value=datetime.now().time(), key="time_of_day")
    date = st.date_input("Date", value=datetime.now().date(), key="date")

    # RC300 1 Instruments
    st.subheader("RC300 1 Instruments")
    rc300_1_patch1 = st.text_input("Patch 1 Instrument", key="rc300_1_patch1")
    rc300_1_patch2 = st.text_input("Patch 2 Instrument", key="rc300_1_patch2")
    rc300_1_patch3 = st.text_input("Patch 3 Instrument", key="rc300_1_patch3")

    # RC300 2 Instruments
    st.subheader("RC300 2 Instruments")
    rc300_2_patch1 = st.text_input("Patch 1 Instrument", key="rc300_2_patch1")
    rc300_2_patch2 = st.text_input("Patch 2 Instrument", key="rc300_2_patch2")
    rc300_2_patch3 = st.text_input("Patch 3 Instrument", key="rc300_2_patch3")

    # Form submit button
    submitted = st.form_submit_button("Submit")

# Handle form submission
if submitted:
    track_data = {
        "Track Name": track_name,
        "BPM": bpm,
        "Notes": track_notes,
        "Take Number": take_number,
        "Time of Day": time_of_day.strftime('%H:%M'),
        "Date": date.strftime('%Y-%m-%d'),
        "RC300 1 - Patch 1 Instrument": rc300_1_patch1,
        "RC300 1 - Patch 2 Instrument": rc300_1_patch2,
        "RC300 1 - Patch 3 Instrument": rc300_1_patch3,
        "RC300 2 - Patch 1 Instrument": rc300_2_patch1,
        "RC300 2 - Patch 2 Instrument": rc300_2_patch2,
        "RC300 2 - Patch 3 Instrument": rc300_2_patch3
    }
    pdf_file = create_pdf(track_data)
    st.success("Track Information Submitted Successfully! PDF Generated.")
    with open(pdf_file, "rb") as file:
        st.download_button("Download PDF", file, file_name=pdf_file)

