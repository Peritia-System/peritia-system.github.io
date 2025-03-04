import os

# Function to create a file with specific content
def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

# Function to create an index.md file with content
def create_index_file(path, content):
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.md"), "w") as f:
        f.write(content)

# Define the peritia structure with groups and their alters
peritia_path = "_peritia"

groups = {
    "Host": ["Selena", "Mergan"],
    "Protector": ["Rust"]
}

# Files to create for each alter
unique_files = {
    "A letter from": "A heartfelt letter from {alter}",
    "A personal message from": "A personal message just for {alter}"
}

# Filler data for each alter
filler_data = {
    "Selena": "This is a filler content for Selena, explaining her role and backstory.",
    "Mergan": "This is a filler content for Mergan, explaining his role and backstory.",
    "Rust": "This is a filler content for Rust, explaining his role and backstory."
}

# Extra files for specific alters
extra_files = {
    "Selena": ["funfacts.md"],
    "Mergan": [],
    "Rust": []
}

# Iterate through each group and their alters
for group, alters in sorted(groups.items()):  # Sort groups alphabetically
    # Create a index-directory for each group (e.g., _peritia/Host)
    group_path = os.path.join(peritia_path, group)

    # Create the index.md for the group
    group_content = f"""---
layout: default
title: {group}
subtitle: {group} System
role: {group}
role-index: true
alter-index: false
author: System
header-style: text
category:
   - Peritia-System
permalink: /peritia/{group.lower()}/
---
# {group}
Content for the {group} group.
"""
    create_index_file(group_path, group_content)

    # Sort the alters within each group and create their index.md files
    for alter in sorted(alters):  # Sort alters alphabetically within each group
        alter_path = os.path.join(group_path, alter)

        # Set alter-specific content with parent-child logic
        alter_content = f"""---
layout: alter-system
title: {alter}
subtitle: {alter} Alter
role: {group}
role-index: false
alter-index: true
author: {alter}
parent: {group}
header-style: text
category:
   - Peritia-System
permalink: /peritia/{group.lower()}/{alter.lower()}/
---
# {alter}
{filler_data.get(alter, "Default filler content for the alter.")}
"""
        create_index_file(alter_path, alter_content)

        # Create additional files for specific alters like "funfacts.md" for Selena
        for extra_file in extra_files.get(alter, []):
            file_content = f"""---
layout: alter-system
title: {extra_file.replace('.md', '').replace('-', ' ').title()} {alter}
subtitle: Some unique content for {alter}
role: {group}
role-index: false
alter-index: false
author: {alter}
parent: {alter}
header-style: text
category:
   - Peritia-System
permalink: /peritia/{group.lower()}/{alter.lower()}/{extra_file.replace('.md', '').replace(' ', '-').lower()}/
---
# {extra_file.replace('.md', '').replace('-', ' ').title()} {alter}

Unique content for {alter} goes here...
"""
            file_path = os.path.join(alter_path, extra_file)
            create_file(file_path, file_content)

        # Create the "Stories" subdirectory for each alter
        stories_path = os.path.join(alter_path, "Stories")
        os.makedirs(stories_path, exist_ok=True)

        # Create unique files (e.g., a-letter-from-{alter}.md) in the Stories subdirectory
        for file_title, file_description in sorted(unique_files.items()):  # Sort file titles alphabetically
            file_content = f"""---
layout: alter-system
title: {file_title} {alter}
subtitle: {file_description.format(alter=alter)}
role: {group}
role-index: false
alter-index: false
author: {alter}
parent: {alter}
header-style: text
category:
   - Peritia-System
permalink: /peritia/{group.lower()}/{alter.lower()}/stories/{file_title.replace(' ', '-').lower()}/
---
# {file_title} {alter}

{file_description.format(alter=alter)} content goes here...
"""
            file_path = os.path.join(stories_path, f"{file_title.replace(' ', '-').lower()}-{alter.lower()}.md")
            create_file(file_path, file_content)

        # If the alter is Rust, create the "fights" subdirectory and files
        if alter == "Rust":
            fights_path = os.path.join(alter_path, "fights")
            os.makedirs(fights_path, exist_ok=True)

            fights_files = ["Day36.md", "iambetter.md"]
            for fight_file in fights_files:
                fight_file_path = os.path.join(fights_path, fight_file)
                create_file(fight_file_path, f"---\nlayout: alter-system\ntitle: {fight_file.replace('.md', '')}\nsubtitle: Fight content\nrole: {group}\nrole-index: false\nalter-index: false\nauthor: Rust\nparent: Rust\nheader-style: text\ncategory:\n  - Peritia-System\npermalink: /peritia/{group.lower()}/{alter.lower()}/fights/{fight_file.replace('.md', '').lower()}/\n---\n# {fight_file.replace('.md', '')}\nContent about {fight_file.replace('.md', '')} goes here...\n")

print("Index.md and unique files created successfully!")
