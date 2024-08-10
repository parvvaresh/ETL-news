from sklearn.naive_bayes import MultinomialNB

def get_nb():
    param_naive_bayes = {
        'alpha': [0.1, 0.5, 1.0, 2.0, 5.0]  
    }
    
    return MultinomialNB(), param_naive_bayes
