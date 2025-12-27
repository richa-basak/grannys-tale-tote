#!/usr/bin/env bash
set -e

APP_NAME="Granny’s Tale Tote"
PYTHON_BIN=python3
VENV_DIR=".venv"

echo "🧺 Starting $APP_NAME..."

if [ -d "$VENV_DIR" ]; then
  source "$VENV_DIR/bin/activate"
fi

if ! command -v $PYTHON_BIN &> /dev/null; then
  echo "❌ Python3 not found"
  exit 1
fi


$PYTHON_BIN -m app.main

