import streamlit as st
import zipfile
import io
import json
import datetime
import re
import requests

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v39.0 | Ultra Stable", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# --- 2. GLOBAL VARIABLE INITIALIZATION (PREVENTS NAME ERROR) ---
# This section guarantees that every variable exists before the UI tries to set it.
biz_name = "StopWebRent.com"
biz_tagline = "Stop Renting."
biz_phone = ""
biz_email = ""
prod_url = ""
biz_addr = ""
map_iframe = ""
seo_d = ""
logo_url = ""
pwa_short = "App"
pwa_desc = "Web App"
pwa_icon = ""
lang_sheet = ""
fb_link = ""
ig_link = ""
x_link = ""
li_link = ""
yt_link = ""
wa_num = ""
hero_h = ""
hero_sub = ""
hero_video_id = ""
hero_img_1 = ""
hero_img_2 = ""
hero_img_3 = ""
stat_1 = ""; label_1 = ""
stat_2 = ""; label_2 = ""
stat_3 = ""; label_3 = ""
f_title = ""; feat_data_input = ""
about_h_in = ""; about_img = ""; about_short_in = ""; about_long = ""
top_bar_enabled = False; top_bar_text = ""; top_bar_link = ""
popup_enabled = False; popup_delay = 5; popup_title = ""; popup_text = ""; popup_cta = ""
titan_price = ""; titan_mo = ""; wix_name = ""; wix_mo = ""; save_val = ""
sheet_url = ""; custom_feat = ""; paypal_link = ""; upi_id = ""
blog_sheet_url = ""; blog_hero_title = ""; blog_hero_sub = ""
booking_embed = ""; booking_title = ""; booking_desc = ""
testi_data = ""; faq_data = ""; priv_txt = ""; term_txt = ""
# Design Defaults
theme_mode = "Midnight SaaS (Dark)"
p_color = "#0F172A"
s_color = "#EF4444"
hero_layout = "Center"
btn_style = "Pill (Rounded)"
h_font = "Space Grotesk"
b_font = "Inter"
border_rad = "12px"
anim_type = "Fade Up"

# --- 3. CSS SYSTEM ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #ef4444; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important; border: 1px solid #cbd5e1 !important; border-radius: 8px !important; color: #0f172a !important;
    }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5rem;
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
        color: white; font-weight: 800; border: none; box-shadow: 0 4px 15px rgba(15, 23, 42, 0.3); text-transform: uppercase; letter-spacing: 1px; transition: transform 0.2s;
    }
    .stButton>button:hover { transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR INPUTS ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v39.0 | Zero-Error Core")
    st.divider()
    
    with st.expander("🎨 Design Studio", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Midnight SaaS (Dark)", "Clean Corporate (Light)", "Glassmorphism (Blur)", "Cyberpunk Neon", "Luxury Gold", "Forest Eco", "Ocean Breeze", "Stark Minimalist"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#0F172A") 
        s_color = c2.color_picker("Action (CTA)", "#EF4444")  
        hero_layout = st.selectbox("Hero Alignment", ["Center", "Left"])
        btn_style = st.selectbox("Button Style", ["Pill (Rounded)", "Sharp (Square)", "Soft (Default)"])
        h_font = st.selectbox("Headings Font", ["Space Grotesk", "Montserrat", "Playfair Display", "Oswald", "Clash Display"])
        b_font = st.selectbox("Body Font", ["Inter", "Open Sans", "Roboto", "Satoshi", "Lora"])

    with st.expander("🧩 Modules", expanded=False):
        show_hero = st.checkbox("Hero Section", value=True)
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

    with st.expander("⚙️ SEO", expanded=False):
        seo_area = st.text_input("Service Area", "Global")
        seo_kw = st.text_area("SEO Keywords", "web design, static site")
        gsc_tag = st.text_input("Google ID")
        og_image = st.text_input("Social Share Image")

# --- 5. MAIN TABS (DATA BINDING) ---
st.title("🏗️ StopWebRent Site Builder v39.0")
tabs = st.tabs(["1. Identity & PWA", "2. Content", "3. Marketing", "4. Pricing", "5. Store", "6. Blog", "7. Booking", "8. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent.com")
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
    fb_link = st.text_input("Facebook URL")
    ig_link = st.text_input("Instagram URL")
    x_link = st.text_input("X (Twitter) URL")
    li_link = st.text_input("LinkedIn URL")
    yt_link = st.text_input("YouTube URL")
    wa_num = st.text_input("WhatsApp Number (No +)", "966572562151")

with tabs[1]:
    st.subheader("Hero Section")
    hero_h = st.text_input("Hero Headline", "Stop Paying Rent for Your Website.")
    hero_sub = st.text_input("Hero Subtext", "The Titan Engine is the world’s first 0.1s website architecture.")
    hero_video_id = st.text_input("YouTube Video ID (Background)", placeholder="e.g. dQw4w9WgXcQ")
    hero_img_1 = st.text_input("Slide 1", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    hero_img_2 = st.text_input("Slide 2", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1600")
    hero_img_3 = st.text_input("Slide 3", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1600")
    
    st.divider()
    col_s1, col_s2, col_s3 = st.columns(3)
    stat_1 = col_s1.text_input("Stat 1", "0.1s"); label_1 = col_s1.text_input("Label 1", "Speed")
    stat_2 = col_s2.text_input("Stat 2", "$0"); label_2 = col_s2.text_input("Label 2", "Fees")
    stat_3 = col_s3.text_input("Stat 3", "100%"); label_3 = col_s3.text_input("Label 3", "Ownership")

    f_title = st.text_input("Features Title", "Value Pillars")
    feat_data_input = st.text_area("Features List", "bolt | Speed | 0.1s Load\nwallet | Cost | $0 Fees\nshield | Security | Zero-DB", height=150)
    
    st.subheader("About")
    about_h_in = st.text_input("About Title", "Control Your Empire")
    about_img = st.text_input("About Image", "https://images.unsplash.com/photo-1543286386-713df548e9cc?q=80&w=1600")
    about_short_in = st.text_area("Short Summary", "No WordPress dashboard.", height=100)
    about_long = st.text_area("Full Content", "The Digital Landlord Trap...", height=200)

with tabs[2]:
    st.subheader("📣 Marketing")
    top_bar_enabled = st.checkbox("Enable Top Bar")
    top_bar_text = st.text_input("Promo Text", "🔥 50% OFF Launch Sale")
    top_bar_link = st.text_input("Promo Link", "#pricing")
    st.divider()
    popup_enabled = st.checkbox("Enable Popup")
    popup_delay = st.slider("Delay (sec)", 1, 30, 5)
    popup_title = st.text_input("Popup Title", "Wait!")
    popup_text = st.text_input("Popup Body", "Get free guide.")
    popup_cta = st.text_input("Popup Button", "Get it Now")

with tabs[3]:
    st.subheader("💰 Pricing")
    col_p1, col_p2, col_p3 = st.columns(3)
    titan_price = col_p1.text_input("Setup Price", "$199")
    titan_mo = col_p1.text_input("Monthly Fee", "$0")
    wix_name = col_p2.text_input("Competitor", "Wix")
    wix_mo = col_p2.text_input("Comp. Monthly", "$29/mo")
    save_val = col_p3.text_input("Savings", "$1,466")

with tabs[4]:
    st.subheader("🛒 Store")
    st.info("Multi-Image: `url1|url2`")
    sheet_url = st.text_input("Store CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Default Product Img", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")
    col_pay1, col_pay2 = st.columns(2)
    paypal_link = col_pay1.text_input("PayPal Link", "https://paypal.me/yourid")
    upi_id = col_pay2.text_input("UPI ID", "name@upi")

with tabs[5]:
    st.subheader("📰 Blog")
    blog_sheet_url = st.text_input("Blog CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    blog_hero_title = st.text_input("Blog Title", "Latest Insights")
    blog_hero_sub = st.text_input("Blog Subtext", "Thoughts on tech.")

with tabs[6]:
    st.subheader("📅 Booking")
    booking_embed = st.text_area("Embed Code", height=150, value='<!-- Calendly -->')
    booking_title = st.text_input("Booking Title", "Book an Appointment")
    booking_desc = st.text_input("Booking Subtext", "Select a time slot.")

with tabs[7]:
    st.subheader("Legal")
    testi_data = st.text_area("Testimonials", "Rajesh Gupta | Titan stopped the bleeding.", height=100)
    faq_data = st.text_area("FAQ", "Do I pay $0? ? Yes.", height=100)
    priv_txt = st.text_area("Privacy", "We collect minimum data.", height=100)
    term_txt = st.text_area("Terms", "You own the code.", height=100)

# ==========================================
# 6. COMPILER ENGINE (DEFINITIONS)
# ==========================================

def format_text(text):
    if not text: return ""
    processed = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    return processed.replace('\n', '<br>')

def gen_schema():
    schema = { "@context": "https://schema.org", "@type": "LocalBusiness", "name": biz_name, "image": logo_url or hero_img_1, "telephone": biz_phone, "url": prod_url, "description": seo_d }
    return f'<script type="application/ld+json">{json.dumps(schema)}</script>'

def gen_pwa_manifest():
    return json.dumps({ "name": biz_name, "short_name": pwa_short, "start_url": "./index.html", "display": "standalone", "background_color": "#ffffff", "theme_color": p_color, "description": pwa_desc, "icons": [{"src": pwa_icon, "sizes": "512x512", "type": "image/png"}] })

def gen_sw():
    return """self.addEventListener('install', (e) => { e.waitUntil(caches.open('titan-store').then((cache) => cache.addAll(['./index.html']))); }); self.addEventListener('fetch', (e) => { e.respondWith(caches.match(e.request).then((response) => response || fetch(e.request))); });"""

def get_theme_css():
    # Base Defaults
    bg_color, text_color, card_bg, glass_nav = "#ffffff", "#0f172a", "#ffffff", "rgba(255, 255, 255, 0.95)"
    
    if "Midnight" in theme_mode: bg_color, text_color, card_bg, glass_nav = "#0f172a", "#f8fafc", "#1e293b", "rgba(15, 23, 42, 0.9)"
    elif "Cyberpunk" in theme_mode: bg_color, text_color, card_bg, glass_nav = "#050505", "#00ff9d", "#111", "rgba(0,0,0,0.8)"
    elif "Luxury" in theme_mode: bg_color, text_color, card_bg, glass_nav = "#1c1c1c", "#D4AF37", "#2a2a2a", "rgba(28,28,28,0.95)"
    elif "Ocean" in theme_mode: bg_color, text_color, card_bg, glass_nav = "#e0f7fa", "#006064", "#ffffff", "rgba(224,247,250,0.9)"

    btn_rad = "8px"
    if btn_style == "Pill (Rounded)": btn_rad = "50px"
    elif btn_style == "Sharp (Square)": btn_rad = "0px"

    hero_align = "text-align: center; justify-content: center;"
    if hero_layout == "Left": hero_align = "text-align: left; justify-content: flex-start; align-items: center;"

    hero_css = f"""
    .hero {{ position: relative; min-height: 90vh; overflow: hidden; display: flex; {hero_align} color: white; padding-top: 80px; background-color: var(--p); }}
    .carousel-slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.5s ease-in-out; z-index: 0; }}
    .carousel-slide.active {{ opacity: 1; }}
    .hero-overlay {{ background: rgba(0,0,0,0.5); position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }}
    .hero-content {{ z-index: 2; position: relative; animation: slideUp 1s ease-out; width: 100%; padding: 0 20px; }}
    @keyframes slideUp {{ from {{ opacity:0; transform: translateY(30px); }} to {{ opacity:1; transform: translateY(0); }} }}
    """

    extra_css = """
    #cart-float { position: fixed; bottom: 100px; right: 30px; background: var(--p); color: white; padding: 15px 20px; border-radius: 50px; box-shadow: 0 10px 20px rgba(0,0,0,0.2); cursor: pointer; z-index: 998; display: flex; align-items: center; gap: 10px; font-weight: bold; }
    #cart-modal { display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: var(--card); width: 90%; max-width: 500px; padding: 2rem; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.3); z-index: 1001; border: 1px solid rgba(128,128,128,0.2); color: var(--txt); }
    #cart-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; }
    .cart-item { display: flex; justify-content: space-between; border-bottom: 1px solid #eee; padding: 10px 0; }
    
    /* Social Share */
    .share-row { display: flex; gap: 10px; margin-top: 20px; flex-wrap: wrap; }
    .share-btn { width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 50%; color: white; transition: 0.3s; border: none; cursor: pointer; text-decoration: none; }
    .share-btn:hover { transform: translateY(-3px); filter: brightness(1.1); }
    .share-btn svg { width: 20px; height: 20px; fill: white; }
    
    .bg-fb { background: #1877F2; } .bg-x { background: #000000; } .bg-li { background: #0A66C2; } 
    .bg-wa { background: #25D366; } .bg-rd { background: #FF4500; } .bg-link { background: #64748b; }
    
    /* Top Bar */
    #top-bar { position: fixed; top: 0; width: 100%; background: var(--s); color: white; text-align: center; padding: 10px; z-index: 1002; font-weight: bold; font-size: 0.9rem; transition: transform 0.3s; }
    #top-bar a { color: white; text-decoration: underline; }
    
    #lead-popup { display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: var(--card); padding: 3rem; text-align: center; border-radius: var(--radius); z-index: 2000; box-shadow: 0 25px 100px rgba(0,0,0,0.5); width: 90%; max-width: 450px; border: 1px solid rgba(0,0,0,0.1); color: var(--txt); }
    .close-popup { position: absolute; top: 15px; right: 15px; cursor: pointer; font-size: 1.5rem; opacity: 0.5; }
    
    #theme-toggle { position: fixed; bottom: 30px; left: 30px; width: 40px; height: 40px; background: var(--card); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 5px 15px rgba(0,0,0,0.1); cursor: pointer; z-index: 999; font-size: 1.2rem; border: 1px solid rgba(0,0,0,0.1); }
    """

    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg_color}; --txt: {text_color}; --card: {card_bg}; --radius: {btn_rad}; --nav: {glass_nav}; --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif; }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--b-font); margin: 0; line-height: 1.6; overflow-x: hidden; }}
    body.dark-mode {{ --bg: #0f172a; --txt: #f8fafc; --card: #1e293b; --nav: rgba(15, 23, 42, 0.95); }}
    
    h1, h2, h3, h4 {{ font-family: var(--h-font); color: var(--p); line-height: 1.2; margin-bottom: 1rem; }}
    h1 {{ font-size: clamp(2.5rem, 5vw, 4.5rem); background: linear-gradient(120deg, var(--p), var(--s)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
    h2 {{ font-size: clamp(2rem, 4vw, 3rem); }}
    
    .hero h1 {{ background: none; -webkit-text-fill-color: white; color: white !important; text-shadow: 0 4px 20px rgba(0,0,0,0.4); }}
    .hero p {{ color: rgba(255,255,255,0.95) !important; font-size: clamp(1.1rem, 2vw, 1.3rem); max-width: 700px; margin: 0 auto 2rem auto; text-shadow: 0 2px 10px rgba(0,0,0,0.4); }}
    
    .card {{ background: var(--card); padding: 2rem; border-radius: 16px; border: 1px solid rgba(128,128,128,0.1); transition: all 0.4s; height: 100%; display: flex; flex-direction: column; position: relative; overflow: hidden; }}
    .card:hover {{ transform: translateY(-10px); box-shadow: 0 30px 60px -15px rgba(0,0,0,0.1); border-color: var(--s); }}
    .card h1, .card h2, .card h3, .card h4, .card a {{ color: var(--txt) !important; text-decoration: none; }}
    .card p {{ color: var(--txt); opacity: 0.9; }}
    
    .prod-img {{ width: 100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 12px; margin-bottom: 1.5rem; background: #f1f5f9; transition: transform 0.5s; }}
    .card:hover .prod-img {{ transform: scale(1.05); }}
    
    .btn {{ 
        display: inline-flex; align-items: center; justify-content: center;
        padding: 0.8rem 1.5rem; border-radius: var(--radius); 
        font-weight: 700; text-decoration: none; transition: 0.3s; 
        text-transform: uppercase; cursor: pointer; border: none; text-align: center;
        white-space: normal; line-height: 1.2; word-wrap: break-word; font-size: 0.9rem; letter-spacing: 0.5px;
    }}
    .btn-primary {{ background: var(--p); color: white !important; }}
    .btn-accent {{ background: var(--s); color: white !important; box-shadow: 0 10px 20px -5px rgba(239, 68, 68, 0.4); }}
    .btn:hover {{ transform: translateY(-3px); filter: brightness(1.15); }}
    .btn-outline {{ background: transparent; border: 2px solid var(--p); color: var(--p) !important; }}
    .btn-outline:hover {{ background: var(--p); color: white !important; }}

    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; background: var(--nav); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(100,100,100,0.1); padding: 1rem 0; transition: top 0.3s; }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; align-items: center; gap: 2rem; }}
    .nav-links a {{ text-decoration: none; font-weight: 600; color: var(--txt); opacity: 0.8; transition:0.2s; }}
    .nav-links a:hover {{ opacity: 1; color: var(--s); }}
    .mobile-menu {{ display: none; font-size: 1.5rem; cursor: pointer; }}
    
    {hero_css}
    
    section {{ padding: clamp(1rem, 3vw, 2.5rem) 0; }} /* REDUCED PADDING FIX */
    .section-head {{ text-align: center; margin-bottom: clamp(1.5rem, 4vw, 3rem); }}
    
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .about-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }}
    .contact-grid {{ display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; }}
    .detail-view {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start; }}
    
    /* MODAL STYLES */
    .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.6); backdrop-filter: blur(5px); }}
    .modal-content {{ background-color: var(--card); margin: 15% auto; padding: 2rem; border: 1px solid #888; width: 90%; max-width: 400px; border-radius: 16px; text-align: center; color: var(--txt); }}
    .close-modal {{ color: #aaa; float: right; font-size: 28px; font-weight: bold; cursor: pointer; }}
    
    /* Gallery */
    .gallery-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 10px; }}
    .gallery-thumb {{ width: 100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 8px; cursor: pointer; border: 2px solid transparent; }}
    .gallery-thumb:hover {{ border-color: var(--s); }}

    footer {{ background: var(--p); color: white; padding: 4rem 0; margin-top: auto; }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; }}
    footer a {{ color: rgba(255,255,255,0.8) !important; text-decoration: none; display: block; margin-bottom: 0.5rem; transition: 0.3s; }}
    footer a:hover {{ color: #ffffff !important; text-decoration: underline; }}
    .social-icon {{ width: 24px; height: 24px; fill: rgba(255,255,255,0.7); }}

    .blog-badge {{ background: var(--s); color: white; padding: 0.3rem 0.8rem; border-radius: 50px; font-size: 0.75rem; text-transform: uppercase; font-weight: bold; width: fit-content; margin-bottom: 1rem; display:inline-block; }}
    
    {anim_css}
    {extra_css}
    
    @media (max-width: 768px) {{
        .nav-links {{ 
            position: fixed; top: 60px; left: -100%; width: 100%; height: calc(100vh - 60px); 
            background: var(--bg); flex-direction: column; padding: 2rem; transition: 0.3s; 
            align-items: flex-start; justify-content: flex-start; border-top: 1px solid rgba(0,0,0,0.1); gap: 1.5rem;
        }}
        .nav-links.active {{ left: 0; }}
        .mobile-menu {{ display: block; }}
        .about-grid, .contact-grid, .detail-view {{ grid-template-columns: 1fr !important; gap: 2rem; }}
        .about-grid img {{ order: -1; }}
        #top-bar {{ font-size: 0.7rem; }}
        .btn {{ width: 100%; margin-bottom: 0.5rem; min-height: 3.5rem; }}
    }}
    """

def gen_nav():
    logo = f'<img src="{logo_url}" height="32" alt="{biz_name}">' if logo_url else f'<span style="font-weight:900;font-size:1.5rem;color:var(--p)" id="nav-logo">{biz_name}</span>'
    blog_link = '<a href="blog.html" onclick="toggleMenu()" id="nav-blog">Blog</a>' if show_blog else ''
    book_link = '<a href="booking.html" onclick="toggleMenu()" id="nav-book">Book Now</a>' if show_booking else ''
    lang_btn = f'<a href="#" onclick="openLangModal()" title="Language">🌐 Lang</a>' if lang_sheet else ''
    
    return f"""
    {f'<div id="top-bar"><a href="{top_bar_link}" style="color:white;">{top_bar_text}</a></div>' if top_bar_enabled else ''}
    <nav><div class="container nav-flex">
        <a href="index.html" style="text-decoration:none">{logo}</a>
        <div class="mobile-menu" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</div>
        <div class="nav-links">
            <a href="index.html" onclick="toggleMenu()" id="nav-home">Home</a>
            {'<a href="index.html#features" onclick="toggleMenu()" id="nav-features">Features</a>' if show_features else ''}
            {'<a href="index.html#pricing" onclick="toggleMenu()" id="nav-pricing">Savings</a>' if show_pricing else ''}
            {'<a href="index.html#inventory" onclick="toggleMenu()" id="nav-store">Store</a>' if show_inventory else ''}
            {blog_link}
            {book_link}
            {lang_btn}
            <a href="contact.html" onclick="toggleMenu()" id="nav-contact">Contact</a>
            <a href="tel:{biz_phone}" class="btn-accent" style="padding:0.6rem 1.5rem; border-radius:50px; color:white !important;" id="nav-call">Call Now</a>
        </div>
    </div></nav>
    <div id="langModal" class="modal"><div class="modal-content"><span class="close-modal" onclick="closeLangModal()">&times;</span><h3>Select Language</h3><div style="display:flex; flex-direction:column; gap:10px; margin-top:20px;"><button onclick="switchLanguage('en')" class="btn btn-outline" style="width:100%;">English</button><button onclick="switchLanguage('es')" class="btn btn-primary" style="width:100%;">Espanol</button></div></div></div>
    <div id="theme-toggle" onclick="document.body.classList.toggle('dark-mode')">🌓</div>
    <script>
        function toggleMenu() {{ document.querySelector('.nav-links').classList.remove('active'); }}
        function openLangModal() {{ document.getElementById("langModal").style.display = "block"; }}
        function closeLangModal() {{ document.getElementById("langModal").style.display = "none"; }}
        if({str(top_bar_enabled).lower()}) {{ document.querySelector('nav').style.top = '40px'; if(window.innerWidth <= 768) {{ document.querySelector('.nav-links').style.top = '100px'; }} }}
    </script>
    """

def gen_hero():
    bg = f"""<div class="carousel-slide active" style="background-image: url('{hero_img_1}')"></div>"""
    if hero_video_id: bg = f"""<iframe src="https://www.youtube.com/embed/{hero_video_id}?autoplay=1&mute=1&loop=1&playlist={hero_video_id}&controls=0&showinfo=0&rel=0" style="position:absolute; top:50%; left:50%; width:100vw; height:100vh; transform:translate(-50%, -50%); pointer-events:none; object-fit:cover; z-index:0; min-width:177.77vh; min-height:56.25vw;" frameborder="0"></iframe>"""
    return f"""<section class="hero"><div class="hero-overlay"></div>{bg}<div class="container hero-content"><h1 id="hero-title">{hero_h}</h1><p id="hero-sub">{hero_sub}</p><div style="display:flex; gap:1rem; flex-wrap:wrap; {'justify-content:center;' if hero_layout == 'Center' else ''}"><a href="#inventory" class="btn btn-accent" id="btn-explore">Explore Now</a><a href="contact.html" class="btn" style="background:rgba(255,255,255,0.2); backdrop-filter:blur(10px); color:white;" id="btn-contact">Contact Us</a></div></div></section>"""

def get_simple_icon(name):
    path = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"
    if "bolt" in name: path = "M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"
    return f'<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="{path}"/></svg>'

def gen_features():
    cards = ""
    lines = [x for x in feat_data_input.split('\n') if x.strip()]
    for line in lines:
        parts = line.split('|')
        if len(parts) >= 3: cards += f"""<div class="card reveal"><div style="color:var(--s); margin-bottom:1rem;">{get_simple_icon(parts[0])}</div><h3>{parts[1].strip()}</h3><div>{format_text(parts[2].strip())}</div></div>"""
    return f"""<section id="features"><div class="container"><div class="section-head reveal"><h2 id="feature-title">{f_title}</h2></div><div class="grid-3">{cards}</div></div></section>"""

def gen_stats():
    return f"""<div style="background:var(--p); color:white; padding:3rem 0; text-align:center;"><div class="container grid-3"><div class="reveal"><h3>{stat_1}</h3><p style="color:rgba(255,255,255,0.7);">{label_1}</p></div><div class="reveal"><h3>{stat_2}</h3><p style="color:rgba(255,255,255,0.7);">{label_2}</p></div><div class="reveal"><h3>{stat_3}</h3><p style="color:rgba(255,255,255,0.7);">{label_3}</p></div></div></div>"""

def gen_pricing_table():
    if not show_pricing: return ""
    return f"""<section id="pricing"><div class="container"><div class="section-head reveal"><h2 id="pricing-title">Pricing</h2></div><div class="pricing-wrapper reveal"><table class="pricing-table"><thead><tr><th style="width:40%">Expense Category</th><th style="background:var(--s);">Titan</th><th>{wix_name}</th></tr></thead><tbody><tr><td>Initial Setup Fee</td><td><strong>{titan_price}</strong></td><td>$0</td></tr><tr><td>Annual Costs</td><td><strong>{titan_mo}</strong></td><td>{wix_mo}</td></tr><tr><td><strong>5-Year Savings</strong></td><td style="color:var(--s); font-size:1.3rem;">You Save {save_val}</td><td>$0</td></tr></tbody></table></div></div></section>"""

def gen_csv_parser():
    return """<script>function parseCSVLine(str){const res=[];let cur='';let inQuote=false;for(let i=0;i<str.length;i++){const c=str[i];if(c==='"'){if(inQuote&&str[i+1]==='"'){cur+='"';i++}else{inQuote=!inQuote}}else if(c===','&&!inQuote){res.push(cur.trim());cur=''}else{cur+=c}}res.push(cur.trim());return res}function parseMarkdown(text){if(!text)return'';let html=text.replace(/\\r\\n/g,'\\n').replace(/\\n/g,'<br>').replace(/\\*\\*(.*?)\\*\\*/g,'<strong>$1</strong>');return html}</script>"""

def gen_lang_script():
    if not lang_sheet: return ""
    return f"""<script>async function switchLanguage(lang){{if(lang==='en'){{location.reload();return}}try{{const res=await fetch('{lang_sheet}');const txt=await res.text();const lines=txt.split(/\\r\\n|\\n/);for(let i=1;i<lines.length;i++){{const row=parseCSVLine(lines[i]);if(row.length>1){{const el=document.getElementById(row[0]);if(el)el.innerText=row[1]}}}}closeLangModal()}}catch(e){{console.log(e)}}}}</script>"""

def gen_inventory_js(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""
    {gen_csv_parser()}
    <script>
    {demo_flag}
    async function loadInv() {{
        try {{
            const res = await fetch('{sheet_url}'); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/);
            const box = document.getElementById('inv-grid'); if(!box) return; box.innerHTML = '';
            for(let i=1; i<lines.length; i++) {{
                const c = parseCSVLine(lines[i]);
                if(c.length > 1) {{
                    let img = (c[3] || '{custom_feat}').split('|')[0];
                    const prodName = encodeURIComponent(c[0]);
                    // Minimal UI: Image, Title, Price, Button
                    box.innerHTML += `
                    <div class="card reveal" style="padding:1.5rem;">
                        <img src="${{img}}" class="prod-img" style="margin-bottom:1rem;">
                        <h3 style="font-size:1.1rem; margin-bottom:0.2rem;">${{c[0]}}</h3>
                        <p style="font-weight:900; color:var(--s); font-size:1.1rem; margin-bottom:1rem;">${{c[1]}}</p>
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:auto;">
                            <a href="product.html?item=${{prodName}}" class="btn btn-outline" style="font-size:0.8rem; padding:0.5rem;">View</a>
                            <button onclick="addToCart('${{c[0]}}', '${{c[1]}}')" class="btn btn-primary" style="font-size:0.8rem; padding:0.5rem;">Add</button>
                        </div>
                    </div>`;
                }}
            }}
        }} catch(e) {{}}
    }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);
    </script>
    """

def gen_inventory():
    if not show_inventory: return ""
    return f"""<section id="inventory" style="background:rgba(0,0,0,0.02)"><div class="container"><div class="section-head reveal"><h2 id="store-title">Store</h2></div><div id="inv-grid" class="grid-3"><div>Loading...</div></div></div></section>{gen_inventory_js(is_demo=False)}"""

def gen_about_section():
    return f"""<section id="about"><div class="container"><div class="about-grid"><div class="reveal"><h2 id="about-title">{about_h_in}</h2><div>{format_text(about_short_in)}</div><a href="about.html" class="btn btn-primary" id="about-btn">Read More</a></div><img src="{about_img}" class="reveal" style="width:100%; border-radius:var(--radius);"></div></div></section>"""

def gen_faq_section():
    items = "".join([f"<details class='reveal'><summary>{l.split('?')[0]}?</summary><p>{l.split('?')[1]}</p></details>" for l in faq_data.split('\n') if "?" in l])
    return f"""<section id="faq"><div class="container" style="max-width:800px;"><div class="section-head reveal"><h2 id="faq-title">Frequently Asked Questions</h2></div>{items}</div></section>"""

def gen_footer():
    return f"""<footer><div class="container"><div class="footer-grid"><div><h3>{biz_name}</h3><p style="opacity:0.8;">{biz_addr}</p></div><div><h4>Explore</h4><a href="index.html">Home</a><a href="blog.html">Blog</a></div><div><h4>Legal</h4><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a></div></div></div></footer>"""

def gen_wa_widget():
    if not wa_num: return ""
    clean_wa = wa_num.replace("+", "").replace(" ", "").replace("-", "")
    return f"""<a href="https://wa.me/{clean_wa}" class="wa-float" target="_blank" style="position:fixed; bottom:30px; right:30px; background:#25d366; color:white; width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 30px rgba(37,211,102,0.4); z-index:9999;"><svg style="width:32px;height:32px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></path></svg></a>"""

def gen_scripts():
    return """<script>window.addEventListener('scroll', () => { var r = document.querySelectorAll('.reveal'); for (var i = 0; i < r.length; i++) { if (r[i].getBoundingClientRect().top < window.innerHeight - 100) r[i].classList.add('active'); } }); window.dispatchEvent(new Event('scroll'));</script>"""

def gen_inner_header(title):
    return f"""<section class="hero" style="min-height: 40vh; background:var(--p);"><div class="container"><h1>{title}</h1></div></section>"""

def gen_blog_index_html():
    return f"""
    <section class="hero" style="min-height:40vh; background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{hero_img_1}'); background-size: cover;">
        <div class="container"><h1>{blog_hero_title}</h1><p>{blog_hero_sub}</p></div>
    </section>
    <section><div class="container"><div id="blog-grid" class="grid-3">Loading...</div></div></section>
    {gen_csv_parser()}
    <script>
    async function loadBlog() {{
        try {{
            const res = await fetch('{blog_sheet_url}'); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/);
            const box = document.getElementById('blog-grid'); box.innerHTML = '';
            for(let i=1; i<lines.length; i++) {{
                const r = parseCSVLine(lines[i]);
                if(r.length > 4) {{
                    box.innerHTML += `
                    <div class="card reveal">
                        <img src="${{r[5]}}" class="prod-img">
                        <div style="flex-grow:1;">
                            <span class="blog-badge">${{r[3]}}</span>
                            <h3 style="margin-top:0.5rem;"><a href="post.html?id=${{r[0]}}">${{r[1]}}</a></h3>
                            <p style="font-size:0.9rem; opacity:0.8;">${{r[4]}}</p>
                        </div>
                        <a href="post.html?id=${{r[0]}}" class="btn btn-primary" style="width:100%; margin-top:1rem;">Read Article</a>
                    </div>`;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadBlog();
    </script>
    """

def gen_product_page_content(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""
    <section style="padding-top:120px;"><div class="container"><div id="product-detail">Loading...</div></div></section>
    {gen_csv_parser()}
    <script>
    {demo_flag}
    function changeMainImg(src) {{ document.getElementById('main-img').src = src; }}
    function shareWA(url, title) {{ window.open('https://wa.me/?text=' + encodeURIComponent(title + ' ' + url), '_blank'); }}
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
                    let allImgs = (clean[3] || '{custom_feat}').split('|');
                    let mainImg = allImgs[0];
                    let galleryHtml = '';
                    if(allImgs.length > 1) {{
                        galleryHtml = '<div class="gallery-grid">';
                        allImgs.forEach(img => galleryHtml += `<img src="${{img}}" class="gallery-thumb" onclick="changeMainImg('${{img}}')">`);
                        galleryHtml += '</div>';
                    }}
                    let btn = `<button onclick="addToCart('${{clean[0]}}', '${{clean[1]}}')" class="btn btn-primary" style="width:100%; margin-top:1rem;">Add to Cart</button>`;
                    const u = encodeURIComponent(window.location.href);
                    
                    document.getElementById('product-detail').innerHTML = `
                        <div class="detail-view">
                            <div><img id="main-img" src="${{mainImg}}" style="width:100%; border-radius:12px; aspect-ratio:1/1; object-fit:cover;">${{galleryHtml}}</div>
                            <div>
                                <h1 style="line-height:1.1;">${{clean[0]}}</h1>
                                <p style="font-size:2rem; color:var(--s); font-weight:bold; margin-bottom:1.5rem;">${{clean[1]}}</p>
                                <p style="opacity:0.9; line-height:1.6;">${{clean[2]}}</p>
                                ${{btn}}
                            </div>
                        </div>
                    `;
                    break;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadProduct();
    </script>
    """

def gen_booking_content():
    return f"""
    <section class="hero" style="min-height:30vh; background:var(--p);">
        <div class="container hero-content"><h1>{booking_title}</h1><p>{booking_desc}</p></div>
    </section>
    <section>
        <div class="container" style="text-align:center;">
            <div style="background:white; border-radius:12px; overflow:hidden; box-shadow:0 10px 40px rgba(0,0,0,0.1); width:100%;">
                {booking_embed}
            </div>
        </div>
    </section>
    """

# --- 7. DEPLOYMENT & LAUNCHPAD ---
home_content = ""
if show_hero: home_content += gen_hero()
if show_stats: home_content += gen_stats()
if show_features: home_content += gen_features()
if show_pricing: home_content += gen_pricing_table()
if show_inventory: home_content += gen_inventory()
if show_gallery: home_content += gen_about_section()
if show_testimonials: 
    t_cards = "".join([f'<div class="card reveal" style="text-align:center;"><i>"{x.split("|")[1]}"</i><br><b>- {x.split("|")[0]}</b></div>' for x in testi_data.split('\n') if "|" in x])
    home_content += f'<section style="background:#f8fafc"><div class="container"><div class="section-head reveal"><h2>Client Stories</h2></div><div class="grid-3">{t_cards}</div></div></section>'
if show_faq: home_content += gen_faq_section()
if show_cta: home_content += f'<section style="background:var(--s); color:white; text-align:center;"><div class="container reveal"><h2 id="cta-title">Start Owning Your Future</h2><p style="margin-bottom:2rem;" id="cta-sub">Stop paying rent.</p><a href="contact.html" class="btn" style="background:white; color:var(--s);" id="cta-btn">Get Started</a></div></section>'

st.divider()
st.subheader("🚀 Launchpad")
preview_mode = st.radio("Preview Page:", ["Home", "About", "Contact", "Blog Index", "Booking Page"], horizontal=True)

contact_content = f"""{gen_inner_header("Contact Us")}<section><div class="container"><div class="contact-grid"><div><div style="background:var(--card); padding:2rem; border-radius:12px; border:1px solid #eee;"><h3>Get In Touch</h3><p>{biz_addr}</p><p><a href="tel:{biz_phone}">{biz_phone}</a></p><p>{biz_email}</p><br><a href="https://wa.me/{wa_num}" target="_blank" class="btn btn-accent" style="width:100%;">WhatsApp Us</a></div></div><div class="card"><h3>Send Message</h3><form action="https://formsubmit.co/{biz_email}" method="POST"><label>Name</label><input type="text" name="name" required><label>Email</label><input type="email" name="email" required><label>Message</label><textarea name="msg" rows="4" required></textarea><button class="btn btn-primary" type="submit">Send</button></form></div></div><br><div style="border-radius:12px;overflow:hidden;">{map_iframe}</div></div></section>"""

c1, c2 = st.columns([3, 1])
with c1:
    if preview_mode == "Home": st.components.v1.html(build_page("Home", home_content), height=600, scrolling=True)
    elif preview_mode == "About": st.components.v1.html(build_page("About", f"{gen_inner_header('About')}<div class='container'>{format_text(about_long)}</div>"), height=600, scrolling=True)
    elif preview_mode == "Contact": st.components.v1.html(build_page("Contact", contact_content), height=600, scrolling=True)
    elif preview_mode == "Blog Index": st.components.v1.html(build_page("Blog", gen_blog_index_html()), height=600, scrolling=True)
    elif preview_mode == "Booking Page": st.components.v1.html(build_page("Book Now", gen_booking_content()), height=600, scrolling=True)

with c2:
    if st.button("DOWNLOAD WEBSITE ZIP", type="primary"):
        z_b = io.BytesIO()
        with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
            zf.writestr("index.html", build_page("Home", home_content))
            zf.writestr("about.html", build_page("About", f"{gen_inner_header('About')}<div class='container'>{format_text(about_long)}</div>"))
            zf.writestr("contact.html", build_page("Contact", contact_content))
            zf.writestr("privacy.html", build_page("Privacy", f"{gen_inner_header('Privacy')}<div class='container'>{format_text(priv_txt)}</div>"))
            zf.writestr("terms.html", build_page("Terms", f"{gen_inner_header('Terms')}<div class='container'>{format_text(term_txt)}</div>"))
            zf.writestr("booking.html", build_page("Book Now", gen_booking_content()))
            zf.writestr("product.html", build_page("Product Details", gen_product_page_content(is_demo=False)))
            if show_blog: 
                zf.writestr("blog.html", build_page("Blog", gen_blog_index_html()))
                zf.writestr("post.html", build_page("Article", gen_blog_post_html()))
            zf.writestr("manifest.json", gen_pwa_manifest())
            zf.writestr("service-worker.js", gen_sw())
        st.download_button("📥 Click to Save", z_b.getvalue(), f"{biz_name.lower().replace(' ','_')}_site.zip", "application/zip")
