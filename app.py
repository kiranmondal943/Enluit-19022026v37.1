import streamlit as st
import zipfile
import io
import json
import re
import requests

# --- 0. STATE MANAGEMENT ---
def init_state(key, default_val):
    if key not in st.session_state:
        st.session_state[key] = default_val

init_state('hero_h', "Stop Paying Rent for Your Website.")
init_state('hero_sub', "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees. Pay once. Own it forever.")
init_state('about_h', "Control Your Empire")
init_state('about_short', "No WordPress dashboard. No plugins to update. Just open your private Google Sheet, change a text, and watch your site update globally in seconds.")
init_state('feat_data', "bolt | The Performance Pillar | **0.1s High-Velocity Loading**. While traditional sites take 3–5s, Titan loads instantly.\nwallet | The Economic Pillar | **$0 Monthly Fees**. We eliminated hosting subscriptions.\ntable | The Functional Pillar | **Google Sheets CMS**. Update prices and photos directly from a simple spreadsheet.\nshield | The Authority Pillar | **Unhackable Security**. Zero-DB Architecture removes the hacker's primary entry point.\nlayers | The Reliability Pillar | **Global Edge Deployment**. Distributed across 100+ servers worldwide.\nstar | The Conversion Pillar | **One-Tap WhatsApp**. Direct-to-Chat technology.")

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan Architect", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# --- 2. INPUTS: SIDEBAR & TABS ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v41.0 | Visual Engine Rewrite")
    st.divider()
    
    # --- AI GENERATOR ---
    with st.expander("🤖 AI Copywriter", expanded=False):
        raw_key = st.text_input("Groq API Key", type="password")
        groq_key = raw_key.strip() if raw_key else ""
        biz_desc = st.text_input("Business Description")
        
        if st.button("✨ Auto-Generate"):
            if not groq_key or not biz_desc:
                st.error("Key & Description required.")
            else:
                try:
                    with st.spinner("Designing Experience..."):
                        url = "https://api.groq.com/openai/v1/chat/completions"
                        headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                        prompt = f"Act as a web copywriter. Return JSON for '{biz_desc}': hero_h, hero_sub, about_h, about_short, feat_data (icon|Title|Desc format)."
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

    with st.expander("🎨 Visual Identity", expanded=True):
        theme_mode = st.selectbox("Aesthetic", ["Midnight SaaS (Dark)", "Clean Corporate (Light)", "Glassmorphism (Blur)", "Cyberpunk Neon", "Luxury Gold"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Brand Color", "#3B82F6") 
        s_color = c2.color_picker("Accent Color", "#10B981")  
        
        st.markdown("**Typography & Layout**")
        hero_layout = st.selectbox("Hero Style", ["Center", "Left Split", "Minimal"])
        btn_style = st.selectbox("Button Shape", ["Pill (Rounded)", "Sharp (Square)", "Soft (Default)"])
        h_font = st.selectbox("Heading Font", ["Space Grotesk", "Inter", "Playfair Display", "Outfit", "Clash Display"])
        b_font = st.selectbox("Body Font", ["Inter", "Open Sans", "DM Sans", "Satoshi"])

    with st.expander("🧩 Component Stack", expanded=False):
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

    with st.expander("⚙️ SEO & Analytics", expanded=False):
        seo_area = st.text_input("Service Area", "Global")
        seo_kw = st.text_area("SEO Keywords", "web design, static site")
        gsc_tag = st.text_input("Google ID")
        og_image = st.text_input("Social Share Image")

st.title("🏗️ StopWebRent Builder")
tabs = st.tabs(["1. Core Identity", "2. Content Layers", "3. Growth Tools", "4. Economics", "5. Commerce", "6. Content", "7. Booking", "8. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Brand Name", "StopWebRent.com")
        biz_phone = st.text_input("Phone Channel", "966572562151")
        biz_email = st.text_input("Support Email", "hello@kaydiemscriptlab.com")
    with c2:
        prod_url = st.text_input("Production URL", "https://www.stopwebrent.com")
        biz_addr = st.text_area("Physical HQ", "Kaydiem Script Lab\nKolkata, India", height=100)
        map_iframe = st.text_area("Map Embed", placeholder='<iframe src="..."></iframe>', height=100)
        seo_d = st.text_area("Meta Description", "Stop paying monthly fees.", height=100)
        logo_url = st.text_input("Logo Asset (URL)")

    st.subheader("📱 PWA Configuration")
    pwa_short = st.text_input("App Short Name", biz_name[:12])
    pwa_icon = st.text_input("App Icon (512x512)", logo_url)
    lang_sheet = st.text_input("i18n Sheet URL", help="Col 1: ElementID, Col 2: Text")
        
    st.subheader("Social Grid")
    sc1, sc2, sc3 = st.columns(3)
    fb_link = sc1.text_input("Facebook")
    ig_link = sc2.text_input("Instagram")
    x_link = sc3.text_input("X (Twitter)")
    sc4, sc5, sc6 = st.columns(3)
    li_link = sc4.text_input("LinkedIn")
    yt_link = sc5.text_input("YouTube")
    wa_num = sc6.text_input("WhatsApp (No +)", "966572562151")

with tabs[1]:
    st.subheader("Hero Architecture")
    hero_h = st.text_input("Headline", key="hero_h")
    hero_sub = st.text_input("Sub-Headline", key="hero_sub")
    hero_video_id = st.text_input("Background Video ID (YouTube)", placeholder="e.g. dQw4w9WgXcQ")
    
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Visual 1", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    hero_img_2 = hc2.text_input("Visual 2", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1600")
    hero_img_3 = hc3.text_input("Visual 3", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1600")
    
    st.divider()
    st.subheader("Data Visualization")
    col_s1, col_s2, col_s3 = st.columns(3)
    stat_1 = col_s1.text_input("Metric 1", "0.1s")
    label_1 = col_s1.text_input("Label 1", "Speed")
    stat_2 = col_s2.text_input("Metric 2", "$0")
    label_2 = col_s2.text_input("Label 2", "Fees")
    stat_3 = col_s3.text_input("Metric 3", "100%")
    label_3 = col_s3.text_input("Label 3", "Ownership")

    f_title = st.text_input("Grid Title", "Value Pillars")
    feat_data_input = st.text_area("Feature Data (Icon|Title|Desc)", key="feat_data", height=150)
    
    st.subheader("Narrative")
    about_h_in = st.text_input("About Header", key="about_h")
    about_img = st.text_input("About Visual", "https://images.unsplash.com/photo-1543286386-713df548e9cc?q=80&w=1600")
    about_short_in = st.text_area("Summary", key="about_short", height=100)
    about_long = st.text_area("Full Story", "The Digital Landlord Trap...", height=200)

with tabs[2]:
    st.subheader("📣 Conversion Tools")
    top_bar_enabled = st.checkbox("Sticky Promo Bar")
    top_bar_text = st.text_input("Bar Text", "🔥 50% OFF Launch Sale")
    top_bar_link = st.text_input("Bar Link", "#pricing")
    
    st.divider()
    popup_enabled = st.checkbox("Exit Intent Popup")
    popup_delay = st.slider("Trigger Delay (s)", 1, 30, 5)
    popup_title = st.text_input("Popup Header", "Wait!")
    popup_text = st.text_input("Popup Body", "Get free guide.")
    popup_cta = st.text_input("Popup CTA", "Get it Now")

with tabs[3]:
    st.subheader("💰 Pricing Strategy")
    col_p1, col_p2, col_p3 = st.columns(3)
    titan_price = col_p1.text_input("Your Price", "$199")
    titan_mo = col_p1.text_input("Your Monthly", "$0")
    wix_name = col_p2.text_input("Competitor Name", "Wix")
    wix_mo = col_p2.text_input("Comp. Monthly", "$29/mo")
    save_val = col_p3.text_input("Total Savings", "$1,466")

with tabs[4]:
    st.subheader("🛒 Commerce Engine")
    st.info("Format: Name, Price, Desc, ImageURL|ImageURL2")
    sheet_url = st.text_input("Google Sheet CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Fallback Image", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")

with tabs[5]:
    st.subheader("📰 CMS (Blog)")
    blog_sheet_url = st.text_input("Blog CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    blog_hero_title = st.text_input("Blog Header", "Latest Insights")
    blog_hero_sub = st.text_input("Blog Sub", "Thoughts on tech.")

with tabs[6]:
    st.subheader("📅 Scheduling")
    booking_embed = st.text_area("Widget Code", height=150, value='<!-- Calendly -->')
    booking_title = st.text_input("Page Title", "Book an Appointment")
    booking_desc = st.text_input("Page Sub", "Select a time slot.")

with tabs[7]:
    st.subheader("Legal & Trust")
    testi_data = st.text_area("Social Proof", "Rajesh Gupta | Titan stopped the bleeding.", height=100)
    faq_data = st.text_area("F.A.Q. Data", "Do I pay $0? ? Yes.", height=100)
    priv_txt = st.text_area("Privacy Policy", "We collect minimum data.", height=100)
    term_txt = st.text_area("Terms of Service", "You own the code.", height=100)

# ==========================================
# 4. COMPILER ENGINE (ULTRA MODERN CSS FOR GENERATED SITE)
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
    # --- MODERN COLOR PALETTES ---
    bg_color, text_color, card_bg, nav_bg, nav_text = "#ffffff", "#0f172a", "#ffffff", "rgba(255, 255, 255, 0.7)", "#0f172a"
    hero_overlay = "rgba(0,0,0,0.5)"
    
    if "Midnight" in theme_mode:
        bg_color, text_color, card_bg, nav_bg, nav_text = "#030712", "#F9FAFB", "#111827", "rgba(3, 7, 18, 0.7)", "#ffffff"
        hero_overlay = "linear-gradient(180deg, rgba(3,7,18,0.7) 0%, rgba(3,7,18,1) 100%)"
    elif "Glass" in theme_mode:
        bg_color, text_color, card_bg, nav_bg, nav_text = "#f0f2f5", "#1f2937", "rgba(255,255,255,0.6)", "rgba(255, 255, 255, 0.3)", "#1f2937"
    elif "Cyberpunk" in theme_mode:
        bg_color, text_color, card_bg, nav_bg, nav_text = "#000000", "#e2e8f0", "#0f0f0f", "rgba(0, 0, 0, 0.8)", "#e2e8f0"

    btn_rad = "10px"
    if btn_style == "Pill (Rounded)": btn_rad = "50px"
    elif btn_style == "Sharp (Square)": btn_rad = "0px"

    hero_align = "text-align: center; justify-content: center; align-items: center;"
    if hero_layout == "Left Split": hero_align = "text-align: left; justify-content: flex-start; align-items: center;"

    # CSS MESH GRADIENTS & BENTO GRIDS
    return f"""
    :root {{
        --primary: {p_color};
        --accent: {s_color};
        --bg: {bg_color};
        --text: {text_color};
        --card-bg: {card_bg};
        --radius: {btn_rad};
        --nav-bg: {nav_bg};
        --nav-text: {nav_text};
        --font-head: '{h_font}', sans-serif;
        --font-body: '{b_font}', sans-serif;
    }}
    
    * {{ box-sizing: border-box; margin: 0; padding: 0; outline: none; }}
    
    html {{ 
        font-size: 16px; scroll-behavior: smooth; 
        -webkit-font-smoothing: antialiased; 
    }}
    
    body {{ 
        background-color: var(--bg); 
        color: var(--text); 
        font-family: var(--font-body); 
        line-height: 1.6; 
        overflow-x: hidden;
    }}

    /* TYPOGRAPHY */
    h1, h2, h3, h4 {{ font-family: var(--font-head); font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; }}
    h1 {{ font-size: clamp(3rem, 8vw, 5.5rem); }}
    h2 {{ font-size: clamp(2.2rem, 5vw, 3.5rem); margin-bottom: 1.5rem; }}
    h3 {{ font-size: 1.4rem; font-weight: 600; margin-bottom: 0.5rem; }}
    p {{ margin-bottom: 1.5rem; font-size: 1.125rem; opacity: 0.85; max-width: 65ch; }}

    /* UTILS */
    .container {{ width: 92%; max-width: 1280px; margin: 0 auto; position: relative; z-index: 2; }}
    .reveal {{ opacity: 0; transform: translateY(40px); transition: all 1s cubic-bezier(0.16, 1, 0.3, 1); }}
    .reveal.active {{ opacity: 1; transform: translateY(0); }}
    
    /* GLASSMORPHISM NAVIGATION */
    nav {{ 
        position: fixed; top: 0; width: 100%; z-index: 1000; 
        background: var(--nav-bg); 
        backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255,255,255,0.05); padding: 1.2rem 0; 
        transition: all 0.3s ease; 
    }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; gap: 2rem; align-items: center; }}
    .nav-links a {{ 
        text-decoration: none; color: var(--nav-text); font-weight: 500; font-size: 0.95rem; 
        position: relative; transition: 0.2s; opacity: 0.8;
    }}
    .nav-links a:hover {{ opacity: 1; color: var(--primary); }}
    
    /* HERO SECTION */
    .hero {{ 
        position: relative; min-height: 100vh; display: flex; {hero_align} 
        background: #000; overflow: hidden; padding-top: 80px; 
    }}
    .hero-overlay {{ 
        position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
        background: {hero_overlay}; z-index: 1; pointer-events: none;
    }}
    .hero-content {{ 
        position: relative; z-index: 2; color: white; width: 100%; 
        animation: heroFade 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards; 
    }}
    @keyframes heroFade {{ from {{ opacity: 0; transform: translateY(60px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    
    .hero h1 {{ 
        background: linear-gradient(180deg, #fff 0%, rgba(255,255,255,0.7) 100%); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
        margin-bottom: 1.5rem; 
        text-shadow: 0 0 50px rgba(255,255,255,0.2);
    }}
    .hero p {{ color: rgba(255,255,255,0.8); font-size: 1.35rem; font-weight: 300; margin-bottom: 2.5rem; }}
    
    /* CAROUSEL BACKGROUND */
    .carousel-slide {{ 
        position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
        background-size: cover; background-position: center; opacity: 0; 
        transition: opacity 1.5s ease-in-out, transform 8s ease; 
        transform: scale(1.1);
    }}
    .carousel-slide.active {{ opacity: 1; transform: scale(1); }}

    /* BENTO GRIDS & MODERN CARDS */
    .grid-3 {{ 
        display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); 
        gap: 2rem; margin-top: 2rem; 
    }}
    .card {{ 
        background: var(--card-bg); padding: 2.5rem; border-radius: 24px;
        border: 1px solid rgba(128,128,128,0.1); 
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s ease;
        display: flex; flex-direction: column; justify-content: flex-start;
    }}
    .card:hover {{ 
        transform: translateY(-8px) scale(1.01); 
        box-shadow: 0 20px 40px -5px rgba(0,0,0,0.1); 
        border-color: var(--primary); 
    }}
    .icon-box {{
        width: 56px; height: 56px; border-radius: 16px; background: rgba(59, 130, 246, 0.1);
        display: flex; align-items: center; justify-content: center; color: var(--primary);
        margin-bottom: 1.5rem;
    }}
    
    /* MODERN BUTTONS */
    .btn {{ 
        padding: 1rem 2.2rem; border-radius: var(--radius); font-weight: 600; 
        text-decoration: none; display: inline-flex; align-items: center; justify-content: center;
        transition: all 0.3s; cursor: pointer; border: none; font-size: 1.05rem; letter-spacing: -0.01em;
    }}
    .btn-primary {{ 
        background: var(--primary); color: white; 
        background-image: linear-gradient(to bottom right, rgba(255,255,255,0.2), rgba(0,0,0,0));
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3); border: 1px solid rgba(255,255,255,0.1);
    }}
    .btn-accent {{ 
        background: var(--accent); color: white;
        background-image: linear-gradient(to bottom right, rgba(255,255,255,0.2), rgba(0,0,0,0));
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }}
    .btn:hover {{ transform: translateY(-2px); filter: brightness(1.1); box-shadow: 0 8px 20px rgba(0,0,0,0.2); }}

    /* SECTION SPACING */
    section {{ padding: clamp(5rem, 10vw, 8rem) 0; }}
    
    /* FOOTER */
    footer {{ background: #030712; color: white; padding: 6rem 0 3rem; margin-top: auto; border-top: 1px solid rgba(255,255,255,0.08); }}
    footer a {{ color: #9ca3af; transition: 0.2s; }}
    footer a:hover {{ color: white; }}

    /* RESPONSIVE */
    @media (max-width: 768px) {{
        .nav-links {{ 
            position: fixed; top: 0; right: -100%; width: 85%; height: 100vh; 
            background: var(--bg); flex-direction: column; padding: 6rem 2rem; 
            box-shadow: -10px 0 30px rgba(0,0,0,0.2); transition: right 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            border-left: 1px solid rgba(128,128,128,0.1); justify-content: flex-start; align-items: flex-start;
        }}
        .nav-links.active {{ right: 0; }}
        .nav-links a {{ font-size: 1.5rem; color: var(--text); }}
        .hero {{ text-align: center; justify-content: center; }}
        .hero h1 {{ font-size: 3rem; }}
        .mobile-menu {{ display: block !important; font-size: 1.8rem; cursor: pointer; color: var(--nav-text); }}
        .grid-3 {{ grid-template-columns: 1fr; }}
    }}
    .mobile-menu {{ display: none; }}
    """

def gen_nav():
    logo = f'<img src="{logo_url}" height="36" alt="{biz_name}">' if logo_url else f'<span style="font-weight:800;font-size:1.5rem;letter-spacing:-0.5px;">{biz_name}</span>'
    blog_link = '<a href="blog.html">Insights</a>' if show_blog else ''
    return f"""
    {f'<div id="top-bar" style="background:var(--accent);color:white;text-align:center;padding:12px;font-weight:600;font-size:0.9rem;position:fixed;top:0;width:100%;z-index:2000;"><a href="{top_bar_link}" style="color:white;text-decoration:none">{top_bar_text}</a></div>' if top_bar_enabled else ''}
    <nav><div class="container nav-flex">
        <a href="index.html" style="text-decoration:none; color:var(--text);">{logo}</a>
        <div class="mobile-menu" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</div>
        <div class="nav-links">
            <span class="mobile-menu" onclick="document.querySelector('.nav-links').classList.remove('active')" style="position:absolute;top:20px;right:20px;">✕</span>
            <a href="index.html">Home</a>
            <a href="index.html#features">Features</a>
            <a href="index.html#pricing">Pricing</a>
            <a href="index.html#inventory">Store</a>
            {blog_link}
            <a href="contact.html">Contact</a>
            <a href="tel:{biz_phone}" class="btn-primary" style="padding:0.6rem 1.4rem; border-radius:50px; color:white !important;">Call Now</a>
        </div>
    </div></nav>
    <script>if({str(top_bar_enabled).lower()}) document.querySelector('nav').style.top = '45px';</script>
    """

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
        }}, 5000);
    </script>
    """
    if hero_video_id:
        bg_media = f"""<iframe src="https://www.youtube.com/embed/{hero_video_id}?autoplay=1&mute=1&loop=1&playlist={hero_video_id}&controls=0&showinfo=0&rel=0" style="position:absolute; top:50%; left:50%; width:100vw; height:100vh; transform:translate(-50%, -50%); pointer-events:none; object-fit:cover; z-index:0; min-width:177.77vh; min-height:56.25vw;" frameborder="0"></iframe>"""

    return f"""<section class="hero"><div class="hero-overlay"></div>{bg_media}<div class="container hero-content"><h1>{hero_h}</h1><p>{hero_sub}</p><div style="display:flex; gap:1.2rem; flex-wrap:wrap; {'justify-content:center;' if hero_layout == 'Center' else ''}"><a href="#inventory" class="btn btn-primary">Start Exploring</a><a href="contact.html" class="btn" style="background:rgba(255,255,255,0.05); backdrop-filter:blur(10px); color:white; border:1px solid rgba(255,255,255,0.2);">Contact Sales</a></div></div></section>"""

def get_simple_icon(name):
    path = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"
    if "bolt" in name: path = "M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"
    return f'<div class="icon-box"><svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="{path}"/></svg></div>'

def gen_features():
    cards = ""
    lines = [x for x in feat_data_input.split('\n') if x.strip()]
    for line in lines:
        parts = line.split('|')
        if len(parts) >= 3:
            cards += f"""<div class="card reveal">{get_simple_icon(parts[0])}<h3>{parts[1].strip()}</h3><div>{format_text(parts[2].strip())}</div></div>"""
    return f"""<section id="features"><div class="container"><div class="reveal" style="text-align:center; max-width:700px; margin:0 auto 3rem auto;"><h2>{f_title}</h2><p>Our platform is engineered for growth, security, and velocity.</p></div><div class="grid-3">{cards}</div></div></section>"""

def gen_stats():
    return f"""<div style="background:var(--primary); color:white; padding:5rem 0; margin:2rem 0; border-radius:0;"><div class="container" style="display:flex; justify-content:space-around; flex-wrap:wrap; text-align:center; gap:3rem;"><div class="reveal"><h1>{stat_1}</h1><p style="color:white; opacity:0.8;">{label_1}</p></div><div class="reveal"><h1>{stat_2}</h1><p style="color:white; opacity:0.8;">{label_2}</p></div><div class="reveal"><h1>{stat_3}</h1><p style="color:white; opacity:0.8;">{label_3}</p></div></div></div>"""

def gen_pricing_table():
    if not show_pricing: return ""
    return f"""<section id="pricing"><div class="container"><div class="reveal" style="text-align:center; margin-bottom:3rem;"><h2>Pricing Strategy</h2></div><div class="reveal" style="overflow-x:auto; background:var(--card-bg); padding:2rem; border-radius:24px; border:1px solid rgba(128,128,128,0.1); box-shadow:0 10px 40px -10px rgba(0,0,0,0.05);"><table style="width:100%; border-collapse:collapse; text-align:left;"><thead><tr style="border-bottom:2px solid rgba(128,128,128,0.1);"><th style="padding:1.5rem;">Cost Item</th><th style="padding:1.5rem; color:var(--primary); font-size:1.2rem;">Titan Engine</th><th style="padding:1.5rem; color:#9ca3af;">{wix_name}</th></tr></thead><tbody><tr><td style="padding:1.5rem; border-bottom:1px solid rgba(128,128,128,0.1);">Setup</td><td style="padding:1.5rem; border-bottom:1px solid rgba(128,128,128,0.1);"><strong>{titan_price}</strong></td><td style="padding:1.5rem; border-bottom:1px solid rgba(128,128,128,0.1);">$0</td></tr><tr><td style="padding:1.5rem; border-bottom:1px solid rgba(128,128,128,0.1);">Monthly Recurring</td><td style="padding:1.5rem; border-bottom:1px solid rgba(128,128,128,0.1);"><strong>{titan_mo}</strong></td><td style="padding:1.5rem; border-bottom:1px solid rgba(128,128,128,0.1);">{wix_mo}</td></tr><tr><td style="padding:1.5rem;"><strong>5-Year TCO</strong></td><td style="padding:1.5rem; color:var(--accent); font-weight:800; font-size:1.4rem;">Save {save_val}</td><td style="padding:1.5rem;">$0</td></tr></tbody></table></div></div></section>"""

def gen_csv_parser():
    return """<script>
    function parseCSVLine(str) { const res = []; let cur = ''; let inQuote = false; for (let i = 0; i < str.length; i++) { const c = str[i]; if (c === '"') { if (inQuote && str[i+1] === '"') { cur += '"'; i++; } else { inQuote = !inQuote; } } else if (c === ',' && !inQuote) { res.push(cur.trim()); cur = ''; } else { cur += c; } } res.push(cur.trim()); return res; }
    function parseMarkdown(text) { if (!text) return ''; let html = text.replace(/\\r\\n/g, '\\n').replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>'); return html; }
    </script>"""

def gen_cart_system():
    if not show_inventory: return ""
    clean_wa = wa_num.replace("+", "").replace(" ", "").replace("-", "")
    return f"""
    <div id="cart-float" onclick="openCart()" style="position:fixed; bottom:100px; right:30px; background:var(--primary); color:white; padding:15px 25px; border-radius:50px; box-shadow:0 15px 40px rgba(0,0,0,0.3); cursor:pointer; z-index:998; display:flex; align-items:center; gap:12px; font-weight:700; transition:all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="white"><path d="M7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zM1 2v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.14 0-.25-.11-.25-.25l.03-.12.9-1.63h7.45c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.08-.14.12-.31.12-.48 0-.55-.45-1-1-1H5.21l-.94-2H1zm16 16c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z"></path></svg>
        <span id="cart-count" style="background:white; color:var(--primary); border-radius:50%; min-width:24px; height:24px; display:flex; align-items:center; justify-content:center; font-size:0.85rem;">0</span>
    </div>

    <div id="cartModal" class="modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.6); z-index:2000; backdrop-filter:blur(8px);">
        <div class="modal-content" style="background:var(--card-bg); margin:5vh auto; padding:2.5rem; width:90%; max-width:420px; border-radius:24px; position:relative; box-shadow:0 25px 80px rgba(0,0,0,0.4); border:1px solid rgba(128,128,128,0.1);">
            <span onclick="closeCart()" style="position:absolute; top:20px; right:20px; font-size:1.5rem; cursor:pointer; opacity:0.5;">&times;</span>
            <h3 style="margin-top:0;">Your Selection</h3>
            <div id="cart-items" style="max-height:400px; overflow-y:auto; margin:20px 0; border-top:1px solid rgba(128,128,128,0.1);"></div>
            <div style="font-size:1.3rem; font-weight:800; text-align:right; margin-bottom:1.5rem; color:var(--primary);">Total: <span id="cart-total">0.00</span></div>
            <button class="btn btn-accent" style="width:100%; justify-content:center;" onclick="checkoutWA()">Complete on WhatsApp</button>
        </div>
    </div>

    <script>
    let cart = [];
    function addToCart(name, price) {{ cart.push({{name: name, price: price}}); updateCart(); document.getElementById('cart-float').style.transform = "scale(1.1) rotate(-3deg)"; setTimeout(()=>document.getElementById('cart-float').style.transform = "scale(1) rotate(0deg)", 200); }}
    function removeFromCart(index) {{ cart.splice(index, 1); updateCart(); }}
    function updateCart() {{
        document.getElementById('cart-count').innerText = cart.length;
        const box = document.getElementById('cart-items');
        let html = ''; let total = 0;
        cart.forEach((item, index) => {{
            html += `<div style="display:flex; justify-content:space-between; padding:15px 0; border-bottom:1px solid rgba(128,128,128,0.1); align-items:center;"><span style="font-weight:500;">${{item.name}}</span><div><b style="margin-right:12px;">${{item.price}}</b><span onclick="removeFromCart(${{index}})" style="color:#ef4444;cursor:pointer;font-weight:bold;">✕</span></div></div>`;
            let p = parseFloat(item.price.replace(/[^0-9.]/g, '')); if(!isNaN(p)) total += p;
        }});
        box.innerHTML = html || '<p style="padding:40px; text-align:center; opacity:0.5;">Your bag is empty.</p>';
        document.getElementById('cart-total').innerText = total.toFixed(2);
    }}
    function openCart() {{ document.getElementById('cartModal').style.display = 'block'; }}
    function closeCart() {{ document.getElementById('cartModal').style.display = 'none'; }}
    function checkoutWA() {{
        if(cart.length === 0) return;
        let msg = "New Order Inquiry:\\n"; cart.forEach(i => {{ msg += `- ${{i.name}} (${{i.price}})\\n`; }});
        msg += "\\nTotal Value: " + document.getElementById('cart-total').innerText;
        window.open("https://wa.me/{clean_wa}?text=" + encodeURIComponent(msg), '_blank');
    }}
    </script>
    """

def gen_popup():
    if not popup_enabled: return ""
    return f"""
    <div id="lead-popup" style="display:none; position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); background:var(--card-bg); padding:3rem; border-radius:24px; z-index:5000; box-shadow:0 30px 100px rgba(0,0,0,0.6); width:90%; max-width:480px; text-align:center; border:1px solid rgba(128,128,128,0.1);">
        <span onclick="document.getElementById('lead-popup').style.display='none'" style="position:absolute; top:20px; right:20px; cursor:pointer; font-size:1.5rem; opacity:0.5;">&times;</span>
        <h3 style="margin-bottom:1rem; font-size:1.8rem;">{popup_title}</h3>
        <p style="margin-bottom:2rem; color:var(--text); opacity:0.8;">{popup_text}</p>
        <a href="{top_bar_link if top_bar_link else '#'}" class="btn btn-primary" onclick="document.getElementById('lead-popup').style.display='none'" style="width:100%; justify-content:center;">{popup_cta}</a>
    </div>
    <script>
        setTimeout(() => {{ if(!sessionStorage.getItem('titanPopupShown')) {{ document.getElementById('lead-popup').style.display = 'block'; sessionStorage.setItem('titanPopupShown', 'true'); }} }}, {popup_delay}000);
    </script>
    """

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
                if(!lines[i].trim()) continue;
                const c = parseCSVLine(lines[i]);
                let allImgs = (c[3] || '{custom_feat}').split('|');
                let mainImg = allImgs[0];
                if(c.length > 1) {{
                    const prodName = encodeURIComponent(c[0]);
                    const cleanName = c[0].replace(/'/g, "\\'");
                    const cleanPrice = c[1].replace(/'/g, "\\'");
                    box.innerHTML += `
                    <div class="card reveal" style="padding:1.5rem;">
                        <div style="height:260px; border-radius:16px; background-image:url('${{mainImg}}'); background-size:cover; background-position:center; margin-bottom:1.5rem; transition:transform 0.4s;"></div>
                        <div style="display:flex; justify-content:space-between; align-items:start; margin-bottom:0.8rem;">
                            <h3 style="font-size:1.25rem; margin:0; line-height:1.3;">${{c[0]}}</h3>
                            <span style="background:rgba(16, 185, 129, 0.1); color:#10b981; padding:6px 12px; border-radius:30px; font-size:0.9rem; font-weight:700;">${{c[1]}}</span>
                        </div>
                        <p style="font-size:0.95rem; line-height:1.5; margin-bottom:1.5rem; flex-grow:1;">${{c[2].substring(0,70)}}...</p>
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                            <a href="product.html?item=${{prodName}}" class="btn" style="border:1px solid rgba(128,128,128,0.2); padding:0.7rem; font-size:0.9rem;">Details</a>
                            <button onclick="addToCart('${{cleanName}}', '${{cleanPrice}}')" class="btn btn-primary" style="padding:0.7rem; font-size:0.9rem;">Add</button>
                        </div>
                    </div>`;
                }}
            }}
        }} catch(e) {{ console.log(e); }}
    }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);
    </script>
    """

def gen_inventory():
    if not show_inventory: return ""
    return f"""<section id="inventory"><div class="container"><div class="section-head reveal"><h2 style="text-align:center">Featured Products</h2></div><div id="inv-grid" class="grid-3"><div>Loading Products...</div></div></div></section>{gen_inventory_js(is_demo=False)}"""

def gen_about_section():
    return f"""<section id="about"><div class="container"><div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(350px, 1fr)); gap:5rem; align-items:center;"><div class="reveal"><h2>{about_h_in}</h2><div>{format_text(about_short_in)}</div><br><a href="about.html" class="btn btn-primary">Our Story</a></div><img src="{about_img}" class="reveal" style="width:100%; border-radius:24px; box-shadow:0 30px 60px -10px rgba(0,0,0,0.15);"></div></div></section>"""

def gen_faq_section():
    items = "".join([f"<details class='reveal' style='background:var(--card-bg); margin-bottom:12px; padding:1.5rem; border-radius:16px; cursor:pointer; border:1px solid rgba(128,128,128,0.1);'><summary style='font-weight:600; font-size:1.1rem;'>{l.split('?')[0]}?</summary><p style='margin-top:1rem; opacity:0.8;'>{l.split('?')[1]}</p></details>" for l in faq_data.split('\n') if "?" in l])
    return f"""<section id="faq"><div class="container" style="max-width:800px;"><div class="section-head reveal" style="text-align:center"><h2>Common Questions</h2></div>{items}</div></section>"""

def gen_footer():
    return f"""
    <footer><div class="container">
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:3rem;">
            <div>
                <h3 style="color:white; margin-bottom:1.5rem;">{biz_name}</h3>
                <p style="opacity:0.6;">{biz_addr}</p>
            </div>
            <div>
                <h4 style="color:white;">Explore</h4>
                <a href="index.html" style="display:block; margin-bottom:0.8rem; opacity:0.7;">Home</a>
                <a href="blog.html" style="display:block; margin-bottom:0.8rem; opacity:0.7;">Insights</a>
                <a href="contact.html" style="display:block; margin-bottom:0.8rem; opacity:0.7;">Contact</a>
            </div>
            <div>
                <h4 style="color:white;">Legal</h4>
                <a href="privacy.html" style="display:block; margin-bottom:0.8rem; opacity:0.7;">Privacy</a>
                <a href="terms.html" style="display:block; margin-bottom:0.8rem; opacity:0.7;">Terms</a>
            </div>
        </div>
        <div style="border-top:1px solid rgba(255,255,255,0.08); margin-top:4rem; padding-top:2rem; text-align:center; opacity:0.4; font-size:0.9rem;">
            &copy; 2026 {biz_name}. Built on Titan Architecture.
        </div>
    </div></footer>
    """

def gen_wa_widget():
    if not wa_num: return ""
    clean_wa = wa_num.replace("+", "").replace(" ", "").replace("-", "")
    return f"""<a href="https://wa.me/{clean_wa}" target="_blank" style="position:fixed; bottom:30px; right:30px; background:#25d366; color:white; width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 40px rgba(37,211,102,0.4); z-index:9999; transition:transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);"><svg style="width:32px;height:32px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></path></svg></a>"""

def gen_scripts():
    return """<script>
    const observer = new IntersectionObserver((entries) => { entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('active'); } }); }, { threshold: 0.1 });
    document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
    </script>"""

def build_page(title, content, extra_js=""):
    pwa_tags = f'<link rel="manifest" href="manifest.json"><meta name="theme-color" content="{p_color}"><link rel="apple-touch-icon" href="{pwa_icon}">'
    sw_script = "<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('service-worker.js'); }</script>"
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title>{pwa_tags}{gen_schema()}<link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@400;600;700&family={b_font.replace(' ', '+')}:wght@300;400;600&display=swap" rel="stylesheet"><style>{get_theme_css()}</style></head><body>{gen_nav()}{content}{gen_footer()}{gen_wa_widget()}{gen_cart_system()}{gen_scripts()}{sw_script}{gen_popup()}{extra_js}</body></html>"""

def gen_inner_header(title):
    return f"""<section class="hero" style="min-height: 40vh; background: #000;"><div class="container" style="text-align:center;"><h1>{title}</h1></div></section>"""

def gen_blog_index_html():
    return f"""
    <section class="hero" style="min-height:45vh; background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{hero_img_1}'); background-size: cover;">
        <div class="container" style="text-align:center;"><h1>{blog_hero_title}</h1><p>{blog_hero_sub}</p></div>
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
                    <div class="card reveal" style="padding:0; overflow:hidden;">
                        <img src="${{r[5]}}" style="width:100%; height:240px; object-fit:cover; transition:transform 0.5s;">
                        <div style="padding:2rem;">
                            <span style="font-size:0.8rem; font-weight:700; color:var(--accent); text-transform:uppercase; letter-spacing:1px;">${{r[3]}}</span>
                            <h3 style="margin:0.8rem 0;"><a href="post.html?id=${{r[0]}}" style="text-decoration:none; color:var(--text);">${{r[1]}}</a></h3>
                            <p style="font-size:0.95rem; margin-bottom:2rem; opacity:0.8;">${{r[4]}}</p>
                            <a href="post.html?id=${{r[0]}}" class="btn btn-primary" style="width:100%;">Read Article</a>
                        </div>
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
    <section style="padding-top:160px;"><div class="container"><div id="product-detail">Loading...</div></div></section>
    {gen_csv_parser()}
    <script>
    {demo_flag}
    function changeMainImg(src) {{ document.getElementById('main-img').src = src; }}
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
                    let allImgs = rawImgs.split('|');
                    let galleryHtml = '';
                    if(allImgs.length > 1) {{
                        galleryHtml = '<div style="display:flex; gap:12px; margin-top:1.5rem;">';
                        allImgs.forEach(img => galleryHtml += `<img src="${{img}}" style="width:70px; height:70px; border-radius:12px; cursor:pointer; object-fit:cover; border:2px solid transparent;" onclick="changeMainImg('${{img}}')">`);
                        galleryHtml += '</div>';
                    }}
                    const cleanName = clean[0].replace(/'/g, "\\'");
                    const cleanPrice = clean[1].replace(/'/g, "\\'");
                    document.getElementById('product-detail').innerHTML = `
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(350px, 1fr)); gap:5rem;">
                            <div><img id="main-img" src="${{allImgs[0]}}" style="width:100%; border-radius:24px; box-shadow:0 25px 50px rgba(0,0,0,0.1);">${{galleryHtml}}</div>
                            <div>
                                <h1 style="font-size:3rem; line-height:1.1; margin-bottom:1rem;">${{clean[0]}}</h1>
                                <p style="font-size:2.2rem; color:var(--primary); font-weight:700; margin:0 0 1.5rem 0;">${{clean[1]}}</p>
                                <p style="line-height:1.8; margin-bottom:2.5rem; font-size:1.1rem;">${{clean[2]}}</p>
                                <button onclick="addToCart('${{cleanName}}', '${{cleanPrice}}')" class="btn btn-primary" style="width:100%; padding:1.2rem; font-size:1.1rem;">Add to Cart</button>
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

def gen_blog_post_html():
    return f"""
    <div id="post-container" style="padding-top:80px;">Loading...</div>
    {gen_csv_parser()}
    <script>
    async function loadPost() {{
        const params = new URLSearchParams(window.location.search);
        const slug = params.get('id');
        try {{
            const res = await fetch('{blog_sheet_url}');
            const txt = await res.text();
            const lines = txt.split(/\\r\\n|\\n/);
            const container = document.getElementById('post-container');
            for(let i=1; i<lines.length; i++) {{
                const r = parseCSVLine(lines[i]);
                if(r[0] === slug) {{
                    const contentHtml = parseMarkdown(r[6]);
                    container.innerHTML = `
                        <div style="background:#000; padding:8rem 1rem 6rem; color:white; text-align:center;">
                            <div class="container">
                                <span style="color:var(--accent); font-weight:700; text-transform:uppercase; letter-spacing:1px; font-size:0.9rem;">${{r[3]}}</span>
                                <h1 style="font-size:clamp(2.5rem, 6vw, 4.5rem); margin-top:1.5rem; background:none; -webkit-text-fill-color:white;">${{r[1]}}</h1>
                            </div>
                        </div>
                        <div class="container" style="max-width:840px; padding:4rem 1.5rem;">
                            <img src="${{r[5]}}" style="width:100%; border-radius:24px; margin-bottom:4rem; box-shadow:0 30px 60px rgba(0,0,0,0.15);">
                            <div style="line-height:2; font-size:1.2rem; color:var(--text);">${{contentHtml}}</div>
                            <hr style="margin:4rem 0; border:0; border-top:1px solid rgba(128,128,128,0.2);">
                            <a href="blog.html" class="btn btn-primary">&larr; Back to Insights</a>
                        </div>
                    `;
                    break;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadPost();
    </script>
    """

def gen_booking_content():
    return f"""
    <section class="hero" style="min-height:35vh; background:#000;">
        <div class="container hero-content" style="text-align:center;"><h1>{booking_title}</h1><p>{booking_desc}</p></div>
    </section>
    <section>
        <div class="container" style="text-align:center;">
            <div style="background:white; border-radius:24px; overflow:hidden; box-shadow:0 30px 80px rgba(0,0,0,0.1); padding:20px;">
                {booking_embed}
            </div>
        </div>
    </section>
    """

# --- 6. PAGE ASSEMBLY ---
home_content = ""
if show_hero: home_content += gen_hero()
if show_stats: home_content += gen_stats()
if show_features: home_content += gen_features()
if show_pricing: home_content += gen_pricing_table()
if show_inventory: home_content += gen_inventory()
if show_gallery: home_content += gen_about_section()
if show_testimonials: 
    t_cards = "".join([f'<div class="card reveal" style="text-align:center;"><i>"{x.split("|")[1]}"</i><br><b style="color:var(--primary); display:block; margin-top:1.5rem; font-size:0.9rem;">- {x.split("|")[0]}</b></div>' for x in testi_data.split('\n') if "|" in x])
    home_content += f'<section style="background:var(--card-bg)"><div class="container"><div class="section-head reveal" style="text-align:center"><h2>Client Success</h2></div><div class="grid-3">{t_cards}</div></div></section>'
if show_faq: home_content += gen_faq_section()
if show_cta: home_content += f'<section style="background:var(--primary); color:white; text-align:center; padding:8rem 0;"><div class="container reveal"><h2 style="margin-bottom:1.5rem; font-size:3rem;">Start Owning Your Future</h2><p style="margin-bottom:2.5rem; opacity:0.9; font-size:1.3rem;">Stop paying rent. Start building equity.</p><a href="contact.html" class="btn" style="background:white; color:var(--primary);">Get Started Now</a></div></section>'

# --- 7. DEPLOYMENT ---
st.divider()
st.subheader("🚀 Deployment Command")
preview_mode = st.radio("Live Preview:", ["Home", "About", "Contact", "Blog Index", "Blog Post", "Privacy", "Terms", "Product Detail", "Booking"], horizontal=True)

contact_content = f"""{gen_inner_header("Contact Us")}<section><div class="container"><div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:4rem;"><div><div style="background:var(--card-bg); padding:3rem; border-radius:24px; border:1px solid rgba(0,0,0,0.05); box-shadow:0 10px 40px rgba(0,0,0,0.05);"><h3>Get In Touch</h3><p>{biz_addr}</p><p><a href="tel:{biz_phone}" style="color:var(--primary); font-weight:700; text-decoration:none;">{biz_phone}</a></p><p>{biz_email}</p><br><a href="https://wa.me/{wa_num}" target="_blank" class="btn btn-accent" style="width:100%; justify-content:center;">WhatsApp Chat</a></div></div><div class="card"><h3>Send Message</h3><form action="https://formsubmit.co/{biz_email}" method="POST" style="display:flex; flex-direction:column; gap:18px;"><input type="text" name="name" placeholder="Name" required style="padding:16px; border-radius:12px; border:1px solid rgba(128,128,128,0.2); background:var(--bg); color:var(--text);"><input type="email" name="email" placeholder="Email" required style="padding:16px; border-radius:12px; border:1px solid rgba(128,128,128,0.2); background:var(--bg); color:var(--text);"><textarea name="msg" rows="4" placeholder="Message" required style="padding:16px; border-radius:12px; border:1px solid rgba(128,128,128,0.2); background:var(--bg); color:var(--text);"></textarea><button class="btn btn-primary" type="submit">Send Message</button></form></div></div><br><div style="border-radius:24px;overflow:hidden; box-shadow:0 20px 50px rgba(0,0,0,0.1);">{map_iframe}</div></div></section>"""

c1, c2 = st.columns([3, 1])
with c1:
    if preview_mode == "Home": st.components.v1.html(build_page("Home", home_content), height=800, scrolling=True)
    elif preview_mode == "About": st.components.v1.html(build_page("About", f"{gen_inner_header('About')}<div class='container' style='padding:5rem 0;'>{format_text(about_long)}</div>"), height=800, scrolling=True)
    elif preview_mode == "Contact": st.components.v1.html(build_page("Contact", contact_content), height=800, scrolling=True)
    elif preview_mode == "Privacy": st.components.v1.html(build_page("Privacy", f"{gen_inner_header('Privacy')}<div class='container' style='padding:5rem 0;'>{format_text(priv_txt)}</div>"), height=800, scrolling=True)
    elif preview_mode == "Terms": st.components.v1.html(build_page("Terms", f"{gen_inner_header('Terms')}<div class='container' style='padding:5rem 0;'>{format_text(term_txt)}</div>"), height=800, scrolling=True)
    elif preview_mode == "Blog Index": st.components.v1.html(build_page("Blog", gen_blog_index_html()), height=800, scrolling=True)
    elif preview_mode == "Blog Post": st.components.v1.html(build_page("Article", gen_blog_post_html()), height=800, scrolling=True)
    elif preview_mode == "Product Detail":
        st.info("ℹ️ Demo Mode: Simulating first product load.")
        st.components.v1.html(build_page("Product", gen_product_page_content(is_demo=True)), height=800, scrolling=True)
    elif preview_mode == "Booking":
        st.components.v1.html(build_page("Book Now", gen_booking_content()), height=800, scrolling=True)

with c2:
    st.success("✨ Build Complete")
    
    z_b = io.BytesIO()
    with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
        zf.writestr("index.html", build_page("Home", home_content))
        zf.writestr("about.html", build_page("About", f"{gen_inner_header('About')}<div class='container' style='padding:5rem 0;'>{format_text(about_long)}</div>"))
        zf.writestr("contact.html", build_page("Contact", contact_content))
        zf.writestr("privacy.html", build_page("Privacy", f"{gen_inner_header('Privacy')}<div class='container' style='padding:5rem 0;'>{format_text(priv_txt)}</div>"))
        zf.writestr("terms.html", build_page("Terms", f"{gen_inner_header('Terms')}<div class='container' style='padding:5rem 0;'>{format_text(term_txt)}</div>"))
        zf.writestr("booking.html", build_page("Book Now", gen_booking_content()))
        zf.writestr("product.html", build_page("Product Details", gen_product_page_content(is_demo=False)))
        if show_blog: 
            zf.writestr("blog.html", build_page("Blog", gen_blog_index_html()))
            zf.writestr("post.html", build_page("Article", gen_blog_post_html()))
        
        zf.writestr("manifest.json", gen_pwa_manifest())
        zf.writestr("service-worker.js", gen_sw())
        zf.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}/sitemap.xml")
        zf.writestr("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{prod_url}/</loc></url></urlset>""")

    st.download_button(
        label="⚡ DOWNLOAD ZIP", 
        data=z_b.getvalue(), 
        file_name=f"{biz_name.lower().replace(' ','_')}_site.zip", 
        mime="application/zip",
        type="primary"
    )
