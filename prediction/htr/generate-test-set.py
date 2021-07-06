import glob
import os.path as path


current_path = path.dirname(path.abspath(__file__))
print(current_path)

print(path.join(current_path, "**", "*.xml"))
for file in glob.glob(path.join(current_path, "**", "*.xml")):
	with open(path.join(current_path, "test-sets", f"colorized-{path.basename(file)}.txt"), "w") as f:
		f.write(path.normpath(file))

for file in glob.glob(path.join(current_path, "..", "..", "gt", "htr", "**", "*.xml")):
	with open(path.join(current_path, "test-sets", f"microfilm-{path.basename(file)}.txt"), "w") as f:
		f.write(path.normpath(file))