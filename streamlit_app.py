import re
import streamlit as st

st.set_page_config(page_title="Free AI Detector")

ban_list = ['adventure', 'adventures', 'adventuring', 'apologize', 'autonomy', 'apologizes', 'apologizing', 'architect', 'architecting', 'architects', 'bastion', 'bastions', 'beacon', 'beacons', 'boast', 'boasting', 'boasts', 'boost', 'boosting', 'boosts', 'bustling', 'commend', 'commendable', 'commends', 'confusion', 'crucial', 'crucially', 'dazzle', 'dazzling', 'deep understanding', 'delve', 'delves', 'delving', 'delving', 'demistify', 'demistifying', 'depicted', 'depicting', 'discover', 'discovering', 'discovers', 'dive', 'dives', 'diving', 'eerie connection', 'electrifies', 'electrify', 'electrifying', 'elegant', 'elegantly', 'elevate', 'elevates', 'elevating', 'embark', 'embarking', 'embarks', 'empower', 'empowering', 'empowers', 'endeavor', 'endeavoring', 'endeavors', 'enhance', 'enhances', 'enhancing', 'enlighten', 'enlightening', 'enlightens', 'enrich', 'enriches', 'enriching', 'entanglement', 'entanglements', 'esteem', 'ever-evolving', 'expertise', 'foster', 'fostering', 'fosters', 'grapple', 'grapples', 'grappling', 'harness', 'harnesses', 'harnessing', 'holistic', 'hurdle', 'hurdles', 'hurdling', 'illuminate', 'illuminated', 'illuminates', 'inherent', 'insurmountable', 'intersection', 'intersections', 'intricate', 'intricately', 'intrigue', 'intrigues', 'intriguing', 'invaluable', 'journey', 'journeying', 'journeys', 'labyrinth', 'labyrinths', 'landscape', 'landscapes', 'landscaping', 'large language model', 'leverag', 'leverages', 'leveraging', 'meticulously', 'multifaceted', 'myriad', 'navigate', 'navigates', 'navigating', 'navigation', 'nestled', 'nestling', 'nests', 'new era', 'nexus', 'nexuses', 'offer', 'offerings', 'offers', 'paramount', 'picture', 'pictures', 'poignantly', 'picturing', 'poised', 'powerful', 'pride', 'prides', 'priding', 'pulsate', 'pulsates', 'pulsating', 'realm', 'realms', 'relentless', 'resonate', 'resonates', 'resonating', 'revolutionize', 'revolutionizes', 'revolutionizing', 'rich', 'richly', 'seamless', 'shed light', 'supercharge', 'supercharges', 'supercharging', 'systemic', 'tailored', 'tailoring', 'tapestries', 'tapestries', 'timeless', 'tapestry', 'tapestry', 'uncover', 'uncovering', 'uncovers', 'underscore', 'underscores', 'underscoring', 'unleash', 'unleashes', 'unleashing', 'unliving', 'unlock', 'unlocking', 'unlocks', 'unprecedented', 'unravel', 'unraveling', 'unravels', 'unveiling the power', 'valuable', 'vibrant', 'vibrantly', 'weigh', 'weighing', 'weighs', 'zeitgeist']

flags = []

st.title("Common AI Word Detector")

def analyze(string):
    string = string.lower()

    for word in ban_list:
        if word.lower() in string:
            flags.append(word)      

txt = st.text_area("Text to analyze")

analyze(txt)

if txt == 0:
    ai_percent = 0
else:
    ai_percent = 100 * (len(flags)**2.5) // len(txt.split())

if st.button("Analyze text"):
    if len(flags) == 0:
        st.markdown("0 flagged words")
    else:
        st.markdown(f"{len(flags)} flagged words")
        st.write(f"Flagged words: \n{flags}")
        st.markdown(f":red[_An AI detector would flag this as **{ai_percent}% AI-generated content** ({100-ai_percent}% human-generated)_]")

st.divider()
# st.caption(":red[**Educate yourself:**] AI detectors are flawed due to oversimplification of writing styles, often mistaking consistent human writing for AI-generated text. They can unfairly target non-native English speakers by misclassifying their textbook writing patterns as artificial. These tools also struggle with AI's inability to track its past outputs, leading to misidentification.\n\n:red[**Get This:**]\nEven OpenAI was not able to track GPT-generated text, with their classifier only correctly identifying 26% of AI-written text as 'likely AI-written' (https://openai.com/blog/new-ai-classifier-for-indicating-ai-written-text)")
st.caption(":red[**Many so-called 'AI detectors'**] have resorted to flagging the mere usage of certain words as 'AI-generated'")
st.caption("This tool is for students to catch these words beforehand so they don't get falsely flagged. :triangular_flag_on_post:")




