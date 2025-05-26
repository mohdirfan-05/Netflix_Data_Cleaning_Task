import pandas as pd

# Load the dataset
df = pd.read_excel("/content/Netflix_show.xlsx")

# Check shape and data types
print(df.shape)
print(df.info())

# Check missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)

# Drop rows with missing critical fields
df.dropna(subset=['date_added', 'rating', 'duration'], inplace=True)

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'])

# Standardize text fields
text_cols = ['type', 'title', 'director', 'cast', 'country', 'rating', 'duration', 'listed_in']
for col in text_cols:
    df[col] = df[col].str.lower().str.strip()

# Rename columns
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Export cleaned file
df.to_excel('cleaned_Netflix_show.xlsx', index=False)
print("Cleaned dataset saved successfully.")