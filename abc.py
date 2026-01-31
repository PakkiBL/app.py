import streamlit as st

st.set_page_config(page_title="Resume Skill Gap Analyzer", page_icon="📄")

st.title("📄 Resume Skill Gap Analyzer")
st.write("Identify missing skills for your target job role")

# Job roles and required skills
job_roles = {
    "Data Analyst": ["Python", "SQL", "Excel", "Power BI", "Statistics"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
    "Software Tester": ["Manual Testing", "Automation", "Selenium", "SQL", "JIRA"],
    "Digital Marketer": ["SEO", "Content Writing", "Google Ads", "Analytics"],
    "Cloud Engineer": ["AWS", "Linux", "Networking", "Docker", "Python"]
}

role = st.selectbox("🎯 Select Job Role", list(job_roles.keys()))

user_skills = st.text_input(
    "🛠 Enter your skills (comma separated)",
    placeholder="Example: Python, Excel, SQL"
)

if st.button("Analyze Skill Gap"):
    if user_skills.strip() == "":
        st.warning("Please enter at least one skill")
    else:
        user_skill_list = [s.strip().title() for s in user_skills.split(",")]
        required_skills = job_roles[role]

        matched = list(set(user_skill_list) & set(required_skills))
        missing = list(set(required_skills) - set(user_skill_list))

        st.subheader("✅ Matched Skills")
        if matched:
            st.success(", ".join(matched))
        else:
            st.info("No matching skills")

        st.subheader("❌ Missing Skills")
        if missing:
            st.error(", ".join(missing))
        else:
            st.success("You have all required skills 🎉")

        score = int((len(matched) / len(required_skills)) * 100)
        st.metric("🎯 Skill Match Percentage", f"{score}%")

        if score < 50:
            st.warning("Strong upskilling required")
        elif score < 80:
            st.info("Good progress, improve missing skills")
        else:
            st.success("Job-ready profile 👍")
