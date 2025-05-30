# wordbank.py

WORDS = {
    "Det": [
        "the", "a", "an", "some", "this", "that", "these", "those",
        "each", "every", "no", "any", "another", "such",
        "my", "your", "his", "her", "its", "our", "their", "enough", "little", "much",
        "more", "most", "least", "fewer", "many", "several", "various"
    ],

    "Noun": [
        "cat", "dog", "ball", "car", "tree", "house", "student", "teacher", "book", "phone", "computer",
        "bottle", "city", "boy", "girl", "bird", "apple", "school", "street", "child", "man", "woman",
        "table", "chair", "window", "door", "shirt", "shoe", "hat", "cup", "glass", "watch", "bag",
        "bus", "train", "plane", "boat", "river", "mountain", "lake", "forest", "flower", "leaf",
        "animal", "fish", "horse", "cow", "sheep", "pig", "mouse", "monkey", "elephant", "lion", "tiger",
        "doctor", "nurse", "police", "firefighter", "engineer", "painter", "driver", "cook", "baker",
        "actor", "singer", "dancer", "lawyer", "judge", "president", "king", "queen", "soldier",
        "friend", "enemy", "neighbor", "boss", "worker", "child", "adult", "baby", "parent", "guest",
        "university", "library", "kitchen", "garden", "hospital", "market", "restaurant", "office",
        "company", "factory", "store", "beach", "desert", "valley", "cave", "island", "jungle", "swamp", "volcano",
        "scientist", "artist", "writer", "athlete", "musician", "photographer", "designer", "manager",
        "pants", "jacket", "scarf", "glove", "sock", "belt", "tie", "banana", "orange", "grape", "lemon",
        "mango", "peach", "pear", "plum", "team", "group", "family", "couple", "crowd", "audience",
        "staff", "crew", "language", "idea", "thought", "dream", "plan", "goal", "choice", "chance", "risk"
    ],

    "Adj": [
        "big", "small", "happy", "sad", "fast", "slow", "bright", "dark", "cold", "hot", "new", "old",
        "young", "funny", "angry", "smart", "clean", "loud", "quiet", "tall", "short", "fat", "thin",
        "strong", "weak", "rich", "poor", "beautiful", "ugly", "friendly", "kind", "mean", "brave",
        "scared", "lazy", "active", "tired", "sick", "healthy", "busy", "free", "nice", "bad", "good",
        "early", "late", "soft", "hard", "sweet", "sour",
        "noisy", "polite", "rude", "generous", "selfish", "jealous", "proud", "grateful", "honest",
        "curious", "serious", "careful", "careless", "faithful", "lucky", "unlucky", "nervous", "calm",
        "gorgeous", "handsome", "plain", "attractive", "elegant", "charming", "graceful",
        "important", "necessary", "optional", "urgent", "famous", "unknown", "ancient", "modern"
    ],

    "Verb": [
        "runs", "eats", "plays", "jumps", "drives", "reads", "writes", "talks", "sings", "walks",
        "sleeps", "studies", "laughs", "cries", "looks", "cooks", "drinks", "opens", "closes", "sees",
        "likes", "hates", "loves", "calls", "helps", "finds", "loses", "breaks", "fixes", "builds",
        "cleans", "cuts", "throws", "catches", "holds", "pushes", "pulls", "starts", "stops", "teaches",
        "learns", "draws", "paints", "hears", "smells", "touches", "thinks", "knows", "understands",
        "remembers", "forgets", "buys", "sells", "pays", "sends", "receives", "answers", "asks", "waits",
        "needs", "wants", "chooses", "joins", "leaves", "enters", "returns", "arrives", "leads", "follows",
        "turns", "climbs", "dances", "explains", "decides", "tries", "fails", "succeeds", "shouts",
        "whispers", "smiles", "warns", "invites", "agrees", "disagrees", "admires",
        "avoids", "enjoys", "spends", "saves", "kills", "rescues", "forgives", "judges", "argues",
        "admits", "blames", "borrows", "cheats", "claps", "delivers", "destroys", "discovers", "divides",
        "encourages", "escapes", "examines", "excuses", "explores", "fights", "guesses",
        "hugs", "imagines", "improves", "invents", "jokes", "kisses", "measures", "mentions",
        "notices", "offers", "orders", "owns", "packs", "prefers", "promises", "protects", "punishes",
        "refuses", "removes", "repairs", "shakes", "shares", "skips", "slides", "spills", "steals",
        "stretches", "suffers", "thanks", "trains", "trusts"
    ],

    "Pronoun": [
        "he", "she", "they", "we", "i", "you", "it",
        "mine", "yours", "his", "hers", "ours", "theirs", "me", "him", "her", "us", "them", "oneself"
    ],

    "Adv": [
        "quickly", "slowly", "happily", "sadly", "silently", "loudly", "well", "badly", "always", "never",
        "often", "rarely", "sometimes", "usually", "soon", "later", "now", "then", "here", "there",
        "everywhere", "anywhere", "upstairs", "downstairs", "outside", "inside", "forward", "backward",
        "easily", "hardly", "truly", "really", "barely", "deeply", "fully", "gently", "calmly", "clearly",
        "abruptly", "briskly", "cheerfully", "eagerly", "fiercely", "gracefully", "hungrily", "innocently",
        "jokingly", "kindly", "lazily", "merrily", "neatly", "obediently", "politely", "roughly",
        "sharply", "tensely", "urgently", "vividly", "wildly", "yearly"
    ],

    "Prep": [
        "on", "in", "under", "over", "with", "without", "to", "from", "at", "by", "through", "across",
        "against", "around", "behind", "beside", "between", "beyond", "during", "inside", "outside",
        "near", "off", "onto", "upon", "within", "above", "below", "toward", "along",
        "beneath", "regarding", "concerning", "except", "including", "minus", "per", "plus", "save", "versus", "via"
    ],

    "Conj": [
        "and", "but", "or", "so", "because", "although", "while", "if", "when", "before",
        "after", "as", "though", "unless", "until", "whereas", "since", "even though", "whether", "once",
        "nor", "lest", "provided", "albeit", "inasmuch", "inasmuch as", "rather than", "just as", "in case"
    ],

    "Aux": [
        "is", "am", "are", "was", "were", "be", "being", "been",
        "do", "does", "did", "have", "has", "had", "will", "would", "shall", "should", "can", "could", "may", "might", "must"
    ],

    "VerbPart": [
        "eating", "playing", "reading", "sleeping", "running", "walking",
        "talking", "drinking", "cooking", "writing", "drawing", "studying",
        "laughing", "crying", "singing", "working", "watching", "listening", "learning",
        "shopping", "fighting", "traveling", "jogging", "swimming", "hiking", "exploring",
        "baking", "texting", "driving", "fishing", "gardening", "cleaning", "repairing"
    ]
}
