"""Downloads the wiki images the tooltips use and writes src/areas.json.

Run once from the repo root: python tools/fetch_wiki_images.py
Images are CC BY-NC 3.0, IdleOn MMO Wiki contributors (see img/README.md).
"""
import json, pathlib, subprocess, time, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
W = "https://idleon.wiki/images/"
WORLDS = {
    "w1": ("0/08/Blunder_Hills_Area_Map.png", [[502.5,157],[543.5,177],[459.5,198],[333.5,141],[233.5,152],[472.5,129],[410.5,117],[285.5,167],[296.5,195],[194.5,210],[694.5,191],[577.5,207],[441.5,123],[647.5,223],[612.5,157],[705.5,156],[695.5,243],[610.5,256],[567.5,286],[485.5,320],[470.5,366],[733.5,214],[733.5,117],[258.5,218],[575.5,151],[587.5,232],[428.5,182],[458.5,169],[540.5,139],[602.5,122]]),
    "w2": ("4/48/Yum_Yum_Desert_Area_Map.png", [[255.5,142],[328.5,175],[369.5,250],[445.5,264],[170.5,144],[137.5,172],[548.5,260],[492.5,220],[450.5,179],[430.5,112],[167.5,202],[506.5,117],[601.5,116],[680.5,168],[672.5,246],[742.5,208],[419.5,314],[315.5,261],[438.5,323],[382.5,195]]),
    "w3": ("0/0d/Frostbite_Tundra_Area_Map.png", [[203.5,317],[223.5,262],[139.5,252],[234.5,214],[303.5,178],[366.5,211],[424.5,226],[507.5,246],[623.5,272],[624.5,232],[638.5,195],[601.5,154],[551.5,123],[610.5,108],[689.5,113],[293.5,122],[227.5,101],[234.5,335],[250.5,74]]),
    "w4": ("f/f8/Hyperion_Nebula_Area_Map.png", [[700.5,299],[657.5,230],[591.5,279],[527.5,331],[454.5,259],[334.5,285],[227.5,308],[221.5,221],[156.5,145],[254.5,138],[386.5,136],[485.5,129],[522.5,57],[626.5,94],[588.5,160],[758.5,37]]),
    "w5": ("1/12/Smolderin%27_Plateau_Area_Map.png", [[677.5,99],[631.5,164],[571.5,197],[587.5,250],[550.5,284],[481.5,279],[413.5,255],[358.5,267],[340.5,230],[281.5,251],[230.5,236],[161.5,252],[261.5,344],[369.5,364],[99.5,259],[557.5,184],[759.5,275]]),
    "w6": ("6/65/Spirited_Valley_Area_Map.png", [[612.5,354],[574.5,341],[511.5,344],[480.5,369],[416.5,372],[341.5,370],[185.5,347],[269.5,280],[489.5,204],[596.5,117],[397.5,140],[263.5,166],[158.5,176],[105.5,111],[140.5,90],[178.5,88]]),
}
# star id: (world, highlighted [x, y] on the 811x433 world map, monsters on the map as (name, wiki image path))
STARS = {
 "A-1":("w1",[502.5,157],[]), "A-2":("w1",[733.5,117],[("Wood Mushroom","3/3f/Wood_Mushroom_Idle.gif")]),
 "A-3":("w1",[577.5,207],[("Bored Bean","0/02/Bored_Bean_Idle.gif")]), "A-4":("w1",[470.5,366],[("Gigafrog","9/94/Gigafrog_Idle.gif")]),
 "A-5":("w1",[410.5,117],[("Dr Defecaus","5/5c/Dr_Defecaus_Idle.gif")]), "A-6":("w1",[233.5,152],[]),
 "A-7":("w1",[695.5,243],[("Baby Boa","f/ff/Baby_Boa_Idle.gif")]), "A-8":("w1",[575.5,151],[]),
 "A-9":(None,None,[]), "A-10":("w1",[296.5,195],[]),
 "B-1":("w2",[369.5,250],[("Biggie Hours","9/92/Biggie_Hours_Idle.gif"),("Mimic","a/a7/Mimic_Idle.gif")]), "B-2":("w2",[137.5,172],[]),
 "B-3":("w2",[548.5,260],[("Mafioso","d/dc/Mafioso_Idle.gif")]), "B-4":("w2",[430.5,112],[("Mashed Potato","5/50/Mashed_Potato_Idle.gif")]),
 "B-5":("w2",[315.5,261],[]), "B-6":("w2",[742.5,208],[]), "B-7":("w2",[601.5,116],[("Moonmoon","a/a2/Moonmoon_Idle.gif")]),
 "B-8":("w2",[255.5,142],[]),
 "C-1":("w3",[203.5,317],[]), "C-2":("w3",[223.5,262],[("Sheepie","7/71/Sheepie_Idle.gif")]), "C-3":("w3",[139.5,252],[]),
 "C-4":("w3",[366.5,211],[("Bloque","6/6b/Bloque_Idle.gif"),("Dilapidated Slush","5/5f/Dilapidated_Slush_Idle.gif")]),
 "C-5":("w3",[507.5,246],[("Snowman","4/4c/Snowman_Idle.gif")]), "C-6":("w3",[624.5,232],[("Thermister","9/92/Thermister_Idle.gif")]),
 "C-7":("w3",[610.5,108],[("Neyeptune","3/3f/Neyeptune_Idle.gif")]), "C-8":("w3",[227.5,101],[("Bloodbone","f/ff/Bloodbone_Idle.gif")]),
 "D-1":("w4",[700.5,299],[]), "D-2":("w4",[657.5,230],[("Mutated Mush","0/05/Mutated_Mush_Idle.gif"),("Purp Mushroom","7/75/Purp_Mushroom_Idle.gif")]),
 "D-3":("w4",[527.5,331],[("Donut","3/35/Donut_Idle.gif")]), "D-4":("w4",[227.5,308],[("Flying Worm","5/54/Flying_Worm_Idle.gif")]),
 "D-5":("w4",[156.5,145],[("Choccie","e/e7/Choccie_Idle.gif")]), "D-6":("w4",[254.5,138],[("Biggole Wurm","8/8d/Biggole_Wurm_Idle.gif")]),
 "D-7":("w4",[386.5,136],[("Clammie","5/58/Clammie_Idle.gif")]),
 "E-1":("w5",[677.5,99],[]), "E-2":("w5",[571.5,197],[("Maccie","c/cb/Maccie_Idle.gif")]),
 "E-3":("w5",[550.5,284],[("Cheese Nub","c/c2/Cheese_Nub_Idle.gif")]), "E-4":("w5",[413.5,255],[("Molti","4/44/Molti_Idle.gif")]),
 "E-5":("w5",[340.5,230],[("Citringe","f/f5/Citringe_Idle.gif")]), "E-6":("w5",[161.5,252],[("Biggole Mole","f/f4/Biggole_Mole_Idle.gif")]),
 "E-7":("w5",[369.5,364],[("Tremor Wurm","0/01/Tremor_Wurm_Idle.gif")]),
 "F-1":("w6",[612.5,354],[]), "F-2":("w6",[574.5,341],[("Sprout Spirit","a/a0/Sprout_Spirit_Idle.gif")]),
 "F-3":("w6",[480.5,369],[("River Spirit","9/91/River_Spirit_Idle.gif")]), "F-4":("w6",[341.5,370],[("Woodlin Spirit","1/11/Woodlin_Spirit_Idle.gif")]),
 "F-5":("w6",[269.5,280],[("Lantern Spirit","8/86/Lantern_Spirit_Idle.gif")]), "F-6":("w6",[596.5,117],[("Leek Spirit","c/cc/Leek_Spirit_Idle.gif")]),
 "F-7":("w6",[263.5,166],[("Skydoggie Spirit","b/bc/Skydoggie_Spirit_Idle.gif")]), "F-8":("w6",[158.5,176],[("Royal Egg","b/ba/Royal_Egg_Idle.gif")]),
 "F-9":("w6",[140.5,90],[("Samurai Guardian","6/66/Samurai_Guardian_Idle.gif")]),
}

def get(path, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return dest.stat().st_size
    # curl, because the wiki's CDN stalls Python's own HTTP client
    tmp = dest.with_suffix(dest.suffix + ".part")
    subprocess.run(["curl", "-sSf", "--retry", "8", "--retry-all-errors", "-C", "-", "--max-time", "600",
                    "-A", "idleon-star-chart (github.com/StimDesu/idleon-star-chart)",
                    "-o", str(tmp), W + path], check=True)
    tmp.replace(dest)
    data = dest.read_bytes()
    time.sleep(0.3)
    return len(data)

total = 0
for w, (path, _) in WORLDS.items():
    total += get(path, ROOT / "img/maps" / f"{w}.png")
areas = {"worlds": {w: dots for w, (_, dots) in WORLDS.items()}, "stars": {}}
for sid, (w, hi, mobs) in STARS.items():
    files = []
    for name, path in mobs:
        fn = urllib.parse.unquote(path.split("/")[-1])
        total += get(path, ROOT / "img/mobs" / fn)
        files.append([name, fn])
    areas["stars"][sid] = {"w": w, "hi": hi, "mobs": files}
(ROOT / "src/areas.json").write_text(json.dumps(areas, ensure_ascii=False), encoding="utf-8")
print(f"{total // 1024} KB of images, areas.json written")
