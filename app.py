"""
Search Engine v2 — Inverted Index + TF-IDF + Cosine Similarity
Supports user-uploaded .txt documents + default document collection
Flask Web Application
"""

import math
import os
import shutil
from collections import defaultdict, Counter
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "searchengine_secret_key"