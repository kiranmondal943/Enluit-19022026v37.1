import streamlit as st
import zipfile
import io
import json
import datetime
import re
import requests

# --- 0. STATE MANAGEMENT ---
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
    page_title="Titan v41.0 | Professional Output", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED UI SYSTEM (STREAMLIT SIDE - ORIGINAL V37) ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #ef4444; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    [data-testid="stSidebar"] h1 { 
        background: linear-gradient(90deg, #0f172a, #ef4444);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important; font-size: 1.8rem !important;
    }
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

# --- 3. SIDEBAR: THE CONTROL CENTER (ORIGINAL V37) ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v41.0 | Professional Engine")
    st.divider()
    
    # --- AI GENERATOR ---
    with st.expander("🤖 Titan AI Generator", expanded=False):
        raw_key = st.text_input("Groq API Key", type="password")
        groq_key = raw_key.strip() if raw_key else ""
        biz_desc = st.text_input("Business Description")
        
        if st.button("✨ Generate Copy"):
            if not groq_key or not biz_desc:
                st.error("Key & Description required.")
            else:
                try:
                    with st.spinner("Writing..."):
                        url = "https://api.groq.com/openai/v1/chat/completions"
                        headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                        prompt = f"Act as a copywriter. Return JSON for '{biz_desc}': hero_h, hero_sub, about_h, about_short, feat_data (icon|Title|Desc format)."
                        data = {"messages": [{"role": "user", "content": prompt}], "model": "llama-3.1-8b-instant", "response_format": {"type": "json_object"}}
                        resp = requests.post(url, headers=headers, json=data)
                        if resp.status_code == 200:
                            res = resp.json()['choices'][0]['message']['content']
                            parsed = json.loads(res)
                            if 'hero_h' in parsed: st.session_state.hero_h = str(parsed['hero_h'])
                            if 'hero_sub' in parsed: st.session_state.hero_sub = str(parsed['hero_sub'])
                            if 'about_h' in parsed: st.session_state.about_h = str(parsed['about_h'])
                            if 'about_short' in parsed: st.session_state.about_short = str(parsed['about_short'])
                            if 'feat_data' in parsed:
                                if isinstance(parsed['feat_data'], list): st.session_state.feat_data = "\n".join(map(str, parsed['feat_data']))
                                else: st.session_state.feat_data = str(parsed['feat_data'])
                            st.success("Generated!")
                            st.rerun()
                except Exception as e: st.error(f"Error: {e}")

    # 3.1 VISUAL DNA
    with st.expander("🎨 Design Studio", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Modern Glass (Light)", "Midnight Glass (Dark)", "Neo-Brutalism", "Luxury Gold", "Forest Eco", "Ocean Breeze", "Stark Minimalist"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#0F172A") 
        s_color = c2.color_picker("Action (CTA)", "#EF4444")  
        
        st.markdown("**Layout & Physics**")
        hero_layout = st.selectbox("Hero Alignment", ["Center", "Left"])
        btn_style = st.selectbox("Button Style", ["Rounded (Default)", "Sharp (Square)", "Pill (Full Round)"])
        border_rad = "8px"
        if btn_style == "Sharp (Square)": border_rad = "0px"
        elif btn_style == "Pill (Full Round)": border_rad = "50px"
        
        anim_type = st.selectbox("Animation Style", ["Fade Up", "Zoom In", "Slide Right", "None"])
        h_font = st.selectbox("Headings Font", ["Outfit", "Space Grotesk", "Playfair Display", "Oswald", "Clash Display"])
        b_font = st.selectbox("Body Font", ["Plus Jakarta Sans", "Inter", "Roboto", "Satoshi", "Lora"])

    # 3.2 MODULE MANAGER
    with st.expander("🧩 Section Manager", expanded=False):
        show_hero = st.checkbox("Hero Section", value=True)
        show_stats = st.checkbox("Trust Stats", value=True)
        show_features = st.checkbox("Feature Grid", value=True)
        show_pricing = st.checkbox("Pricing Table", value=True)
        show_inventory = st.checkbox("Store/Inventory", value=True)
        show_blog = st.checkbox("Blog Engine", value=True)
        show_gallery = st.checkbox("About Section", value=True)
        show_testimonials = st.checkbox("Testimonials", value=True)
        show_faq = st.checkbox("F.A.Q.", value=True)
        show_cta = st.checkbox("Final CTA", value=True)
        show_booking = st.checkbox("Booking Engine", value=True)

    # 3.3 TECHNICAL
    with st.expander("⚙️ SEO & Analytics", expanded=False):
        seo_area = st.text_input("Service Area", "Global / Online")
        seo_kw = st.text_area("SEO Keywords", "web design, no monthly fees")
        gsc_tag = st.text_input("Google Verification ID")
        ga_tag = st.text_input("Google Analytics ID")
        og_image = st.text_input("Social Share Image URL")

# --- 4. MAIN WORKSPACE ---
st.title("🏗️ StopWebRent Site Builder v41.0")

tabs = st.tabs(["1. Identity & PWA", "2. Content Blocks", "3. Marketing Tools", "4. Pricing", "5. Store", "6. Booking", "7. Blog", "8. Legal"])

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
        seo_d = st.text_area("Meta Description", "Stop paying monthly fees for Wix.", height=100)
        logo_url = st.text_input("Logo URL (PNG/SVG)")

    st.subheader("📱 Progressive Web App (PWA)")
    pwa_short = st.text_input("App Short Name", biz_name[:12])
    pwa_desc = st.text_input("App Description", "Official App")
    pwa_icon = st.text_input("App Icon (512x512 PNG)", logo_url)
    
    st.subheader("🌍 Multi-Language")
    lang_sheet = st.text_input("Translation Sheet CSV URL")
    st.caption("IDs are: nav-home, nav-blog, hero-title, hero-sub, btn-explore, feature-title, etc.")
        
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
    st.subheader("Hero Carousel")
    hero_h = st.text_input("Hero Headline", key="hero_h")
    hero_sub = st.text_input("Hero Subtext", key="hero_sub")
    
    st.caption("Use EITHER Image Slides OR a Video Background")
    hero_video_id = st.text_input("YouTube Video ID (Background Override)", placeholder="e.g. dQw4w9WgXcQ")
    
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Slide 1", "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1600")
    hero_img_2 = hc2.text_input("Slide 2", "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=1600")
    hero_img_3 = hc3.text_input("Slide 3", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1600")
    
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
    st.subheader("📣 Marketing Suite")
    st.markdown("**1. Top Announcement Bar**")
    top_bar_enabled = st.checkbox("Enable Top Bar")
    top_bar_text = st.text_input("Promo Text", "🔥 50% OFF Launch Sale - Ends Soon!")
    top_bar_link = st.text_input("Promo Link", "#pricing")
    
    st.divider()
    st.markdown("**2. Lead Gen Popup**")
    popup_enabled = st.checkbox("Enable Popup")
    popup_delay = st.slider("Delay (seconds)", 1, 30, 5)
    popup_title = st.text_input("Popup Headline", "Wait! Don't leave empty handed.")
    popup_text = st.text_input("Popup Body", "Get our free pricing guide on WhatsApp.")
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
    st.subheader("🛒 Store & Payments")
    st.info("Col 1: Name, Col 2: Price, Col 3: Desc, Col 4: Img1|Img2, Col 5: StripeLink")
    sheet_url = st.text_input("Store CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Default Product Img", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=1600")
    col_pay1, col_pay2 = st.columns(2)
    paypal_link = col_pay1.text_input("PayPal Link", "https://paypal.me/yourid")
    upi_id = col_pay2.text_input("UPI ID", "name@upi")

with tabs[5]:
    st.subheader("📅 Booking Engine")
    booking_embed = st.text_area("Embed Code", height=150, value='<!-- Calendly inline widget begin -->\n<div class="calendly-inline-widget" data-url="https://calendly.com/titan-demo/30min" style="min-width:320px;height:630px;"></div>\n<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>\n<!-- Calendly inline widget end -->')
    booking_title = st.text_input("Booking Title", "Book an Appointment")
    booking_desc = st.text_input("Booking Subtext", "Select a time slot.")

with tabs[6]:
    st.subheader("📰 Blog")
    blog_sheet_url = st.text_input("Blog CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    blog_hero_title = st.text_input("Blog Title", "Latest Insights")
    blog_hero_sub = st.text_input("Blog Subtext", "Thoughts on tech.")

with tabs[7]:
    st.subheader("Legal")
    testi_data = st.text_area("Testimonials", "Rajesh Gupta | Titan stopped the bleeding.\nSarah Jenkins | Easy updates.", height=100)
    faq_data = st.text_area("FAQ", "Do I pay $0? ? Yes.\nIs it secure? ? Yes.", height=100)
    priv_txt = st.text_area("Privacy", "We collect minimum data.", height=100)
    term_txt = st.text_area("Terms", "You own the code.", height=100)

# ==========================================
# 4. COMPILER ENGINE (ULTRA MODERN PROFESSIONAL UI)
# ==========================================

def format_text(text):
    if not text: return ""
    processed_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    lines = processed_text.split('\n')
    html_out = ""
    in_list = False
    for line in lines:
        clean_line = line.strip()
        if not clean_line: continue
        if clean_line.startswith("* "):
            if not in_list: html_out += '<ul style="margin-bottom:1rem; padding-left:1.5rem;">'; in_list = True
            content = clean_line[2:] 
            html_out += f'<li style="margin-bottom:0.5rem; opacity:0.9; color:inherit;">{content}</li>'
        else:
            if in_list: html_out += "</ul>"; in_list = False
            html_out += f"<p style='margin-bottom:1rem; opacity:0.9; color:inherit;'>{clean_line}</p>"
    if in_list: html_out += "</ul>"
    return html_out

def gen_schema():
    schema = {
        "@context": "https://schema.org", "@type": "LocalBusiness",
        "name": biz_name, "image": logo_url or hero_img_1,
        "telephone": biz_phone, "email": biz_email, "url": prod_url, "description": seo_d
    }
    return f'<script type="application/ld+json">{json.dumps(schema)}</script>'

def gen_pwa_manifest():
    return json.dumps({
        "name": biz_name, "short_name": pwa_short, "start_url": "./index.html",
        "display": "standalone", "background_color": "#ffffff", "theme_color": p_color,
        "description": pwa_desc, "icons": [{"src": pwa_icon, "sizes": "512x512", "type": "image/png"}]
    })

def gen_sw():
    return """
    self.addEventListener('install', (e) => { e.waitUntil(caches.open('titan-store').then((cache) => cache.addAll(['./index.html']))); });
    self.addEventListener('fetch', (e) => { e.respondWith(caches.match(e.request).then((response) => response || fetch(e.request))); });
    """

def get_theme_css():
    # --- ULTRA MODERN PALETTE & VARS ---
    bg_color, text_color, card_bg = "#F8FAFC", "#0F172A", "rgba(255, 255, 255, 0.7)"
    nav_bg, border_color = "rgba(255, 255, 255, 0.8)", "rgba(255, 255, 255, 0.5)"
    
    if "Midnight" in theme_mode: 
        bg_color, text_color, card_bg = "#0B0F19", "#F1F5F9", "rgba(30, 41, 59, 0.6)"
        nav_bg, border_color = "rgba(15, 23, 42, 0.8)", "rgba(255, 255, 255, 0.1)"
    
    hero_align = "justify-content: center; text-align: center;"
    if hero_layout == "Left": hero_align = "justify-content: flex-start; text-align: left;"
    
    anim_css = ".reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease-out; } .reveal.active { opacity: 1; transform: translateY(0); }"
    if anim_type == "Zoom In":
        anim_css = ".reveal { opacity: 0; transform: scale(0.95); transition: all 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); } .reveal.active { opacity: 1; transform: scale(1); }"
    elif anim_type == "None":
        anim_css = ".reveal { opacity: 1; }"

    return f"""
    :root {{
        --p: {p_color}; --s: {s_color};
        --bg: {bg_color}; --txt: {text_color};
        --card-bg: {card_bg}; --nav-bg: {nav_bg};
        --border: {border_color};
        --radius: {border_rad};
        --glass: blur(16px) saturate(180%);
        --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        --font-h: '{h_font}', sans-serif;
        --font-b: '{b_font}', sans-serif;
    }}
    * {{ box-sizing: border-box; outline: none; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--font-b); margin: 0; line-height: 1.6; overflow-x: hidden; }}
    
    h1, h2, h3, h4 {{ font-family: var(--font-h); color: var(--txt); line-height: 1.1; margin-bottom: 1rem; }}
    h1 {{ font-size: clamp(3rem, 6vw, 5rem); font-weight: 800; }}
    .gradient-text {{ background: linear-gradient(135deg, var(--p) 0%, var(--s) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}

    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
    
    .btn {{
        display: inline-flex; align-items: center; justify-content: center;
        padding: 1rem 2rem; border-radius: var(--radius); font-weight: 600;
        text-decoration: none; transition: all 0.3s ease; cursor: pointer;
        border: none; font-size: 1rem; gap: 0.5rem; text-align: center;
    }}
    .btn-primary {{ background: linear-gradient(135deg, var(--p), var(--s)); color: white !important; box-shadow: 0 10px 20px -5px var(--p); }}
    .btn-primary:hover {{ transform: translateY(-3px); filter: brightness(1.1); }}
    .btn-accent {{ background: var(--s); color: white !important; }}
    .btn-outline {{ background: transparent; border: 1px solid var(--border); color: var(--txt) !important; }}
    .btn-outline:hover {{ border-color: var(--p); color: var(--p) !important; background: rgba(255,255,255,0.05); }}

    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; background: var(--nav-bg); backdrop-filter: var(--glass); -webkit-backdrop-filter: var(--glass); border-bottom: 1px solid var(--border); padding: 1rem 0; }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; gap: 2rem; align-items: center; }}
    .nav-links a {{ text-decoration: none; font-weight: 500; color: var(--txt); opacity: 0.8; transition: 0.2s; }}
    .nav-links a:hover {{ opacity: 1; color: var(--p); }}
    
    #top-bar {{ background: var(--s); color: white; text-align: center; padding: 10px; font-weight: bold; font-size: 0.9rem; }}
    #top-bar a {{ color: white; text-decoration: underline; }}

    .hero {{ position: relative; min-height: 100vh; display: flex; align-items: center; {hero_align} overflow: hidden; padding-top: 80px; }}
    .hero-bg {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; }}
    .hero-overlay {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0.3), var(--bg)); z-index: 0; }}
    .hero-content {{ z-index: 2; position: relative; max-width: 900px; animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1); }}
    .hero h1 {{ color: white !important; text-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
    .hero p {{ color: rgba(255,255,255,0.9); font-size: 1.25rem; margin-bottom: 2.5rem; max-width: 600px; { "margin-left: auto; margin-right: auto;" if hero_layout == "Center" else "" } }}

    .card {{ background: var(--card-bg); backdrop-filter: blur(12px); border: 1px solid var(--border); border-radius: var(--radius); padding: 2rem; display: flex; flex-direction: column; height: 100%; }}
    
    .prod-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; position: relative; transition: 0.3s; }}
    .prod-card:hover {{ transform: translateY(-5px); box-shadow: var(--shadow-lg); }}
    .prod-img-wrap {{ position: relative; padding-top: 100%; overflow: hidden; }}
    .prod-img {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s; }}
    .prod-card:hover .prod-img {{ transform: scale(1.08); }}
    .prod-info {{ padding: 1.5rem; }}
    .prod-price {{ font-size: 1.2rem; font-weight: 800; color: var(--p); }}
    
    /* DUAL ACTION BUTTONS */
    .prod-actions {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-top: 1rem; opacity: 0; transform: translateY(10px); transition: 0.3s; }}
    .prod-card:hover .prod-actions {{ opacity: 1; transform: translateY(0); }}
    .btn-sm {{ padding: 0.6rem 1rem; font-size: 0.85rem; border-radius: 8px; text-align: center; }}

    section {{ padding: clamp(4rem, 8vw, 6rem) 0; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; }}
    
    /* FAQ & Testimonials */
    details {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; margin-bottom: 1rem; padding: 1.5rem; cursor: pointer; }}
    details summary {{ font-weight: bold; font-size: 1.1rem; }}
    
    /* Blog Badge */
    .blog-badge {{ background: var(--s); color: white; padding: 0.3rem 0.8rem; border-radius: 50px; font-size: 0.75rem; text-transform: uppercase; font-weight: bold; display:inline-block; margin-bottom: 0.5rem; }}

    {anim_css}
    
    .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); backdrop-filter: blur(8px); }}
    .modal-content {{ background: var(--bg); border: 1px solid var(--border); margin: 10vh auto; padding: 2.5rem; width: 90%; max-width: 450px; border-radius: 24px; position: relative; animation: slideUp 0.3s; }}
    
    /* SOCIAL SHARE */
    .share-row {{ display: flex; gap: 10px; margin-top: 20px; flex-wrap: wrap; }}
    .share-btn {{ width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 50%; color: white; transition: 0.3s; border: none; cursor: pointer; text-decoration: none; }}
    .share-btn:hover {{ transform: translateY(-3px); filter: brightness(1.1); }}
    .share-btn svg {{ width: 20px; height: 20px; fill: white; }}
    .bg-fb {{ background: #1877F2; }} .bg-x {{ background: #000000; }} .bg-li {{ background: #0A66C2; }} .bg-wa {{ background: #25D366; }} .bg-rd {{ background: #FF4500; }}

    footer {{ background: #0f172a; color: white; padding: 5rem 0; }}
    @keyframes fadeInUp {{ from {{ opacity:0; transform:translateY(40px); }} to {{ opacity:1; transform:translateY(0); }} }}
    @keyframes slideUp {{ from {{ opacity:0; transform:translateY(20px); }} to {{ opacity:1; transform:translateY(0); }} }}

    @media (max-width: 768px) {{
        .nav-links {{ position: fixed; top: 70px; left: -100%; width: 100%; height: calc(100vh - 70px); background: var(--bg); flex-direction: column; padding: 2rem; transition: 0.3s; align-items: flex-start; border-top: 1px solid var(--border); }}
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
    lang_btn = f'<button onclick="openModal(\'langModal\')" class="btn-outline" style="padding: 0.5rem 1rem; border-radius: 50px;">Lang</button>' if lang_sheet else ''

    return f"""
    {f'<div id="top-bar"><a href="{top_bar_link}">{top_bar_text}</a></div>' if top_bar_enabled else ''}
    <nav><div class="container nav-flex">
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
    </div></nav>
    <div id="langModal" class="modal"><div class="modal-content">
        <span onclick="closeModal('langModal')" style="position:absolute; right:20px; top:15px; font-size:1.5rem; cursor:pointer;">&times;</span>
        <h3 class="gradient-text">Select Language</h3>
        <button onclick="toggleLang()" class="btn btn-outline" style="width:100%;">Switch Language</button>
    </div></div>
    <script>
        function toggleMenu() {{ document.querySelector('.nav-links').classList.remove('active'); }}
        function openModal(id) {{ document.getElementById(id).style.display = 'block'; }}
        function closeModal(id) {{ document.getElementById(id).style.display = 'none'; }}
    </script>
    """

def gen_hero():
    bg_html = f"""<div class="hero-bg"><div class="carousel-slide active" style="background-image: url('{hero_img_1}'); background-size: cover; background-position: center; position:absolute; width:100%; height:100%; transition: opacity 1.5s;"></div></div>"""
    if hero_video_id: bg_html = f"""<div class="hero-bg"><iframe src="https://www.youtube.com/embed/{hero_video_id}?autoplay=1&mute=1&loop=1&playlist={hero_video_id}&controls=0&showinfo=0&rel=0" style="width:100vw; height:100vh; object-fit:cover; pointer-events:none;" frameborder="0"></iframe></div>"""
    return f"""<section class="hero"><div class="hero-overlay"></div>{bg_html}<div class="container hero-content"><h1>{hero_h}</h1><p>{hero_sub}</p><div style="display:flex; gap:1rem; flex-wrap:wrap; {'justify-content:center;' if hero_layout == 'Center' else ''}"><a href="#inventory" class="btn btn-primary">Explore Now</a><a href="contact.html" class="btn btn-outline" style="color:white !important;">Contact</a></div></div></section>"""

def get_simple_icon(name):
    d = "M12 2L2 7l10 5 10-5-10-5zm0 9l2.5-1.25L12 8.5l-2.5 1.25L12 11zm0 2.5l-5-2.5-5 2.5L12 22l10-8.5-5-2.5-5 2.5z"
    if "bolt" in name: d="M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"
    return f'<svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="{d}"/></svg>'

def gen_features():
    cards = ""
    lines = [x for x in feat_data_input.split('\n') if x.strip()]
    for line in lines:
        parts = line.split('|')
        if len(parts) >= 3:
            icon = f'<div style="color:var(--p); margin-bottom:1.5rem; background:rgba(255,255,255,0.05); width:60px; height:60px; display:flex; align-items:center; justify-content:center; border-radius:16px;">{get_simple_icon(parts[0])}</div>'
            cards += f"""<div class="card reveal">{icon}<h3>{parts[1].strip()}</h3><div style="opacity:0.8;">{format_text(parts[2].strip())}</div></div>"""
    return f"""<section id="features"><div class="container"><div class="section-head reveal"><h2 class="gradient-text">{f_title}</h2></div><div class="grid-3">{cards}</div></div></section>"""

def gen_inventory():
    if not show_inventory: return ""
    return f"""
    <section id="inventory" style="background:var(--bg);"><div class="container">
        <div class="section-head reveal"><h2 class="gradient-text">Featured Collection</h2></div>
        <div id="inv-grid" class="grid-3"><div>Loading Products...</div></div>
    </div></section>
    {gen_csv_parser()}
    <script>
    async function loadInv() {{
        const url = '{sheet_url}';
        const box = document.getElementById('inv-grid');
        if(!url) {{ box.innerHTML = `<div class="prod-card reveal"><div class="prod-img-wrap"><img src="{custom_feat}" class="prod-img"></div><div class="prod-info"><h3>Demo Product</h3><span class="prod-price">$99.00</span><br><br><button class="btn btn-primary btn-sm">Add</button></div></div>`; return; }}
        try {{
            const res = await fetch(url); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/);
            if(!box) return; box.innerHTML = '';
            for(let i=1; i<lines.length; i++) {{
                const row = parseCSVLine(lines[i]);
                if(row.length < 2) continue;
                let mainImg = (row[3] || '{custom_feat}').split('|')[0];
                let stripeLink = (row.length > 4 && row[4].includes('http')) ? row[4] : '';
                let btn = stripeLink ? `<a href="${{stripeLink}}" class="btn btn-primary btn-sm">Buy Now</a>` : `<button onclick="addToCart('${{row[0].replace(/'/g, "\\'")}}', '${{row[1].replace(/'/g, "\\'")}}')" class="btn btn-primary btn-sm">Add</button>`;
                
                box.innerHTML += `<div class="prod-card reveal"><div class="prod-img-wrap"><img src="${{mainImg}}" class="prod-img" loading="lazy"></div><div class="prod-info"><div style="display:flex; justify-content:space-between; align-items:start;"><h3 style="font-size:1.1rem; margin:0;">${{row[0]}}</h3><span class="prod-price">${{row[1]}}</span></div><div class="prod-actions"><a href="product.html?item=${{encodeURIComponent(row[0])}}" class="btn btn-outline btn-sm">Details</a>${{btn}}</div></div></div>`;
            }}
        }} catch(e) {{ console.log(e); }}
    }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);
    </script>
    """

def gen_cart_system():
    if not wa_num: return ""
    clean_wa = wa_num.replace("+", "").replace(" ", "").replace("-", "")
    return f"""
    <div id="cart-float" onclick="openModal('cartModal')" style="position:fixed; bottom:30px; right:30px; background:var(--bg); color:var(--txt); padding:12px 20px; border-radius:50px; box-shadow:var(--shadow-lg); cursor:pointer; z-index:998; display:flex; align-items:center; gap:10px; font-weight:bold; border:1px solid var(--border);">
        <span>🛒</span><span id="cart-count" style="background:var(--s); color:white; border-radius:50%; width:20px; height:20px; display:flex; align-items:center; justify-content:center; font-size:0.7rem;">0</span>
    </div>
    <div id="cartModal" class="modal"><div class="modal-content">
        <span onclick="closeModal('cartModal')" style="position:absolute; right:20px; top:20px; font-size:1.5rem; cursor:pointer;">&times;</span>
        <h3 class="gradient-text">Cart</h3>
        <div id="cart-items" style="max-height: 300px; overflow-y: auto; margin: 20px 0;"></div>
        <div style="border-top: 1px solid var(--border); padding-top: 15px; display:flex; justify-content:space-between; font-weight:bold;"><span>Total:</span> <span id="cart-total">0.00</span></div>
        <button class="btn btn-primary" style="width: 100%; margin-top: 20px;" onclick="checkoutWA()">Checkout via WhatsApp</button>
    </div></div>
    <script>
    let cart = [];
    function addToCart(name, price) {{ cart.push({{name: name, price: price}}); updateCart(); }}
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
    return f"""<a href="https://wa.me/{clean_wa}" target="_blank" style="position:fixed; bottom:100px; right:30px; background:#25D366; color:white; width:50px; height:50px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 25px rgba(37,211,102,0.4); z-index:9999;"><svg style="width:28px;height:28px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></path></svg></a>"""

def gen_scripts():
    return """<script>
    window.addEventListener('scroll', () => { var r = document.querySelectorAll('.reveal'); for (var i = 0; i < r.length; i++) { if (r[i].getBoundingClientRect().top < window.innerHeight - 80) r[i].classList.add('active'); } });
    window.dispatchEvent(new Event('scroll'));
    </script>"""

def gen_csv_parser():
    return """<script>
    function parseCSVLine(str) { const res = []; let cur = ''; let inQuote = false; for (let i = 0; i < str.length; i++) { const c = str[i]; if (c === '"') { if (inQuote && str[i+1] === '"') { cur += '"'; i++; } else { inQuote = !inQuote; } } else if (c === ',' && !inQuote) { res.push(cur.trim()); cur = ''; } else { cur += c; } } res.push(cur.trim()); return res; }
    function parseMarkdown(text) { if (!text) return ''; let html = text.replace(/\\r\\n/g, '\\n').replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>'); return html; }
    </script>"""

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
def gen_lang_script():
    if not lang_sheet: return ""
    return f"""<script>async function toggleLang() {{ try {{ const res=await fetch('{lang_sheet}'); const txt=await res.text(); const lines=txt.split(/\\r\\n|\\n/); for(let i=1;i<lines.length;i++){{ const r=parseCSVLine(lines[i]); if(r.length>1){{ const el=document.getElementById(r[0]); if(el) el.innerText=r[1]; }} }} closeModal('langModal'); }} catch(e){{ console.log(e); }} }}</script>"""
def gen_booking_content():
    return f"""<section class="hero" style="min-height:30vh; background:var(--p);"><div class="container"><h1>{booking_title}</h1><p>{booking_desc}</p></div></section><section><div class="container" style="text-align:center;"><div style="background:white; border-radius:12px; overflow:hidden; box-shadow:var(--shadow-lg); width:100%;">{booking_embed}</div></div></section>"""
def gen_popup():
    if not popup_enabled: return ""
    return f"""<div id="lead-popup" class="modal"><div class="modal-content" style="text-align:center;"><span onclick="closeModal('lead-popup')" style="position:absolute; right:15px; top:15px; cursor:pointer;">&times;</span><h3 class="gradient-text">{popup_title}</h3><p>{popup_text}</p><a href="{top_bar_link}" class="btn btn-primary">{popup_cta}</a></div></div><script>setTimeout(() => {{ if(!sessionStorage.getItem('pop')) {{ document.getElementById('lead-popup').style.display='block'; sessionStorage.setItem('pop','1'); }} }}, {popup_delay}000);</script>"""

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
                    box.innerHTML += `<div class="card reveal"><img src="${{r[5]}}" class="prod-img" style="border-radius:var(--radius)"><div><span class="blog-badge">${{r[3]}}</span><h3 style="margin-top:0.5rem;"><a href="post.html?id=${{r[0]}}" style="text-decoration:none;">${{r[1]}}</a></h3></div></div>`;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadBlog();
    </script>
    """

def gen_blog_post_html():
    return f"""
    <div id="post-container" style="padding-top:120px;">Loading...</div>
    {gen_csv_parser()}
    <script>
    async function loadPost() {{
        const params = new URLSearchParams(window.location.search);
        const slug = params.get('id');
        try {{
            const res = await fetch('{blog_sheet_url}'); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/);
            const container = document.getElementById('post-container');
            for(let i=1; i<lines.length; i++) {{
                const r = parseCSVLine(lines[i]);
                if(r[0] === slug) {{
                    const contentHtml = parseMarkdown(r[6]);
                    container.innerHTML = `<section class="hero" style="min-height:40vh; background:var(--p);"><div class="container"><h1>${{r[1]}}</h1></div></section><div class="container" style="padding:4rem 1rem; max-width:800px;"><img src="${{r[5]}}" style="width:100%; border-radius:var(--radius); margin-bottom:2rem;"><div style="line-height:1.8; opacity:0.9;">${{contentHtml}}</div><a href="blog.html" class="btn btn-outline" style="margin-top:2rem;">&larr; Back to Blog</a></div>`;
                    break;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadPost();
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
                    
                    let rawImgs = clean[3] || '{custom_feat}';
                    let imgs = rawImgs.split('|');
                    let mainImg = imgs[0];
                    let stripeLink = (clean.length > 4 && clean[4].includes('http')) ? clean[4] : '';
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
                    
                    let mainBtn = `<button onclick="addToCart('${{safeName}}', '${{safePrice}}')" class="btn btn-primary" style="flex:1;">Add to Cart</button>`;
                    if(stripeLink) mainBtn = `<a href="${{stripeLink}}" class="btn btn-primary" style="flex:1;">Buy Now</a>`;

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
                                    ${{mainBtn}}
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

def build_page(title, content, extra_js=""):
    pwa_tags = f'<link rel="manifest" href="manifest.json"><meta name="theme-color" content="{p_color}"><link rel="apple-touch-icon" href="{pwa_icon}">'
    sw_script = "<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('service-worker.js'); }</script>"
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title>{pwa_tags}{gen_schema()}<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@400;700;900&family={b_font.replace(' ', '+')}:wght@300;400;600;800&display=swap" rel="stylesheet"><style>{get_theme_css()}</style></head><body>{gen_nav()}{content}{f'<footer><div class="container" style="text-align:center;"><h2 style="color:white;">{biz_name}</h2><p>{biz_addr}</p><p>&copy; 2026 {biz_name}</p></div></footer>'}{gen_wa_widget()}{gen_cart_system()}{gen_scripts()}{gen_lang_script()}{sw_script}{gen_popup()}{extra_js}</body></html>"""

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

st.success("System Ready.")

# ZIP GENERATION
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
