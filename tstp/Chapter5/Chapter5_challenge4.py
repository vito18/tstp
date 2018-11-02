profile = {"name": "Takumi",
           "height": 174,
           "weight": 55,
           "colors": "black",
           "major": "engineering"
           }

print(profile)

key = input("何を聞く?")

if key in profile:
    print(profile[key])

else:
    print("見つかりません")
    
