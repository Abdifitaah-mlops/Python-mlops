{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Abdifitaah-mlops/Python-mlops/blob/main/mlops-pipeline.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import mlflow\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import r2_score\n",
        "\n",
        "# 1. Create Dataset\n",
        "data = {\n",
        "    \"rooms\": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],\n",
        "    \"house_age\": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],\n",
        "    \"price\": [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]\n",
        "}\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "# 2. Train Model\n",
        "X = df[[\"rooms\", \"house_age\"]]\n",
        "y = df[\"price\"]\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\n",
        "model = LinearRegression()\n",
        "model.fit(X_train, y_train)\n",
        "accuracy = r2_score(y_test, model.predict(X_test))\n",
        "\n",
        "# 3. MLflow Tracking\n",
        "mlflow.start_run()\n",
        "mlflow.log_param(\"model\", \"LinearRegression\")\n",
        "mlflow.log_metric(\"accuracy\", accuracy)\n",
        "mlflow.end_run()\n",
        "\n",
        "# 4. Predict\n",
        "new_house = pd.DataFrame({\"rooms\": [6], \"house_age\": [20]})\n",
        "prediction = model.predict(new_house)\n",
        "\n",
        "print(\"Pipeline completed!\")\n",
        "print(\"Accuracy:\", accuracy)\n",
        "print(\"Prediction:\", prediction[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EzB9sjycL6z8",
        "outputId": "79c7ffa2-9efe-4e79-da45-c004c66bc908"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Pipeline completed!\n",
            "Accuracy: 1.0\n",
            "Prediction: 407.6923076923077\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPbAwExadRFhkTEzlvX10ar",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}