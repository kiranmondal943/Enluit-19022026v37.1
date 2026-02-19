import streamlit as st
import zipfile
import io
import json
import re
import requests
import datetime

# --- 0. STATE MANAGEMENT ---
def init_state(key, default_val):
    if key not in st.session_state:
        st.session_state[key] = default_val

# Load Default Data (Persisting v37 Defaults)
init_state('hero_h', "Stop Paying Rent for Your Website.")
init_state('hero_sub', "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees. Pay once. Own it forever.")
init_state('about_h', "Control Your Empire from a Spreadsheet")
init_state('about_short', "No WordPress dashboard. No plugins to update. Just open your private Google Sheet, change a text, and watch your site update globally in seconds.")
init_state('feat_data', "bolt | The Performance Pillar | **0.1s High-Velocity Loading**. Titan loads instantly.\nwallet | The Economic Pillar | **$0 Monthly Fees**. We eliminated hosting subscriptions.\ntable | The Functional Pillar | **Google Sheets CMS**. Update prices/photos from a spreadsheet.\nshield | The Authority Pillar | **Unhackable Security**. Zero-DB Architecture.\nlayers | The Reliability Pillar | **Global Edge Deployment**. Distributed across 100+ servers.\nstar | The Conversion Pillar | **One-Tap WhatsApp**. Direct-to-Chat technology.")

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v100 | Eternity Edition", 
    layout="wide", 
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# --- 2. STREAMLIT UI STYLING (The Builder Interface) ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #ef4444; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3rem;
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
        color: white; font-weight: 700; border: none; transition: transform 0.2s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: THE COCKPIT ---
with st.sidebar:
    st.title("💎 Titan Architect")
    st.caption("v100.0 | Eternity Edition")
    
    # DIAGNOSTICS (NEW)
    with st.expander("🩺 System Diagnostics", expanded=True):
        health = 100
        issues = []
        if not st.session_state.hero_h: health -= 20; issues.append("Missing Hero Text")
        if not st.session_state.feat_data: health -= 20; issues.append("Missing Features")
        st.metric("Health Score", f"{health}%", f"{0 if health==100 else -1*(100-health)}")
        if issues: st.caption("Issues: " + ", ".join(issues))
        else: st.caption("System Optimal")

    # AI GENERATOR (V37 Feature)
    with st.expander("🤖 AI Neural Writer", expanded=False):
        groq_key = st.text_input("Groq API Key", type="password")
        biz_desc = st.text_input("Business Context")
        if st.button("✨ Generate DNA"):
            if groq_key and biz_desc:
                try:
                    with st.spinner("Synthesizing..."):
                        url = "https://api.groq.com/openai/v1/chat/completions"
                        headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                        prompt = f"Return JSON for '{biz_desc}': hero_h, hero_sub, about_h, about_short, feat_data (icon|Title|Desc)."
                        data = {"messages": [{"role": "user", "content": prompt}], "model": "llama3-8b-8192", "response_format": {"type": "json_object"}}
                        resp = requests.post(url, headers=headers, json=data).json()['choices'][0]['message']['content']
                        parsed = json.loads(resp)
                        for k,v in parsed.items():
                            if k == 'feat_data' and isinstance(v, list): v = "\n".join(v)
                            st.session_state[k] = str(v)
                        st.success("Neural injection complete.")
                        st.rerun()
                except Exception as e: st.error(f"Error: {e}")

    # VISUAL DNA (Merged V37 & V50)
    with st.expander("🎨 Visual DNA", expanded=True):
        # Includes all V37 themes + New Glassmorphism
        theme_mode = st.selectbox("Base Theme", ["Glassmorphism (Blur)", "Clean Corporate (Light)", "Midnight SaaS (Dark)", "Cyberpunk Neon", "Luxury Gold", "Forest Eco", "Ocean Breeze", "Stark Minimalist"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#0F172A") 
        s_color = c2.color_picker("Accent (CTA)", "#EF4444")
        
        st.markdown("**Typography & Physics**")
        font_pair = st.selectbox("Font Pairing", ["Montserrat / Inter", "Playfair / Lato", "Space Grotesk / Roboto", "Oswald / Open Sans"])
        border_rad = st.slider("Corner Radius", 0, 50, 16)
        anim_type = st.selectbox("Animation", ["Fade Up", "Zoom In", "Slide Right", "None"])

    # MODULES (Smart Nav Inputs)
    with st.expander("🧩 Quantum Modules", expanded=False):
        show_hero = st.checkbox("Hero Section", True)
        show_stats = st.checkbox("Trust Stats", True)
        show_features = st.checkbox("Features Grid", True)
        show_pricing = st.checkbox("Pricing Table", True)
        show_inventory = st.checkbox("Smart Store", True)
        show_blog = st.checkbox("Blog Engine", True)
        show_gallery = st.checkbox("About/Gallery", True)
        show_testimonials = st.checkbox("Testimonials", True)
        show_faq = st.checkbox("FAQ Accordion", True)
        show_cta = st.checkbox("Final CTA", True)
        show_booking = st.checkbox("Booking Widget", True)
        
        st.caption("Advanced Features (v100)")
        show_cookie = st.checkbox("GDPR Cookie Banner", True)
        show_wa_float = st.checkbox("Floating WhatsApp", True)
        show_dark_toggle = st.checkbox("Frontend Dark Toggle", True)

# --- 4. MAIN WORKSPACE ---
st.title("💎 Titan v100 Builder")
tabs = st.tabs(["1. Identity", "2. Content", "3. Marketing", "4. Pricing", "5. Store", "6. Booking", "7. Blog", "8. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent.com")
        biz_phone = st.text_input("Phone", "966572562151")
        biz_email = st.text_input("Email", "hello@titan.com")
    with c2:
        prod_url = st.text_input("Live URL", "https://stopwebrent.com")
        logo_url = st.text_input("Logo URL (PNG/SVG)")
        biz_addr = st.text_area("Address", "Kaydiem Script Lab, India", height=100)

    st.subheader("Social & PWA")
    wa_num = st.text_input("WhatsApp (No +)", "966572562151")
    lang_sheet = st.text_input("Translation CSV URL")
    
    sc1, sc2, sc3 = st.columns(3)
    fb_link = sc1.text_input("Facebook URL")
    x_link = sc2.text_input("X (Twitter) URL")
    ig_link = sc3.text_input("Instagram URL")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", st.session_state.hero_h)
    hero_sub = st.text_input("Hero Subtext", st.session_state.hero_sub)
    hero_video_id = st.text_input("YouTube Video ID (Optional Background)", placeholder="e.g. dQw4w9WgXcQ")
    
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Slide 1", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    hero_img_2 = hc2.text_input("Slide 2", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1600")
    hero_img_3 = hc3.text_input("Slide 3", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1600")
    
    st.divider()
    st.subheader("Stats & Features")
    c1, c2, c3 = st.columns(3)
    stat_1 = c1.text_input("Stat 1", "0.1s")
    label_1 = c1.text_input("Label 1", "Speed")
    stat_2 = c2.text_input("Stat 2", "$0")
    label_2 = c2.text_input("Label 2", "Fees")
    stat_3 = c3.text_input("Stat 3", "100%")
    label_3 = c3.text_input("Label 3", "Ownership")
    
    f_title = st.text_input("Features Title", "Value Pillars")
    feat_data_input = st.text_area("Features (icon|Title|Desc)", st.session_state.feat_data, height=150)
    
    st.subheader("About")
    about_h_in = st.text_input("About Title", st.session_state.about_h)
    about_img = st.text_input("About Image", "https://images.unsplash.com/photo-1543286386-713df548e9cc?q=80&w=1600")
    about_short_in = st.text_area("About Summary", st.session_state.about_short, height=100)
    about_long = st.text_area("About Full Text (Markdown)", "**The Trap**\nMost business owners pay rent...", height=150)

with tabs[2]:
    st.subheader("Marketing Suite (V37 Legacy)")
    top_bar_enabled = st.checkbox("Enable Top Announcement Bar")
    top_bar_text = st.text_input("Top Bar Text", "🔥 50% OFF Launch Sale - Ends Soon!")
    top_bar_link = st.text_input("Top Bar Link", "#pricing")
    
    st.divider()
    popup_enabled = st.checkbox("Enable Lead Gen Popup")
    popup_delay = st.slider("Popup Delay (sec)", 1, 30, 5)
    popup_title = st.text_input("Popup Title", "Wait! Don't leave empty handed.")
    popup_text = st.text_input("Popup Body", "Get our free pricing guide.")
    popup_cta = st.text_input("Popup Button", "Get Offer")

with tabs[3]:
    c1, c2, c3 = st.columns(3)
    titan_price = c1.text_input("Your Setup Price", "$199")
    titan_mo = c1.text_input("Your Monthly Fee", "$0")
    wix_name = c2.text_input("Competitor Name", "Wix")
    wix_mo = c2.text_input("Competitor Monthly", "$29/mo")
    save_val = c3.text_input("Total Savings", "$1,466")

with tabs[4]:
    st.info("💡 **Pro Tip (v50):** Separate multiple images with `|`. Example: `img1.jpg | img2.jpg`")
    sheet_url = st.text_input("Store CSV URL", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Fallback Image", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")
    c1, c2 = st.columns(2)
    paypal_link = c1.text_input("PayPal Link")
    upi_id = c2.text_input("UPI ID")

with tabs[5]:
    booking_embed = st.text_area("Calendly Embed Code", height=100)
    booking_title = st.text_input("Booking Title", "Book a Call")
    booking_desc = st.text_input("Booking Subtext", "Select a time below.")

with tabs[6]:
    blog_sheet_url = st.text_input("Blog CSV URL")
    blog_hero_title = st.text_input("Blog Title", "Insights")
    blog_hero_sub = st.text_input("Blog Subtext", "Latest updates from the team.")

with tabs[7]:
    seo_d = st.text_area("Meta Description", "Stop paying monthly fees.")
    seo_kw = st.text_input("Keywords", "website builder, no code")
    testi_data = st.text_area("Testimonials (Name|Quote)", "Elon M.|Incredible architecture.\nJeff B.|Fastest site ever.")
    faq_data = st.text_area("FAQ (Q? ? A)", "Is it free? ? Yes, you own the code.")
    priv_txt = st.text_area("Privacy Policy", "We collect minimal data.")
    term_txt = st.text_area("Terms of Service", "You own the source code.")
    cookie_txt = st.text_input("Cookie Text", "We use cookies to improve experience.")

# --- 5. THE QUANTUM COMPILER ---

def format_text(text):
    if not text: return ""
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    lines = text.split('\n')
    html = ""
    in_list = False
    for line in lines:
        if line.strip().startswith("* "):
            if not in_list: html += '<ul style="margin-bottom:1rem; padding-left:1.5rem;">'; in_list = True
            html += f'<li style="margin-bottom:0.5rem; opacity:0.9;">{line.strip()[2:]}</li>'
        else:
            if in_list: html += "</ul>"; in_list = False
            if line.strip(): html += f"<p style='margin-bottom:1rem; opacity:0.9;'>{line}</p>"
    if in_list: html += "</ul>"
    return html

def get_simple_icon(name):
    name = name.lower().strip()
    path = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"
    if "bolt" in name: path = "M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"
    if "wallet" in name: path = "M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"
    if "shield" in name: path = "M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"
    if "star" in name: path = "M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
    if "layers" in name: path = "M11.99 18.54l-7.37-5.73L3 14.07l9 7 9-7-1.63-1.27-7.38 5.74zM12 16l7.36-5.73L21 9l-9-7-9 7 1.63 1.27L12 16z"
    if "table" in name: path = "M10 10.02h5V21h-5zM17 21h3c1.1 0 2-.9 2-2v-9h-5v11zm3-18H5c-1.1 0-2 .9-2 2v3h19V5c0-1.1-.9-2-2-2zM3 19c0 1.1.9 2 2 2h3V10H3v9z"
    return f'<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="{path}"/></svg>'

def get_theme_css():
    h_font = font_pair.split(" / ")[0]
    b_font = font_pair.split(" / ")[1]
    
    # CSS Variable Logic for Hybrid Theme Engine
    bg, txt, card, glass_bg, glass_border = "#ffffff", "#0f172a", "#ffffff", "rgba(255, 255, 255, 0.8)", "rgba(255, 255, 255, 0.3)"
    
    if "Midnight" in theme_mode:
        bg, txt, card, glass_bg, glass_border = "#0f172a", "#f8fafc", "#1e293b", "rgba(15, 23, 42, 0.8)", "rgba(255, 255, 255, 0.1)"
    elif "Cyberpunk" in theme_mode:
        bg, txt, card, glass_bg, glass_border = "#050505", "#00ff9d", "#111", "rgba(0,0,0,0.8)", "rgba(0, 255, 157, 0.2)"
    elif "Glassmorphism" in theme_mode:
        bg = "linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%)"
        card = "rgba(255, 255, 255, 0.4)" # Translucent cards
    elif "Luxury" in theme_mode:
        bg, txt, card, glass_bg, glass_border = "#1c1c1c", "#D4AF37", "#2a2a2a", "rgba(28,28,28,0.9)", "rgba(212, 175, 55, 0.2)"
    
    anim_css = ""
    if anim_type == "Fade Up": anim_css = ".reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease-out; } .reveal.active { opacity: 1; transform: translateY(0); }"
    elif anim_type == "Zoom In": anim_css = ".reveal { opacity: 0; transform: scale(0.95); transition: all 0.8s ease; } .reveal.active { opacity: 1; transform: scale(1); }"

    # HERO LAYOUT CSS
    hero_align = "text-align: center; justify-content: center;"
    if hero_layout == "Left": hero_align = "text-align: left; justify-content: flex-start; align-items: center;"

    return f"""
    :root {{
        --p: {p_color}; --s: {s_color}; --bg: {bg}; --txt: {txt}; --card: {card};
        --glass: {glass_bg}; --border: {glass_border}; --radius: {border_rad}px;
        --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ 
        background: var(--bg); color: var(--txt); font-family: var(--b-font); 
        line-height: 1.6; overflow-x: hidden; transition: background 0.3s, color 0.3s;
    }}
    
    /* DARK MODE ENGINE */
    body.dark-mode {{ 
        --bg: #0f172a; --txt: #f8fafc; --card: #1e293b; 
        --glass: rgba(30, 41, 59, 0.8); --border: rgba(255, 255, 255, 0.05); 
    }}

    h1, h2, h3 {{ font-family: var(--h-font); font-weight: 800; line-height: 1.1; margin-bottom: 1rem; }}
    a {{ text-decoration: none; color: inherit; transition: 0.3s; }}
    
    /* GLASSMORPHISM UTILS */
    .glass {{
        background: var(--glass);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.05);
    }}
    
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
    section {{ padding: clamp(3rem, 5vw, 6rem) 0; }}
    
    /* NAVIGATION */
    nav {{ 
        position: fixed; top: 0; left: 0; width: 100%; z-index: 1000;
        padding: 1rem 0; transition: top 0.3s;
        border-bottom: 1px solid var(--border);
    }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; gap: 2rem; align-items: center; }}
    .nav-links a {{ font-weight: 600; opacity: 0.8; font-size: 0.9rem; position: relative; }}
    .nav-links a:hover {{ opacity: 1; color: var(--s); }}
    .mobile-menu {{ display: none; font-size: 1.5rem; cursor: pointer; }}

    /* HERO */
    .hero {{ 
        position: relative; min-height: 90vh; display: flex; {hero_align} 
        color: white; padding-top: 80px; overflow: hidden; background: var(--p);
    }}
    .carousel-slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.5s ease-in-out; z-index: 0; }}
    .carousel-slide.active {{ opacity: 1; }}
    .hero-overlay {{ background: rgba(0,0,0,0.5); position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }}
    .hero-content {{ z-index: 2; position: relative; max-width: 800px; padding: 0 20px; }}
    .hero h1 {{ 
        font-size: clamp(2.5rem, 5vw, 4.5rem); margin-bottom: 1rem; 
        text-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }}
    .hero p {{ font-size: 1.2rem; opacity: 0.95; margin-bottom: 2rem; color: white !important; }}

    /* APPLE-STYLE CARDS */
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 2rem; }}
    .card {{ 
        background: var(--card); border-radius: var(--radius); border: 1px solid var(--border); 
        overflow: hidden; transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex; flex-direction: column;
    }}
    .card:hover {{ transform: translateY(-10px); box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1); border-color: var(--s); }}
    
    .prod-img-box {{ height: 280px; width: 100%; background: #f1f5f9; overflow: hidden; position: relative; }}
    .prod-img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
    .card:hover .prod-img {{ transform: scale(1.05); }}
    .card-content {{ padding: 1.5rem; text-align: center; }}
    
    /* BUTTONS */
    .btn {{ 
        padding: 0.8rem 2rem; border-radius: {border_rad if btn_style == 'Rounded (Default)' else '50px' if btn_style == 'Pill (Full Round)' else '0px'};
        font-weight: 700; cursor: pointer; border: none; display: inline-block; transition: 0.3s;
        text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem;
    }}
    .btn-primary {{ background: var(--p); color: white; }}
    .btn-accent {{ background: var(--s); color: white; }}
    .btn:hover {{ transform: translateY(-2px); box-shadow: 0 10px 20px rgba(0,0,0,0.15); filter: brightness(1.1); }}

    /* PRODUCT DETAIL & GALLERY */
    .detail-container {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; padding-top: 150px; }}
    .gallery-main {{ 
        width: 100%; height: 500px; object-fit: cover; border-radius: var(--radius); 
        margin-bottom: 1rem; box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }}
    .gallery-thumbs {{ display: flex; gap: 10px; overflow-x: auto; padding-bottom: 10px; }}
    .thumb {{ 
        width: 80px; height: 80px; object-fit: cover; border-radius: 12px; 
        cursor: pointer; opacity: 0.6; transition: 0.3s; border: 2px solid transparent;
    }}
    .thumb:hover, .thumb.active {{ opacity: 1; border-color: var(--s); }}

    /* TOAST SYSTEM */
    #toast-box {{ position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%); z-index: 9999; display: flex; flex-direction: column; gap: 10px; }}
    .toast {{ 
        background: var(--txt); color: var(--bg); padding: 12px 24px; border-radius: 50px; 
        font-weight: 600; box-shadow: 0 10px 30px rgba(0,0,0,0.2); 
        opacity: 0; transform: translateY(20px); transition: 0.4s;
    }}
    .toast.show {{ opacity: 1; transform: translateY(0); }}

    /* FLOATING WIDGETS */
    .float-btn {{ 
        position: fixed; width: 50px; height: 50px; border-radius: 50%; 
        display: flex; align-items: center; justify-content: center; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); z-index: 990; cursor: pointer; border: 1px solid var(--border);
    }}
    #wa-float {{ bottom: 100px; right: 30px; background: #25D366; color: white; border: none; }}
    #cart-float {{ bottom: 30px; right: 30px; background: var(--p); color: white; border: none; }}
    #mode-toggle {{ bottom: 30px; left: 30px; background: var(--card); color: var(--txt); }}

    /* UTILS */
    .about-grid, .contact-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }}
    footer {{ background: var(--p); color: white; padding: 4rem 0; margin-top: auto; }}
    footer a {{ color: rgba(255,255,255,0.7); display: block; margin-bottom: 0.5rem; }}
    .social-icon {{ width: 24px; height: 24px; fill: white; margin-right: 10px; }}
    
    #top-bar {{ position: fixed; top: 0; width: 100%; background: var(--s); color: white; text-align: center; padding: 8px; z-index: 1002; font-weight: bold; font-size: 0.85rem; }}
    #top-bar a {{ color: white; text-decoration: underline; }}
    
    #lead-popup {{ display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: var(--card); padding: 3rem; text-align: center; border-radius: var(--radius); z-index: 2000; box-shadow: 0 25px 100px rgba(0,0,0,0.5); width: 90%; max-width: 450px; border: 1px solid var(--border); }}
    
    .pricing-table {{ width: 100%; border-collapse: collapse; min-width: 600px; }}
    .pricing-table th {{ background: var(--p); color: white; padding: 1.5rem; text-align: left; }}
    .pricing-table td {{ padding: 1.5rem; border-bottom: 1px solid var(--border); background: var(--card); }}

    {anim_css}
    
    @media (max-width: 768px) {{
        .nav-links {{ display: none; position: absolute; top: 100%; left: 0; width: 100%; background: var(--bg); flex-direction: column; padding: 2rem; border-bottom: 1px solid var(--border); }}
        .nav-links.active {{ display: flex; }}
        .mobile-menu {{ display: block; }}
        .about-grid, .contact-grid, .detail-view {{ grid-template-columns: 1fr; gap: 2rem; }}
        .hero h1 {{ font-size: 2.5rem; }}
        .gallery-main {{ height: 300px; }}
    }}
    """

def gen_js_engine():
    # THE BRAIN: Handles Dark Mode, Toasts, Cart, Gallery, Lang, Popups
    clean_wa = wa_num.replace("+", "").strip()
    return f"""
    <script>
    // --- 1. TOAST SYSTEM ---
    function showToast(msg) {{
        const box = document.getElementById('toast-box');
        const el = document.createElement('div');
        el.className = 'toast';
        el.innerText = msg;
        box.appendChild(el);
        setTimeout(() => el.classList.add('show'), 10);
        setTimeout(() => {{
            el.classList.remove('show');
            setTimeout(() => el.remove(), 400);
        }}, 3000);
    }}

    // --- 2. DARK MODE ENGINE ---
    const body = document.body;
    const storedTheme = localStorage.getItem('titanTheme');
    if (storedTheme) body.classList.add(storedTheme);

    function toggleTheme() {{
        body.classList.toggle('dark-mode');
        const isDark = body.classList.contains('dark-mode');
        localStorage.setItem('titanTheme', isDark ? 'dark-mode' : '');
        showToast(isDark ? '🌙 Dark Mode Active' : '☀️ Light Mode Active');
    }}

    // --- 3. GALLERY ENGINE ---
    function switchImg(url, el) {{
        document.getElementById('main-img').src = url;
        document.querySelectorAll('.thumb').forEach(t => t.classList.remove('active'));
        if(el) el.classList.add('active');
    }}

    // --- 4. CSV PARSER & DATA LOGIC ---
    function parseCSV(str) {{
        const arr = [];
        let quote = false;
        for (let row = 0, col = 0, c = 0; c < str.length; c++) {{
            let cc = str[c], nc = str[c+1];
            arr[row] = arr[row] || [];
            arr[row][col] = arr[row][col] || '';
            if (cc == '"' && quote && nc == '"') {{ arr[row][col] += cc; ++c; continue; }}
            if (cc == '"') {{ quote = !quote; continue; }}
            if (cc == ',' && !quote) {{ ++col; continue; }}
            if (cc == '\\r' && nc == '\\n' && !quote) {{ ++row; col = 0; ++c; continue; }}
            if (cc == '\\n' && !quote) {{ ++row; col = 0; continue; }}
            if (cc == '\\r' && !quote) {{ ++row; col = 0; continue; }}
            arr[row][col] += cc;
        }}
        return arr;
    }}

    // --- 5. CART SYSTEM ---
    let cart = JSON.parse(localStorage.getItem('titanCart')) || [];
    function addToCart(name, price) {{
        cart.push({{name, price}});
        localStorage.setItem('titanCart', JSON.stringify(cart));
        updateCartUI();
        showToast('🛒 Added ' + name + ' to cart');
    }}
    function updateCartUI() {{
        document.getElementById('cart-count').innerText = cart.length;
        document.getElementById('cart-float').style.display = cart.length > 0 ? 'flex' : 'none';
    }}
    function toggleCart() {{
        const modal = document.getElementById('cart-modal');
        modal.style.display = modal.style.display === 'block' ? 'none' : 'block';
        if(modal.style.display === 'block') renderCartItems();
    }}
    function renderCartItems() {{
        const list = document.getElementById('cart-items');
        list.innerHTML = '';
        let total = 0;
        cart.forEach((item, i) => {{
            let p = parseFloat(item.price.replace(/[^0-9.]/g, '')) || 0;
            total += p;
            list.innerHTML += `<div style="display:flex; justify-content:space-between; margin-bottom:10px; border-bottom:1px solid var(--border); padding-bottom:5px;">
                <span>${{item.name}}</span>
                <span>${{item.price}} <b onclick="cart.splice(${{i}},1);localStorage.setItem('titanCart',JSON.stringify(cart));renderCartItems();updateCartUI()" style="color:red;cursor:pointer;margin-left:10px;">×</b></span>
            </div>`;
        }});
        document.getElementById('cart-total').innerText = total.toFixed(2);
    }}
    function checkout() {{
        let msg = "Order Request:%0A";
        let total = 0;
        cart.forEach(i => {{ msg += `- ${{i.name}} (${{i.price}})%0A`; total += parseFloat(i.price.replace(/[^0-9.]/g,'')) || 0; }});
        msg += `%0ATotal: ${{total.toFixed(2)}}%0A%0APayment: UPI {upi_id} | PayPal {paypal_link}`;
        window.open(`https://wa.me/{clean_wa}?text=${{msg}}`, '_blank');
    }}

    // --- 6. UTILS (Lang, Popup, Cookies) ---
    async function toggleLang() {{
        showToast('🌐 Language Switched (Demo)');
    }}
    
    // Cookie Banner
    setTimeout(() => {{
        if(!localStorage.getItem('cookieAccepted')) 
            document.getElementById('cookie-banner').style.transform = 'translateY(0)';
    }}, 2000);
    function acceptCookies() {{
        localStorage.setItem('cookieAccepted', 'true');
        document.getElementById('cookie-banner').style.transform = 'translateY(100%)';
    }}

    // Marketing Popup
    setTimeout(() => {{
        if(!localStorage.getItem('popupShown') && {str(popup_enabled).lower()}) {{
            document.getElementById('lead-popup').style.display = 'block';
            localStorage.setItem('popupShown', 'true');
        }}
    }}, {popup_delay * 1000});

    // Mobile Menu
    function toggleMenu() {{ document.querySelector('.nav-links').classList.toggle('active'); }}

    window.addEventListener('load', updateCartUI);
    window.addEventListener('scroll', () => {{
        document.querySelectorAll('.reveal').forEach(r => {{
            if(r.getBoundingClientRect().top < window.innerHeight - 80) r.classList.add('active');
        }});
    }});
    </script>
    """

def gen_csv_parser_script():
    # Only used inside product/blog pages if needed, but gen_js_engine covers most
    return "" 

def build_page(title, content):
    # META SEO INJECTION
    meta = f"""<meta name="description" content="{seo_d}"><meta property="og:title" content="{title} | {biz_name}"><meta property="og:description" content="{seo_d}"><meta property="og:image" content="{logo_url}">"""
    
    # SMART NAVIGATION CONSTRUCTION
    nav_links = f'<a href="index.html">Home</a>'
    if show_features: nav_links += '<a href="index.html#features">Features</a>'
    if show_pricing: nav_links += '<a href="index.html#pricing">Pricing</a>'
    if show_inventory: nav_links += '<a href="index.html#store">Store</a>'
    if show_blog: nav_links += '<a href="blog.html">Blog</a>'
    if show_booking: nav_links += '<a href="booking.html">Book</a>'
    nav_links += '<a href="contact.html">Contact</a>'
    
    # TOP BAR LOGIC
    top_bar = f'<div id="top-bar"><a href="{top_bar_link}">{top_bar_text}</a></div>' if top_bar_enabled else ''
    nav_top_offset = "40px" if top_bar_enabled else "0px"

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | {biz_name}</title>
        {meta}
        <link rel="manifest" href="manifest.json">
        <link rel="apple-touch-icon" href="{logo_url}">
        <link href="https://fonts.googleapis.com/css2?family={font_pair.replace(' / ', '+').replace(' ', '+')}:wght@400;700;800&display=swap" rel="stylesheet">
        <style>{get_theme_css()}</style>
    </head>
    <body>
        {top_bar}
        <nav class="glass" style="top:{nav_top_offset}">
            <div class="container nav-flex">
                <a href="index.html" style="font-weight:800; font-size:1.2rem;">{biz_name}</a>
                <div class="nav-links">
                    {nav_links}
                    <a href="#" onclick="toggleLang()">🌐</a>
                </div>
                <div class="mobile-menu" onclick="toggleMenu()">☰</div>
            </div>
        </nav>
        
        <!-- CONTENT INJECTION -->
        {content}
        
        <!-- FOOTER -->
        <footer><div class="container">
            <div class="about-grid">
                <div><h3>{biz_name}</h3><p style="opacity:0.8">{biz_addr}</p></div>
                <div style="text-align:right">
                    <a href="index.html">Home</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a>
                    <div style="margin-top:1rem; opacity:0.5">&copy; {datetime.datetime.now().year} {biz_name}</div>
                </div>
            </div>
        </div></footer>

        <!-- FLOATING WIDGETS -->
        <div id="toast-box"></div>
        {f'<div class="float-btn" id="mode-toggle" onclick="toggleTheme()">🌓</div>' if show_dark_toggle else ''}
        {f'<a href="https://wa.me/{wa_num.replace("+","")}" target="_blank" class="float-btn" id="wa-float"><svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.008-.57-.008-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></path></svg></a>' if show_wa_float else ''}
        <div class="float-btn" id="cart-float" onclick="toggleCart()" style="display:none">🛒 <span id="cart-count">0</span></div>
        
        <!-- MODALS & POPUPS -->
        <div id="cart-modal" class="glass" style="display:none; position:fixed; top:50%; left:50%; transform:translate(-50%,-50%); padding:2rem; z-index:2000; width:90%; max-width:400px;">
            <h3>Your Cart</h3><hr style="margin:10px 0; opacity:0.2">
            <div id="cart-items"></div>
            <div style="margin-top:20px; font-weight:bold;">Total: <span id="cart-total">0.00</span></div>
            <button class="btn btn-accent" style="width:100%; margin-top:10px;" onclick="checkout()">Checkout</button>
            <button class="btn" style="width:100%; margin-top:5px; background:transparent;" onclick="toggleCart()">Close</button>
        </div>

        {f'<div id="cookie-banner" class="glass" style="position:fixed; bottom:0; left:0; width:100%; padding:1rem; transform:translateY(100%); transition:0.5s; z-index:9000; display:flex; justify-content:space-between; align-items:center;"><div>{cookie_txt}</div><button class="btn btn-primary" onclick="acceptCookies()">Accept</button></div>' if show_cookie else ''}
        
        {f'<div id="lead-popup"><div style="position:absolute; top:10px; right:10px; cursor:pointer;" onclick="document.getElementById(\'lead-popup\').style.display=\'none\'">✕</div><h3>{popup_title}</h3><p>{popup_text}</p><a href="https://wa.me/{wa_num}?text=I want the offer" class="btn btn-accent" target="_blank">{popup_cta}</a></div>' if popup_enabled else ''}

        <!-- ENGINE -->
        {gen_js_engine()}
    </body>
    </html>
    """

# --- 6. PAGE GENERATORS (Using Updated Logic) ---

def gen_hero():
    bg_media = f"""
    <div class="carousel-slide active" style="background-image: url('{hero_img_1}')"></div>
    <div class="carousel-slide" style="background-image: url('{hero_img_2}')"></div>
    <div class="carousel-slide" style="background-image: url('{hero_img_3}')"></div>
    <script>
        let slides = document.querySelectorAll('.carousel-slide');
        let currentSlide = 0;
        setInterval(() => {{
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }}, 4000);
    </script>
    """
    if hero_video_id:
        bg_media = f"""<iframe src="https://www.youtube.com/embed/{hero_video_id}?autoplay=1&mute=1&loop=1&playlist={hero_video_id}&controls=0&showinfo=0&rel=0" style="position:absolute; top:50%; left:50%; width:100vw; height:100vh; transform:translate(-50%, -50%); pointer-events:none; object-fit:cover; z-index:0; min-width:177.77vh; min-height:56.25vw;" frameborder="0" allow="autoplay; encrypted-media"></iframe>"""

    return f"""
    <section class="hero">
        <div class="hero-overlay"></div>
        {bg_media}
        <div class="hero-content reveal">
            <h1>{hero_h}</h1>
            <p>{hero_sub}</p>
            <div style="display:flex; gap:1rem; flex-wrap:wrap; {'justify-content:center;' if hero_layout == 'Center' else ''}">
                <a href="#store" class="btn btn-accent">Explore</a>
                <a href="contact.html" class="btn glass">Contact</a>
            </div>
        </div>
    </section>
    """

def gen_features():
    cards = ""
    for line in feat_data_input.split('\n'):
        if "|" in line:
            p = line.split('|')
            cards += f"""<div class="card reveal"><div class="card-content"><div style="color:var(--s); margin-bottom:1rem;">{get_simple_icon(p[0])}</div><h3>{p[1]}</h3><div>{format_text(p[2])}</div></div></div>"""
    return f"""<section id="features"><div class="container"><div class="section-head reveal"><h2 style="text-align:center">{f_title}</h2></div><div class="grid-3">{cards}</div></div></section>"""

def gen_inventory_js_client(is_demo=False):
    demo_flag = "true" if is_demo else "false"
    return f"""
    <script>
    const isDemo = {demo_flag};
    async function loadStore() {{
        try {{
            const res = await fetch('{sheet_url}');
            const text = await res.text();
            const data = parseCSV(text);
            const grid = document.getElementById('store-grid');
            
            // Skip header (i=1)
            for(let i=1; i<data.length; i++) {{
                let row = data[i];
                if(!row || row.length < 2) continue;
                
                // MULTI-IMAGE PARSING: Split by pipe
                let images = row[3] ? row[3].split('|') : ['{custom_feat}'];
                let mainImg = images[0].trim();
                let title = row[0];
                let price = row[1];
                let desc = row[2];
                
                if(grid) {{
                    grid.innerHTML += `
                    <div class="card reveal">
                        <div class="prod-img-box">
                            <img src="${{mainImg}}" class="prod-img">
                        </div>
                        <div class="card-content">
                            <h3>${{title}}</h3>
                            <p style="color:var(--s); font-weight:bold; margin-bottom:0.5rem;">${{price}}</p>
                            <div style="display:flex; gap:0.5rem; justify-content:center;">
                                <a href="product.html?item=${{encodeURIComponent(title)}}" class="btn btn-primary" style="padding:0.5rem 1rem; font-size:0.8rem;">View</a>
                                <button onclick="addToCart('${{title}}', '${{price}}')" class="btn btn-accent" style="padding:0.5rem 1rem; font-size:0.8rem;">Add</button>
                            </div>
                        </div>
                    </div>`;
                }}
            }}
        }} catch(e) {{ console.log(e); }}
    }}
    if(document.getElementById('store-grid')) loadStore();
    </script>
    """

def gen_product_page_content(is_demo=False):
    return f"""
    <div class="container detail-container" id="detail-app">Loading...</div>
    <script>
    async function initProduct() {{
        const params = new URLSearchParams(window.location.search);
        let target = params.get('item');
        if({str(is_demo).lower()} && !target) target = "Demo Product";
        
        const res = await fetch('{sheet_url}');
        const text = await res.text();
        const data = parseCSV(text);
        
        for(let i=1; i<data.length; i++) {{
            let row = data[i];
            if(row[0] === target || (is_demo && i===1)) {{
                // Gallery Logic
                let images = row[3] ? row[3].split('|') : ['{custom_feat}'];
                let thumbsHtml = '';
                images.forEach((img, idx) => {{
                    thumbsHtml += `<img src="${{img.trim()}}" class="thumb ${{idx===0?'active':''}}" onclick="switchImg('${{img.trim()}}', this)">`;
                }});
                
                document.getElementById('detail-app').innerHTML = `
                    <div>
                        <img src="${{images[0].trim()}}" class="gallery-main" id="main-img">
                        <div class="gallery-thumbs">${{thumbsHtml}}</div>
                    </div>
                    <div>
                        <h1 style="font-size:3rem; margin-bottom:0.5rem;">${{row[0]}}</h1>
                        <h2 style="color:var(--s); margin-bottom:1.5rem;">${{row[1]}}</h2>
                        <p style="opacity:0.8; margin-bottom:2rem; font-size:1.1rem;">${{row[2]}}</p>
                        <button onclick="addToCart('${{row[0]}}', '${{row[1]}}')" class="btn btn-primary" style="width:100%; font-size:1.2rem;">Add to Cart</button>
                    </div>
                `;
                break;
            }}
        }}
    }}
    initProduct();
    </script>
    """

def gen_blog_index():
    return f"""
    <section class="hero" style="min-height:40vh; background-image:url('{hero_img_1}'); background-size:cover;">
        <div class="hero-overlay"></div>
        <div class="hero-content"><h1>{blog_hero_title}</h1><p>{blog_hero_sub}</p></div>
    </section>
    <section><div class="container"><div id="blog-grid" class="grid-3">Loading...</div></div></section>
    <script>
    async function loadBlog() {{
        const res = await fetch('{blog_sheet_url}');
        const txt = await res.text();
        const data = parseCSV(txt);
        const grid = document.getElementById('blog-grid');
        grid.innerHTML = '';
        for(let i=1; i<data.length; i++) {{
            let r = data[i];
            if(r.length > 4) {{
                grid.innerHTML += `
                <div class="card reveal">
                    <img src="${{r[5]}}" style="width:100%; height:200px; object-fit:cover;">
                    <div class="card-content">
                        <span style="background:var(--s); color:white; padding:2px 8px; border-radius:4px; font-size:0.8rem;">${{r[3]}}</span>
                        <h3 style="margin-top:0.5rem">${{r[1]}}</h3>
                        <p>${{r[4]}}</p>
                        <a href="post.html?id=${{r[0]}}" class="btn btn-primary" style="margin-top:1rem; width:100%">Read</a>
                    </div>
                </div>`;
            }}
        }}
    }}
    loadBlog();
    </script>
    """

def gen_blog_post():
    return f"""
    <div id="post-container" style="padding-top:100px;">Loading...</div>
    <script>
    async function loadPost() {{
        const params = new URLSearchParams(window.location.search);
        const slug = params.get('id');
        const res = await fetch('{blog_sheet_url}');
        const txt = await res.text();
        const data = parseCSV(txt);
        for(let i=1; i<data.length; i++) {{
            if(data[i][0] === slug) {{
                let r = data[i];
                // Simple markdown parser replacement for demo
                let content = r[6].replace(/\\n/g, '<br>'); 
                document.getElementById('post-container').innerHTML = `
                    <div style="background:var(--p); padding:6rem 1rem; color:white; text-align:center;">
                        <div class="container"><h1>${{r[1]}}</h1><p>${{r[2]}}</p></div>
                    </div>
                    <div class="container" style="max-width:800px; padding:3rem 1rem;">
                        <img src="${{r[5]}}" style="width:100%; border-radius:12px; margin-bottom:2rem;">
                        <div style="line-height:1.8; font-size:1.1rem;">${{content}}</div>
                    </div>
                `;
            }}
        }}
    }}
    loadPost();
    </script>
    """

# --- 7. HOME ASSEMBLY ---
home_body = ""
if show_hero: home_body += gen_hero()
if show_stats: home_body += gen_stats()
if show_features: home_body += gen_features()
if show_pricing: home_body += gen_pricing_table()
if show_inventory: 
    home_body += f'<section id="store" style="background:rgba(0,0,0,0.02)"><div class="container"><div class="section-head reveal"><h2 style="text-align:center">Collection</h2></div><div id="store-grid" class="grid-3"></div></div></section>{gen_inventory_js_client()}'
if show_gallery: home_body += gen_about_section()
if show_testimonials: 
    t_cards = "".join([f'<div class="card reveal"><div class="card-content"><p>"{x.split("|")[1]}"</p><b>- {x.split("|")[0]}</b></div></div>' for x in testi_data.split('\n') if "|" in x])
    home_body += f'<section style="background:#f8fafc"><div class="container"><h2 style="text-align:center; margin-bottom:2rem;">Voices</h2><div class="grid-3">{t_cards}</div></div></section>'
if show_faq: home_body += gen_faq_section()
if show_cta: home_body += f'<section style="background:var(--s); color:white; text-align:center;"><div class="container reveal"><h2>Ready?</h2><p>Start today.</p><a href="contact.html" class="btn glass">Get Started</a></div></section>'

# --- 8. PREVIEW & EXPORT ---
st.divider()
c1, c2 = st.columns([3, 1])

with c1:
    prev_mode = st.radio("Live Preview", ["Home", "Product Detail", "Blog Index", "Blog Post", "Booking", "Legal"], horizontal=True)
    if prev_mode == "Home": st.components.v1.html(build_page("Home", home_body), height=700, scrolling=True)
    elif prev_mode == "Product Detail": st.components.v1.html(build_page("Product", gen_product_page_content(True)), height=700, scrolling=True)
    elif prev_mode == "Blog Index": st.components.v1.html(build_page("Blog", gen_blog_index()), height=700, scrolling=True)
    elif prev_mode == "Blog Post": st.components.v1.html(build_page("Post", gen_blog_post()), height=700, scrolling=True)
    elif prev_mode == "Booking": st.components.v1.html(build_page("Book", gen_booking_content()), height=700, scrolling=True)
    elif prev_mode == "Legal": st.components.v1.html(build_page("Privacy", f"<div class='container' style='padding-top:100px'>{format_text(priv_txt)}</div>"), height=700, scrolling=True)

with c2:
    st.markdown("### 🚀 Launch System")
    if st.button("DOWNLOAD TITAN ZIP", type="primary"):
        z = io.BytesIO()
        with zipfile.ZipFile(z, "a", zipfile.ZIP_DEFLATED, False) as zf:
            zf.writestr("index.html", build_page("Home", home_body))
            zf.writestr("product.html", build_page("Product", gen_product_page_content(False)))
            zf.writestr("about.html", build_page("About", f"{gen_inner_header('About')}<div class='container' style='padding:3rem 1rem'>{format_text(about_long)}</div>"))
            zf.writestr("contact.html", build_page("Contact", f"{gen_inner_header('Contact')}<div class='container'><div class='about-grid'><div><h3>Contact Us</h3><p>{biz_addr}</p><p>{biz_email}</p></div><div>{map_iframe}</div></div></div>"))
            zf.writestr("privacy.html", build_page("Privacy", f"<div class='container' style='padding-top:100px'><h1>Privacy</h1>{format_text(priv_txt)}</div>"))
            zf.writestr("terms.html", build_page("Terms", f"<div class='container' style='padding-top:100px'><h1>Terms</h1>{format_text(term_txt)}</div>"))
            zf.writestr("booking.html", build_page("Book", gen_booking_content()))
            if show_blog: 
                zf.writestr("blog.html", build_page("Blog", gen_blog_index()))
                zf.writestr("post.html", build_page("Post", gen_blog_post()))
            
            zf.writestr("manifest.json", gen_pwa_manifest())
            zf.writestr("service-worker.js", gen_sw())
            zf.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}/sitemap.xml")
            
        st.download_button("📥 Click to Save", z.getvalue(), "titan_eternity.zip", "application/zip")
