fav_lang={
    "anu": "python",
    "prin": "python",
    "aman": "html",
    "abhi": "c++",
}


friends=["abhi", "prin"]
for name in fav_lang.keys():
    print(f"Hi {name}")
    if name in friends:
        languages=fav_lang[name].title()
        print(f"\t{name.title()}, I see you love C")