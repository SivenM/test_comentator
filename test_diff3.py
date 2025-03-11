import os
import yaml
import argparse
from flask import Flask, request, jsonify, redirect, send_from_directory, session
from loguru import logger
from adapters.orm import JsonRepository
from adapters.jira_api import JiraMaster
from domain.commit_utils import CommitDataHadler




def plot(test_loss, train_loss):
    %matplotlib inline
    plt.figure(figsize=(25, 20))
    plt.plot(test_loss, 'r', linewidth=2)
    plt.plot(train_loss, 'g', linewidth=2)
    
    plt.legend(['test', 'train'])
    plt.show()
    
def get_loss(clf, X, y):
    loss = []
    # Используйте метод staged_decision_function для предсказания качества
    # на обучающей и тестовой выборке на каждой итерации.
    for y_pred in clf.staged_decision_function(X):
        # Вычислите и постройте график значений log-loss (которую можно посчитать с помощью функции
        # sklearn.metrics.log_loss) на обучающей и тестовой выборках, а также найдите минимальное значение метрики
        #  и номер итерации, на которой оно достигается.
        loss.append(log_loss(y, 1.0 / (1.0 + np.exp(-y_pred))))

    min_iter = np.argmin(loss)
    min_loss = loss[min_iter]
    return loss, min_iter, min_loss