import streamlit as st
from PIL import Image
import os
import random
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Character Reveal", page_icon="⭐", layout="centered")

# --- 2. CUSTOM STAR ANIMATION FUNCTION ---
def let_it_star():
    colors =["#FFD700", "#FF4500", "#00FF00", "#1E90FF", "#FF69B4", "#9400D3", "#00FFFF"]
    
    css_code = """
    <style>
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }
    .star {
        position: fixed;
        top: -10vh;
        font-size: 1cm;
        z-index: 99999;
        animation-name: fall;
        animation-timing-function: linear;
        animation-fill-mode: forwards;
        pointer-events: none;
    }
    </style>
    """
    
    html_code = "<div id='star-container'>"
    for _ in range(60):
        left_position = random.randint(0, 100)
        fall_duration = random.uniform(2.5, 6.0) 
        fall_delay = random.uniform(0, 2)        
        star_color = random.choice(colors)
        
        style = f"left: {left_position}vw; color: {star_color}; animation-duration: {fall_duration}s; animation-delay: {fall_delay}s;"
        html_code += f"<div class='star' style='{style}'>★</div>"
    html_code += "</div>"
    
    st.markdown(css_code + html_code, unsafe_allow_html=True)

# --- 3. HEADER & UI ---
st.title("⭐ Discover Your Character!")
st.markdown("Enter your birth date below to see which character you got.")

birth_date = st.number_input("Select your birth date:", min_value=1, max_value=31, step=1)

# --- 4. DICTIONARY MAPPING (UPDATED WITH TEXT) ---
# Now it maps the date to BOTH the image path and your custom text!
dct = {
    1: {
        "image": "images/Captain.jpg",
        "text": "The 1st isn’t just a date — it feels like the beginning of something strong and steady. The kind of strength that doesn’t need attention to be noticed. Calm, loyal, and quietly powerful. I may not carry a shield, but I believe in standing firm for what matters. And somehow, your presence feels like something worth protecting. 🛡️❤️✨"
    },
    7: {
        "image": "images/Bucky.jpg",
        "text": "Bucky Barnes is complex, brave, and emotionally strong. Though he struggles with his past as the Winter Soldier, he tries hard to make things right. He is loyal to his friends, especially Captain America, and shows quiet courage. His personality reflects resilience, guilt, redemption, and a deep desire for peace and forgiveness."
    },
    3: {
        "image": "images/Thor.jpg",
        "text": "it a great Barnes is complex, brave, and emotionally strong. Thoug 𝒶𝒾𝓃 𝒜𝓂𝑒𝓇𝒾𝒸𝒶 ✨ 𝒾𝓈 𝒷𝓇𝒶𝓋𝑒 🛡️, 𝒹𝒾𝓈𝒸𝒾𝓅𝓁𝒾𝓃𝑒𝒹 ⚔️, 𝒶𝓃𝒹 𝒹𝑒𝑒𝓅𝓁𝓎 𝓁𝑜𝓎𝒶𝓁 🤝. 𝒽𝑒 𝒷𝑒𝓁𝒾𝑒𝓋𝑒𝓈 𝒾𝓃 𝒿𝓊𝓈𝓉𝒾𝒸𝑒 ⚖️, 𝒻𝓇𝑒𝑒𝒹𝑜𝓂 🕊️, 𝒶𝓃𝒹"
    },
        4: {
        "image": "images/Ancient one.jpg",
        "text": "The Ancient One is calm, wise, and deeply mysterious. She speaks softly but carries immense power within her presence. Her intelligence feels magnetic, drawing others toward her guidance. She values balance and knowledge above ego. With graceful confidence and quiet strength, she teaches that true power comes from understanding, not domination."
    },
    5: {
        "image": "images/Ant man.jpg",
        "text": "Ant-Man is clever, playful, and surprisingly brave. Behind his humor lies a sharp mind and a caring heart. He may joke in tough moments, but when it matters, he stands fearless. His charm feels natural and warm. He proves that even the smallest hero can carry the biggest impact."
    },
    6: {
        "image": "images/Black panther.jpg",
        "text": "Black Panther is royal, disciplined, and powerfully composed. His confidence is quiet but undeniable. He protects his people with strength and intelligence. Every move he makes carries purpose. Beneath his warrior spirit lies compassion and loyalty. He leads not with noise, but with presence and unwavering responsibility."
    },
    2: {
        "image": "images/Dr strange.jpg",
        "text": "February 2nd created someone who thinks deeply, feels quietly, and notices more than he says. Like Doctor Strange, I believe timing matters. Not everything has to be loud to be meaningful. Some moments are subtle, yet unforgettable. And sometimes, the most powerful changes happen without anyone even realizing it. 🔮✨"
    },
    8: {
        "image": "images/Drax.jpg",
        "text": "Drax is blunt, fearless, and unexpectedly pure-hearted. His honesty is raw and unapologetic. Though serious in battle, his innocence creates surprising charm. Loyalty drives his every action. He values friendship deeply and fights with powerful intensity. Beneath his tough exterior lies emotional depth and devotion."
    },
    9: {
        "image": "images/Falcon.jpg",
        "text": "Falcon is disciplined, loyal, and quietly strong. He carries responsibility with confidence and integrity. His grounded nature makes him relatable and inspiring. Brave in action and thoughtful in words, he stands firm for justice. His leadership grows from empathy and courage, not ego."
    },
    10: {
        "image": "images/Gamora.jpg",
        "text": "Gamora is fierce, intelligent, and emotionally layered. Strength defines her presence, yet vulnerability shapes her depth. She carries pain from her past but moves forward with resilience. Her determination feels powerful and captivating. Independent and bold, she fights for redemption and chooses loyalty over fear."
    },
    11: {
        "image": "images/Groot.jpg",
        "text": "Groot is gentle, loyal, and deeply protective. His quiet nature hides a courageous heart. Though his words are few, his actions speak loudly. He values friendship and sacrifice. Strong yet innocent, Groot reminds everyone that true strength often grows from kindness and devotion."
    },
    12: {
        "image": "images/Hawkeye.jpg",
        "text": "Hawkeye is focused, disciplined, and emotionally grounded. He may not seek attention, but his skill speaks clearly. Calm under pressure, he values family and loyalty above glory. His silent strength and sharp precision make him reliable and quietly heroic."
    },
    13: {
        "image": "images/Hulk.jpg",
        "text": "Hulk is powerful, intense, and emotionally complex. Behind his rage lives a mind searching for peace. His strength feels unstoppable, yet his vulnerability makes him human. He struggles with control, but when balanced, he becomes both brilliant and unstoppable."
    },
    26: {
        "image": "images/Iron man.jpg",
        "text": "February 26th created someone who doesn’t wait for perfect moments — he builds them. A little bold, a little sarcastic, but always real. I don’t promise magic tricks or dramatic speeches. Just genuine energy, smart moves, and showing up when it counts. Some things aren’t complicated… they’re just meant to be tried. 🔥✨"
    },
    15: {
        "image": "images/Loki.jpg",
        "text": "Loki is charming, unpredictable, and dangerously intelligent. His words feel smooth, yet his mind always calculates. Mischief dances in his personality, but pain shapes his depth. He seeks recognition and belonging. Mysterious and magnetic, Loki turns chaos into an art form."
    },
    16: {
        "image": "images/Moon knight.jpg",
        "text": "Moon Knight is intense, mysterious, and mentally layered. His personality shifts with emotional depth and hidden strength. He walks between darkness and justice. Fearless and complex, he confronts his inner battles while fighting external enemies with relentless determination."
    },
    17: {
        "image": "images/Natasha.jpg",
        "text": "Natasha is intelligent, graceful, and emotionally controlled. Her calm exterior hides sharp instincts and strategic brilliance. She carries her past with quiet strength. Loyal and fearless, she protects those she loves. Her subtle confidence and composure make her captivating and strong."
    },
    18: {
        "image": "images/Nick fury.jpg",
        "text": "Nick Fury is strategic, commanding, and always three steps ahead. His authority feels natural and undeniable. He trusts carefully and speaks with purpose. Calm under pressure, he leads with intelligence and bold decisions. His presence alone demands respect."
    },
    19: {
        "image": "images/Rocket.jpg",
        "text": "Rocket is sharp-tongued, brilliant, and emotionally guarded. His sarcasm hides deep loyalty and unexpected tenderness. Intelligent and inventive, he thrives in chaos. Though he pushes others away, he cares fiercely. His wit and fire make him unforgettable."
    },
    20: {
        "image": "images/Shang chi.jpg",
        "text": "Shang-Chi is disciplined, humble, and deeply skilled. His calm confidence feels effortless. He carries tradition with respect while forging his own path. Focused and balanced, he fights with grace and purpose. His quiet strength makes him truly powerful."
    },
    21: {
        "image": "images/Spider.jpg",
        "text": "Spider-Man is energetic, intelligent, and kind-hearted. His youthful humor hides strong responsibility. He struggles, learns, and grows with every challenge. Brave beyond fear, he protects others selflessly. His innocence and courage create a naturally charming presence."
    },
    22: {
        "image": "images/Star lord.jpg",
        "text": "Star-Lord is bold, emotional, and effortlessly charismatic. His playful attitude masks deep loyalty. He leads with heart rather than perfection. Confident yet flawed, he fights passionately for those he loves. His charm feels spontaneous and magnetic."
    },
    23: {
        "image": "images/Supergirl.jpg",
        "text": "Supergirl is compassionate, strong, and hopeful. Her power shines through courage and empathy. She stands firm for justice with graceful determination. Confident yet caring, she inspires others to believe in goodness. Her strength feels both powerful and uplifting."
    },
    24: {
        "image": "images/Thanos.jpg",
        "text": "Thanos is calm, calculated, and terrifyingly determined. His belief in balance drives his ruthless decisions. He speaks with quiet certainty and unwavering focus. Powerful and composed, he follows his vision without hesitation, making him both commanding and intimidating."
    },
    25: {
        "image": "images/Vision.jpg",
        "text": "Vision is thoughtful, intelligent, and emotionally curious. Though synthetic, his humanity feels genuine. He values logic and love equally. Calm and philosophical, he seeks understanding in conflict. His quiet wisdom and gentle nature make him uniquely compelling."
    },
    14: {
        "image": "images/Wanda.jpg",
        "text": "On the 14th, it feels like the universe created its own Wanda…🌸 you. Strong, beautiful, and quietly magical. You don’t need chaos magic to change the atmosphere — your smile already does that effortlessly. Being around you feels different, in the best way. There’s something about your presence that turns ordinary moments into memories worth holding onto.💫❤️🌙"
    },
    27: {
        "image": "images/Wolverine.jpg",
        "text": "Wolverine is rugged, fearless, and emotionally guarded. His toughness hides silent pain and loyalty. He protects fiercely and loves deeply, though rarely shows it. Strong, intense, and instinctive, he walks alone but fights for those he respects."
    },
    28: {
        "image": "images/War machine.jpg",
        "text": "War Machine is disciplined, loyal, and battle-hardened. He carries strength with responsibility and stands firm beside his allies. Calm under pressure, he combines military precision with deep friendship. His confidence is steady, not loud. Dependable and courageous, he fights with honor and unwavering commitment."
    },
    29: {
        "image": "images/Flash.jpg",
        "text": "Flash is energetic, confident, and incredibly fast. His playful personality hides a brave heart ready to protect others. He moves with excitement and youthful charm. Even when unsure, he steps forward without hesitation. His speed is powerful, but his determination truly defines him."
    },
    30: {
        "image": "images/Shuri.jpg",
        "text": "Shuri is brilliant, innovative, and naturally confident. Her intelligence shines through creativity and fearless curiosity. She balances science with strength, leading with sharp focus. Calm yet bold, she protects her people with wisdom and power. Her presence feels modern, strong, and inspiring."
    },
    31: {
        "image": "images/Captain marvel.jpg",
        "text": "Captain Marvel is powerful, fearless, and fiercely independent. Her confidence radiates in every battle. She stands tall with unstoppable energy and calm determination. Strong-willed and direct, she protects the universe without doubt. Her strength feels limitless, matched only by her inner resilience."
    }
}

# --- 5. ACTION BUTTON ---
if st.button("Reveal My Character 🚀", type="primary"):
    
    if birth_date in dct:
        character_data = dct[birth_date]
        image_path = character_data["image"]
        description = character_data["text"]
        
        if os.path.exists(image_path):
            with st.spinner("Decoding character file... Building suspense..."):
                time.sleep(3) 
                img = Image.open(image_path)
                
            # 1. Display the image (without the tiny standard caption)
            st.image(img, use_container_width=True)
            
            # 2. Display the text beautifully aligned below the image
            # text-align: justify forces the text to touch exactly the left and right edges!
            st.markdown(
                f"""
                <div style="
                    text-align: justify; 
                    font-size: 18px; 
                    line-height: 1.6; 
                    margin-top: 15px;
                    padding: 10px;
                    background-color: rgba(255, 255, 255, 0.05);
                    border-radius: 8px;">
                    {description}
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # 3. Trigger the stars!
            let_it_star()
                
        else:
            st.error(f"⚠️ Oops! The image '{image_path}' was not found.")
    else:
        st.warning(f"No character has been assigned to date {birth_date} yet!")





