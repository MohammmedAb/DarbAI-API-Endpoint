from fastai.vision.all import *
from PIL import Image

import pathlib

plt = platform.system()
if plt == 'Windows': pathlib.PosixPath = pathlib.WindowsPath
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

learn = load_learner('SaudiLandmarkClassifier.pkl') 

landmark_descriptions = {
    "Al Faisaliah Tower": {
        "description": "The Al Faisaliah Tower, located in Riyadh's al-Olaya district, is a commercial skyscraper and mixed-use complex, noted for being Saudi Arabia's first skyscraper",
        "image_url":"https://res.cloudinary.com/dr2baapqk/image/upload/v1701290040/33325463182_40892081ff_b_jo4ntl.jpg"
    },
    "Al Masmak Palace": {
        "description": "The palace was constructed in the hijri 14th century during the reign of Imam Abdullah bin Faisal as his residence and the center of power and money. The palace is a strong fort against enemies with its solid high walls. It has only two entrances and small openings in the walls for gun barrels at the time of battles. Today, the palace stands as a symbol of the history of regaining power and rule of the country displaying in its corridors the features of that era and its leaders after it had been turned into a museum in 1995/1416",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290013/9-al-masmak-palace-museum-riyadh-province_muph7i.jpg"
    },
    "Al Rahmah Mosque": {
        "description": "one of the most distinctive symbols of Jeddah. The Floating Mosque was built in 1985 on a water surface, with bases planted under the surface of the sea. It is marked by its bright white color and its turquoise dome which paints a wonderful scene especially when the sun shines on it to reflect the beauty of architecture joined with Islamic and traditional constructive art",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290050/Al-Rahma-Mosque_pglkal.jpg"
    },
    "Diriyah": {
        "description": "Diriyah has always been of new beginnings, a source of Saudi identity and national pride. A place of history and heritage, Diriyah, was born on an ancient crossroads of culture and trade, and rises through gatherings of artists, merchants and scientists into a globally connected city",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290128/Screenshot_2023-11-29_204814_lw4dch.png"
    },
    "Hegra": {
        "description": "Also known as Al-Hijr or Madain Saleh, is an ancient archaeological site located in the Al-Ula sector, within the Al Madinah Region of Saudi Arabia. A former Nabatean city, it's known for its well-preserved rock-cut tombs with intricate facades, dating back to the 1st century AD. It's Saudi Arabia's first UNESCO World Heritage Site, showcasing the Nabateans' architectural and engineering prowess",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290059/Hegra-1536x1024_djpash.jpg"
    },
    "Ibrahim Palace": {
        "description": "It was built in 1556 by Ali Ibn Ahmed Ibn Lawand Al-Burayki, the Ottoman governor of the time.A palace of historical importance, it was known in the past as Al Kut. It was the headquarter of the Ottoman army during their rule of Al-Ahsa, and the palace was attributed to the governor, Ibrahim bin Afaisan, Prince of Al-Ahsa during the reign of Imam Saud",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290068/IbrahimPlace_jyokw9.png"
    },
    "Ithra": {
        "description": "Iconic cultural center. Designed as a hub for knowledge, creativity, and cross-cultural engagement, it comprises a library, museum, theater, cinema, and exhibition halls. Its striking architecture symbolizes a beacon of knowledge and is a testament to Saudi Arabia's commitment to cultural development",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290076/Ithra_nzxhtz.png"
    },
    "Jabal AlFil (Elephant Rock)": {
        "description": "stunning natural rock formation located in the Al-Ula region. Resembling an elephant with a 'trunk' and 'body' formed from sandstone, this geological marvel is a popular attraction, especially at sunset, for its breathtaking beauty and the play of light and shadows over its unique shape",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290152/this-spectacular-rock_hsskiz.jpg"
    },
    "King Abdullah Financial District (KAFD)": {
        "description": "KAFD was inspired by King Abdullah’s vision to create a new financial district that will take the economy of Riyadh to new heights. Following its acquisition by the Public Investment Fund (PIF) of Saudi Arabia, KAFD has evolved to become a prime business and lifestyle destination capturing the core values of Vision 2030.",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701285193/KAFD_bx8up3.jpg"
    },
    'Kingdom Tower': {
        "description": "Kingdom Centre, formerly Kingdom Tower, is a 99-story, 302.3 m skyscraper in the al-Olaya district of Riyadh, Saudi Arabia. When completed in 2002, it overtook the 267-meter Faisaliyah Tower as the tallest tower in Saudi Arabia.",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290083/Kingdom_Tower_bonxtf.jpg"
    },
    'Maraya': {
        "description": "located in Al-Ula, is a strikingly modern concert hall known for its mirrored facade that reflects the surrounding landscape. As the largest mirrored building in the world, it hosts various cultural events, blending arts and entertainment with the region's natural beauty and heritage.",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290088/MARAYA_m22nnb.jpg"
    },
    'Nassif House Museum': {
        "description": "located in Jeddah's historical Al-Balad area, is a traditional 19th-century Saudi house turned museum. It showcases the region's cultural and architectural history, with a focus on Hejazi-style architecture, featuring intricate wooden lattices and beautifully crafted balconies.",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290107/Nassif-House-Museum_bma0qd.jpg"
    },
    "Quba Mosque": {
        "description": "The Quba Mosque in Medina is of great significance in Islamic history, being the first mosque built by Prophet Muhammad after his migration from Mecca to Medina. It's a place of worship and historical interest, revered by Muslims for its spiritual importance and architectural beauty.",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290098/Masjid-Quba_xictay.jpg"
    },
    "Riyadh Water Tower": {
        "description": "iconic structure in Riyadh's skyline. Located in King Fahd Park, this functional and architectural marvel is not just a water tower but also a popular tourist attraction, offering panoramic views of the city.",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290118/Riyadh_Water_Tower_hahndd.jpg"
    },
    "The Clock Towers": {
        "description": "The Abraj Al Bait, known for its towering clock tower, overlooks the Grand Mosque in Mecca. This complex is among the world's tallest buildings and features a massive clock visible from miles away, symbolizing Islamic heritage and modernity.",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290138/The_Clock_Towers_y7f5bb.jpg"
    },
    "The Kaaba": {
        "description": "The Kaaba is the most sacred site in Islam, located in the center of the Grand Mosque in Mecca. It's a cube-shaped structure draped in a black silk cloth embroidered with gold, towards which Muslims around the world face during prayers. It's a focal point of the Hajj pilgrimage, embodying unity and faith in the Islamic world.",
        "image_url": "https://res.cloudinary.com/dr2baapqk/image/upload/v1701290145/The_Kaaba_hf24ab.jpg"
    },
}

def predict(image: Image):
    img = image.resize((224, 224))
    pred, pred_idx, probs = learn.predict(img)
    confidence_threshold = 0.7
    probability = probs[pred_idx].item() 
    if probability < confidence_threshold:
        return None, probability, None,None
    else:
        landmark_info = landmark_descriptions.get(pred)
        return pred, probability, landmark_info
        