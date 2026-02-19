import streamlit as st
import zipfile
import io
import json
import re
import requests
import datetime

# --- 0. TITAN CONFIGURATION & STATE ---
st.set_page_config(
    page_title="Titan v50.0 | Quantum Glass", 
    layout="wide", 
    page_icon="💎",
    initial_sidebar_state="expanded"
)

def init_state(key, default_val):
    if key not in st.session_state:
        st.session_state[key] = default_val

# Default Data
init_state('hero_h', "The Future is Faster.")
init_state('hero_sub', "Experience the world's first 0.1s latency architecture. No databases. No lag. Pure speed.")
init_state('feat_data', "bolt|Instant Load|0.1s load times via Edge CDN.\nshield|Zero-DB Security|Unhackable static architecture.\nlayers|Glass UI|Premium aesthetic built-in.")

# --- 1. SIDEBAR: DIAGNOSTICS & CONTROLS ---
with st.sidebar:
    st.title("💎 Titan Architect")
    st.caption("v50.0 | Quantum Glass Edition")
    
    # SYSTEM DIAGNOSTICS (NEW FEATURE)
    with st.expander("🩺 System Diagnostics", expanded=True):
        health_score = 100
        issues = []
        
        if not st.session_state.hero_h: 
            issues.append("❌ Missing Hero Headline")
            health_score -= 20
        
        # Check if email is set (we access the widget key via session state if initialized, else default)
        if 'biz_email' in st.session_state and not st.session_state.biz_email:
             issues.append("⚠️ No Business Email")
             health_score -= 10
            
        st.metric("Health Score", f"{health_score}%", f"{0 if health_score == 100 else -1 * (100-health_score)}")
        
        if issues:
            for i in issues: st.caption(i)
        else:
            st.success("System Optimal")

    # AI GENERATOR
    with st.expander("🤖 AI Neural Writer", expanded=False):
        groq_key = st.text_input("Groq API Key", type="password")
        biz_desc = st.text_input("Business Context")
        if st.button("Generate DNA"):
            if groq_key and biz_desc:
                try:
                    with st.spinner("Synthesizing..."):
                        url = "https://api.groq.com/openai/v1/chat/completions"
                        headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                        prompt = f"Return strictly valid JSON for '{biz_desc}': keys hero_h, hero_sub, feat_data (icon|Title|Desc)."
                        data = {"messages": [{"role": "user", "content": prompt}], "model": "llama3-8b-8192", "response_format": {"type": "json_object"}}
                        resp = requests.post(url, headers=headers, json=data).json()['choices'][0]['message']['content']
                        parsed = json.loads(resp)
                        st.session_state.hero_h = parsed.get('hero_h', "")
                        st.session_state.hero_sub = parsed.get('hero_sub', "")
                        if 'feat_data' in parsed:
                            st.session_state.feat_data = "\n".join(parsed['feat_data']) if isinstance(parsed['feat_data'], list) else parsed['feat_data']
                        st.success("Neural injection complete.")
                        st.rerun()
                except Exception as e: st.error(f"Neural Failure: {e}")

    # VISUAL DNA
    with st.expander("🎨 Visual DNA", expanded=True):
        theme_mode = st.selectbox("UI Paradigm", ["Glassmorphism (Blur)", "Midnight Cyberpunk", "Clean Corporate", "Luxury Gold"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#2563EB") 
        s_color = c2.color_picker("Accent / CTA", "#F43F5E")
        font_pair = st.selectbox("Typography", ["Inter / Roboto", "Playfair / Lato", "Space Grotesk / Inter"])
        border_rad = st.slider("Glass Radius", 0, 40, 16)

    # MODULES (SMART NAV)
    with st.expander("🧩 Quantum Modules", expanded=False):
        show_hero = st.checkbox("Hero Section", True)
        show_features = st.checkbox("Features Grid", True)
        show_inventory = st.checkbox("Smart Store", True)
        show_blog = st.checkbox("Blog Engine", True)
        show_booking = st.checkbox("Booking Widget", True)
        show_gallery = st.checkbox("About/Gallery", True)
        show_testimonials = st.checkbox("Testimonials", True)
        show_faq = st.checkbox("FAQ Accordion", True)
        
        st.caption("Advanced Features")
        show_cookie = st.checkbox("GDPR Cookie Banner", True)
        show_wa_float = st.checkbox("Floating WhatsApp", True)
        show_dark_toggle = st.checkbox("Frontend Dark Toggle", True)

# --- 2. MAIN INPUTS ---
st.title("💎 StopWebRent: The Quantum Builder")
tabs = st.tabs(["1. Identity", "2. Content", "3. Store", "4. Marketing", "5. Legal & SEO"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "Titan Industries")
        biz_email = st.text_input("Email", "hello@titan.com", key="biz_email")
        biz_phone = st.text_input("Phone", "1234567890")
    with c2:
        prod_url = st.text_input("Live URL", "https://titan.com")
        logo_url = st.text_input("Logo URL")
        biz_addr = st.text_input("Address", "Silicon Valley, CA")

    st.subheader("Social & PWA")
    sc1, sc2 = st.columns(2)
    wa_num = sc1.text_input("WhatsApp (No +)", "1234567890")
    lang_sheet = sc2.text_input("Translation CSV URL")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", st.session_state.hero_h)
    hero_sub = st.text_input("Hero Subtext", st.session_state.hero_sub)
    hero_img = st.text_input("Hero Background Image", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1600")
    
    st.markdown("### Feature Grid")
    feat_data_input = st.text_area("Icon | Title | Desc", st.session_state.feat_data, height=100)

    st.markdown("### About Section")
    about_h = st.text_input("About Title", "Our Story")
    about_txt = st.text_area("About Text", "We are building the future...", height=100)
    about_img = st.text_input("About Image", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=800")

with tabs[2]:
    st.info("💡 **Pro Tip:** For multiple images, separate URLs with `|` in your CSV. Example: `img1.jpg | img2.jpg`")
    sheet_url = st.text_input("Store CSV URL", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Fallback Image", "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=800")
    
    pc1, pc2 = st.columns(2)
    paypal_link = pc1.text_input("PayPal.me Link")
    upi_id = pc2.text_input("UPI ID")

with tabs[3]:
    st.subheader("Booking & Blog")
    booking_embed = st.text_area("Calendly Embed Code", height=100)
    blog_sheet = st.text_input("Blog CSV URL")
    
    st.subheader("Social Proof")
    testi_data = st.text_area("Testimonials (Name|Quote)", "Elon|This is the future.\nJeff|Incredible speed.")
    faq_data = st.text_area("FAQ (Q? ? A)", "Is it fast? ? Yes, 0.1s.")

with tabs[4]:
    seo_d = st.text_area("Meta Description", "The fastest website on earth.")
    seo_kw = st.text_input("Keywords", "speed, design, glassmorphism")
    priv_txt = st.text_area("Privacy Policy", "Standard privacy text...")
    term_txt = st.text_area("Terms of Service", "Standard terms...")
    cookie_txt = st.text_input("Cookie Text", "We use cookies to enhance the quantum experience.")

# --- 3. THE QUANTUM COMPILER ---

def get_theme_css():
    # Visual Logic
    h_font = font_pair.split("/")[0].strip()
    b_font = font_pair.split("/")[1].strip()
    
    # Theme Presets
    bg, txt, glass_bg, glass_border = "#ffffff", "#0f172a", "rgba(255, 255, 255, 0.7)", "rgba(255, 255, 255, 0.3)"
    
    if "Midnight" in theme_mode:
        bg, txt, glass_bg, glass_border = "#050505", "#e2e8f0", "rgba(20, 20, 20, 0.7)", "rgba(255, 255, 255, 0.1)"
    elif "Glassmorphism" in theme_mode:
        bg = "linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%)"
    elif "Luxury Gold" in theme_mode:
        bg, txt, glass_bg, glass_border = "#1a1a1a", "#d4af37", "rgba(30,30,30,0.85)", "rgba(212,175,55,0.2)"
        
    return f"""
    :root {{
        --p: {p_color}; --s: {s_color}; --bg: {bg}; --txt: {txt};
        --glass: {glass_bg}; --border: {glass_border};
        --radius: {border_rad}px;
        --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif;
    }}
    
    /* RESET & CORE */
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ 
        background: var(--bg); color: var(--txt); font-family: var(--b-font); 
        line-height: 1.6; overflow-x: hidden; transition: background 0.3s, color 0.3s;
    }}
    
    /* DARK MODE OVERRIDES */
    body.dark-mode {{
        --bg: #0f172a; --txt: #f8fafc; 
        --glass: rgba(30, 41, 59, 0.7); --border: rgba(255, 255, 255, 0.05);
    }}

    h1, h2, h3 {{ font-family: var(--h-font); font-weight: 800; line-height: 1.1; }}
    a {{ text-decoration: none; color: inherit; transition: 0.3s; }}
    
    /* GLASSMORPHISM UTILS */
    .glass {{
        background: var(--glass);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
    }}
    
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
    .section-pad {{ padding: clamp(3rem, 5vw, 6rem) 0; }}
    
    /* NAVIGATION */
    nav {{ 
        position: fixed; top: 20px; left: 50%; transform: translateX(-50%); 
        width: 90%; max-width: 1200px; z-index: 1000;
        padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center;
    }}
    .nav-links {{ display: flex; gap: 2rem; align-items: center; }}
    .nav-links a {{ font-weight: 600; opacity: 0.8; font-size: 0.9rem; }}
    .nav-links a:hover {{ opacity: 1; color: var(--s); }}
    
    /* HERO */
    .hero {{ 
        min-height: 100vh; display: flex; align-items: center; justify-content: center;
        background-image: url('{hero_img}'); background-size: cover; background-position: center;
        position: relative; text-align: center; color: white;
    }}
    .hero::before {{ content:''; position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.4); }}
    .hero-content {{ position: relative; z-index: 2; max-width: 800px; animation: fadeInUp 1s ease-out; }}
    .hero h1 {{ 
        font-size: clamp(3rem, 6vw, 5rem); margin-bottom: 1rem; 
        background: linear-gradient(to right, #fff, #e2e8f0); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    
    @keyframes fadeInUp {{ from {{ opacity:0; transform:translateY(30px); }} to {{ opacity:1; transform:translateY(0); }} }}
    
    /* ULTRA-MODERN PRODUCT CARDS (APPLE STYLE) */
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 2rem; }}
    
    .product-card {{ 
        display: flex; flex-direction: column; overflow: hidden; transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .product-card:hover {{ transform: translateY(-10px); }}
    .product-img-box {{ 
        height: 300px; width: 100%; background: #f1f5f9; overflow: hidden; border-radius: var(--radius); position: relative;
    }}
    .product-img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
    .product-card:hover .product-img {{ transform: scale(1.05); }}
    .product-details {{ padding: 1.5rem 0.5rem; text-align: center; }}
    .product-title {{ font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem; }}
    .product-price {{ color: var(--s); font-weight: 600; margin-bottom: 1rem; display: block; }}
    
    /* BUTTONS */
    .btn {{ 
        padding: 0.8rem 2rem; border-radius: 50px; font-weight: 700; cursor: pointer; border: none;
        display: inline-block; transition: 0.3s;
    }}
    .btn-primary {{ background: var(--p); color: white; }}
    .btn-accent {{ background: var(--s); color: white; }}
    .btn:hover {{ transform: scale(1.05); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
    
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
    .thumb:hover, .thumb.active {{ opacity: 1; border-color: var(--p); }}
    
    /* TOAST NOTIFICATIONS */
    #toast-box {{ position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%); z-index: 9999; display: flex; flex-direction: column; gap: 10px; }}
    .toast {{ 
        background: var(--txt); color: var(--bg); padding: 12px 24px; border-radius: 50px; 
        font-weight: 600; box-shadow: 0 10px 30px rgba(0,0,0,0.2); 
        opacity: 0; transform: translateY(20px); transition: 0.4s;
    }}
    .toast.show {{ opacity: 1; transform: translateY(0); }}
    
    /* FLOATING ELEMENTS */
    .float-btn {{ 
        position: fixed; width: 50px; height: 50px; border-radius: 50%; 
        display: flex; align-items: center; justify-content: center; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); z-index: 990; cursor: pointer;
    }}
    #wa-float {{ bottom: 100px; right: 30px; background: #25D366; color: white; }}
    #cart-float {{ bottom: 30px; right: 30px; background: var(--p); color: white; }}
    #mode-toggle {{ bottom: 30px; left: 30px; background: var(--glass); color: var(--txt); }}

    /* RESPONSIVE */
    @media (max-width: 768px) {{
        .nav-links {{ display: none; position: absolute; top: 70px; left: 0; width: 100%; background: var(--glass); flex-direction: column; padding: 2rem; }}
        .nav-links.active {{ display: flex; }}
        .detail-container {{ grid-template-columns: 1fr; padding-top: 100px; }}
        .hero h1 {{ font-size: 2.5rem; }}
        .gallery-main {{ height: 350px; }}
    }}
    """

def gen_js_engine():
    # JavaScript Engine for Logic, Cart, Gallery, and UI States
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

    // --- 4. CSV PARSER & STORE LOGIC ---
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
            list.innerHTML += `<div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                <span>${{item.name}}</span>
                <span>${{item.price}} <b onclick="cart.splice(${{i}},1);localStorage.setItem('titanCart',JSON.stringify(cart));renderCartItems();updateCartUI()" style="color:red;cursor:pointer;">×</b></span>
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

    // --- 6. TRANSLATION ENGINE ---
    async function toggleLang() {{
        // Logic to fetch CSV and swap text would go here
        showToast('🌐 Language Switched (Demo)');
    }}

    window.addEventListener('load', updateCartUI);
    
    // COOKIE BANNER
    setTimeout(() => {{
        if(!localStorage.getItem('cookieAccepted')) 
            document.getElementById('cookie-banner').style.transform = 'translateY(0)';
    }}, 2000);
    
    function acceptCookies() {{
        localStorage.setItem('cookieAccepted', 'true');
        document.getElementById('cookie-banner').style.transform = 'translateY(100%)';
    }}
    </script>
    """

def gen_html_components():
    # Generators for HTML sections
    
    # NAVIGATION (SMART NAV)
    nav_links = f'<a href="index.html">Home</a>'
    if show_features: nav_links += '<a href="index.html#features">Features</a>'
    if show_inventory: nav_links += '<a href="index.html#store">Store</a>'
    if show_blog: nav_links += '<a href="blog.html">Blog</a>'
    nav_links += '<a href="contact.html">Contact</a>'
    
    nav_html = f"""
    <nav class="glass">
        <div style="font-weight:900; font-size:1.2rem;">{biz_name}</div>
        <div class="nav-links">
            {nav_links}
            <a href="#" onclick="toggleLang()">🌐</a>
        </div>
        <div style="font-size:1.5rem; cursor:pointer;" class="mobile-toggle" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</div>
    </nav>
    """
    
    # FLOATING WIDGETS
    floats = f"""
    <div id="toast-box"></div>
    {f'<div class="float-btn" id="mode-toggle" onclick="toggleTheme()">🌓</div>' if show_dark_toggle else ''}
    {f'<a href="https://wa.me/{wa_num.replace("+","")}" target="_blank" class="float-btn" id="wa-float"><svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.008-.57-.008-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></path></svg></a>' if show_wa_float else ''}
    <div class="float-btn" id="cart-float" onclick="toggleCart()" style="display:none">🛒 <span id="cart-count">0</span></div>
    
    <div id="cart-modal" class="glass" style="display:none; position:fixed; top:50%; left:50%; transform:translate(-50%,-50%); padding:2rem; z-index:2000; width:90%; max-width:400px;">
        <h3>Your Cart</h3><hr style="margin:10px 0; opacity:0.2">
        <div id="cart-items"></div>
        <div style="margin-top:20px; font-weight:bold;">Total: <span id="cart-total">0.00</span></div>
        <button class="btn btn-accent" style="width:100%; margin-top:10px;" onclick="checkout()">Checkout</button>
        <button class="btn" style="width:100%; margin-top:5px; background:transparent;" onclick="toggleCart()">Close</button>
    </div>

    {f'<div id="cookie-banner" class="glass" style="position:fixed; bottom:0; left:0; width:100%; padding:1rem; transform:translateY(100%); transition:0.5s; z-index:9000; display:flex; justify-content:space-between; align-items:center;"><div>{cookie_txt}</div><button class="btn btn-primary" onclick="acceptCookies()">Accept</button></div>' if show_cookie else ''}
    """
    
    return nav_html, floats

def gen_hero():
    return f"""
    <header class="hero">
        <div class="hero-content">
            <h1>{hero_h}</h1>
            <p style="font-size:1.2rem; opacity:0.9; margin-bottom:2rem;">{hero_sub}</p>
            <div style="display:flex; gap:1rem; justify-content:center;">
                <a href="#store" class="btn btn-primary">Explore Collection</a>
                <a href="#about" class="btn glass">Our Story</a>
            </div>
        </div>
    </header>
    """

def gen_inventory_js(is_demo=False):
    demo_val = "true" if is_demo else "false"
    return f"""
    <script>
    const isDemo = {demo_val};
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
                    <div class="product-card glass">
                        <div class="product-img-box">
                            <img src="${{mainImg}}" class="product-img">
                        </div>
                        <div class="product-details">
                            <div class="product-title">${{title}}</div>
                            <span class="product-price">${{price}}</span>
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
    # This generates the logic for the product.html file
    # It parses the CSV again client-side to find the specific item and render the gallery
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
            if(row[0] === target || (isDemo && i===1)) {{
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

def build_page(title, body_content, page_type="home"):
    # Meta Tags for SEO Injection
    meta_tags = f"""
    <meta name="description" content="{seo_d}">
    <meta property="og:title" content="{title} | {biz_name}">
    <meta property="og:description" content="{seo_d}">
    <meta property="og:image" content="{logo_url}">
    <meta property="og:type" content="website">
    """
    
    nav, floats = gen_html_components()
    css = get_theme_css()
    js = gen_js_engine()
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | {biz_name}</title>
        {meta_tags}
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Playfair+Display:wght@700&family=Space+Grotesk:wght@700&display=swap" rel="stylesheet">
        <style>{css}</style>
    </head>
    <body>
        {nav}
        {body_content}
        {floats}
        
        <footer class="section-pad" style="background:var(--txt); color:var(--bg); margin-top:4rem;">
            <div class="container" style="text-align:center;">
                <h3>{biz_name}</h3>
                <p style="opacity:0.7">{biz_addr}</p>
                <div style="margin-top:2rem; opacity:0.5; font-size:0.9rem;">
                    &copy; {datetime.datetime.now().year} {biz_name}. Built with Titan.
                    <br><a href="privacy.html">Privacy</a> | <a href="terms.html">Terms</a>
                </div>
            </div>
        </footer>
        
        {js}
    </body>
    </html>
    """

# --- 4. PREVIEW & EXPORT ENGINE ---

# Assemble Home Body
home_body = ""
if show_hero: home_body += gen_hero()
if show_features: 
    feats = "".join([f'<div class="product-card glass" style="padding:2rem;"><div style="font-size:2rem; color:var(--s); margin-bottom:1rem;">{line.split("|")[0]}</div><h3>{line.split("|")[1]}</h3><p>{line.split("|")[2]}</p></div>' for line in feat_data_input.split('\n') if "|" in line])
    home_body += f'<section id="features" class="section-pad"><div class="container"><h2 style="text-align:center; margin-bottom:3rem;">Why Choose Us</h2><div class="grid-3">{feats}</div></div></section>'

if show_inventory:
    home_body += f'<section id="store" class="section-pad" style="background:rgba(0,0,0,0.02)"><div class="container"><h2 style="text-align:center; margin-bottom:3rem;">Latest Collection</h2><div id="store-grid" class="grid-3"></div></div></section>{gen_inventory_js()}'

if show_gallery:
    home_body += f'<section id="about" class="section-pad"><div class="container detail-container" style="padding-top:0;"><img src="{about_img}" style="width:100%; border-radius:var(--radius);"><div><h2>{about_h}</h2><p>{about_txt}</p></div></div></section>'

# Preview Tabs
st.divider()
c1, c2 = st.columns([3, 1])

with c1:
    prev_mode = st.radio("Live View", ["Home", "Product Detail", "Blog", "Legal"], horizontal=True)
    if prev_mode == "Home":
        st.components.v1.html(build_page("Home", home_body), height=700, scrolling=True)
    elif prev_mode == "Product Detail":
        st.components.v1.html(build_page("Product", gen_product_page_content(True)), height=700, scrolling=True)
    elif prev_mode == "Legal":
        st.components.v1.html(build_page("Privacy", f"<div class='container section-pad'><h1>Privacy Policy</h1><p>{priv_txt}</p></div>"), height=700, scrolling=True)

with c2:
    st.success("Quantum Core: Active")
    if st.button("DOWNLOAD TITAN ZIP", type="primary"):
        z = io.BytesIO()
        with zipfile.ZipFile(z, "a", zipfile.ZIP_DEFLATED, False) as zf:
            # Core
            zf.writestr("index.html", build_page("Home", home_body))
            zf.writestr("product.html", build_page("Product", gen_product_page_content(False)))
            # Content
            zf.writestr("privacy.html", build_page("Privacy Policy", f"<div class='container section-pad'><h1>Privacy Policy</h1><div class='glass' style='padding:2rem'>{priv_txt}</div></div>"))
            zf.writestr("terms.html", build_page("Terms", f"<div class='container section-pad'><h1>Terms</h1><div class='glass' style='padding:2rem'>{term_txt}</div></div>"))
            zf.writestr("contact.html", build_page("Contact", f"<div class='container section-pad'><h1>Contact Us</h1><p>{biz_addr}</p><p>{biz_email}</p></div>"))
            # Assets
            if show_blog: zf.writestr("blog.html", build_page("Blog", "<div class='container section-pad'><h1>Blog</h1><p>Loading...</p></div>"))
            
        st.download_button("📥 Save Package", z.getvalue(), "titan_v50_quantum.zip", "application/zip")
