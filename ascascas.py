import os
import yaml
'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
from flask import Flask, request, jsonify, redirect, send_from_directory, session
from loguru import logger
from adapters.orm import JsonRepository
from domain.commit_utils import CommitDataHadler




def plot(test_loss, train_loss):
    %matplotlib inline
    plt.figure(figsize=(25, 20))
    plt.plot(test_loss, 'r', linewidth=2)
    plt.plot(train_loss, 'g', linewidth=2)
    
    plt.legend(['test', 'trai'])
    ''

def get_loss(clf, X, y):
    loss = []
    # Используйте метод staged_decision_function для предсказания качества
    # на обучающей и тестовой выборке на каждой итерации.
    for y_pred in clf.staged_decision_function(X):
        # Вычислите и постройте график значений log-loss