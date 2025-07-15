import polars as pl

FILENAME = 'SocialMediaTop100.csv'

def print_stats(title, df):
    print(f'\n--- {title} ---')
    print(df.describe())
    for col in df.columns:
        if df[col].dtype == pl.String:
            print(f"{col} unique: {df[col].n_unique()}")
            mode = df[col].mode()
            print(f"{col} most frequent: {mode[0] if len(mode) > 0 else None}")

def main():
    import io
    with open(FILENAME, 'r', encoding='ISO-8859-1') as f:
        content = f.read()
    utf8_content = content.encode('utf-8', errors='replace').decode('utf-8')
    csv_buffer = io.StringIO(utf8_content)
    df = pl.read_csv(csv_buffer, schema_overrides={
        'N': pl.Float64,
        'FOLLOWERS': pl.Float64,
        'POSTS': pl.Float64
    }, ignore_errors=True)
    print_stats('Overall', df)

    # By Platform
    for platform in df['Platform'].unique().to_list():
        group_df = df.filter(df['Platform'] == platform)
        print_stats(f'Platform={platform}', group_df)

    # By Platform + PROFILE
    for row in df.select(['Platform', 'PROFILE']).unique().iter_rows():
        platform, profile = row
        group_df = df.filter((df['Platform'] == platform) & (df['PROFILE'] == profile))
        print_stats(f'Platform={platform}, PROFILE={profile}', group_df)

if __name__ == '__main__':
    main() 