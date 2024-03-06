import csv
def load_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data
def find_s_algorithm(data):
    hypothesis = data[0][:-1] 
    for instance in data:
        if instance[-1] == 'Yes': 
            for i in range(len(hypothesis)):
                if instance[i] != hypothesis[i]:
                    hypothesis[i] = '?'  
    return hypothesis
def demonstrate_hypothesis(hypothesis):
    print("The most specific hypothesis is:", hypothesis)
def main():
    filename = 'enjoysport.csv'  
    data = load_data(filename)
    hypothesis = find_s_algorithm(data)
    demonstrate_hypothesis(hypothesis)
if __name__ == "__main__":
    main()
