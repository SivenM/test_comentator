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
    
    plt.legend(['test', 'trai