import pandas as pd

FILENAME = 'SocialMediaTop100.csv'

def print_stats(title, df):
    print(f'\n--- {title} ---')
    print(df.describe(include='all'))
    for col in df.select_dtypes(include='object').columns:
        print(f"{col} unique: {df[col].nunique()}")
        print(f"{col} most frequent: {df[col].mode().iloc[0] if not df[col].mode().empty else None}")

def main():
    df = pd.read_csv(FILENAME, encoding='ISO-8859-1')
    print_stats('Overall', df)

    # By Platform
    for platform, group in df.groupby('Platform'):
        print_stats(f'Platform={platform}', group)

    # By Platform + PROFILE
    for (platform, profile), group in df.groupby(['Platform', 'PROFILE']):
        print_stats(f'Platform={platform}, PROFILE={profile}', group)

if __name__ == '__main__':
    main() 