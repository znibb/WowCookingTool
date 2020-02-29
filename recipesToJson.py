#!/usr/bin/env python3.7

recipes = {
    "Bear Meat": {
        "Recipe":   "Smoked Bear Meat",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    40,
        "Yellow":   80,
        "Green":    100,
        "Grey":     120
    },
    "Big Bear Meat": {
        "Recipe":   "Big Bear Steak",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 1},
        "Learn":    110,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190
    },
    "Boar Ribs": {
        "Recipe":   "Dry Pork Ribs",
        "Source":   "Trainer",
        "Amount":   1,
        "AddMats":  {"Mild Spices": 1},
        "Learn":    80,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160
    },
    "Buzzard Wing": {
        "Recipe":   "Barbequed Buzzard Wing",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 1},
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255
    },
    "Chunk of Boar Meat": {
        "Recipe":   "Roasted Boar Meat",
        "Source":   "Trainer",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85
    },
    "Clam Meat": {
        "Recipe":   "Boiled Clams",
        "Source":   "Trainer",
        "Amount":   1,
        "AddMats":  {"Refreshing Spring Water": 1},
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130
    },
    "Coyote Meat": {
        "Recipe":   "Coyote Steak",
        "Source":   "Trainer",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130
    },
    "Crawler Meat": {
        "Recipe":   "Crab Cake",
        "Source":   "Trainer",
        "Amount":   1,
        "AddMats":  {"Mild Spices": 1},
        "Learn":    75,
        "Yellow":   115,
        "Green":    135,
        "Grey":     155
    },
    "Darkclaw Lobster": {
        "Recipe":   "Lobster Stew",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Refreshing Spring Water": 1},
        "Learn":    275,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355
    },
    "Giant Egg": {
        "Recipe":   "Monster Omelet",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Soothing Spices": 2},
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305
    },
		"Kodo Meat": {
				"Recipe":		"Roasted Kodo Meat",
				"Source":		"Recipe",
				"Amount":		1,
				"AddMats":	{"Mild Spices": 1},
				"Learn":		35,
				"Yellow":		75,
				"Green":		95,
				"Grey":			115
		},
    "Lean Wolf Flank": {
        "Recipe":   "Lean Wolf Steak",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Mild Spices": 1},
        "Learn":    125,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205
    },
    "Lion Meat": {
        "Recipe":   "Hot Lion Chops",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 1},
        "Learn":    125,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215
    },
    "Meaty Bat Wing": {
        "Recipe":   "Crispy Bat Wing",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Mild Spices": 1},
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85
    },
    "Mystery Meat": {
        "Recipe":   "Carrion Surprise",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 1},
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255
    },
    "Raptor Egg": {
        "Recipe":   "Curiously Tasty Omelet",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 1},
        "Learn":    130,
        "Yellow":   170,
        "Green":    190,
        "Grey":     210
    },
    "Raptor Flesh": {
        "Recipe":   "Roast Raptor",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 1},
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255
    },
    "Raw Brilliant Smallfish": {
        "Recipe":   "Brilliant Smallfish",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85
    },
    "Raw Bristle Whisker Catfish": {
        "Recipe":   "Bristle Whisker Catfish",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    100,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180
    },
    "Raw Glossy Mightfish": {
        "Recipe":   "Cooked Glossy Mightfish",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Soothing Spices": 1},
        "Learn":    225,
        "Yellow":   265,
        "Green":    2285,
        "Grey":     305
    },
    "Raw Greater Sagefish": {
        "Recipe":   "Sagefish Delight",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 1},
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255
    },
    "Raw Longjaw Mud Snapper": {
        "Recipe":   "Longjaw Mud Snapper",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130
    },
    "Raw Mithril Head Trout": {
        "Recipe":   "Mithril Head Trout",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255
    },
    "Raw Nightfin Snapper": {
        "Recipe":   "Nightfin Soup",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Refreshing Spring Water": 1},
        "Learn":    250,
        "Yellow":   290,
        "Green":    310,
        "Grey":     330
    },
    "Raw Rainbow Fin Albacore": {
        "Recipe":   "Rainbow Fin Albacore",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130
    },
    "Raw Redgill": {
        "Recipe":   "Filet of Redgill",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305
    },
    "Raw Rockscale Cod": {
        "Recipe":   "Rockscale Cod",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    175,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230
    },
    "Raw Sagefish": {
        "Recipe":   "Smoked Sagefish",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Mild Spices": 1},
        "Learn":    80,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160
    },
    "Raw Spotted Yellowtail": {
        "Recipe":   "Spotted Yellowtail",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305
    },
    "Raw Summer Bass": {
        "Recipe":   "Hot Smoked Bass",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 2},
        "Learn":    240,
        "Yellow":   280,
        "Green":    300,
        "Grey":     320
    },
    "Raw Sunscale Salmon": {
        "Recipe":   "Poached Sunscale Salmon",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    250,
        "Yellow":   290,
        "Green":    310,
        "Grey":     330
    },
    "Raw Whitescale Salmon": {
        "Recipe":   "Baked Salmon",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Soothing Spices": 1},
        "Learn":    275,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355
    },
    "Red Wolf Meat": {
        "Recipe":   "Hot Wolf Ribs",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 1},
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255
    },
    "Sandworm Meat": {
        "Recipe":   "Smoked Desert Dumplings",
        "Source":   "Quest",
        "Amount":   1,
        "AddMats":  {"Soothing Spices": 1},
        "Learn":    285,
        "Yellow":   325,
        "Green":    345,
        "Grey":     365
    },
    "Scorpid Stinger": {
        "Recipe":   "Scorpid Surprise",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    20,
        "Yellow":   60,
        "Green":    80,
        "Grey":     100
    },
    "Small Egg": {
        "Recipe":   "Herb Baked Egg",
        "Source":   "Trainer",
        "Amount":   1,
        "AddMats":  {"Mild Spices": 1},
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85
    },
    "Stag Meat": {
        "Recipe":   "Lean Venison",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Mild Spices": 4},
        "Learn":    110,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190
    },
    "Strider Meat": {
        "Recipe":   "Strider Stew",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Shiny Red Apple": 1},
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130
    },
    "Stringy Wolf Meat": {
        "Recipe":   "Charred Wolf Meat",
        "Source":   "Trainer",
        "Amount":   1,
        "AddMats":  {},
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85
    },
    "Tangy Clam Meat": {
        "Recipe":   "Goblin Deviled Clams",
        "Source":   "Trainer",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 1},
        "Learn":    125,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205
    },
    "Tender Crab Meat": {
        "Recipe":   "Spiced Chili Crab",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 2},
        "Learn":    225,
        "Yellow":   265,
        "Green":    186,
        "Grey":     305
    },
    "Tender Crocolisk Meat": {
        "Recipe":   "Heavy Crocolisk Stew",
        "Source":   "Recipe",
        "Amount":   2,
        "AddMats":  {"Soothing Spices": 1},
        "Learn":    150,
        "Yellow":   160,
        "Green":    180,
        "Grey":     200
    },
    "Tender Wolf Meat": {
        "Recipe":   "Tender Wolf Steak",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Soothing Spices": 1},
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305
    },
    "Thunder Lizard Tail": {
        "Recipe":   "Crispy Lizard Tail",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Hot Spices": 1},
        "Learn":    100,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180
    },
    "Tiger Meat": {
        "Recipe":   "Jungle Stew",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Refreshing Spring Water": 1, "Shiny Red Apple": 2},
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255
    },
    "Turtle Meat": {
        "Recipe":   "Soothing Turtle Bisque",
        "Source":   "Recipe",
        "Amount":   1,
        "AddMats":  {"Soothing Spices": 1},
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255
    },
    "White Spider Meat": {
        "Recipe":   "Spider Sausage",
        "Source":   "Trainer",
        "Amount":   2,
        "AddMats":  {},
        "Learn":    200,
        "Yellow":   240,
        "Green":    260,
        "Grey":     280
    },
    "Zesty Clam Meat": {
        "Recipe":   "Undermine Clam Chowder",
        "Source":   "Recipe",
        "Amount":   2,
        "AddMats":  {"Hot Spices": 1, "Cold Milk": 1},
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305
    }
}

import json
with open('recipes.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)
