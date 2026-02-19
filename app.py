import streamlit as st
import zipfile
import io
import json
import datetime
import re
import requests

# --- 0. STATE MANAGEMENT (AI INTEGRATION) ---
def init_state(key, default_val):
    if key not in st.session_state:
        st.session_state[key] = default_val

init_state('hero_h', "Stop Paying Rent for Your Website.")
init_state('hero_sub', "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees. Pay once. Own it forever.")
init_state('about_h', "Control Your Empire from a Spreadsheet")
init_state('about_short', "No WordPress dashboard. No plugins to update. Just open your private Google Sheet, change a text, and watch your site update globally in seconds.")
init_state('feat_data', "bolt | The Performance Pillar | **0.1s High-Velocity Loading**. While traditional sites take 3–5s, Titan loads instantly.\nwallet | The Economic Pillar | **$0 Monthly Fees**. We eliminated hosting subscriptions.\ntable | The Functional Pillar | **Google Sheets CMS**. Update prices and photos directly from a simple spreadsheet.\nshield | The Authority Pillar | **Unhackable Security**. Zero-DB Architecture removes the hacker's primary entry point.\nlayers | The Reliability Pillar | **Global Edge Deployment**. Distributed across 100+ servers worldwide.\nstar | The Conversion Pillar | **One-Tap WhatsApp**. Direct-to-Chat technology.")

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v40.0 | Ultra Modern UI", 
    layout="wide", 
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# --- 2. STREAMLIT UI SYSTEM ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #3b82f6; }
    .stApp { background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    [data-testid="stSidebar"] h1 { 
        background: linear-gradient(90deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900 !important; font-size: 1.8rem !important;
    }
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #334155 !important; border: 1px solid #475569 !important; border-radius: 8px !important; color: white !important;
    }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5rem;
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white; font-weight: 800; border: none; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4); 
        text-transform: uppercase; letter-spacing: 1px; transition: transform 0.2s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(59, 130, 246, 0.6); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: THE CONTROL CENTER ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v40.0 | Glass-Morphism Core")
    st.divider()
    
    # --- FEATURE 1: TITAN AI GENERATOR ---
    with st.expander("🤖 Titan AI Generator", expanded=True):
        raw_key = st.text_input("Groq API Key", type="password")
        groq_key = raw_key.strip() if raw_key else ""
        biz_desc = st.text_input("Business Description")
        
        if st.button("✨ Generate Copy"):
            if not groq_key or not biz_desc:
                st.error("Key & Description required.")
            else:
                try:
                    with st.spinner("Designing Content..."):
                        url = "https://api.groq.com/openai/v1/chat/completions"
                        headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                        prompt = f"Act as a web copywriter. Return JSON for '{biz_desc}': hero_h, hero_sub, about_h, about_short, feat_data (icon|Title|Desc format)."
                        data = {"messages": [{"role": "user", "content": prompt}], "model": "llama-3.1-8b-instant", "response_format": {"type": "json_object"}}
                        resp = requests.post(url, headers=headers, json=data)
                        if resp.status_code == 200:
                            res = resp.json()['choices'][0]['message']['content']
                            parsed = json.loads(res)
                            
                            def clean_str(val):
                                if val is None: return ""
                                if isinstance(val, list): return " ".join([str(x) for x in val])
                                return str(val)

                            if 'hero_h' in parsed: st.session_state.hero_h = clean_str(parsed['hero_h'])
                            if 'hero_sub' in parsed: st.session_state.hero_sub = clean_str(parsed['hero_sub'])
                            if 'about_h' in parsed: st.session_state.about_h = clean_str(parsed['about_h'])
                            if 'about_short' in parsed: st.session_state.about_short = clean_str(parsed['about_short'])
                            if 'feat_data' in parsed:
                                if isinstance(parsed['feat_data'], list): st.session_state.feat_data = "\n".join(map(str, parsed['feat_data']))
                                else: st.session_state.feat_data = clean_str(parsed['feat_data'])
                            st.success("Generated!")
                            st.rerun()
                except Exception as e: st.error(f"Error: {e}")

    # 3.1 VISUAL DNA
    with st.expander("🎨 Visual DNA", expanded=False):
        theme_mode = st.selectbox("Base Theme", ["Midnight Glass (Dark)", "Modern Glass (Light)", "Neo-Brutalism", "Luxury Gold"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#3B82F6") 
        s_color = c2.color_picker("Accent (CTA)", "#F43F5E")  
        
        st.markdown("**Layout**")
        hero_layout = st.selectbox("Hero Alignment", ["Center", "Left"])
        # Font logic is now auto-handled by the Ultra Modern Engine (Outfit + Plus Jakarta Sans)

    # 3.2 MODULE MANAGER
    with st.expander("🧩 Section Manager", expanded=False):
        show_hero = st.checkbox("Hero Carousel", value=True)
        show_stats = st.checkbox("Trust Stats", value=True)
        show_features = st.checkbox("Feature Grid", value=True)
        show_pricing = st.checkbox("Pricing Table", value=True)
        show_inventory = st.checkbox("Store/Inventory", value=True)
        show_blog = st.checkbox("Blog Engine", value=True)
        show_gallery = st.checkbox("About Section", value=True)
        show_testimonials = st.checkbox("Testimonials", value=True)
        show_faq = st.checkbox("F.A.Q.", value=True)
        show_booking = st.checkbox("Booking Engine", value=True)
        show_cta = st.checkbox("Final CTA", value=True)

    # 3.3 TECHNICAL
    with st.expander("⚙️ SEO & Analytics", expanded=False):
        seo_area = st.text_input("Service Area", "Global")
        seo_kw = st.text_area("SEO Keywords", "web design, static site")
        gsc_tag = st.text_input("Google ID")
        og_image = st.text_input("Social Share Image")

# --- 4. MAIN WORKSPACE ---
st.title("💎 Titan v40.0 Site Builder")

tabs = st.tabs(["1. Identity & PWA", "2. Content", "3. Pricing", "4. Store", "5. Booking", "6. Blog", "7. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent.com")
        biz_tagline = st.text_input("Tagline", "Stop Renting. Start Owning.")
        biz_phone = st.text_input("Phone", "966572562151")
        biz_email = st.text_input("Email", "hello@kaydiemscriptlab.com")
    with c2:
        prod_url = st.text_input("Website URL", "https://www.stopwebrent.com")
        biz_addr = st.text_area("Address", "Kaydiem Script Lab\nKolkata, India", height=100)
        map_iframe = st.text_area("Google Map Embed", placeholder='<iframe src="..."></iframe>', height=100)
        seo_d = st.text_area("Meta Description", "Stop paying monthly fees.", height=100)
        logo_url = st.text_input("Logo URL (PNG/SVG)")

    st.subheader("📱 PWA & Language")
    pwa_short = st.text_input("App Short Name", biz_name[:12])
    pwa_icon = st.text_input("App Icon (512px)", logo_url)
    lang_sheet = st.text_input("Translation CSV URL", help="Col 1: ElementID, Col 2: Text")
        
    st.subheader("Social Links")
    sc1, sc2, sc3 = st.columns(3)
    fb_link = sc1.text_input("Facebook URL")
    ig_link = sc2.text_input("Instagram URL")
    x_link = sc3.text_input("X (Twitter) URL")
    sc4, sc5, sc6 = st.columns(3)
    li_link = sc4.text_input("LinkedIn URL")
    yt_link = sc5.text_input("YouTube URL")
    wa_num = sc6.text_input("WhatsApp Number (No +)", "966572562151")

with tabs[1]:
    st.subheader("Hero Section")
    hero_h = st.text_input("Hero Headline", key="hero_h")
    hero_sub = st.text_input("Hero Subtext", key="hero_sub")
    
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Slide 1", "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1600")
    hero_img_2 = hc2.text_input("Slide 2", "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=1600")
    hero_img_3 = hc3.text_input("Slide 3", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1600")
    hero_video_id = st.text_input("YouTube Video ID (Background)", placeholder="e.g. dQw4w9WgXcQ")
    
    st.divider()
    st.subheader("Stats & Features")
    col_s1, col_s2, col_s3 = st.columns(3)
    stat_1 = col_s1.text_input("Stat 1", "0.1s")
    label_1 = col_s1.text_input("Label 1", "Speed")
    stat_2 = col_s2.text_input("Stat 2", "$0")
    label_2 = col_s2.text_input("Label 2", "Fees")
    stat_3 = col_s3.text_input("Stat 3", "100%")
    label_3 = col_s3.text_input("Label 3", "Ownership")

    f_title = st.text_input("Features Title", "Value Pillars")
    feat_data_input = st.text_area("Features List", key="feat_data", height=150)
    
    st.subheader("About")
    about_h_in = st.text_input("About Title", key="about_h")
    about_img = st.text_input("About Image", "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=1600")
    about_short_in = st.text_area("Short Summary", key="about_short", height=100)
    about_long = st.text_area("Full Content", "The Digital Landlord Trap...", height=200)

with tabs[2]:
    st.subheader("💰 Pricing")
    col_p1, col_p2, col_p3 = st.columns(3)
    titan_price = col_p1.text_input("Setup Price", "$199")
    titan_mo = col_p1.text_input("Monthly Fee", "$0")
    wix_name = col_p2.text_input("Competitor", "Wix")
    wix_mo = col_p2.text_input("Comp. Monthly", "$29/mo")
    save_val = col_p3.text_input("Savings", "$1,466")

with tabs[3]:
    st.subheader("🛒 Store")
    st.info("Multi-Image Support: Separate URLs with `|` (e.g. `img1.jpg|img2.jpg`) for gallery.")
    sheet_url = st.text_input("Store CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Default Product Img", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=1600")
    col_pay1, col_pay2 = st.columns(2)
    paypal_link = col_pay1.text_input("PayPal Link", "https://paypal.me/yourid")
    upi_id = col_pay2.text_input("UPI ID", "name@upi")

with tabs[4]:
    st.subheader("📅 Booking")
    st.info("Paste your Calendly inline embed code here.")
    booking_embed = st.text_area("Embed Code", height=150, value='<!-- Calendly -->')
    booking_title = st.text_input("Booking Title", "Book an Appointment")
    booking_desc = st.text_input("Booking Subtext", "Select a time slot.")

with tabs[5]:
    st.subheader("📰 Blog")
    blog_sheet_url = st.text_input("Blog CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    blog_hero_title = st.text_input("Blog Title", "Latest Insights")
    blog_hero_sub = st.text_input("Blog Subtext", "Thoughts on tech.")

with tabs[6]:
    st.subheader("Legal")
    testi_data = st.text_area("Testimonials", "Rajesh Gupta | Titan stopped the bleeding.", height=100)
    faq_data = st.text_area("FAQ", "Do I pay $0? ? Yes.", height=100)
    priv_txt = st.text_area("Privacy", "We collect minimum data.", height=100)
    term_txt = st.text_area("Terms", "You own the code.", height=100)

# ==========================================
# 4. COMPILER ENGINE (ULTRA MODERN EDITION)
# ==========================================

def format_text(text):
    if not text: return ""
    processed = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    return processed.replace('\n', '<br>')

def gen_schema():
    schema = { "@context": "https://schema.org", "@type": "LocalBusiness", "name": biz_name, "image": logo_url or hero_img_1, "telephone": biz_phone, "url": prod_url, "description": seo_d }
    return f'<script type="application/ld+json">{json.dumps(schema)}</script>'

def gen_pwa_manifest():
    return json.dumps({ "name": biz_name, "short_name": pwa_short, "start_url": "./index.html", "display": "standalone", "background_color": "#ffffff", "theme_color": p_color, "description": seo_d, "icons": [{"src": pwa_icon, "sizes": "512x512", "type": "image/png"}] })

def gen_sw():
    return """self.addEventListener('install', (e) => { e.waitUntil(caches.open('titan-store').then((cache) => cache.addAll(['./index.html']))); }); self.addEventListener('fetch', (e) => { e.respondWith(caches.match(e.request).then((response) => response || fetch(e.request))); });"""

def get_theme_css():
    # --- ULTRA MODERN PALETTE & VARS ---
    bg_color, text_color, card_bg = "#F8FAFC", "#0F172A", "rgba(255, 255, 255, 0.7)"
    nav_bg, border_color = "rgba(255, 255, 255, 0.8)", "rgba(255, 255, 255, 0.5)"
    
    if "Midnight" in theme_mode: 
        bg_color, text_color, card_bg = "#0B0F19", "#F1F5F9", "rgba(30, 41, 59, 0.6)"
        nav_bg, border_color = "rgba(15, 23, 42, 0.8)", "rgba(255, 255, 255, 0.1)"
    
    hero_align = "justify-content: center; text-align: center;"
    if hero_layout == "Left": hero_align = "justify-content: flex-start; text-align: left;"

    return f"""
    :root {{
        --p: {p_color}; --s: {s_color};
        --bg: {bg_color}; --txt: {text_color};
        --card-bg: {card_bg}; --nav-bg: {nav_bg};
        --border: {border_color};
        --glass: blur(16px) saturate(180%);
        --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        --font-h: 'Outfit', sans-serif;
        --font-b: 'Plus Jakarta Sans', sans-serif;
    }}
    
    * {{ box-sizing: border-box; outline: none; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ 
        background-color: var(--bg); color: var(--txt); 
        font-family: var(--font-b); margin: 0; line-height: 1.6; 
        overflow-x: hidden; -webkit-font-smoothing: antialiased;
    }}
    
    /* TYPOGRAPHY */
    h1, h2, h3, h4 {{ font-family: var(--font-h); color: var(--txt); line-height: 1.1; margin-bottom: 1rem; letter-spacing: -0.02em; }}
    h1 {{ font-size: clamp(3rem, 6vw, 5rem); font-weight: 800; }}
    h2 {{ font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 700; }}
    
    .gradient-text {{
        background: linear-gradient(135deg, var(--p) 0%, var(--s) 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    /* COMPONENTS */
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
    
    .btn {{
        display: inline-flex; align-items: center; justify-content: center;
        padding: 1rem 2rem; border-radius: 12px; font-weight: 600;
        text-decoration: none; transition: all 0.3s ease; cursor: pointer;
        border: none; font-size: 1rem; gap: 0.5rem;
    }}
    .btn-primary {{ 
        background: linear-gradient(135deg, var(--p), var(--s)); 
        color: white !important; box-shadow: 0 10px 20px -5px var(--p);
    }}
    .btn-primary:hover {{ transform: translateY(-3px); box-shadow: 0 15px 30px -5px var(--p); filter: brightness(1.1); }}
    
    .btn-outline {{ 
        background: transparent; border: 1px solid var(--border); color: var(--txt) !important; 
    }}
    .btn-outline:hover {{ border-color: var(--p); color: var(--p) !important; background: rgba(255,255,255,0.05); }}

    /* NAVIGATION - GLASS */
    nav {{ 
        position: fixed; top: 0; width: 100%; z-index: 1000;
        background: var(--nav-bg); backdrop-filter: var(--glass);
        -webkit-backdrop-filter: var(--glass);
        border-bottom: 1px solid var(--border); padding: 1rem 0;
        transition: top 0.3s;
    }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; gap: 2rem; align-items: center; }}
    .nav-links a {{ 
        text-decoration: none; font-weight: 500; color: var(--txt); 
        opacity: 0.8; transition: 0.2s; font-size: 0.95rem;
    }}
    .nav-links a:hover {{ opacity: 1; color: var(--p); }}
    
    /* HERO */
    .hero {{ 
        position: relative; min-height: 100vh; display: flex; align-items: center; 
        {hero_align} overflow: hidden; padding-top: 80px;
    }}
    .hero-bg {{ 
        position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; 
    }}
    .hero-overlay {{
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(to bottom, rgba(0,0,0,0.3), var(--bg)); z-index: 0;
    }}
    .hero-content {{ z-index: 2; position: relative; max-width: 900px; animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1); }}
    .hero h1 {{ color: white !important; text-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
    .hero p {{ color: rgba(255,255,255,0.9); font-size: 1.25rem; margin-bottom: 2.5rem; max-width: 600px; { "margin-left: auto; margin-right: auto;" if hero_layout == "Center" else "" } }}

    /* CARDS - GLASSMORPHISM 2.0 */
    .card {{
        background: var(--card-bg); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border); border-radius: 24px; padding: 2rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex; flex-direction: column; height: 100%; position: relative; overflow: hidden;
    }}
    .card:hover {{ 
        transform: translateY(-8px); 
        border-color: var(--p); 
        box-shadow: var(--shadow-lg); 
    }}
    
    /* PRODUCT CARDS - MINIMALIST */
    .prod-card {{
        background: var(--card-bg); border: 1px solid var(--border);
        border-radius: 20px; overflow: hidden; position: relative;
        transition: 0.3s;
    }}
    .prod-card:hover {{ transform: translateY(-5px); box-shadow: var(--shadow-lg); }}
    .prod-img-wrap {{ position: relative; padding-top: 100%; overflow: hidden; }}
    .prod-img {{ 
        position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
        object-fit: cover; transition: transform 0.6s; 
    }}
    .prod-card:hover .prod-img {{ transform: scale(1.08); }}
    .prod-info {{ padding: 1.5rem; text-align: left; }}
    .prod-price {{ font-size: 1.2rem; font-weight: 800; color: var(--p); }}
    
    /* DUAL ACTION BUTTONS */
    .prod-actions {{
        display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-top: 1rem;
        opacity: 0; transform: translateY(10px); transition: 0.3s;
    }}
    .prod-card:hover .prod-actions {{ opacity: 1; transform: translateY(0); }}
    .btn-sm {{ padding: 0.6rem 1rem; font-size: 0.85rem; border-radius: 8px; text-align: center; }}

    /* SECTIONS */
    section {{ padding: clamp(4rem, 8vw, 6rem) 0; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; }}
    
    /* ANIMATIONS */
    .reveal {{ opacity: 0; transform: translateY(30px); transition: all 0.8s ease-out; }}
    .reveal.active {{ opacity: 1; transform: translateY(0); }}
    
    /* MODALS & CART */
    .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); backdrop-filter: blur(8px); }}
    .modal-content {{ 
        background: var(--bg); border: 1px solid var(--border);
        margin: 10vh auto; padding: 2.5rem; width: 90%; max-width: 450px; 
        border-radius: 24px; position: relative; animation: slideUp 0.3s;
    }}
    
    /* FOOTER */
    footer {{ background: #0f172a; color: white; padding: 5rem 0; border-top: 1px solid rgba(255,255,255,0.1); }}
    
    @keyframes fadeInUp {{ from {{ opacity:0; transform:translateY(40px); }} to {{ opacity:1; transform:translateY(0); }} }}
    @keyframes slideUp {{ from {{ opacity:0; transform:translateY(20px); }} to {{ opacity:1; transform:translateY(0); }} }}

    /* RESPONSIVE */
    @media (max-width: 768px) {{
        .nav-links {{ 
            position: fixed; top: 70px; left: -100%; width: 100%; height: calc(100vh - 70px); 
            background: var(--bg); flex-direction: column; padding: 2rem; transition: 0.3s; 
            align-items: flex-start; border-top: 1px solid var(--border);
        }}
        .nav-links.active {{ left: 0; }}
        .mobile-menu {{ display: block; font-size: 1.5rem; cursor: pointer; }}
        h1 {{ font-size: 2.8rem; }}
        .prod-actions {{ opacity: 1; transform: translateY(0); }}
    }}
    """

def gen_nav():
    logo = f'<img src="{logo_url}" height="32" alt="{biz_name}">' if logo_url else f'<span style="font-weight:800;font-size:1.4rem;letter-spacing:-0.03em;" class="gradient-text">{biz_name}</span>'
    blog_link = '<a href="blog.html" onclick="toggleMenu()">Blog</a>' if show_blog else ''
    book_link = '<a href="booking.html" onclick="toggleMenu()">Book Now</a>' if show_booking else ''
    
    lang_btn = ""
    if lang_sheet:
        lang_btn = f"""
        <button onclick="openModal('langModal')" class="btn-outline" style="padding: 0.5rem 1rem; border-radius: 50px; display: flex; align-items: center; gap: 5px;">
            <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"></path></svg>
            <span>Lang</span>
        </button>
        """

    return f"""
    <nav>
        <div class="container nav-flex">
            <a href="index.html" style="text-decoration:none; display:flex; align-items:center;">{logo}</a>
            <div class="mobile-menu" onclick="document.querySelector('.nav-links').classList.toggle('active')">
                <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
            </div>
            <div class="nav-links">
                <a href="index.html" onclick="toggleMenu()">Home</a>
                {'<a href="index.html#features" onclick="toggleMenu()">Features</a>' if show_features else ''}
                {'<a href="index.html#pricing" onclick="toggleMenu()">Pricing</a>' if show_pricing else ''}
                {'<a href="index.html#inventory" onclick="toggleMenu()">Store</a>' if show_inventory else ''}
                {blog_link}
                {book_link}
                {lang_btn}
                <a href="contact.html" onclick="toggleMenu()">Contact</a>
                <a href="tel:{biz_phone}" class="btn btn-primary" style="padding:0.6rem 1.4rem; border-radius:50px;">Call Now</a>
            </div>
        </div>
    </nav>
    
    <!-- Language Modal -->
    <div id="langModal" class="modal">
        <div class="modal-content">
            <span class="close-modal" onclick="closeModal('langModal')" style="position:absolute; right:20px; top:15px; font-size:1.5rem; cursor:pointer;">&times;</span>
            <h3 class="gradient-text">Select Language</h3>
            <div style="display:grid; gap:10px; margin-top:20px;">
                <button onclick="toggleLang()" class="btn btn-outline" style="width:100%; justify-content:flex-start;">🇺🇸 Switch Language</button>
            </div>
        </div>
    </div>
    <script>
        function toggleMenu() {{ document.querySelector('.nav-links').classList.remove('active'); }}
        function openModal(id) {{ document.getElementById(id).style.display = 'block'; }}
        function closeModal(id) {{ document.getElementById(id).style.display = 'none'; }}
        window.onclick = function(event) {{ if (event.target.classList.contains('modal')) {{ event.target.style.display = "none"; }} }}
    </script>
    """

def gen_hero():
    # Parallax Background Logic
    bg_html = f"""
    <div class="hero-bg">
        <div class="carousel-slide active" style="background-image: url('{hero_img_1}'); background-size: cover; background-position: center; position:absolute; width:100%; height:100%; transition: opacity 1.5s;"></div>
        <div class="carousel-slide" style="background-image: url('{hero_img_2}'); background-size: cover; background-position: center; position:absolute; width:100%; height:100%; opacity:0; transition: opacity 1.5s;"></div>
        <div class="carousel-slide" style="background-image: url('{hero_img_3}'); background-size: cover; background-position: center; position:absolute; width:100%; height:100%; opacity:0; transition: opacity 1.5s;"></div>
    </div>
    <script>
        let slides = document.querySelectorAll('.carousel-slide');
        let current = 0;
        setInterval(() => {{
            slides[current].style.opacity = 0;
            current = (current + 1) % slides.length;
            slides[current].style.opacity = 1;
        }}, 5000);
    </script>
    """
    if hero_video_id:
        bg_html = f"""<div class="hero-bg"><iframe src="https://www.youtube.com/embed/{hero_video_id}?autoplay=1&mute=1&loop=1&playlist={hero_video_id}&controls=0&showinfo=0&rel=0" style="width:100vw; height:100vh; object-fit:cover; pointer-events:none;" frameborder="0"></iframe></div>"""

    return f"""
    <section class="hero">
        <div class="hero-overlay"></div>
        {bg_html}
        <div class="container hero-content">
            <h1>{hero_h}</h1>
            <p>{hero_sub}</p>
            <div style="display:flex; gap:1rem; flex-wrap:wrap; { 'justify-content:center;' if hero_layout == 'Center' else '' }">
                <a href="#inventory" class="btn btn-primary" style="padding: 1.2rem 2.5rem; font-size:1.1rem;">Explore Now</a>
                <a href="contact.html" class="btn btn-outline" style="color:white !important; border-color:rgba(255,255,255,0.4);">Contact Us</a>
            </div>
        </div>
    </section>
    """

def get_simple_icon(name):
    # Standardized Icon Set
    d = "M12 2L2 7l10 5 10-5-10-5zm0 9l2.5-1.25L12 8.5l-2.5 1.25L12 11zm0 2.5l-5-2.5-5 2.5L12 22l10-8.5-5-2.5-5 2.5z"
    if "bolt" in name: d="M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"
    if "wallet" in name: d="M21 18v1c0 1.1-.9 2-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h14a2 2 0 012 2v1h-9a2 2 0 00-2 2v8a2 2 0 002 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"
    if "star" in name: d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
    return f'<svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="{d}"/></svg>'

def gen_features():
    cards = ""
    lines = [x for x in feat_data_input.split('\n') if x.strip()]
    for line in lines:
        parts = line.split('|')
        if len(parts) >= 3:
            icon_svg = f'<div style="color:var(--p); margin-bottom:1.5rem; background:rgba(255,255,255,0.05); width:60px; height:60px; display:flex; align-items:center; justify-content:center; border-radius:16px;">{get_simple_icon(parts[0])}</div>'
            cards += f"""<div class="card reveal">{icon_svg}<h3>{parts[1].strip()}</h3><div style="opacity:0.8;">{format_text(parts[2].strip())}</div></div>"""
    return f"""<section id="features"><div class="container"><div class="section-head reveal"><h2 class="gradient-text">{f_title}</h2></div><div class="grid-3">{cards}</div></div></section>"""

def gen_inventory():
    if not show_inventory: return ""
    return f"""
    <section id="inventory" style="background:var(--bg);">
        <div class="container">
            <div class="section-head reveal"><h2 class="gradient-text">Featured Collection</h2></div>
            <div id="inv-grid" class="grid-3"><div>Loading Products...</div></div>
        </div>
    </section>
    {gen_csv_parser()}
    <script>
    async function loadInv() {{
        try {{
            const res = await fetch('{sheet_url}'); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/);
            const box = document.getElementById('inv-grid'); if(!box) return; box.innerHTML = '';
            for(let i=1; i<lines.length; i++) {{
                const row = parseCSVLine(lines[i]);
                if(row.length < 2) continue;
                
                // MULTI IMAGE LOGIC (Clean split)
                let rawImgs = row[3] || '{custom_feat}';
                let mainImg = rawImgs.split('|')[0];
                
                const safeName = row[0].replace(/'/g, "\\'");
                const safePrice = row[1].replace(/'/g, "\\'");
                const urlName = encodeURIComponent(row[0]);
                
                box.innerHTML += `
                <div class="prod-card reveal">
                    <div class="prod-img-wrap">
                        <img src="${{mainImg}}" class="prod-img" loading="lazy">
                    </div>
                    <div class="prod-info">
                        <div style="display:flex; justify-content:space-between; align-items:start;">
                            <h3 style="font-size:1.1rem; margin:0;">${{row[0]}}</h3>
                            <span class="prod-price">${{row[1]}}</span>
                        </div>
                        <div class="prod-actions">
                            <a href="product.html?item=${{urlName}}" class="btn btn-outline btn-sm">Details</a>
                            <button onclick="addToCart('${{safeName}}', '${{safePrice}}')" class="btn btn-primary btn-sm">Add</button>
                        </div>
                    </div>
                </div>`;
            }}
        }} catch(e) {{ console.log(e); }}
    }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);
    </script>
    """

def gen_product_page_content(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""
    <section style="padding-top:140px; min-height:80vh;"><div class="container"><div id="product-detail">Loading...</div></div></section>
    {gen_csv_parser()}
    <script>
    {demo_flag}
    function changeMainImg(src) {{ 
        document.getElementById('main-img').style.opacity = 0;
        setTimeout(() => {{
            document.getElementById('main-img').src = src;
            document.getElementById('main-img').style.opacity = 1;
        }}, 200);
    }}
    async function loadProduct() {{
        const params = new URLSearchParams(window.location.search);
        let targetName = params.get('item');
        if(isDemo && !targetName) targetName = "Demo Item";
        try {{
            const res = await fetch('{sheet_url}');
            const txt = await res.text();
            const lines = txt.split(/\\r\\n|\\n/);
            for(let i=1; i<lines.length; i++) {{
                const clean = parseCSVLine(lines[i]);
                if(isDemo) targetName = clean[0];
                if(clean[0] === targetName) {{
                    
                    // GALLERY LOGIC
                    let rawImgs = clean[3] || '{custom_feat}';
                    let imgs = rawImgs.split('|');
                    let mainImg = imgs[0];
                    let thumbs = '';
                    if(imgs.length > 1) {{
                        thumbs = '<div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:10px; margin-top:20px;">';
                        imgs.forEach(url => {{
                            thumbs += `<img src="${{url}}" style="width:100%; aspect-ratio:1; object-fit:cover; border-radius:8px; cursor:pointer; border:2px solid transparent;" onmouseover="this.style.borderColor='var(--p)'" onmouseout="this.style.borderColor='transparent'" onclick="changeMainImg('${{url}}')">`;
                        }});
                        thumbs += '</div>';
                    }}

                    const safeName = clean[0].replace(/'/g, "\\'");
                    const safePrice = clean[1].replace(/'/g, "\\'");
                    
                    document.getElementById('product-detail').innerHTML = `
                        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:4rem; align-items:start;">
                            <div>
                                <img id="main-img" src="${{mainImg}}" style="width:100%; border-radius:24px; box-shadow:var(--shadow-lg); transition:opacity 0.2s;">
                                ${{thumbs}}
                            </div>
                            <div>
                                <h1 class="gradient-text">${{clean[0]}}</h1>
                                <p style="font-size:2.5rem; font-weight:800; color:var(--txt); margin:1rem 0;">${{clean[1]}}</p>
                                <p style="opacity:0.8; font-size:1.1rem; margin-bottom:2rem;">${{clean[2]}}</p>
                                
                                <div style="display:flex; gap:1rem;">
                                    <button onclick="addToCart('${{safeName}}', '${{safePrice}}')" class="btn btn-primary" style="flex:1;">Add to Cart</button>
                                    <button onclick="navigator.clipboard.writeText(window.location.href);alert('Link Copied!')" class="btn btn-outline">Share</button>
                                </div>
                            </div>
                        </div>
                    `;
                    if(window.innerWidth < 768) {{ document.getElementById('product-detail').children[0].style.gridTemplateColumns = '1fr'; }}
                    break;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadProduct();
    </script>
    """

def gen_cart_system():
    if not show_inventory: return ""
    clean_wa = wa_num.replace("+", "").replace(" ", "").replace("-", "")
    return f"""
    <div id="cart-float" onclick="openModal('cartModal')" style="position:fixed; bottom:30px; right:100px; background:var(--bg); color:var(--txt); padding:12px 20px; border-radius:50px; box-shadow:var(--shadow-lg); cursor:pointer; z-index:998; display:flex; align-items:center; gap:10px; font-weight:bold; border:1px solid var(--border);">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="var(--p)"><path d="M7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zM1 2v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.14 0-.25-.11-.25-.25l.03-.12.9-1.63h7.45c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.08-.14.12-.31.12-.48 0-.55-.45-1-1-1H5.21l-.94-2H1zm16 16c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z"></path></svg>
        <span>Cart</span>
        <span id="cart-count" style="background:var(--s); color:white; border-radius:50%; width:20px; height:20px; display:flex; align-items:center; justify-content:center; font-size:0.7rem;">0</span>
    </div>

    <div id="cartModal" class="modal">
        <div class="modal-content">
            <span class="close-modal" onclick="closeModal('cartModal')" style="position:absolute; right:20px; top:20px; font-size:1.5rem; cursor:pointer;">&times;</span>
            <h3 class="gradient-text">Your Cart</h3>
            <div id="cart-items" style="max-height: 300px; overflow-y: auto; margin: 20px 0;"></div>
            <div style="border-top: 1px solid var(--border); padding-top: 15px; display:flex; justify-content:space-between; font-weight:bold; font-size:1.2rem;">
                <span>Total:</span> <span id="cart-total">0.00</span>
            </div>
            <button class="btn btn-primary" style="width: 100%; margin-top: 20px;" onclick="checkoutWA()">Checkout via WhatsApp</button>
        </div>
    </div>
    <script>
    let cart = [];
    function addToCart(name, price) {{
        cart.push({{name: name, price: price}});
        updateCart();
    }}
    function updateCart() {{
        document.getElementById('cart-count').innerText = cart.length;
        const box = document.getElementById('cart-items');
        const totalBox = document.getElementById('cart-total');
        if (cart.length === 0) {{ box.innerHTML = '<p style="opacity:0.6; text-align:center;">Empty.</p>'; totalBox.innerText = '0.00'; return; }}
        let html = '', total = 0;
        cart.forEach((item, index) => {{
            html += `<div style="display:flex; justify-content:space-between; padding:10px 0;"><div><b>${{item.name}}</b><br>${{item.price}}</div><div onclick="cart.splice(${{index}},1);updateCart()" style="cursor:pointer;color:var(--s)">✕</div></div>`;
            total += parseFloat(item.price.replace(/[^0-9.]/g, '')) || 0;
        }});
        box.innerHTML = html;
        totalBox.innerText = total.toFixed(2);
    }}
    function checkoutWA() {{
        let msg = "New Order:\\n"; cart.forEach(i => {{ msg += `- ${{i.name}} (${{i.price}})\\n`; }});
        msg += "\\nTotal: " + document.getElementById('cart-total').innerText;
        window.open("https://wa.me/{clean_wa}?text=" + encodeURIComponent(msg), '_blank');
    }}
    </script>
    """

def gen_wa_widget():
    if not wa_num: return ""
    clean_wa = wa_num.replace("+", "").replace(" ", "").replace("-", "")
    return f"""<a href="https://wa.me/{clean_wa}" target="_blank" style="position:fixed; bottom:30px; right:30px; background:#25D366; color:white; width:50px; height:50px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 25px rgba(37,211,102,0.4); z-index:9999; transition:transform 0.3s;"><svg style="width:28px;height:28px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></path></svg></a>"""

def gen_scripts():
    return """<script>
    window.addEventListener('scroll', () => { 
        var r = document.querySelectorAll('.reveal'); 
        for (var i = 0; i < r.length; i++) { 
            if (r[i].getBoundingClientRect().top < window.innerHeight - 80) r[i].classList.add('active'); 
        } 
    });
    window.dispatchEvent(new Event('scroll'));
    </script>"""

def gen_csv_parser():
    return """<script>
    function parseCSVLine(str) { const res = []; let cur = ''; let inQuote = false; for (let i = 0; i < str.length; i++) { const c = str[i]; if (c === '"') { if (inQuote && str[i+1] === '"') { cur += '"'; i++; } else { inQuote = !inQuote; } } else if (c === ',' && !inQuote) { res.push(cur.trim()); cur = ''; } else { cur += c; } } res.push(cur.trim()); return res; }
    function parseMarkdown(text) { if (!text) return ''; let html = text.replace(/\\r\\n/g, '\\n').replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>'); return html; }
    </script>"""

# --- PRESERVED FEATURES ---
def gen_stats():
    return f"""<div style="background:var(--p); color:white; padding:3rem 0; text-align:center;"><div class="container grid-3"><div class="reveal"><h3>{stat_1}</h3><p style="opacity:0.8;">{label_1}</p></div><div class="reveal"><h3>{stat_2}</h3><p style="opacity:0.8;">{label_2}</p></div><div class="reveal"><h3>{stat_3}</h3><p style="opacity:0.8;">{label_3}</p></div></div></div>"""
def gen_pricing_table():
    if not show_pricing: return ""
    return f"""<section id="pricing"><div class="container"><div class="section-head reveal"><h2 class="gradient-text">Pricing</h2></div><div class="reveal card"><table style="width:100%; text-align:left; border-collapse:collapse;"><thead><tr style="border-bottom:1px solid var(--border);"><th style="padding:1rem;">Category</th><th style="padding:1rem; color:var(--p);">Titan</th><th style="padding:1rem;">{wix_name}</th></tr></thead><tbody><tr><td style="padding:1rem;">Setup</td><td style="padding:1rem; font-weight:bold;">{titan_price}</td><td style="padding:1rem;">$0</td></tr><tr><td style="padding:1rem;">Monthly</td><td style="padding:1rem; font-weight:bold;">{titan_mo}</td><td style="padding:1rem;">{wix_mo}</td></tr></tbody></table></div></div></section>"""
def gen_about_section():
    return f"""<section id="about"><div class="container"><div class="grid-3" style="align-items:center;"><div class="reveal"><h2 class="gradient-text">{about_h_in}</h2><p>{format_text(about_short_in)}</p></div><img src="{about_img}" class="reveal" style="width:100%; border-radius:24px; box-shadow:var(--shadow-lg);"></div></div></section>"""
def gen_faq_section():
    items = "".join([f"<details class='card reveal' style='margin-bottom:1rem;'><summary style='font-weight:bold; cursor:pointer;'>{l.split('?')[0]}?</summary><p style='margin-top:10px;'>{l.split('?')[1]}</p></details>" for l in faq_data.split('\n') if "?" in l])
    return f"""<section id="faq"><div class="container" style="max-width:800px;"><div class="section-head reveal"><h2 class="gradient-text">F.A.Q.</h2></div>{items}</div></section>"""
def gen_blog_index_html(): return f"<section class='container' style='padding-top:150px;'><h1>Blog Coming Soon</h1></section>"
def gen_blog_post_html(): return f"<section class='container' style='padding-top:150px;'><h1>Article Loading...</h1></section>"
def gen_lang_script():
    if not lang_sheet: return ""
    return f"""<script>async function toggleLang() {{ try {{ const res=await fetch('{lang_sheet}'); const txt=await res.text(); const lines=txt.split(/\\r\\n|\\n/); for(let i=1;i<lines.length;i++){{ const r=parseCSVLine(lines[i]); if(r.length>1){{ const el=document.getElementById(r[0]); if(el) el.innerText=r[1]; }} }} closeModal('langModal'); }} catch(e){{ console.log(e); }} }}</script>"""
def gen_booking_content():
    return f"""<section class="hero" style="min-height:30vh; background:var(--p);"><div class="container"><h1>{booking_title}</h1><p>{booking_desc}</p></div></section><section><div class="container" style="text-align:center;"><div style="background:white; border-radius:12px; overflow:hidden; box-shadow:var(--shadow-lg); width:100%;">{booking_embed}</div></div></section>"""

def build_page(title, content, extra_js=""):
    pwa_tags = f'<link rel="manifest" href="manifest.json"><meta name="theme-color" content="{p_color}"><link rel="apple-touch-icon" href="{pwa_icon}">'
    sw_script = "<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('service-worker.js'); }</script>"
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title>{pwa_tags}{gen_schema()}<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap" rel="stylesheet"><style>{get_theme_css()}</style></head><body>{gen_nav()}{content}{f'<footer><div class="container" style="text-align:center;"><h2 style="color:white;">{biz_name}</h2><p>{biz_addr}</p><p>&copy; 2026 {biz_name}</p></div></footer>'}{gen_wa_widget()}{gen_cart_system()}{gen_scripts()}{gen_lang_script()}{sw_script}{extra_js}</body></html>"""

# --- 6. PAGE ASSEMBLY ---
home_content = ""
if show_hero: home_content += gen_hero()
if show_stats: home_content += gen_stats()
if show_features: home_content += gen_features()
if show_pricing: home_content += gen_pricing_table()
if show_inventory: home_content += gen_inventory()
if show_gallery: home_content += gen_about_section()
if show_testimonials: 
    t_cards = "".join([f'<div class="card reveal" style="text-align:center;"><i>"{x.split("|")[1]}"</i><br><b class="gradient-text">- {x.split("|")[0]}</b></div>' for x in testi_data.split('\n') if "|" in x])
    home_content += f'<section><div class="container"><div class="section-head reveal"><h2 class="gradient-text">Client Stories</h2></div><div class="grid-3">{t_cards}</div></div></section>'
if show_faq: home_content += gen_faq_section()
if show_cta: home_content += f'<section style="background:linear-gradient(135deg, var(--p), var(--s)); color:white; text-align:center;"><div class="container reveal"><h2>Start Owning Your Future</h2><a href="contact.html" class="btn" style="background:white; color:var(--p); margin-top:1rem;">Get Started</a></div></section>'

# --- 7. DEPLOYMENT ---
st.divider()
st.subheader("🚀 Launchpad")
preview_mode = st.radio("Preview Page:", ["Home", "Product Detail (Demo)", "Booking Page"], horizontal=True)

if preview_mode == "Home": st.components.v1.html(build_page("Home", home_content), height=700, scrolling=True)
elif preview_mode == "Product Detail (Demo)": st.components.v1.html(build_page("Product", gen_product_page_content(is_demo=True)), height=700, scrolling=True)
elif preview_mode == "Booking Page": st.components.v1.html(build_page("Book Now", gen_booking_content()), height=700, scrolling=True)

st.success("System Ready. All features active.")

# ZIP GENERATION LOGIC (Fixed to avoid nested button issues)
z_b = io.BytesIO()
with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
    zf.writestr("index.html", build_page("Home", home_content))
    zf.writestr("product.html", build_page("Product", gen_product_page_content()))
    zf.writestr("booking.html", build_page("Book Now", gen_booking_content()))
    zf.writestr("contact.html", build_page("Contact", f"<section style='padding-top:150px;' class='container'><h1>Contact Us</h1><p>{biz_phone}</p></section>"))
    if show_blog:
        zf.writestr("blog.html", build_page("Blog", gen_blog_index_html()))
        zf.writestr("post.html", build_page("Article", gen_blog_post_html()))
    zf.writestr("manifest.json", gen_pwa_manifest())
    zf.writestr("service-worker.js", gen_sw())

st.download_button(
    label="📥 DOWNLOAD GLASS UI WEBSITE",
    data=z_b.getvalue(),
    file_name="titan_glass_ui.zip",
    mime="application/zip",
    type="primary"
)
