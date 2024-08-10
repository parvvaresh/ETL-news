from sklearn.neural_network import MLPClassifier


def get_mlp():
    param_mlp = {
        'hidden_layer_sizes': [(50,), (100,), (50, 50), (100, 100)],
        'activation': ['tanh', 'relu'],
        'solver': ['sgd', 'adam'],
        'alpha': [0.0001, 0.001, 0.01],
        'learning_rate': ['constant', 'adaptive'],
        'max_iter': [100, 200, 300, 400, 500],
    }

    return MLPClassifier(), param_mlp