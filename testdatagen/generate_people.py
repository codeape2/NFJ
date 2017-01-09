# husk SET PYTHONIOENCODING=utf8 før kjøring
import itertools

from datagen.datagen import generate_persons


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("count")

    args = parser.parse_args()

    for p in itertools.islice(generate_persons(), 0, int(args.count)):
        print(p.name, p.sex, "00000000000", sep=';')