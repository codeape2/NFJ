from datagen import datareader
import itertools


class PersonData:
    def __init__(self, name, sex, birthdate):
        self.name = name
        self.sex = sex
        self.birthdate = birthdate


def generate_persons():
    boy_names = itertools.cycle(datareader.read_guttenavn())
    girl_names = itertools.cycle(datareader.read_jentenavn())
    last_names = itertools.cycle(datareader.read_etternavn())

    while True:
        last_name = next(last_names)
        yield PersonData("{} {}".format(next(boy_names), last_name), "M", "TODO")
        yield PersonData("{} {}".format(next(girl_names), last_name), "F", "TODO")
