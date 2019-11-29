from pyDatalog.pyDatalog import create_terms, ask, load, assert_fact, clear

if __name__ == '__main__':
    clear()
    create_terms('X, age, glycemie, concerned, diabete')

    load("""
            concerned(X) <= (age(X) <= 5)
            hyperglycemic_risk(X) <= concerned(X) & (glycemie(X) > 10)
            hyperglycemic_risk(X) <= concerned(X) & (glycemie(X) < 5)
        """)