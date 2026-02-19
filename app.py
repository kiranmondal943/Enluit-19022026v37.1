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
init_state('about_h', "Control Your Empire")
init_state('about_short', "No WordPress dashboard. No plugins to update. Just open your private Google Sheet, change a text, and watch your site update globally in seconds.")
init_state('feat_data', "bolt | The Performance Pillar | **0.1s High-Velocity Loading**. While traditional sites take 3–5s, Titan loads instantly.\nwallet | The Economic Pillar | **$0 Monthly Fees**. We eliminated hosting subscriptions.\ntable | The Functional Pillar | **Google Sheets CMS**. Update prices and photos directly from a simple spreadsheet.\nshield | The Authority Pillar | **Unhackable Security**. Zero-DB Architecture removes the hacker's primary entry point.\nlayers | The Reliability Pillar | **Global Edge Deployment**. Distributed across 100+ servers worldwide.\nstar | The Conversion Pillar | **One-Tap WhatsApp**. Direct-to-Chat technology.")

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v40.2 | Professional Layout", 
    layout="wide", 
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL DASHBOARD CSS ---
st.markdown("""
    <style>
    /* Global Clean Up */
    :root { --primary: #3b82f6; --bg-dark: #0f172a; --panel: #1e293b; }
    .stApp { background-color: var(--bg-dark); color: #f1f5f9; font-family: 'Inter', sans-serif; }
    
    /* Sidebar Polish */
    [data-testid="stSidebar"] { background-color: var(--panel); border-right: 1px solid #334155; }
    [data-testid="stSidebar"] h1 { 
        background: linear-gradient(90deg, #60a5fa, #c084fc);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 800 !important; font-size: 1.6rem !important; letter-spacing: -0.5px;
    }
    
    /* Input Fields - Softened & Professional */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #0f172a !important; 
        border: 1px solid #334155 !important; 
        border-radius: 6px !important; 
        color: #e2e8f0 !important;
        font-size: 0.95rem;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
    }
    
    /* Buttons - Modern Gradient */
    .stButton>button {
        width: 100%; border-radius: 6px; height: 3rem; font-weight: 600;
        background: linear-gradient(to right, #2563eb, #4f46e5);
        border: none; color: white; transition: all 0.2s;
        text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;
    }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4); }
    
    /* Expander Styling */
    .streamlit-expanderHeader { background-color: #1e293b !important; border-radius: 6px; }
    
    /* Tabs Styling */
    button[data-baseweb="tab"] { color: #94a3b8; font-weight: 600; }
    button[data-baseweb="tab"][aria-selected="true"] { color: #60a5fa !important; border-color: #60a5fa !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR CONTROLS ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v40.2 | Layout Fixed")
    st.divider()
    
    # --- AI SECTION ---
    with st.expander("🤖 AI Generator", expanded=True):
        groq_key = st.text_input("Groq API Key", type="password")
        biz_desc = st.text_input("Business Description")
        if st.button("✨ Auto-Write Content"):
            if not groq_key or not biz_desc:
                st.error("Key & Description required.")
            else:
                try:
                    with st.spinner("Thinking..."):
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

    # --- DESIGN CONTROLS ---
    with st.expander("🎨 Visual Style", expanded=False):
        theme_mode = st.selectbox("Theme", ["Midnight Glass (Dark)", "Modern Glass (Light)", "Neo-Brutalism", "Luxury Gold"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary", "#3B82F6") 
        s_color = c2.color_picker("Accent", "#F43F5E")  
        hero_layout = st.selectbox("Hero Align", ["Center", "Left"])
        border_rad = st.select_slider("Corner Radius", ["0px", "12px", "24px", "40px"], value="24px")
        anim_type = st.selectbox("Animation", ["Fade Up", "Zoom In", "None"])

    # --- MODULES ---
    with st.expander("🧩 Sections", expanded=False):
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            show_hero = st.checkbox("Hero", value=True)
            show_stats = st.checkbox("Stats", value=True)
            show_features = st.checkbox("Features", value=True)
            show_pricing = st.checkbox("Pricing", value=True)
            show_inventory = st.checkbox("Store", value=True)
        with col_m2:
            show_blog = st.checkbox("Blog", value=True)
            show_gallery = st.checkbox("About", value=True)
            show_testimonials = st.checkbox("Reviews", value=True)
            show_faq = st.checkbox("FAQ", value=True)
            show_booking = st.checkbox("Booking", value=True)
            show_cta = st.checkbox("CTA", value=True)

    # --- SEO ---
    with st.expander("⚙️ SEO Settings", expanded=False):
        seo_area = st.text_input("Service Area", "Global")
        seo_kw = st.text_area("Keywords", "web design, static site")
        gsc_tag = st.text_input("Google ID")

# --- 4. MAIN WORKSPACE (FIXED LAYOUT) ---
st.title("💎 Titan v40.2 Builder")

tabs = st.tabs(["1. Brand", "2. Content", "3. Pricing", "4. Store", "5. Booking", "6. Blog", "7. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent.com")
        biz_tagline = st.text_input("Tagline", "Stop Renting. Start Owning.")
        biz_phone = st.text_input("Phone", "966572562151")
        biz_email = st.text_input("Email", "hello@kaydiemscriptlab.com")
    with c2:
        prod_url = st.text_input("Website URL", "https://www.stopwebrent.com")
        biz_addr = st.text_area("Address", "Kaydiem Script Lab\nKolkata, India", height=135)
        logo_url = st.text_input("Logo URL (PNG/SVG)")

    st.subheader("PWA & Socials")
    r1, r2, r3 = st.columns(3)
    pwa_short = r1.text_input("App Name", biz_name[:12])
    pwa_icon = r2.text_input("App Icon", logo_url)
    lang_sheet = r3.text_input("Lang CSV", help="Col 1: ID, Col 2: Text")
    
    s1, s2, s3, s4 = st.columns(4)
    fb_link = s1.text_input("Facebook")
    ig_link = s2.text_input("Instagram")
    x_link = s3.text_input("Twitter/X")
    wa_num = s4.text_input("WhatsApp (No +)", "966572562151")

with tabs[1]:
    st.subheader("Hero Section")
    hero_h = st.text_input("Headline", key="hero_h")
    hero_sub = st.text_area("Subtext", key="hero_sub", height=100)
    
    st.markdown("**Hero Images (Carousel)**")
    i1, i2, i3 = st.columns(3)
    hero_img_1 = i1.text_input("Slide 1", "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1600")
    hero_img_2 = i2.text_input("Slide 2", "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=1600")
    hero_img_3 = i3.text_input("Slide 3", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1600")
    hero_video_id = st.text_input("Or YouTube Video ID (Background)", placeholder="e.g. dQw4w9WgXcQ")
    
    st.divider()
    
    c_feat, c_stats = st.columns([2, 1])
    with c_feat:
        st.subheader("Features")
        f_title = st.text_input("Features Title", "Value Pillars")
        feat_data_input = st.text_area("Features (icon|Title|Desc)", key="feat_data", height=250)
    
    with c_stats:
        st.subheader("Stats")
        stat_1 = st.text_input("Stat 1", "0.1s")
        label_1 = st.text_input("Label 1", "Speed")
        stat_2 = st.text_input("Stat 2", "$0")
        label_2 = st.text_input("Label 2", "Fees")
        stat_3 = st.text_input("Stat 3", "100%")
        label_3 = st.text_input("Label 3", "Own")
    
    st.subheader("About")
    ac1, ac2 = st.columns(2)
    about_h_in = ac1.text_input("Title", key="about_h")
    about_img = ac2.text_input("Image", "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=1600")
    about_short_in = st.text_area("Summary", key="about_short", height=100)

with tabs[2]:
    st.subheader("Pricing")
    pc1, pc2, pc3 = st.columns(3)
    titan_price = pc1.text_input("Your Setup Price", "$199")
    titan_mo = pc1.text_input("Your Monthly", "$0")
    wix_name = pc2.text_input("Competitor Name", "Wix")
    wix_mo = pc2.text_input("Competitor Monthly", "$29/mo")
    save_val = pc3.text_input("Savings Text", "$1,466")

with tabs[3]:
    st.subheader("Store & Payments")
    st.info("Format: Name, Price, Desc, Images, StripeLink (Optional)")
    sheet_url = st.text_input("Inventory CSV URL")
    
    pay1, pay2 = st.columns(2)
    paypal_link = pay1.text_input("PayPal.me Link")
    upi_id = pay2.text_input("UPI ID")

with tabs[4]:
    st.subheader("Booking")
    booking_title = st.text_input("Page Title", "Book an Appointment")
    booking_desc = st.text_input("Page Subtext", "Select a time slot.")
    booking_embed = st.text_area("Calendly Embed Code", height=150, value='<!-- Calendly -->')

with tabs[5]:
    st.subheader("Blog")
    blog_sheet_url = st.text_input("Blog CSV URL")
    blog_hero_title = st.text_input("Blog Title", "Latest Insights")
    blog_hero_sub = st.text_input("Blog Subtext", "Thoughts on tech.")

with tabs[6]:
    st.subheader("Legal Pages")
    l1, l2 = st.columns(2)
    priv_txt = l1.text_area("Privacy Policy", "We collect minimum data.", height=150)
    term_txt = l2.text_area("Terms of Service", "You own the code.", height=150)
    faq_data = st.text_area("FAQ (Q? ? A)", "Do I pay $0? ? Yes.", height=100)
    testi_data = st.text_area("Testimonials (Name|Quote)", "Rajesh | Great service.", height=100)
    map_iframe = st.text_area("Map Embed", height=100)
    seo_d = st.text_area("SEO Description", "Best site builder.", height=100)

# ==========================================
# 4. COMPILER ENGINE (GLASS V2 + BUG FIXES)
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
    bg_color, text_color, card_bg = "#F8FAFC", "#0F172A", "rgba(255, 255, 255, 0.7)"
    nav_bg, border_color = "rgba(255, 255, 255, 0.8)", "rgba(255, 255, 255, 0.5)"
    
    if "Midnight" in theme_mode: 
        bg_color, text_color, card_bg = "#0B0F19", "#F1F5F9", "rgba(30, 41, 59, 0.6)"
        nav_bg, border_color = "rgba(15, 23, 42, 0.8)", "rgba(255, 255, 255, 0.1)"
    elif "Neo-Brutalism" in theme_mode:
        bg_color, text_color, card_bg = "#ffffff", "#000000", "#ffffff"
        nav_bg, border_color = "#ffffff", "#000000"
    
    hero_align = "justify-content: center; text-align: center;"
    if hero_layout == "Left": hero_align = "justify-content: flex-start; text-align: left;"
    
    anim_css = ".reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease-out; } .reveal.active { opacity: 1; transform: translateY(0); }"
    if anim_type == "Zoom In":
        anim_css = ".reveal { opacity: 0; transform: scale(0.95); transition: all 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); } .reveal.active { opacity: 1; transform: scale(1); }"
    elif anim_type == "None":
        anim_css = ".reveal { opacity: 1; }"

    border_style = f"border: 1px solid {border_color};" if "Brutalism" not in theme_mode else "border: 2px solid #000; box-shadow: 4px 4px 0px #000;"
    radius_val = "0px" if "Brutalism" in theme_mode else border_rad

    return f"""
    :root {{
        --p: {p_color}; --s: {s_color};
        --bg: {bg_color}; --txt: {text_color};
        --card-bg: {card_bg}; --nav-bg: {nav_bg};
        --border: {border_color};
        --radius: {radius_val};
        --glass: blur(16px) saturate(180%);
        --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        --font-h: 'Outfit', sans-serif;
        --font-b: 'Plus Jakarta Sans', sans-serif;
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
        border: none; font-size: 1rem; gap: 0.5rem;
    }}
    .btn-primary {{ background: linear-gradient(135deg, var(--p), var(--s)); color: white !important; box-shadow: 0 10px 20px -5px var(--p); }}
    .btn-primary:hover {{ transform: translateY(-3px); filter: brightness(1.1); }}
    .btn-outline {{ background: transparent; {border_style} color: var(--txt) !important; }}

    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; background: var(--nav-bg); backdrop-filter: var(--glass); -webkit-backdrop-filter: var(--glass); border-bottom: 1px solid var(--border); padding: 1rem 0; }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; gap: 2rem; align-items: center; }}
    .nav-links a {{ text-decoration: none; font-weight: 500; color: var(--txt); opacity: 0.8; transition: 0.2s; }}
    .nav-links a:hover {{ opacity: 1; color: var(--p); }}
    
    .hero {{ position: relative; min-height: 100vh; display: flex; align-items: center; {hero_align} overflow: hidden; padding-top: 80px; }}
    .hero-bg {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; }}
    .hero-overlay {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0.3), var(--bg)); z-index: 0; }}
    .hero-content {{ z-index: 2; position: relative; max-width: 900px; animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1); }}
    .hero h1 {{ color: white !important; text-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
    .hero p {{ color: rgba(255,255,255,0.9); font-size: 1.25rem; margin-bottom: 2.5rem; max-width: 600px; { "margin-left: auto; margin-right: auto;" if hero_layout == "Center" else "" } }}

    .card {{ background: var(--card-bg); backdrop-filter: blur(12px); {border_style} border-radius: var(--radius); padding: 2rem; display: flex; flex-direction: column; height: 100%; }}
    
    .prod-card {{ background: var(--card-bg); {border_style} border-radius: var(--radius); overflow: hidden; position: relative; transition: 0.3s; }}
    .prod-img-wrap {{ position: relative; padding-top: 100%; overflow: hidden; }}
    .prod-img {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; }}
    .prod-info {{ padding: 1.5rem; }}
    
    section {{ padding: clamp(4rem, 8vw, 6rem) 0; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; }}
    {anim_css}
    
    .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); backdrop-filter: blur(8px); }}
    .modal-content {{ background: var(--bg); {border_style} margin: 10vh auto; padding: 2.5rem; width: 90%; max-width: 450px; border-radius: 24px; position: relative; animation: slideUp 0.3s; }}
    
    footer {{ background: #0f172a; color: white; padding: 5rem 0; }}
    @keyframes fadeInUp {{ from {{ opacity:0; transform:translateY(40px); }} to {{ opacity:1; transform:translateY(0); }} }}
    @keyframes slideUp {{ from {{ opacity:0; transform:translateY(20px); }} to {{ opacity:1; transform:translateY(0); }} }}

    @media (max-width: 768px) {{
        .nav-links {{ position: fixed; top: 70px; left: -100%; width: 100%; height: calc(100vh - 70px); background: var(--bg); flex-direction: column; padding: 2rem; transition: 0.3s; align-items: flex-start; border-top: 1px solid var(--border); }}
        .nav-links.active {{ left: 0; }}
        .mobile-menu {{ display: block; font-size: 1.5rem; cursor: pointer; }}
        h1 {{ font-size: 2.8rem; }}
    }}
    """

def gen_nav():
    logo = f'<img src="{logo_url}" height="32" alt="{biz_name}">' if logo_url else f'<span style="font-weight:800;font-size:1.4rem;letter-spacing:-0.03em;" class="gradient-text">{biz_name}</span>'
    blog_link = '<a href="blog.html" onclick="toggleMenu()">Blog</a>' if show_blog else ''
    book_link = '<a href="booking.html" onclick="toggleMenu()">Book Now</a>' if show_booking else ''
    lang_btn = f'<button onclick="openModal(\'langModal\')" class="btn-outline" style="padding: 0.5rem 1rem; border-radius: 50px;">Lang</button>' if lang_sheet else ''

    return f"""
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

# --- INVENTORY WITH "LOADING..." BUG FIX ---
def gen_inventory():
    if not show_inventory: return ""
    return f"""
    <section id="inventory" style="background:var(--bg);"><div class="container">
        <div class="section-head reveal"><h2 class="gradient-text">Featured Collection</h2></div>
        <div id="inv-grid" class="grid-3"><div>Loading Products...</div></div>
    </div></section>
    <script>
    function parseCSVLine(str) {{ const res = []; let cur = ''; let inQuote = false; for (let i = 0; i < str.length; i++) {{ const c = str[i]; if (c === '"') {{ if (inQuote && str[i+1] === '"') {{ cur += '"'; i++; }} else {{ inQuote = !inQuote; }} }} else if (c === ',' && !inQuote) {{ res.push(cur.trim()); cur = ''; }} else {{ cur += c; }} }} res.push(cur.trim()); return res; }}
    
    async function loadInv() {{
        const url = '{sheet_url}';
        const box = document.getElementById('inv-grid');
        if(!url) {{
            // HARDCODED DEMO MODE TO PREVENT INFINITE LOADING
            box.innerHTML = `<div class="prod-card reveal"><div class="prod-img-wrap"><img src="{custom_feat}" class="prod-img"></div><div class="prod-info"><h3>Demo Product</h3><span class="prod-price">$99.00</span><br><br><button class="btn btn-primary btn-sm">Add</button></div></div>`;
            return;
        }}
        try {{
            const res = await fetch(url); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/);
            if(!box) return; box.innerHTML = '';
            for(let i=1; i<lines.length; i++) {{
                const row = parseCSVLine(lines[i]);
                if(row.length < 2) continue;
                let mainImg = (row[3] || '{custom_feat}').split('|')[0];
                let stripeLink = (row.length > 4 && row[4].includes('http')) ? row[4] : '';
                let btn = stripeLink ? `<a href="${{stripeLink}}" class="btn btn-primary btn-sm">Buy Now</a>` : `<button onclick="addToCart('${{row[0].replace(/'/g, "\\'")}}', '${{row[1].replace(/'/g, "\\'")}}')" class="btn btn-primary btn-sm">Add</button>`;
                
                box.innerHTML += `<div class="prod-card reveal"><div class="prod-img-wrap"><img src="${{mainImg}}" class="prod-img" loading="lazy"></div><div class="prod-info"><div style="display:flex; justify-content:space-between; align-items:start;"><h3 style="font-size:1.1rem; margin:0;">${{row[0]}}</h3><span class="prod-price">${{row[1]}}</span></div><div style="margin-top:1rem; display:grid; grid-template-columns:1fr 1fr; gap:0.5rem;"><a href="product.html?item=${{encodeURIComponent(row[0])}}" class="btn btn-outline btn-sm">Details</a>${{btn}}</div></div></div>`;
            }}
        }} catch(e) {{ console.log(e); }}
    }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);
    </script>
    """

def gen_cart_system():
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
    clean_wa = wa_num.replace("+", "").replace(" ", "").replace("-", "")
    return f"""<a href="https://wa.me/{clean_wa}" target="_blank" style="position:fixed; bottom:100px; right:30px; background:#25D366; color:white; width:50px; height:50px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 25px rgba(37,211,102,0.4); z-index:9999;"><svg style="width:28px;height:28px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></path></svg></a>"""

def gen_scripts():
    return """<script>
    window.addEventListener('scroll', () => { var r = document.querySelectorAll('.reveal'); for (var i = 0; i < r.length; i++) { if (r[i].getBoundingClientRect().top < window.innerHeight - 80) r[i].classList.add('active'); } });
    window.dispatchEvent(new Event('scroll'));
    </script>"""

def build_page(title, content, extra_js=""):
    pwa_tags = f'<link rel="manifest" href="manifest.json"><meta name="theme-color" content="{p_color}"><link rel="apple-touch-icon" href="{pwa_icon}">'
    sw_script = "<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('service-worker.js'); }</script>"
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title>{pwa_tags}{gen_schema()}<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap" rel="stylesheet"><style>{get_theme_css()}</style></head><body>{gen_nav()}{content}{f'<footer><div class="container" style="text-align:center;"><h2 style="color:white;">{biz_name}</h2><p>{biz_addr}</p><p>&copy; 2026 {biz_name}</p></div></footer>'}{gen_wa_widget()}{gen_cart_system()}{gen_scripts()}{sw_script}{extra_js}</body></html>"""

# --- PAGE ASSEMBLY & DOWNLOAD ---
home_content = ""
if show_hero: home_content += gen_hero()
if show_stats: home_content += f"""<div style="background:var(--p); color:white; padding:3rem 0; text-align:center;"><div class="container grid-3"><div class="reveal"><h3>{stat_1}</h3><p>{label_1}</p></div><div class="reveal"><h3>{stat_2}</h3><p>{label_2}</p></div><div class="reveal"><h3>{stat_3}</h3><p>{label_3}</p></div></div></div>"""
if show_features: home_content += gen_features()
if show_pricing: home_content += f"""<section id="pricing"><div class="container"><div class="section-head reveal"><h2 class="gradient-text">Pricing</h2></div><div class="reveal card"><table style="width:100%; text-align:left; border-collapse:collapse;"><thead><tr style="border-bottom:1px solid var(--border);"><th style="padding:1rem;">Category</th><th style="padding:1rem; color:var(--p);">Titan</th><th style="padding:1rem;">{wix_name}</th></tr></thead><tbody><tr><td style="padding:1rem;">Setup</td><td style="padding:1rem; font-weight:bold;">{titan_price}</td><td style="padding:1rem;">$0</td></tr><tr><td style="padding:1rem;">Monthly</td><td style="padding:1rem; font-weight:bold;">{titan_mo}</td><td style="padding:1rem;">{wix_mo}</td></tr></tbody></table></div></div></section>"""
if show_inventory: home_content += gen_inventory()
if show_gallery: home_content += f"""<section id="about"><div class="container"><div class="grid-3" style="align-items:center;"><div class="reveal"><h2 class="gradient-text">{about_h_in}</h2><p>{format_text(about_short_in)}</p></div><img src="{about_img}" class="reveal" style="width:100%; border-radius:var(--radius); box-shadow:var(--shadow-lg);"></div></div></section>"""
if show_cta: home_content += f'<section style="background:linear-gradient(135deg, var(--p), var(--s)); color:white; text-align:center;"><div class="container reveal"><h2>Start Owning Your Future</h2><a href="contact.html" class="btn" style="background:white; color:var(--p); margin-top:1rem;">Get Started</a></div></section>'

st.divider()
st.subheader("🚀 Launchpad")
preview_mode = st.radio("Preview", ["Home", "Product (Demo)", "Booking"], horizontal=True)

if preview_mode == "Home": st.components.v1.html(build_page("Home", home_content), height=700, scrolling=True)
elif preview_mode == "Product (Demo)": 
    # Hardcoded Demo Product for Preview
    demo_prod_html = f"""<section style="padding-top:140px; min-height:80vh;"><div class="container"><div style="display:grid; grid-template-columns: 1fr 1fr; gap:4rem; align-items:start;"><div><img src="{custom_feat}" style="width:100%; border-radius:24px;"></div><div><h1 class="gradient-text">Demo Product</h1><p style="font-size:2.5rem; font-weight:800; color:var(--txt); margin:1rem 0;">$99.00</p><p style="opacity:0.8; font-size:1.1rem; margin-bottom:2rem;">This is a preview of how your products will look.</p><button class="btn btn-primary">Add to Cart</button></div></div></div></section>"""
    st.components.v1.html(build_page("Product", demo_prod_html), height=700, scrolling=True)
elif preview_mode == "Booking": st.components.v1.html(build_page("Book Now", gen_booking_content()), height=700, scrolling=True)

st.success("System Ready. All features active.")

z_b = io.BytesIO()
with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
    zf.writestr("index.html", build_page("Home", home_content))
    zf.writestr("product.html", build_page("Product", "")) # Placeholder
    zf.writestr("booking.html", build_page("Book Now", gen_booking_content()))
    zf.writestr("contact.html", build_page("Contact", f"<section style='padding-top:150px;' class='container'><h1>Contact Us</h1><p>{biz_phone}</p></section>"))
    zf.writestr("manifest.json", gen_pwa_manifest())
    zf.writestr("service-worker.js", gen_sw())

st.download_button("📥 DOWNLOAD GLASS UI WEBSITE", z_b.getvalue(), "titan_glass_ui.zip", "application/zip", type="primary")
