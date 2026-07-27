FIRST_NAMES = [
    "Chinedu", "Chioma", "Emeka", "Amina", "Ibrahim",
    "Tunde", "Bisi", "Ngozi", "Uche", "Kelechi",
    "Seyi", "Aisha", "David", "Esther", "Musa",
    "Ada", "Samuel", "Blessing", "Emmanuel", "Fatima"
]

LAST_NAMES = [
    "Okafor", "Adebayo", "Balogun", "Mohammed", "Nwosu",
    "Eze", "Ogunleye", "Yusuf", "Ibrahim", "Okeke",
    "Adeyemi", "Bello", "Ojo", "Umeh", "Chukwu",
    "Danjuma", "Aliyu", "Onyeka", "Ekwueme", "Abubakar"
]

import random
from utils.reference_data import FIRST_NAMES, LAST_NAMES

first_name = random.choice(FIRST_NAMES)
last_name = random.choice(LAST_NAMES)

customer_name = f"{first_name} {last_name}"

import random

# ======================================================
# PERSON NAMES
# ======================================================

FIRST_NAMES = [
    "Chinedu", "Chioma", "Emeka", "Uche", "Ngozi",
    "Kelechi", "Amaka", "Obinna", "Ada", "Ifeanyi",
    "Tunde", "Seyi", "Bisi", "Adeola", "Temitope",
    "Ayomide", "Yetunde", "Gbenga", "Oluwaseun",
    "Amina", "Fatima", "Ibrahim", "Musa",
    "Yusuf", "Aisha", "Abubakar", "Hauwa"
]

LAST_NAMES = [
    "Okafor", "Okeke", "Nwosu", "Eze", "Umeh",
    "Chukwu", "Onyeka", "Adebayo", "Adeyemi",
    "Balogun", "Ogunleye", "Ojo", "Akinyemi",
    "Bello", "Mohammed", "Yusuf", "Aliyu",
    "Garba", "Danjuma"
]

# ======================================================
# EMAILS
# ======================================================

EMAIL_DOMAINS = [
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com"
]

def generate_phone():

    prefixes = [
        "0703", "0706", "0708",
        "0802", "0803", "0805",
        "0807", "0808", "0810",
        "0813", "0814", "0816",
        "0818", "0902", "0903",
        "0909", "0912", "0915"
    ]

    prefix = random.choice(prefixes)

    remaining = "".join(
        random.choices("0123456789", k=7)
    )

    return prefix + remaining




#Geography


NIGERIA = {

    "South West": {

        "Lagos": [
            "Ikeja",
            "Lekki",
            "Yaba",
            "Surulere"
        ],

        "Ogun": [
            "Abeokuta",
            "Ijebu Ode"
        ]
    },

    "South East": {

        "Anambra": [
            "Awka",
            "Onitsha",
            "Nnewi"
        ],

        "Enugu": [
            "Enugu",
            "Nsukka"
        ]
    },

    "South South": {

        "Rivers": [
            "Port Harcourt"
        ],

        "Akwa Ibom": [
            "Uyo"
        ]
    },

    "North Central": {

        "FCT": [
            "Abuja"
        ],

        "Benue": [
            "Makurdi"
        ]
    },

    "North West": {

        "Kano": [
            "Kano"
        ],

        "Kaduna": [
            "Kaduna"
        ]
    },

    "North East": {

        "Borno": [
            "Maiduguri"
        ],

        "Bauchi": [
            "Bauchi"
        ]
    }
}

def generate_location():

    region = random.choice(list(NIGERIA.keys()))

    state = random.choice(
        list(NIGERIA[region].keys())
    )

    city = random.choice(
        NIGERIA[region][state]
    )

    return region, state, city