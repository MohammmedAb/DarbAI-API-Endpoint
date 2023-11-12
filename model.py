from fastai.vision.all import *
from PIL import Image

import pathlib
print('1')
plt = platform.system()
if plt == 'Windows': pathlib.PosixPath = pathlib.WindowsPath
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath
print('2')
learn = load_learner('SaudiLandmarkClassifier.pkl') 
print('3')
# This is a simple dictionary. In a real application, you might use a database.
landmark_descriptions = {
    "Al Masmak Palace": "The palace was constructed in the hijri 14th century during the reign of Imam Abdullah bin Faisal as his residence and the center of power and money. The palace is a strong fort against enemies with its solid high walls. It has only two entrances and small openings in the walls for gun barrels at the time of battles. Today, the palace stands as a symbol of the history of regaining power and rule of the country displaying in its corridors the features of that era and its leaders after it had been turned into a museum in 1995/1416",
    "Hegra": "Also known as Al-Hijr or Madain Saleh, is an ancient archaeological site located in the Al-Ula sector, within the Al Madinah Region of Saudi Arabia. A former Nabatean city, it's known for its well-preserved rock-cut tombs with intricate facades, dating back to the 1st century AD. It's Saudi Arabia's first UNESCO World Heritage Site, showcasing the Nabateans' architectural and engineering prowess",
    'Ithra': "Iconic cultural center. Designed as a hub for knowledge, creativity, and cross-cultural engagement, it comprises a library, museum, theater, cinema, and exhibition halls. Its striking architecture symbolizes a beacon of knowledge and is a testament to Saudi Arabia's commitment to cultural development",
    "Jabal AlFil (Elephant Rock)": "stunning natural rock formation located in the Al-Ula region. Resembling an elephant with a 'trunk' and 'body' formed from sandstone, this geological marvel is a popular attraction, especially at sunset, for its breathtaking beauty and the play of light and shadows over its unique shape",
    'Kingdom Tower': "Kingdom Centre, formerly Kingdom Tower, is a 99-story, 302.3 m skyscraper in the al-Olaya district of Riyadh, Saudi Arabia. When completed in 2002, it overtook the 267-meter Faisaliyah Tower as the tallest tower in Saudi Arabia.",
    'Maraya': "located in Al-Ula, is a strikingly modern concert hall known for its mirrored facade that reflects the surrounding landscape. As the largest mirrored building in the world, it hosts various cultural events, blending arts and entertainment with the region's natural beauty and heritage.",
    'Nassif House Museum': "located in Jeddah's historical Al-Balad area, is a traditional 19th-century Saudi house turned museum. It showcases the region's cultural and architectural history, with a focus on Hejazi-style architecture, featuring intricate wooden lattices and beautifully crafted balconies.",
    "Quba Mosque": "The Quba Mosque in Medina is of great significance in Islamic history, being the first mosque built by Prophet Muhammad after his migration from Mecca to Medina. It's a place of worship and historical interest, revered by Muslims for its spiritual importance and architectural beauty.",
    "Riyadh Water Tower": "iconic structure in Riyadh's skyline. Located in King Fahd Park, this functional and architectural marvel is not just a water tower but also a popular tourist attraction, offering panoramic views of the city.",
    "The Clock Towers": "The Abraj Al Bait, known for its towering clock tower, overlooks the Grand Mosque in Mecca. This complex is among the world's tallest buildings and features a massive clock visible from miles away, symbolizing Islamic heritage and modernity.",
    "The Kaaba": "The Kaaba is the most sacred site in Islam, located in the center of the Grand Mosque in Mecca. It's a cube-shaped structure draped in a black silk cloth embroidered with gold, towards which Muslims around the world face during prayers. It's a focal point of the Hajj pilgrimage, embodying unity and faith in the Islamic world.",
}

def predict(image: Image):
    print('4')
    img = image.resize((224, 224))
    pred, pred_idx, probs = learn.predict(img)
    print('5')
    confidence_threshold = 0.7
    probability = probs[pred_idx].item() 
    print('6')
    if probability < confidence_threshold:
        return "The landmark is not recognized", probability, None
    else:
        return pred, probability, landmark_descriptions[pred]
        