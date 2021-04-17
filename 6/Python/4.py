from JFLAP import jflap

DFA = {
    "q0": {"a": "q1", "b": "q2", "c": "q0", "accept": False},
    "q1": {"a": "q0", "b": "q3", "c": "q1", "accept": False},
    "q2": {"a": "q3", "b": "q0", "c": "q2", "accept": True},
    "q3": {"a": "q2", "b": "q1", "c": "q3", "accept": False},
}

jflap(DFA)
