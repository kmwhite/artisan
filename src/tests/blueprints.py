import faker

Foo = {
    'name': lambda: faker.name.name()
}

Bar = {
    'random_attrib': lambda: faker.name.name()
}
