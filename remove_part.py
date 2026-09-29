import os

folder_path = os.getcwd()


targets = [
    ", Packt Publishing",
    "- libgen.li",
    "- libgen.lc",
    "ilide.info-",
    "_OceanofPDF.com_"
]

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.lower().endswith(".pdf"):
            new_name = filename

            # apply all replacements
            for t in targets:
                new_name = new_name.replace(t, "")

            if new_name != filename:
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_name)

                if not os.path.exists(new_path):
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")
                else:
                    print(f"Skipped (exists): {new_path}")

print("Done!")
# import os

# target = ", Packt Publishing"
# target = "- libgen.li"

# for root, dirs, files in os.walk(os.getcwd()):
#     for filename in files:
#         if filename.lower().endswith(".pdf") and target in filename:
#             old_path = os.path.join(root, filename)
#             new_name = filename.replace(target, "")
#             new_path = os.path.join(root, new_name)

#             # Avoid overwriting
#             if not os.path.exists(new_path):
#                 os.rename(old_path, new_path)
#                 print(f"Renamed: {old_path} -> {new_path}")
#             else:
#                 print(f"Skipped (exists): {new_path}")

# print("Done!")
