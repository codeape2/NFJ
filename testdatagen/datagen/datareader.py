import csv
import os
import itertools


def openfile(filename):
    return open(os.path.join(os.path.dirname(__file__), filename), encoding="utf8")


def read_etternavn():
    with openfile("etternavn.csv") as f:
        return [row["Navn"] for row in csv.DictReader(f, delimiter=";")]


def read_guttenavn():
    with openfile("guttenavn.csv") as f:
        return [row[0] for row in itertools.islice(csv.reader(f, delimiter=";"), 1, None)]


def read_jentenavn():
    with openfile("jentenavn.csv") as f:
        return [row[0] for row in itertools.islice(csv.reader(f, delimiter=";"), 1, None)]