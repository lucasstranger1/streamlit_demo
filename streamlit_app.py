import streamlit as st
import pandas as pd

# Set the title of the app
st.title("Student Grade Calculator")

# Introduction
st.write("""
This app calculates your final course grade based on the weights of different components like homework, projects, midterms, and finals.
""")

# Define possible components
possible_components = ["Homework", "Projects", "Midterm Exams", "Final Exams"]

# Input the components
selected_components = st.multiselect(
    "Select the components for your course",
    options=possible_components,
    default=["Homework", "Midterm Exams", "Final Exams"]
)

# Initialize lists to store component weights and scores
component_weights = []
component_scores = []

# Loop through to get details for each selected component
for component in selected_components:
    st.subheader(f"{component}")

    # Input for component weight
    component_weight = st.slider(f"Weight of {component} (%)", min_value=0, max_value=100, value=25)
    component_weights.append(component_weight)
    
    # Input for component score
    component_score = st.slider(f"Score in {component} (%)", min_value=0, max_value=100, value=75)
    component_scores.append(component_score)

# Calculate final grade
total_weight = sum(component_weights)
final_grade = sum([(component_weights[i] * component_scores[i]) for i in range(len(selected_components))]) / total_weight

# Display the final grade
st.subheader("Your Final Grade")
st.write(f"Based on the components you entered, your final grade is **{final_grade:.2f}%**.")

# Determine the letter grade
if final_grade >= 93:
    st.success("You received an **A** in the course! Excellent work!")
elif final_grade >= 85:
    st.success("You received a **B** in the course. Good job!")
elif final_grade >= 75:
    st.warning("You received a **C** in the course. You passed!")
else:
    st.error("You received a **D** or **F** in the course. You may need to retake this course.")

# Optional: Display a summary of inputs
st.subheader("Summary of Inputs")
summary_data = {
    "Component": selected_components,
    "Weight (%)": component_weights,
    "Score (%)": component_scores
}
summary_df = pd.DataFrame(summary_data)
st.dataframe(summary_df)
