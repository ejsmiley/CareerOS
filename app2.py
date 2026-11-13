
import streamlit as st
import re

st.set_page_config(
    page_title="CareerOS | Career Copilot",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------- THEME ---------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
  --bg:#101327;
  --panel:#191e39;
  --panel2:#202747;
  --line:#343c63;
  --text:#f4f5ff;
  --muted:#a7b0cc;
  --purple:#795bff;
  --blue:#38bdf8;
  --mint:#2dd4bf;
  --coral:#fb7185;
  --green:#2dd4a7;
  --amber:#fbbf24;
}
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
.stApp {
  background:
    radial-gradient(ellipse at 88% 0%, rgba(121,91,255,.22), transparent 34%),
    radial-gradient(ellipse at 4% 35%, rgba(56,189,248,.10), transparent 30%),
    var(--bg);
  color:var(--text);
}
.block-container { max-width:1440px; padding-top:1.6rem; padding-bottom:3rem; }
h1,h2,h3,h4 {
  color:var(--text)!important;
  font-family:'Space Grotesk',sans-serif!important;
  letter-spacing:-.035em;
}
p, label, li, .stMarkdown { color:#d2d7eb; }
[data-testid="stSidebar"] {
  background:#131832;
  border-right:1px solid var(--line);
}
[data-testid="stSidebar"] > div { padding-top:1.3rem; }
[data-testid="stMetric"] {
  background:linear-gradient(145deg,#22294b,#191e39);
  border:1px solid #3b4774;
  padding:19px;
  border-radius:17px;
  box-shadow:0 10px 30px rgba(0,0,0,.12);
}
[data-testid="stMetricLabel"] { color:var(--muted)!important; }
[data-testid="stMetricValue"] {
  color:var(--text)!important;
  font-family:'Space Grotesk',sans-serif;
}
[data-testid="stMetricDelta"] { color:var(--mint)!important; }
.stButton > button {
  background:linear-gradient(105deg,var(--purple),#536dff 55%,var(--blue));
  color:white;
  border:1px solid transparent;
  border-radius:11px;
  min-height:45px;
  font-weight:700;
  box-shadow:0 8px 24px rgba(121,91,255,.25);
  transition:all .18s ease;
}
.stButton > button:hover {
  border:1px solid rgba(56,189,248,.65);
  color:white;
  filter:brightness(1.12);
  transform:translateY(-2px);
  box-shadow:0 12px 28px rgba(56,189,248,.18);
}
.stTextInput input,.stTextArea textarea {
  background:#141a33!important;
  color:var(--text)!important;
  border:1px solid #414b76!important;
  border-radius:10px!important;
}
.stTextInput input:focus,.stTextArea textarea:focus {
  border-color:var(--blue)!important;
  box-shadow:0 0 0 1px var(--blue)!important;
}
.stTabs [data-baseweb="tab-list"] {
  gap:8px;
  background:#151a33;
  border:1px solid var(--line);
  padding:7px;
  border-radius:14px;
}
.stTabs [data-baseweb="tab"] {
  color:#c3cbe2;
  border-radius:9px;
  padding:10px 16px;
}
.stTabs [aria-selected="true"] {
  background:linear-gradient(105deg,var(--purple),#536dff)!important;
  color:white!important;
}
div[data-testid="stProgressBar"] > div > div {
  background:linear-gradient(90deg,var(--purple),var(--blue),var(--mint));
  border-radius:99px;
}
hr { border-color:var(--line); }
.eyebrow {
  color:#9e91ff;
  font-size:11px;
  font-weight:800;
  letter-spacing:2px;
  text-transform:uppercase;
}
.hero {
  background:
    radial-gradient(circle at 88% 20%, rgba(56,189,248,.22), transparent 28%),
    linear-gradient(112deg,#292653 0%,#37306f 52%,#18334f 100%);
  border:1px solid #6559a8;
  border-radius:22px;
  padding:30px 32px;
  position:relative;
  overflow:hidden;
  margin-bottom:24px;
  box-shadow:0 18px 45px rgba(0,0,0,.18);
}
.hero:after {
  content:"";
  position:absolute;
  width:260px;height:260px;
  right:-75px;top:-105px;
  border-radius:50%;
  background:rgba(121,91,255,.12);
  border:1px solid rgba(180,170,255,.2);
}
.hero h1 { font-size:36px!important; margin:8px 0 7px 0; }
.hero p { color:#e0e4ff; margin-bottom:0; font-size:15px; }
.pill {
  display:inline-block;
  padding:6px 10px;
  border-radius:99px;
  font-size:11px;
  font-weight:700;
  background:rgba(45,212,191,.16);
  border:1px solid rgba(45,212,191,.35);
  color:#a5fff0;
  margin-top:15px;
}
.section-kicker {
  color:#9e91ff;
  text-transform:uppercase;
  font-size:11px;
  font-weight:800;
  letter-spacing:1.5px;
}
.panel {
  background:linear-gradient(145deg,#202747,#191e39);
  border:1px solid #343f68;
  border-radius:17px;
  padding:19px;
  margin:8px 0;
  box-shadow:0 9px 24px rgba(0,0,0,.10);
}
.panel-title { color:#f5f6ff; font-size:16px; font-weight:800; margin-bottom:5px; }
.muted { color:var(--muted); font-size:13px; }
.score-number {
  font-family:'Space Grotesk',sans-serif;
  font-size:48px;
  line-height:1;
  font-weight:700;
  color:#a99aff;
}
.score-sub { color:var(--muted); font-size:12px; margin-top:7px; }
.skill {
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:10px 12px;
  border-radius:10px;
  background:#151b34;
  border:1px solid #343f68;
  margin:7px 0;
}
.tag { font-size:11px; font-weight:800; padding:4px 8px; border-radius:99px; }
.tag-green { background:rgba(45,212,167,.14); color:#72f2cf; }
.tag-amber { background:rgba(251,191,36,.14); color:#ffdc83; }
.tag-purple { background:rgba(121,91,255,.18); color:#c9bdff; }
.roadmap-step { border-left:2px solid var(--blue); padding:2px 0 14px 15px; margin-left:7px; }
.roadmap-step:last-child { border-left-color:transparent; }
.roadmap-num { color:#80d9ff; font-size:11px; font-weight:800; letter-spacing:1px; }
div[data-testid="stAlert"] { border-radius:12px; }
footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# ------------------------- STATE ----------------------------
defaults = {
    "career_result": False, "job_result": False, "question": False,
    "feedback": False, "answer": "", "job_description": "",
    "question_text": "Tell me about a project where you used your technical skills to solve a problem. What was your contribution?",
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ------------------------- HELPERS --------------------------
def panel(title, body="", extra_class=""):
    st.markdown(
        f'<div class="panel {extra_class}"><div class="panel-title">{title}</div>{body}</div>',
        unsafe_allow_html=True,
    )

def score_card(score, label, note):
    st.markdown(f"""
    <div class="panel" style="text-align:center;padding:23px 15px;">
      <div class="section-kicker">{label}</div>
      <div style="width:142px;height:142px;border-radius:50%;margin:17px auto 12px;
        background:conic-gradient(#795bff {score*3.6}deg,#343c63 0deg);
        display:grid;place-items:center;">
        <div style="width:116px;height:116px;border-radius:50%;background:#191e39;display:flex;flex-direction:column;align-items:center;justify-content:center;">
          <div class="score-number" style="font-size:39px;">{score}</div>
          <div class="muted">/ 100</div>
        </div>
      </div>
      <div class="muted">{note}</div>
    </div>
    """, unsafe_allow_html=True)

def skill_row(name, status, kind):
    st.markdown(
        f'<div class="skill"><span>{name}</span><span class="tag tag-{kind}">{status}</span></div>',
        unsafe_allow_html=True,
    )

# -------------------------- SIDEBAR -------------------------
with st.sidebar:
    st.markdown("## CareerOS")
    st.caption("YOUR PERSONAL CAREER COPILOT")
    st.divider()
    st.markdown("### Your profile")
    name = st.text_input("Your name", "Alex")
    target = st.text_input("Target role", "Data Analyst Intern")
    education = st.text_input("Education", "Computer Science student")
    skills = st.text_area("Your skills", "Python, Excel, communication, teamwork", height=95)
    resume = st.text_area(
        "Experience / Resume",
        "Computer Science student with Python and Excel experience. Completed university projects and worked in a student team.",
        height=125,
    )
    st.divider()
    st.markdown("### Demo environment")
    st.success("SIMULATED DEMO MODE")
    st.caption("Scores and feedback are prepared examples. No external AI service or API calls are used.")
    if st.button("Reset demo", use_container_width=True):
        for key, value in defaults.items():
            st.session_state[key] = value
        st.rerun()

# --------------------------- HEADER -------------------------
st.markdown(f"""
<div class="hero">
  <div class="eyebrow">Your next chapter starts here</div>
  <h1>Build a career that fits you, {name}.</h1>
  <p>Your personal career workspace: understand your strengths, find your fit, and practice your next opportunity.</p>
  <span class="pill">CAREEROS · INTERACTIVE HACKATHON PROTOTYPE</span>
</div>
""", unsafe_allow_html=True)

# ------------------------- OVERVIEW -------------------------
st.markdown('<div class="section-kicker">Your workspace</div>', unsafe_allow_html=True)
st.markdown("## Career overview")
st.caption(f"A snapshot of your progress toward becoming a {target}.")
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Career readiness", "72 / 100" if st.session_state.career_result else "—", "Demo assessment" if st.session_state.career_result else "Ready to assess")
with m2:
    st.metric("Job compatibility", "65 / 100" if st.session_state.job_result else "—", "Demo estimate" if st.session_state.job_result else "Add a job description")
with m3:
    st.metric("Interview practice", "7 / 10" if st.session_state.feedback else "—", "Sample feedback" if st.session_state.feedback else "Not started")

st.markdown("---")
tab1, tab2, tab3 = st.tabs(["Career Analysis", "CareerMatch", "Interview Studio"])

# ======================= CAREER ANALYSIS =====================
with tab1:
    st.markdown("## Discover your potential")
    st.caption(f"Turn your current experience into a practical plan for your {target} goal.")
    a, b = st.columns([1.05, 1.95], gap="large")
    with a:
        panel("Career assessment", '<div class="muted">A guided snapshot of your strengths and development areas.</div>')
        if st.button("Analyze my career readiness", key="career_button", use_container_width=True):
            st.session_state.career_result = True
    with b:
        if st.session_state.career_result:
            score_card(72, "Career readiness", "Illustrative demo score · not an actual AI assessment")
        else:
            panel("Your readiness score", '<div class="score-number">—</div><div class="muted">Run your assessment to reveal your sample readiness snapshot.</div>')
    if st.session_state.career_result:
        st.markdown("### Your strengths & growth areas")
        left, right = st.columns(2, gap="large")
        with left:
            panel("What you already bring", '<div class="muted">Strengths based on the sample profile.</div>')
            for s in ["Python fundamentals", "Excel and spreadsheets", "Communication", "Team collaboration"]:
                skill_row(s, "Strength", "green")
        with right:
            panel("Skills to build next", '<div class="muted">Common development areas for entry-level data roles.</div>')
            for s in ["SQL & database querying", "Data visualization", "Statistics"]:
                skill_row(s, "Priority", "amber")
        st.markdown("### Your career readiness roadmap")
        steps = [
            ("01 · BUILD THE FOUNDATION", "Learn SQL fundamentals", "Practice filtering, joins, grouping, and aggregations."),
            ("02 · SHOW WHAT YOU KNOW", "Create a data dashboard", "Use a public dataset to build a clear, useful visualization."),
            ("03 · MAKE YOUR WORK VISIBLE", "Publish a portfolio project", "Document your process, insights, and results in a portfolio."),
        ]
        for eyebrow, title, desc in steps:
            st.markdown(f'<div class="roadmap-step"><div class="roadmap-num">{eyebrow}</div><b>{title}</b><div class="muted">{desc}</div></div>', unsafe_allow_html=True)
        st.info("Next best step: complete one practical project that demonstrates your data analysis skills.")

# =========================== CAREERMATCH =====================
with tab2:
    st.markdown("## CareerMatch")
    st.caption("See how your current profile lines up with an opportunity—and what could make you a stronger candidate.")
    st.markdown('<div class="panel"><div class="panel-title">01 · Add an opportunity</div><div class="muted">Paste a job description to start your sample match experience.</div></div>', unsafe_allow_html=True)
    job = st.text_area(
        "Job description",
        value=st.session_state.job_description,
        height=145,
        placeholder="Paste the role summary, responsibilities, and qualifications here...",
        label_visibility="collapsed",
    )
    if job != st.session_state.job_description:
        st.session_state.job_description = job
        st.session_state.job_result = False

    if st.button("Generate my match report", key="job_button", use_container_width=True):
        if not job.strip():
            st.warning("Paste a job description first to continue.")
        else:
            st.session_state.job_result = True

    if st.session_state.job_result:
        st.markdown("---")
        st.markdown('<div class="section-kicker">02 · Your match report</div>', unsafe_allow_html=True)
        left, right = st.columns([1, 1.65], gap="large")
        with left:
            score_card(65, "Overall compatibility", "Illustrative demo estimate · not calculated from job text")
        with right:
            panel("Your match at a glance", '<div class="muted">Example comparison for an entry-level data analyst profile.</div>')
            st.markdown("**Skills you can highlight**")
            for s in ["Python fundamentals", "Excel experience", "Communication", "Team collaboration"]:
                skill_row(s, "Matched", "green")
            st.markdown("**Skills to strengthen**")
            for s in ["SQL & database querying", "Power BI / Tableau", "Reporting experience"]:
                skill_row(s, "Gap", "amber")
        st.markdown("### Turn this match into a stronger application")
        c1, c2, c3 = st.columns(3)
        with c1:
            panel("01 · Prove your skills", '<div class="muted">Add a Python or Excel project with a clear outcome to your resume.</div>')
        with c2:
            panel("02 · Close a gap", '<div class="muted">Build a small SQL project using a real-world dataset.</div>')
        with c3:
            panel("03 · Show your impact", '<div class="muted">Describe what you analyzed, what you found, and why it mattered.</div>')
        st.info("Resume tip: use specific, truthful examples. Never claim a skill or experience you do not have.")

# ======================== INTERVIEW STUDIO ==================
with tab3:
    st.markdown("## Interview Studio")
    st.caption(f"Practice communicating your strengths for an entry-level {target} opportunity.")
    panel("Your practice session", '<div class="muted">Answer a sample behavioral question, then review structured example feedback.</div>')
    if st.button("Get an interview question", key="question_button", use_container_width=True):
        st.session_state.question = True
        st.session_state.feedback = False
        st.session_state.answer = ""
    if st.session_state.question:
        st.markdown('<div class="section-kicker">Question 01 · Behavioral</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel"><div style="font-size:19px;font-weight:700;color:#f5f7ff;">“{st.session_state.question_text}”</div><div class="muted" style="margin-top:9px;">Tip: structure your response using Situation, Task, Action, and Result.</div></div>', unsafe_allow_html=True)
        answer = st.text_area("Your answer", key="answer", height=165, placeholder="Write your answer here...")
        if st.button("Review my answer", key="evaluate_button", use_container_width=True):
            if not answer.strip():
                st.warning("Write a response before requesting feedback.")
            else:
                st.session_state.feedback = True
        if st.session_state.feedback:
            st.markdown("---")
            st.markdown('<div class="section-kicker">Example feedback</div>', unsafe_allow_html=True)
            x, y = st.columns([1, 2], gap="large")
            with x:
                score_card(70, "Sample score", "Illustrative feedback · answer not actually analyzed")
            with y:
                panel("What works well", '<div class="muted">• You addressed the prompt<br>• You referenced relevant technical skills<br>• You showed collaboration</div>')
                panel("How to make it stronger", '<div class="muted">• Explain the challenge in more detail<br>• Clarify your personal contribution<br>• Include a measurable result</div>')
            st.info("Try again using STAR: Situation → Task → Action → Result.")

# ---------------------------- FOOTER -------------------------
st.markdown("---")
st.markdown("""
<div style="text-align:center;padding:12px 0 4px;">
  <div style="font-family:'Space Grotesk';font-size:20px;font-weight:700;color:#f3f6ff;">CareerOS</div>
  <div style="font-size:12px;color:#8798b4;">From classroom to career · Interactive prototype with simulated responses</div>
</div>
""", unsafe_allow_html=True)
