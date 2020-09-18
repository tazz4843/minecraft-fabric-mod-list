# coding=utf-8
import re
from json import dump

mod_list_file = open("mod_list.txt", "r")
mod_list_text = mod_list_file.read()
temp_mod_list = mod_list_text.split("\n")

mod_list = []
for item, i in zip(temp_mod_list, range(-3, len(temp_mod_list))):
    if "|" not in item:
        continue
    temp_item = item.split("|")
    if not temp_item[0].startswith("**"):
        continue
    name_regex = re.compile(r"\*\*\[([\s\S]*)]\(([\s\S]*)\)\*\*")
    match = name_regex.search(temp_item[0])
    if not match:
        print("Didn't find a match on line {0}!".format(i+1))
        continue
    mod_name, mod_url = match.group(1, 2)
    mod_short_description = temp_item[1]
    mod_downloads = temp_item[2]
    mod_latest_version = temp_item[3]

    mod_list.append({"id": i+1,
                     "name": mod_name,
                     "url": mod_url,
                     "short_description": mod_short_description,
                     "downloads": mod_downloads,
                     "latest_supported_version": mod_latest_version})

    print("Sucesfully parsed mod on line {0}!".format(i+1))

parsed_mod_list_file = open("parsed_mod_list.json", "w")
dump(mod_list, parsed_mod_list_file, indent=2)
parsed_mod_list_file.close()
print("Done!")
