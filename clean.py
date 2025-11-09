import re, pandas as pd
import emoji

def basic_clean(text: str):
    if not isinstance(text, str): return text
    text = text.lower()
    text = emoji.replace_emoji(text, replace='')
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--in_csv", required=True)
    p.add_argument("--out_csv", required=True)
    p.add_argument("--col", required=True)
    a = p.parse_args()
    df = pd.read_csv(a.in_csv)
    df[a.col] = df[a.col].map(basic_clean)
    df.to_csv(a.out_csv, index=False)
