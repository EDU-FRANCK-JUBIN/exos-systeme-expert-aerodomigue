from pyDatalog.pyDatalog import create_terms, ask, load, assert_fact, clear

if __name__ == "__main__":
    clear()
    create_terms('X, frog, canary, green, yellow, chirps, sings, croakes, eatFlies')

    load("""
        frog(X) <= croakes(X) & eatFlies(X)
        canary(X) <= chirps(X) & sings(X)
        green(X) <= frog(X)
        yellow(X) <= canary(X)
    """)

    assert_fact('croakes', 'fritz')
    assert_fact('eatFlies', 'fritz')

    print("frog: ", ask('frog(X)'))
    print("green: ", ask('green(X)'))
    print("green: ", ask("green('cuitcuit')"))

