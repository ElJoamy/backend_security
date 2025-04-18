import os
import re

input_file = "all_models.py"
output_dir = "src/models"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

imports = []
body_start = content.find("\n\n") + 2
if body_start > 0:
    imports = content[:body_start]

models = re.findall(r"(class\s+\w+\(.*?\n(?:    .*\n)+)", content)

for model in models:
    class_name = re.search(r"class\s+(\w+)", model).group(1)
    file_path = os.path.join(output_dir, f"{class_name.lower()}_model.py")
    with open(file_path, "w", encoding="utf-8") as out_file:
        out_file.write(imports)
        out_file.write(model)
