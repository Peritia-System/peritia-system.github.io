import os
import random
import string

# Function to create a random word of a given length
def generate_random_word(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Function to create a random file with content
def create_random_file(path, group, alter, title):
    random_word = generate_random_word()  # Fix: use generate_random_word
    file_content = f"""---
layout: alter-system
title: {random_word}
subtitle: {random_word} {random_word} {random_word}
role: {group}
role-index: false
alter-index: false
author: {alter}
header-style: text
category: 
  - Peritia-System
permalink: /peritia/{group.lower()}/{alter.lower()}/
---

# {random_word}{random_word}
{random_word}{random_word}{random_word}{random_word}{random_word}{random_word}
{random_word}{random_word}{random_word}{random_word}{random_word}{random_word}{random_word}
"""
    # Create the random file with the generated content
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(file_content)

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
author: System
header-style: text
category: 
   - Peritia-System
permalink: /peritia/{group.lower()}/{alter.lower()}/
---
# {alter}
Content for the {alter} alter.
"""
        create_index_file(alter_path, alter_content)

        # Create 3 random files in the alter directory
        for _ in range(3):
            random_file_title = generate_random_word()
            create_random_file(os.path.join(alter_path, f"{random_file_title}.md"), group, alter, random_file_title)

print("Filler index.md and random files created successfully!")
