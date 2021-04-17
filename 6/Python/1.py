from JFLAP import jflap

DFA = {
    "q0": {"a": "q0", "b": "q1", "accept": False},
    "q1": {"a": "q1", "b": "q2", "accept": False},
    "q2": {"a": "q2", "b": "q3", "accept": True},
    "q3": {"a": "q3", "b": "q3", "accept": False},
}

jflap(DFA)
