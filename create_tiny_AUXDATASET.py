from datasets import load_dataset
from tqdm import tqdm
from itertools import islice

TARGET_SAMPLES = 500_000  # ~10.5–11 GB target
SAVE_PATH = "the_pile_wikipedia.txt"


def load_wiki_data():
    """ Loads RedPajama Wikipedia datase. """
    ds = load_dataset(
        "togethercomputer/  ",
        name="wikipedia",
        split="train",
        trust_remote_code=True,
        streaming=True,
    ).remove_columns("meta")

    return ds

def save_wiki_data_to_txt_file(ds, save_path):
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        for sample in tqdm(islice(ds, TARGET_SAMPLES), total=TARGET_SAMPLES, dynamic_ncols=True):
            f.write(sample["text"].strip() + "\n\n")


def main():
    # Stream RedPajama Wikipedia
    ds = load_wiki_data()
    print(f"Streaming and saving ~11GB ({TARGET_SAMPLES:,} samples)...")

    save_wiki_data_to_txt_file(ds, SAVE_PATH)

    print(f"\n✅ Saved {TARGET_SAMPLES:,} samples to {SAVE_PATH}")

if __name__ == "__main__":
    main()