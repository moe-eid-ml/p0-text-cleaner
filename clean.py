import re, pandas as pd
import emoji

# ASCII punctuation class (so we don't wipe emojis when keep_emoji=True)
ASCII_PUNCT = r'[!"#$%&\'()*+,\-./:;<=>?@\[\]\\^_`{|}~]'

def basic_clean(text: str, keep_emoji: bool = False, keep_punct: bool = False):
    if not isinstance(text, str):
        return text
    text = text.lower()
    if not keep_emoji:
        text = emoji.replace_emoji(text, replace='')
    if not keep_punct:
        if keep_emoji:
            # remove ASCII punctuation only; leave emojis intact
            text = re.sub(ASCII_PUNCT, '', text)
        else:
            # broad: remove anything that's not word/space
            text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Clean a text column in a CSV.")
    p.add_argument("--in_csv", required=True, help="Input CSV path")
    p.add_argument("--out_csv", required=True, help="Output CSV path")
    p.add_argument("--col", required=True, help="Column name to clean")
    p.add_argument("--keep-emoji", action="store_true", help="Keep emojis (default removes)")
    p.add_argument("--keep-punct", action="store_true", help="Keep punctuation (default removes)")
    a = p.parse_args()

    df = pd.read_csv(a.in_csv)
    df[a.col] = df[a.col].map(lambda t: basic_clean(
        t, keep_emoji=a.keep_emoji, keep_punct=a.keep_punct
    ))
    df.to_csv(a.out_csv, index=False)
