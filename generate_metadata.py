import pandas as pd

# Load the data dictionary
df = pd.read_csv("data_dictionary.csv")

# Generate metadata documentation
with open("generated_metadata.md", "w") as f:
    f.write("# Generated Metadata Documentation\\n\\n")
    f.write("## Data Dictionary\\n")
    for _, row in df.iterrows():
        f.write(f"- `{row['Column_Name']}`: {row['Description']} ({row['Data_Type']}).\\n")
    f.write("\\n## Notes\\n")
    f.write("This metadata was auto-generated from the data dictionary.")
print("Metadata documentation generated successfully!")

