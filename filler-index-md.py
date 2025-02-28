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

# Iterate through each group and their alters
for group, alters in groups.items():
    # Create a directory for each group (e.g., _peritia/Host)
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
    
    # Create an index.md for each alter within the group (e.g., _peritia/Host/Selena)
    for alter in alters:
        alter_path = os.path.join(group_path, alter)
        
        # Set alter-specific content
        alter_content = f"""---
layout: alter-system
title: {alter}
subtitle: {alter} Alter
role: {group}
role-index: false
alter-index: true
author: {alter}
header-style: text
category: 
   - Peritia-System
permalink: /peritia/{group.lower()}/{alter.lower()}/
---
# {alter}
Content for the {alter} alter.
"""
        create_index_file(alter_path, alter_content)

        # Create unique files for each alter
        for file_title, file_description in unique_files.items():
            file_content = f"""---
layout: alter-system
title: {file_title} {alter}
subtitle: {file_description.format(alter=alter)}
role: {group}
role-index: false
alter-index: false
author: {alter}
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
