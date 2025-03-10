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

# Iterate through each group and their alters
for group, alters in sorted(groups.items()):  # Sort groups alphabetically
    # Create a index-directory for each group (e.g., _peritia/Host)
    group_path = os.path.join(peritia_path, group)

    # Create the index.md for the group
    group_content = f"""---
layout: System-Index
title: {group}
subtitle: {group} System
role: {group}
role-index: true
alter-index: false
author: System
parent: "This is Peritia"
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

        # Create unique files for each alter, and sort the keys (unique file titles) to ensure order
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
permalink: /peritia/{group.lower()}/{alter.lower()}/{file_title.replace(' ', '-').lower()}/
---
# {file_title} {alter}

{file_description.format(alter=alter)} content goes here...
"""
            file_path = os.path.join(alter_path, f"{file_title.replace(' ', '-').lower()}-{alter.lower()}.md")
            create_file(file_path, file_content)

print("Index.md and unique files created successfully!")
