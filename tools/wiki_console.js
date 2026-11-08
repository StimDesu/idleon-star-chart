// Paste into the browser console on any https://idleon.wiki page.
// Downloads the world maps and monster GIFs the tooltips use as one file,
// idleon-wiki-images.json. Then run: python tools/unpack_wiki_images.py <that file>
(async () => {
  const items = [["0/08/Blunder_Hills_Area_Map.png", "maps/w1.png"], ["4/48/Yum_Yum_Desert_Area_Map.png", "maps/w2.png"], ["0/0d/Frostbite_Tundra_Area_Map.png", "maps/w3.png"], ["f/f8/Hyperion_Nebula_Area_Map.png", "maps/w4.png"], ["1/12/Smolderin%27_Plateau_Area_Map.png", "maps/w5.png"], ["6/65/Spirited_Valley_Area_Map.png", "maps/w6.png"], ["3/3f/Wood_Mushroom_Idle.gif", "mobs/Wood_Mushroom_Idle.gif"], ["0/02/Bored_Bean_Idle.gif", "mobs/Bored_Bean_Idle.gif"], ["9/94/Gigafrog_Idle.gif", "mobs/Gigafrog_Idle.gif"], ["5/5c/Dr_Defecaus_Idle.gif", "mobs/Dr_Defecaus_Idle.gif"], ["f/ff/Baby_Boa_Idle.gif", "mobs/Baby_Boa_Idle.gif"], ["9/92/Biggie_Hours_Idle.gif", "mobs/Biggie_Hours_Idle.gif"], ["a/a7/Mimic_Idle.gif", "mobs/Mimic_Idle.gif"], ["d/dc/Mafioso_Idle.gif", "mobs/Mafioso_Idle.gif"], ["5/50/Mashed_Potato_Idle.gif", "mobs/Mashed_Potato_Idle.gif"], ["a/a2/Moonmoon_Idle.gif", "mobs/Moonmoon_Idle.gif"], ["7/71/Sheepie_Idle.gif", "mobs/Sheepie_Idle.gif"], ["6/6b/Bloque_Idle.gif", "mobs/Bloque_Idle.gif"], ["5/5f/Dilapidated_Slush_Idle.gif", "mobs/Dilapidated_Slush_Idle.gif"], ["4/4c/Snowman_Idle.gif", "mobs/Snowman_Idle.gif"], ["9/92/Thermister_Idle.gif", "mobs/Thermister_Idle.gif"], ["3/3f/Neyeptune_Idle.gif", "mobs/Neyeptune_Idle.gif"], ["f/ff/Bloodbone_Idle.gif", "mobs/Bloodbone_Idle.gif"], ["0/05/Mutated_Mush_Idle.gif", "mobs/Mutated_Mush_Idle.gif"], ["7/75/Purp_Mushroom_Idle.gif", "mobs/Purp_Mushroom_Idle.gif"], ["3/35/Donut_Idle.gif", "mobs/Donut_Idle.gif"], ["5/54/Flying_Worm_Idle.gif", "mobs/Flying_Worm_Idle.gif"], ["e/e7/Choccie_Idle.gif", "mobs/Choccie_Idle.gif"], ["8/8d/Biggole_Wurm_Idle.gif", "mobs/Biggole_Wurm_Idle.gif"], ["5/58/Clammie_Idle.gif", "mobs/Clammie_Idle.gif"], ["c/cb/Maccie_Idle.gif", "mobs/Maccie_Idle.gif"], ["c/c2/Cheese_Nub_Idle.gif", "mobs/Cheese_Nub_Idle.gif"], ["4/44/Molti_Idle.gif", "mobs/Molti_Idle.gif"], ["f/f5/Citringe_Idle.gif", "mobs/Citringe_Idle.gif"], ["f/f4/Biggole_Mole_Idle.gif", "mobs/Biggole_Mole_Idle.gif"], ["0/01/Tremor_Wurm_Idle.gif", "mobs/Tremor_Wurm_Idle.gif"], ["a/a0/Sprout_Spirit_Idle.gif", "mobs/Sprout_Spirit_Idle.gif"], ["9/91/River_Spirit_Idle.gif", "mobs/River_Spirit_Idle.gif"], ["1/11/Woodlin_Spirit_Idle.gif", "mobs/Woodlin_Spirit_Idle.gif"], ["8/86/Lantern_Spirit_Idle.gif", "mobs/Lantern_Spirit_Idle.gif"], ["c/cc/Leek_Spirit_Idle.gif", "mobs/Leek_Spirit_Idle.gif"], ["b/bc/Skydoggie_Spirit_Idle.gif", "mobs/Skydoggie_Spirit_Idle.gif"], ["b/ba/Royal_Egg_Idle.gif", "mobs/Royal_Egg_Idle.gif"], ["6/66/Samurai_Guardian_Idle.gif", "mobs/Samurai_Guardian_Idle.gif"]];
  const out = {};
  for (const [path, name] of items) {
    const r = await fetch("/images/" + path);
    if (!r.ok) { console.error("failed", path, r.status); continue; }
    const b = new Uint8Array(await r.arrayBuffer());
    let s = ""; for (let i = 0; i < b.length; i += 0x8000) s += String.fromCharCode.apply(null, b.subarray(i, i + 0x8000));
    out[name] = btoa(s);
    console.log(Object.keys(out).length + "/" + items.length, name);
  }
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([JSON.stringify(out)], { type: "application/json" }));
  a.download = "idleon-wiki-images.json";
  document.body.appendChild(a); a.click(); a.remove();
  console.log("Done:", Object.keys(out).length, "of", items.length, "files");
})();
