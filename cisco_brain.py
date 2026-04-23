{\rtf1\ansi\ansicpg1252\cocoartf2869
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
from crewai import Agent, Task, Crew, Process\
# Note: In a production tool, you'd use a search tool like SerperDevTool\
# from crewai_tools import SerperDevTool\
\
st.set_page_config(page_title="Cisco Architect Brain", layout="wide")\
\
# UI Styling\
st.title("\uc0\u55358 \u56800  Cisco CVD Multi-Agent Architect")\
st.sidebar.header("Configuration")\
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")\
\
# 1. Define Specialized Cisco Agents\
analyst = Agent(\
    role='Cisco Technical Lead',\
    goal='Provide exact Cisco Validated Design (CVD) specifications for Spine-Leaf fabrics.',\
    backstory='You are a CCIE-certified architect. You prioritize non-blocking fabric, ECMP, and 800G planning.',\
    verbose=True\
)\
\
visionary = Agent(\
    role='Future-Proofing Strategist',\
    goal='Apply 2026 trends like AI-ready lossless Ethernet (RoCEv2) and EVPN-VXLAN migration.',\
    backstory='You focus on scalability, "Super-Spines," and automation using Cisco Intersight.',\
    verbose=True\
)\
\
executive = Agent(\
    role='Decision Lead',\
    goal='Synthesize technical specs into a final deployment blueprint.',\
    backstory='You resolve conflicts between cost, complexity, and performance.',\
    verbose=True\
)\
\
# 2. User Input Area\
query = st.text_input("What Cisco architecture are you designing?", \
                     value="Cisco Nexus Spine-Leaf with BGP-EVPN for an AI cluster")\
\
if st.button("Consult the Brain") and api_key:\
    # 3. Tasks for the Brain\
    t1 = Task(description=f"Extract 2026 Cisco CVD best practices for: \{query\}. Focus on oversubscription and L3 underlay.", agent=analyst)\
    t2 = Task(description=f"Identify AI-specific requirements like PFC, ECN, and lossless behavior for this design.", agent=visionary)\
    t3 = Task(description="Create a 3-step deployment blueprint based on the Analyst and Visionary inputs.", agent=executive)\
\
    # 4. The Collaborative Brain\
    brain_crew = Crew(\
        agents=[analyst, visionary, executive],\
        tasks=[t1, t2, t3],\
        process=Process.sequential\
    )\
\
    with st.status("Agents are collaborating...", expanded=True) as status:\
        result = brain_crew.kickoff()\
        status.update(label="Design Complete!", state="complete")\
\
    # 5. The Output Display\
    st.divider()\
    st.header("\uc0\u55357 \u56523  Final Architecture Blueprint")\
    st.markdown(result)}