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
init_state('feat_data', "bolt | Extreme Speed | **0.1s Loading**. Google loves fast sites. Titan is instant.\nwallet | Zero Rent | **$0 Monthly**. Stop bleeding money on subscriptions.\ntable | Easy Control | **Sheet CMS**. Update content from Excel/Sheets.\nshield | Ironclad | **Zero-DB**. Unhackable static architecture.")

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v38.0 | Future Dominance", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# --- 2. STREAMLIT UI (Builder Interface) ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #ef4444; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5rem;
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
        color: white; font-weight: 800; border: none;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.3); text-transform: uppercase; letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v38.0 | Future UI + Multi-Img")
    st.divider()
    
    # AI GEN
    with st.expander("🤖 Titan AI Writer", expanded=False):
        raw_key = st.text_input("Groq API Key", type="password")
        groq_key = raw_key.strip() if raw_key else ""
        biz_desc = st.text_input("Business Description")
        if st.button("✨ Auto-Generate Content"):
            if groq_key and biz_desc:
                try:
                    with st.spinner("Dreaming up content..."):
                        url = "https://api.groq.com/openai/v1/chat/completions"
                        headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                        prompt = f"Act as a web copywriter. Return JSON for '{biz_desc}': hero_h, hero_sub, about_h, about_short, feat_data (icon|Title|Desc format)."
                        data = {"messages": [{"role": "user", "content": prompt}], "model": "llama-3.1-8b-instant", "response_format": {"type": "json_object"}}
                        resp = requests.post(url, headers=headers, json=data)
                        if resp.status_code == 200:
                            parsed = json.loads(resp.json()['choices'][0]['message']['content'])
                            for k,v in parsed.items(): 
                                if k == 'feat_data' and isinstance(v, list): v = "\n".join(v)
                                st.session_state[k] = str(v)
                            st.success("Generated!"); st.rerun()
                except: st.error("AI Error")

    # DESIGN STUDIO
    with st.expander("🎨 Design Studio", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Clean Corporate", "Midnight SaaS", "Luxury Gold", "Cyberpunk Neon"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Brand Color", "#0F172A") 
        s_color = c2.color_picker("Accent Color", "#EF4444")  
        h_font = st.selectbox("Headings", ["Space Grotesk", "Outfit", "Montserrat", "Playfair Display"])
        b_font = st.selectbox("Body", ["Inter", "Plus Jakarta Sans", "Roboto"])
        hero_layout = st.selectbox("Hero Alignment", ["Center", "Left"])
        border_rad = "16px" # Fixed for modern look

    # MODULES
    with st.expander("🧩 Modules", expanded=False):
        show_hero = st.checkbox("Hero", True)
        show_stats = st.checkbox("Stats", True)
        show_features = st.checkbox("Features", True)
        show_pricing = st.checkbox("Pricing", True)
        show_inventory = st.checkbox("Store (Multi-Img)", True)
        show_blog = st.checkbox("Blog", True)
        show_booking = st.checkbox("Booking", True)
        show_gallery = st.checkbox("About", True)
        show_testimonials = st.checkbox("Testimonials", True)
        show_faq = st.checkbox("FAQ", True)
        show_cta = st.checkbox("CTA", True)

    # SEO
    with st.expander("⚙️ SEO & Analytics", expanded=False):
        seo_area = st.text_input("Service Area", "Global")
        gsc_tag = st.text_input("Google Verification ID")
        og_image = st.text_input("Social Share Image")

# --- 4. WORKSPACE ---
st.title("🏗️ StopWebRent Site Builder")
tabs = st.tabs(["1. Identity", "2. Content", "3. Marketing", "4. Store & Pricing", "5. Blog & Booking", "6. Legal"])

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
        map_iframe = st.text_area("Map Embed", placeholder='<iframe src="..."></iframe>', height=100)
        seo_d = st.text_area("Meta Desc", "Stop paying monthly fees.", height=100)
        logo_url = st.text_input("Logo URL")

    st.subheader("🌍 Multi-Language")
    lang_sheet = st.text_input("Translation CSV URL")
    st.caption("Connects IDs (hero-title, nav-home) to translated text.")

    st.subheader("Social")
    sc1, sc2, sc3 = st.columns(3)
    fb_link = sc1.text_input("Facebook")
    ig_link = sc2.text_input("Instagram")
    x_link = sc3.text_input("Twitter/X")
    li_link = st.text_input("LinkedIn")
    yt_link = st.text_input("YouTube")
    wa_num = st.text_input("WhatsApp (No +)", "966572562151")

with tabs[1]:
    st.subheader("Hero")
    hero_h = st.text_input("Headline", key="hero_h")
    hero_sub = st.text_input("Subtext", key="hero_sub")
    hero_video_id = st.text_input("YouTube Video BG ID (Optional)")
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Img 1", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    hero_img_2 = hc2.text_input("Img 2", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1600")
    hero_img_3 = hc3.text_input("Img 3", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1600")
    
    st.subheader("Stats & Features")
    col_s1, col_s2, col_s3 = st.columns(3)
    stat_1 = col_s1.text_input("Stat 1", "0.1s")
    label_1 = col_s1.text_input("Label 1", "Speed")
    stat_2 = col_s2.text_input("Stat 2", "$0")
    label_2 = col_s2.text_input("Label 2", "Fees")
    stat_3 = col_s3.text_input("Stat 3", "100%")
    label_3 = col_s3.text_input("Label 3", "Ownership")
    f_title = st.text_input("Feat. Title", "Value Pillars")
    feat_data_input = st.text_area("Feat. List", key="feat_data", height=150)
    
    st.subheader("About")
    about_h_in = st.text_input("About Title", key="about_h")
    about_img = st.text_input("About Img", "https://images.unsplash.com/photo-1543286386-713df548e9cc?q=80&w=1600")
    about_short_in = st.text_area("Short Summary", key="about_short")
    about_long = st.text_area("Full About", "Full text here...", height=200)

with tabs[2]:
    st.subheader("📣 Marketing")
    top_bar_enabled = st.checkbox("Top Promo Bar")
    top_bar_text = st.text_input("Promo Text", "🔥 50% OFF Launch Sale!")
    top_bar_link = st.text_input("Promo Link", "#pricing")
    
    popup_enabled = st.checkbox("Exit Intent Popup")
    popup_title = st.text_input("Popup Title", "Wait! Get the Guide.")
    popup_text = st.text_input("Popup Text", "Free PDF on WhatsApp.")
    popup_cta = st.text_input("Popup Button", "Get it Now")

with tabs[3]:
    st.subheader("💰 Pricing")
    c1, c2, c3 = st.columns(3)
    titan_price = c1.text_input("Our Price", "$199")
    titan_mo = c1.text_input("Our Monthly", "$0")
    wix_name = c2.text_input("Comp. Name", "Wix")
    wix_mo = c2.text_input("Comp. Monthly", "$29/mo")
    save_val = c3.text_input("Total Savings", "$1,466")

    st.subheader("🛒 Store Config")
    st.info("CSV Columns: Name, Price, Description, ImageURLs (split by | ), StripeLink")
    sheet_url = st.text_input("Store CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    col_pay1, col_pay2 = st.columns(2)
    paypal_link = col_pay1.text_input("PayPal Link")
    upi_id = col_pay2.text_input("UPI ID")

with tabs[4]:
    st.subheader("📅 Booking")
    booking_embed = st.text_area("Calendly Embed", height=100)
    booking_title = st.text_input("Book Title", "Book an Appointment")
    
    st.subheader("📰 Blog")
    blog_sheet_url = st.text_input("Blog CSV")
    blog_hero_title = st.text_input("Blog Title", "Insights")

with tabs[5]:
    st.subheader("Legal")
    testi_data = st.text_area("Testimonials", "Name | Quote", height=100)
    faq_data = st.text_area("FAQ", "Q? ? A", height=100)
    priv_txt = st.text_area("Privacy Policy", "Text...", height=100)
    term_txt = st.text_area("Terms", "Text...", height=100)

# --- 5. COMPILER ---

def format_text(text):
    if not text: return ""
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    lines = text.split('\n')
    html = ""
    in_list = False
    for line in lines:
        if line.strip().startswith("* "):
            if not in_list: html += '<ul class="feature-list">'; in_list = True
            html += f'<li>{line.strip()[2:]}</li>'
        else:
            if in_list: html += "</ul>"; in_list = False
            if line.strip(): html += f"<p>{line}</p>"
    if in_list: html += "</ul>"
    return html

def gen_schema():
    s = {"@context":"https://schema.org","@type":"LocalBusiness","name":biz_name,"image":logo_url,"url":prod_url}
    return f'<script type="application/ld+json">{json.dumps(s)}</script>'

def get_theme_css():
    # MODERN THEME VARS
    bg, txt, card, nav = "#ffffff", "#0f172a", "rgba(255,255,255,0.8)", "rgba(255,255,255,0.85)"
    
    if "Midnight" in theme_mode: bg, txt, card, nav = "#0f172a", "#f8fafc", "rgba(30,41,59,0.8)", "rgba(15,23,42,0.9)"
    if "Luxury" in theme_mode: bg, txt, card, nav = "#0a0a0a", "#fbbf24", "rgba(23,23,23,0.8)", "rgba(0,0,0,0.9)"
    if "Cyberpunk" in theme_mode: bg, txt, card, nav = "#050505", "#00ff9d", "rgba(10,10,10,0.9)", "rgba(0,0,0,0.9)"

    align_css = "text-align:center; align-items:center;" if hero_layout == "Center" else "text-align:left; align-items:flex-start;"
    
    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg}; --txt: {text_color}; --card: {card}; --nav: {nav}; }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--b-font); margin: 0; line-height: 1.6; overflow-x: hidden; }}
    body.dark-mode {{ --bg: #0f172a; --txt: #f8fafc; --card: rgba(30,41,59,0.9); --nav: rgba(15,23,42,0.95); }}
    
    h1, h2, h3 {{ font-family: var(--h-font); color: var(--txt); font-weight: 800; line-height: 1.1; margin-bottom: 1rem; text-wrap: balance; }}
    h1 {{ font-size: clamp(2.5rem, 6vw, 5rem); background: linear-gradient(135deg, var(--txt) 0%, var(--p) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
    h2 {{ font-size: clamp(2rem, 4vw, 3rem); }}
    p {{ margin-bottom: 1.5rem; opacity: 0.9; font-size: 1.1rem; line-height: 1.7; }}
    
    /* GLASSMORPHISM UI */
    nav, .card, #cart-modal, #lead-popup {{ backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.1); }}
    
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 24px; }}
    
    /* ULTRA MODERN BUTTONS */
    .btn {{ 
        display: inline-flex; align-items: center; justify-content: center;
        padding: 1rem 2.5rem; border-radius: {border_rad}; font-weight: 700; 
        text-transform: uppercase; letter-spacing: 1px; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer; border: none; text-decoration: none; position: relative; overflow: hidden;
        white-space: normal; line-height: 1.2; text-align: center;
    }}
    .btn-primary {{ background: var(--p); color: white !important; box-shadow: 0 10px 30px -10px var(--p); }}
    .btn-accent {{ background: var(--s); color: white !important; box-shadow: 0 10px 30px -10px var(--s); }}
    .btn:hover {{ transform: translateY(-4px); filter: brightness(1.1); box-shadow: 0 20px 40px -10px rgba(0,0,0,0.3); }}
    
    /* PRODUCT CARDS (Redesigned) */
    .product-card {{ 
        background: var(--card); border-radius: 20px; overflow: hidden; 
        transition: 0.4s; position: relative; border: 1px solid rgba(255,255,255,0.05);
        display: flex; flex-direction: column;
    }}
    .product-card:hover {{ transform: translateY(-10px); box-shadow: 0 30px 60px -15px rgba(0,0,0,0.3); }}
    .prod-img {{ width: 100%; height: 300px; object-fit: cover; background: #f1f5f9; }}
    .card-content {{ padding: 1.5rem; display: flex; flex-direction: column; flex-grow: 1; }}
    .card-content h3 {{ font-size: 1.3rem; margin-bottom: 0.5rem; -webkit-text-fill-color: initial; color: var(--txt); }}
    .price-tag {{ font-size: 1.2rem; font-weight: 900; color: var(--s); margin-bottom: 1rem; display: block; }}
    
    /* NAV */
    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; padding: 1rem 0; background: var(--nav); }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; gap: 2rem; align-items: center; }}
    .nav-links a {{ font-weight: 600; color: var(--txt); opacity: 0.8; transition: 0.2s; text-decoration: none; }}
    .nav-links a:hover {{ opacity: 1; color: var(--s); }}
    
    /* HERO */
    .hero {{ min-height: 90vh; display: flex; flex-direction: column; justify-content: center; position: relative; background: var(--p); padding-top: 80px; overflow: hidden; }}
    .hero-content {{ z-index: 2; width: 100%; max-width: 1280px; margin: 0 auto; padding: 0 24px; display: flex; flex-direction: column; {align_css} }}
    .hero h1 {{ color: white !important; -webkit-text-fill-color: white !important; text-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
    .hero p {{ color: rgba(255,255,255,0.9); max-width: 600px; font-size: 1.25rem; margin-bottom: 2rem; }}
    
    /* GRIDS */
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2.5rem; }}
    .gallery-thumb {{ width: 70px; height: 70px; object-fit: cover; border-radius: 8px; cursor: pointer; border: 2px solid transparent; transition: 0.2s; }}
    .gallery-thumb:hover, .gallery-thumb.active {{ border-color: var(--s); transform: scale(1.05); }}
    
    /* FOOTER (FIXED) */
    footer {{ background: var(--p); padding: 5rem 0; color: white; margin-top: auto; }}
    footer a {{ color: rgba(255,255,255,0.7) !important; text-decoration: none; display: block; margin-bottom: 0.8rem; transition: 0.2s; }}
    footer a:hover {{ color: white !important; transform: translateX(5px); }}
    
    /* UTILS & PADDING FIX */
    section {{ padding: clamp(2rem, 5vw, 4rem) 0; }} /* REDUCED PADDING */
    .reveal {{ opacity: 0; transform: translateY(30px); transition: all 0.8s ease; }}
    .reveal.active {{ opacity: 1; transform: translateY(0); }}
    #top-bar {{ background: var(--s); color: white; text-align: center; padding: 0.8rem; font-weight: 700; font-size: 0.9rem; position: fixed; width: 100%; top: 0; z-index: 1001; }}
    #theme-toggle {{ position: fixed; bottom: 20px; left: 20px; width: 45px; height: 45px; background: var(--card); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; cursor: pointer; z-index: 999; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
    
    /* Social Share Buttons */
    .share-row {{ display: flex; gap: 10px; flex-wrap: wrap; margin-top: 15px; }}
    .share-btn {{ width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 50%; color: white; border: none; cursor: pointer; text-decoration: none; }}
    .share-btn:hover {{ transform: translateY(-3px); filter: brightness(1.1); }}
    .bg-fb {{ background: #1877F2; }} .bg-x {{ background: #000000; }} .bg-li {{ background: #0A66C2; }} .bg-rd {{ background: #FF4500; }} .bg-wa {{ background: #25D366; }} .bg-link {{ background: #64748b; }}

    @media (max-width: 768px) {{
        .hero {{ min-height: 70vh; }}
        .nav-links {{ position: fixed; top: 60px; left: -100%; width: 100%; height: 100vh; background: var(--bg); flex-direction: column; padding: 2rem; align-items: flex-start; transition: 0.3s; }}
        .nav-links.active {{ left: 0; }}
        .grid-3, .about-grid, .contact-grid {{ grid-template-columns: 1fr !important; gap: 3rem; }}
        h1 {{ font-size: 2.8rem; }}
        .detail-view {{ grid-template-columns: 1fr !important; }}
    }}
    """

def gen_common_js():
    clean_wa = wa_num.replace("+", "").replace(" ", "")
    return f"""
    <script>
    // SCROLL ANIMATION
    window.addEventListener('scroll', () => {{
        document.querySelectorAll('.reveal').forEach(r => {{
            if(r.getBoundingClientRect().top < window.innerHeight - 100) r.classList.add('active');
        }});
    }});
    // MOBILE MENU
    function toggleMenu() {{ document.querySelector('.nav-links').classList.toggle('active'); }}
    
    // LANGUAGE SWITCHER (FIXED - NO MODAL, INSTANT SWAP)
    async function toggleLang() {{
        try {{
            const res = await fetch('{lang_sheet}');
            const txt = await res.text();
            const rows = txt.split(/\\r\\n|\\n/);
            rows.forEach(row => {{
                // Robust CSV parse for simple key,value
                const parts = row.split(',');
                if(parts.length >= 2) {{
                    const key = parts[0].trim();
                    const val = parts.slice(1).join(',').replace(/"/g, '').trim();
                    const el = document.getElementById(key);
                    if(el) el.innerText = val;
                }}
            }});
            // Toast Notification
            const t = document.createElement('div');
            t.innerText = "Language Switched 🇪🇸";
            t.style.cssText = "position:fixed; top:20px; right:20px; background:#10b981; color:white; padding:10px 20px; border-radius:8px; z-index:9999; box-shadow:0 10px 30px rgba(0,0,0,0.2);";
            document.body.appendChild(t);
            setTimeout(() => t.remove(), 2500);
        }} catch(e) {{ console.log(e); }}
    }}
    
    // CART LOGIC
    let cart = JSON.parse(localStorage.getItem('titanCart')) || [];
    function addToCart(name, price) {{
        cart.push({{name, price}});
        localStorage.setItem('titanCart', JSON.stringify(cart));
        alert(name + " added to cart");
        updateCartDisplay();
    }}
    function updateCartDisplay() {{
        const el = document.getElementById('cart-count');
        if(el) el.innerText = cart.length;
        if(cart.length > 0) document.getElementById('cart-float').style.display = 'flex';
    }}
    function checkout() {{
        let msg = "Order:%0A";
        cart.forEach(i => {{ msg += `- ${{i.name}} (${{i.price}})%0A`; }});
        window.open(`https://wa.me/{clean_wa}?text=${{msg}}`, '_blank');
        cart = []; localStorage.setItem('titanCart', '[]'); updateCartDisplay();
    }}
    window.addEventListener('load', updateCartDisplay);
    </script>
    """

def build_page(title, content):
    pwa = f'<link rel="manifest" href="manifest.json"><meta name="theme-color" content="{p_color}">'
    nav_top = "40px" if top_bar_enabled else "0px"
    
    html = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | {biz_name}</title>
        {pwa}
        <link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@400;700;900&family={b_font.replace(' ', '+')}:wght@300;400;600&display=swap" rel="stylesheet">
        <style>{get_theme_css()}</style>
    </head>
    <body style="padding-top:{nav_top}">
        {gen_nav()}
        {content}
        {gen_footer()}
        {gen_wa_widget()}
        <div id="cart-float" onclick="checkout()" style="position:fixed; bottom:100px; right:30px; background:var(--p); color:white; padding:15px; border-radius:50px; display:none; cursor:pointer; z-index:998; box-shadow:0 10px 30px rgba(0,0,0,0.2);">
            🛒 <span id="cart-count" style="margin-left:5px; font-weight:bold;">0</span>
        </div>
        <div id="theme-toggle" onclick="document.body.classList.toggle('dark-mode')">🌓</div>
        {gen_common_js()}
    </body>
    </html>"""
    return html

# --- GENERATORS WITH NEW UI ---

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
            const res = await fetch('{blog_sheet_url}');
            const raw = await res.text();
            const rows = raw.split(/\\r\\n|\\n/).slice(1);
            const box = document.getElementById('blog-grid');
            box.innerHTML = '';
            
            for(let row of rows) {{
                const c = parseCSVLine(row);
                if(c.length > 4) {{
                    box.innerHTML += `
                    <div class="product-card reveal">
                        <img src="${{c[5]}}" class="prod-img">
                        <div class="card-content">
                            <span class="blog-badge">${{c[3]}}</span>
                            <h3><a href="post.html?id=${{c[0]}}">${{c[1]}}</a></h3>
                            <p>${{c[4].substring(0,100)}}...</p>
                            <a href="post.html?id=${{c[0]}}" class="btn btn-primary" style="margin-top:auto; width:100%;">Read More</a>
                        </div>
                    </div>`;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadBlog();
    </script>
    """

def gen_blog_post():
    # FULL SOCIAL SHARE SUITE + REDDIT
    return f"""
    <div id="blog-content" style="padding: 100px 0;">Loading...</div>
    <script>
    function parseCSV(str) {{
        const arr = []; let quote = false; let c = '';
        for(let x of str) {{ if(x === '"') quote = !quote; else if(x === ',' && !quote) {{ arr.push(c); c = ''; }} else c += x; }}
        arr.push(c); return arr;
    }}
    async function init() {{
        const id = new URLSearchParams(window.location.search).get('id');
        const res = await fetch('{blog_sheet_url}');
        const raw = await res.text();
        const rows = raw.split(/\\r\\n|\\n/).slice(1);
        const container = document.getElementById('blog-content');
        
        for(let row of rows) {{
            const col = parseCSV(row);
            if(col[0] === id) {{
                const url = encodeURIComponent(window.location.href);
                const title = encodeURIComponent(col[1]);
                let body = col[6].replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>').replace(/\\n/g, '<br>');
                
                container.innerHTML = `
                    <div style="background:var(--p); padding:6rem 1rem; text-align:center; color:white;">
                        <div class="container">
                            <span class="blog-badge">${{col[3]}}</span>
                            <h1 style="margin-top:1rem; color:white!important;">${{col[1]}}</h1>
                            <p style="opacity:0.8;">${{col[2]}}</p>
                        </div>
                    </div>
                    <div class="container" style="max-width:800px; margin-top:-3rem; position:relative; z-index:2;">
                        <img src="${{col[5]}}" style="width:100%; border-radius:20px; box-shadow:0 20px 50px rgba(0,0,0,0.2);">
                        <div style="background:var(--card); padding:3rem; border-radius:20px; margin-top:2rem; backdrop-filter:blur(12px);">
                            <div style="font-size:1.1rem; line-height:1.8;">${{body}}</div>
                            
                            <div style="margin-top:3rem; padding-top:2rem; border-top:1px solid rgba(0,0,0,0.1);">
                                <h4>Share This Post</h4>
                                <div class="share-row">
                                    <a href="https://www.facebook.com/sharer/sharer.php?u=${{url}}" target="_blank" class="share-btn bg-fb" title="Facebook"><svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" fill="white"/></svg></a>
                                    <a href="https://twitter.com/intent/tweet?text=${{title}}&url=${{url}}" target="_blank" class="share-btn bg-x" title="X"><svg viewBox="0 0 24 24"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584l-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z" fill="white"/></svg></a>
                                    <a href="https://www.linkedin.com/sharing/share-offsite/?url=${{url}}" target="_blank" class="share-btn bg-li" title="LinkedIn"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2a2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zM4 2a2 2 0 1 1-2 2a2 2 0 0 1 2-2z" fill="white"/></svg></a>
                                    <a href="https://www.reddit.com/submit?url=${{url}}&title=${{title}}" target="_blank" class="share-btn bg-rd" title="Reddit"><svg viewBox="0 0 24 24"><path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0zm5.01 4.744c.688 0 1.25.561 1.25 1.249a1.25 1.25 0 0 1-2.498.056l-2.597-.547-.8 3.747c1.824.07 3.48.632 4.674 1.488.308-.309.73-.491 1.207-.491.968 0 1.754.786 1.754 1.754 0 .716-.435 1.333-1.01 1.614a3.111 3.111 0 0 1 .042.52c0 2.694-3.13 4.87-7.004 4.87-3.874 0-7.004-2.176-7.004-4.87 0-.183.015-.366.043-.534A1.748 1.748 0 0 1 4.028 12c0-.968.786-1.754 1.754-1.754.463 0 .898.196 1.207.49 1.207-.883 2.878-1.43 4.744-1.487l.885-4.182a.342.342 0 0 1 .14-.197.35.35 0 0 1 .238-.042l2.906.617a1.214 1.214 0 0 1 1.108-.701z" fill="white"/></svg></a>
                                    <a href="https://wa.me/?text=${{title}} ${{url}}" target="_blank" class="share-btn bg-wa" title="WhatsApp"><svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z" fill="white"/></svg></a>
                                    <button onclick="navigator.clipboard.writeText(window.location.href);alert('Link Copied!')" class="share-btn bg-link" title="Copy Link"><svg viewBox="0 0 24 24"><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z" fill="white"/></svg></button>
                                </div>
                            </div>
                            <a href="blog.html" class="btn btn-primary" style="margin-top:2rem;">&larr; Back to Blog</a>
                        </div>
                    </div>
                `;
            }}
        }}
    }}
    init();
    </script>
    """

def gen_product_page():
    # MULTI-IMAGE GALLERY SUPPORT + MODERN UI
    return f"""
    <section style="padding:150px 0;"><div class="container" id="prod-box">Loading...</div></section>
    <script>
    function parseCSV(str) {{
        const arr = []; let quote = false; let c = '';
        for(let x of str) {{ if(x === '"') quote = !quote; else if(x === ',' && !quote) {{ arr.push(c); c = ''; }} else c += x; }}
        arr.push(c); return arr;
    }}
    function changeImg(src) {{ document.getElementById('main-img').src = src; }}
    
    async function init() {{
        const id = new URLSearchParams(window.location.search).get('item');
        const res = await fetch('{sheet_url}');
        const rows = (await res.text()).split(/\\r\\n|\\n/).slice(1);
        
        for(let row of rows) {{
            const col = parseCSV(row);
            if(col[0] === id) {{
                // Handle Multi Images (Split by |)
                let images = col[3].split('|').map(s => s.trim());
                let thumbHTML = '';
                images.forEach(img => {{
                    thumbHTML += `<img src="${{img}}" class="gallery-thumb" onclick="changeImg('${{img}}')">`;
                }});
                
                let btn = col[4] ? `<a href="${{col[4]}}" class="btn btn-primary">Buy Now</a>` : `<button onclick="addToCart('${{col[0]}}','${{col[1]}}')" class="btn btn-primary">Add to Cart</button>`;
                
                document.getElementById('prod-box').innerHTML = `
                    <div class="detail-view">
                        <div>
                            <img id="main-img" src="${{images[0]}}" style="width:100%; border-radius:20px; margin-bottom:1rem; box-shadow:0 10px 30px rgba(0,0,0,0.1);">
                            <div style="display:flex; gap:10px;">${{thumbHTML}}</div>
                        </div>
                        <div>
                            <h1 style="line-height:1.1; margin-bottom:0.5rem;">${{col[0]}}</h1>
                            <p style="font-size:1.5rem; font-weight:900; color:var(--s); margin-bottom:1.5rem;">${{col[1]}}</p>
                            <p style="opacity:0.9; margin-bottom:2rem;">${{col[2]}}</p>
                            ${{btn}}
                        </div>
                    </div>
                `;
            }}
        }}
    }}
    init();
    </script>
    """

def gen_booking_content():
    return f"""
    <section class="hero" style="min-height:40vh; background:var(--p);">
        <div class="container hero-content"><h1>{booking_title}</h1><p>{booking_desc}</p></div>
    </section>
    <section>
        <div class="container" style="text-align:center;">
            <div style="background:white; border-radius:20px; overflow:hidden; box-shadow:0 20px 60px rgba(0,0,0,0.1); width:100%;">
                {booking_embed}
            </div>
        </div>
    </section>
    """

def gen_inventory_js(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""
    {gen_csv_parser()}
    <script>
    {demo_flag}
    async function loadInv() {{
        try {{
            const res = await fetch('{sheet_url}');
            const raw = await res.text();
            const rows = raw.split(/\\r\\n|\\n/).slice(1);
            const box = document.getElementById('inv-grid');
            if(!box) return;
            box.innerHTML = '';
            for(let row of rows) {{
                const c = parseCSVLine(row);
                if(c.length > 1) {{
                    let img = c[3].split('|')[0] || '{custom_feat}';
                    let link = encodeURIComponent(c[0]);
                    box.innerHTML += `
                    <div class="product-card reveal">
                        <img src="${{img}}" class="prod-img" loading="lazy">
                        <div class="card-content">
                            <h3>${{c[0]}}</h3>
                            <span class="price-tag">${{c[1]}}</span>
                            <a href="product.html?item=${{link}}" class="btn btn-primary" style="margin-top:auto; width:100%;">View Details</a>
                        </div>
                    </div>`;
                }}
            }}
        }} catch(e) {{}}
    }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);
    </script>
    """

# --- 6. LAUNCHPAD ---
c1, c2 = st.columns([3, 1])
with c2:
    if st.button("🚀 DOWNLOAD WEBSITE", type="primary"):
        z = io.BytesIO()
        with zipfile.ZipFile(z, "a", zipfile.ZIP_DEFLATED, False) as zf:
            # Home
            zf.writestr("index.html", build_page("Home", home_content))
            # Blog
            zf.writestr("blog.html", build_page("Blog", gen_blog_index_html()))
            zf.writestr("post.html", build_page("Article", gen_blog_post()))
            # Product
            zf.writestr("product.html", build_page("Product", gen_product_page()))
            # Others
            zf.writestr("contact.html", build_page("Contact", contact_content))
            zf.writestr("booking.html", build_page("Book", gen_booking_content()))
            zf.writestr("about.html", build_page("About", f"{gen_inner_header(about_h_in)}<div class='container' style='max-width:800px; padding:3rem 0;'>{format_text(about_long)}</div>"))
            zf.writestr("privacy.html", build_page("Privacy", f"{gen_inner_header('Privacy Policy')}<div class='container' style='padding:3rem 0;'>{format_text(priv_txt)}</div>"))
            zf.writestr("terms.html", build_page("Terms", f"{gen_inner_header('Terms of Service')}<div class='container' style='padding:3rem 0;'>{format_text(term_txt)}</div>"))
            
            # Helper files
            zf.writestr("robots.txt", "User-agent: *\\nAllow: /")
            zf.writestr("manifest.json", gen_pwa_manifest())
            zf.writestr("service-worker.js", gen_sw())
            
        st.download_button("📥 Save Zip", z.getvalue(), "titan_site.zip", "application/zip")

# --- PREVIEW LOGIC ---
if 'home_content' not in locals():
    home_content = ""
    if show_hero: home_content += gen_hero()
    if show_stats: home_content += gen_stats()
    if show_features: home_content += gen_features()
    if show_pricing: home_content += gen_pricing_table()
    if show_inventory: home_content += gen_inventory()
    if show_gallery: home_content += gen_about_section()
    if show_faq: home_content += gen_faq_section()
    if show_cta: home_content += f'<section style="background:var(--s); text-align:center; color:white;"><div class="container reveal"><h2>Start Now</h2><a href="contact.html" class="btn" style="background:white; color:var(--s);">Contact</a></div></section>'

# HELPER FOR INNER PAGES
def gen_inner_header(title):
    return f"""<section class="hero" style="min-height: 30vh; background:var(--p);"><div class="container"><h1>{title}</h1></div></section>"""

contact_content = f"""{gen_inner_header("Contact Us")}<section><div class="container"><div class="contact-grid"><div><div class="card"><h3>Get In Touch</h3><p>{biz_addr}</p><p><a href="tel:{biz_phone}">{biz_phone}</a></p><p>{biz_email}</p></div></div><div class="card"><h3>Message Us</h3><form action="https://formsubmit.co/{biz_email}" method="POST"><label>Name</label><input type="text" name="name" required><label>Email</label><input type="email" name="email" required><label>Message</label><textarea name="msg" rows="4" required></textarea><button class="btn btn-primary" type="submit" style="width:100%;">Send</button></form></div></div><br><div style="border-radius:20px;overflow:hidden; box-shadow:0 20px 40px rgba(0,0,0,0.1);">{map_iframe}</div></div></section>"""

with c1:
    prev = st.radio("Preview", ["Home", "Product", "Blog Index", "Blog Post"], horizontal=True)
    if prev == "Home": st.components.v1.html(build_page("Home", home_content), height=600, scrolling=True)
    if prev == "Product": st.components.v1.html(build_page("Prod", gen_product_page()), height=600, scrolling=True)
    if prev == "Blog Index": st.components.v1.html(build_page("Blog", gen_blog_index_html()), height=600, scrolling=True)
    if prev == "Blog Post": st.components.v1.html(build_page("Post", gen_blog_post()), height=600, scrolling=True)
