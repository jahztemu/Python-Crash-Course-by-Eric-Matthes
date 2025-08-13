tree = {
    "tall": {
        "fruit": ["pear", "cashew", "mango"],
        "no fruit": ["oak", "pine", "redwood"],
    },
    "mid": {
        "fruit": ["orange", "grape", "apple", "lime"],
        "no fruit": ["maple", "birch"],
    },
    "short": {
        "fruit": ["cherry", "plum", "peach"],
        "no fruit": ["dog wood", "redbud"],
    },
}
vehicle = {
    "land": {
        "road": ["bus", "car", "van", "truck"],
        "track": ["train", "cable cab"],
        "special": ["caterpillar", "backhoe", "paver", "excavator"],
    },
    "water": {
        "huge": ["cargo ship", "cruise ship", "oil tanker"],
        "mid": ["yacht", "ferry", "sailboat"],
        "small": ["motor boat", "jet ski", "canoe"],
    },
    "air": {
        "huge": ["cargo plane", "airliner", "blimp", "military transport"],
        "mid": ["helicopter", "private jet", "glider"],
        "small": ["drone", "hang glider", "hot air ballon"],
    },
}

object = [tree, vehicle]

print("All data save")
for stuff in object:
    for key, value in stuff.items():
        print(f"\n{key.title()}:")
        for key, value in value.items():
            print(f"\t{key.title()};\n\t {value}")
