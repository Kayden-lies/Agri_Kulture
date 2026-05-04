from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix

def evaluate_model(y_true, y_pred):
    p, r, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted', zero_division=0)
    return {
        'accuracy': float(accuracy_score(y_true, y_pred)),
        'precision': float(p), 'recall': float(r), 'f1_score': float(f1),
        'confusion_matrix': confusion_matrix(y_true, y_pred).tolist(),
    }
