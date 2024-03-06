import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def initialize_hypotheses(n):
    return [('?',) * n]

def is_consistent(hypothesis, instance):
    for hypo, instance_value in zip(hypothesis, instance):
        if hypo != '?' and hypo != instance_value:
            return False
    return True

def is_more_general(hypo1, hypo2):
    for h1, h2 in zip(hypo1, hypo2):
        if h1 != '?' and h2 == '?':
            return False
        elif h1 == '?' and h2 != '?':
            continue
        elif h1 != h2:
            return False
    return True

def is_more_specific(hypo1, hypo2):
    return is_more_general(hypo2, hypo1)

def remove_inconsistent(hypotheses, instance, target):
    consistent_hypotheses = []
    for hypo in hypotheses:
        if is_consistent(hypo, instance):
            consistent_hypotheses.append(hypo)
    for hypo in consistent_hypotheses:
        if target == 'positive':
            if not is_more_general(hypo, instance):
                hypotheses.remove(hypo)
        else:
            if not is_more_specific(hypo, instance):
                hypotheses.remove(hypo)
    return hypotheses

def find_generalizations(instance, target):
    generalizations = []
    n = len(instance)
    for i in range(n):
        if target == 'positive':
            generalization = list(instance)
            generalization[i] = '?'
            generalizations.append(tuple(generalization))
        else:
            if instance[i] != '?':
                generalization = list(instance)
                generalization[i] = '?'
                generalizations.append(tuple(generalization))
    return generalizations

def candidate_elimination(training_data):
    num_attributes = len(training_data[0]) - 1
    S = [tuple(['0' for _ in range(num_attributes)])]
    G = [tuple(['?' for _ in range(num_attributes)])]

    for instance in training_data:
        if instance[-1] == 'positive':
            G = remove_inconsistent(G, instance[:-1], 'positive')
            for s in list(S):
                if not is_consistent(s, instance[:-1]):
                    S.remove(s)
                    generalizations = find_generalizations(instance[:-1], 'positive')
                    for g in generalizations:
                        if not any(is_more_general(g, h) for h in G):
                            S.append(g)
        else:
            S = remove_inconsistent(S, instance[:-1], 'negative')
            for g in list(G):
                if is_consistent(g, instance[:-1]):
                    G.remove(g)
                    specializations = find_generalizations(instance[:-1], 'negative')
                    for s in specializations:
                        if not any(is_more_specific(s, h) for h in S):
                            G.append(s)

    return S, G

# Example usage
file_path = 'enjoysport.csv'
training_data = read_csv(file_path)
S_hypotheses, G_hypotheses = candidate_elimination(training_data)
print("Final Specific hypotheses (S):", S_hypotheses)
print("Final General hypotheses (G):", G_hypotheses)
