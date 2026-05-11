{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5u+ekUTYqdaMJTmh99szc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Abdifitaah-mlops/Python-mlops/blob/main/calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def isku_dar(a, b):\n",
        "    return a + b\n",
        "\n",
        "def ka_jar(a, b):\n",
        "    return a - b\n",
        "\n",
        "def ku_dhuf(a, b):\n",
        "    return a * b\n",
        "\n",
        "def u_qaybi(a, b):\n",
        "    return a / b\n",
        "\n",
        "print(\"10 + 5 =\", isku_dar(10, 5))\n",
        "print(\"10 - 5 =\", ka_jar(10, 5))\n",
        "print(\"10 * 5 =\", ku_dhuf(10, 5))\n",
        "print(\"10 / 5 =\", u_qaybi(10, 5))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Khb2BGTmnudn",
        "outputId": "a061259e-240d-4691-c9d3-5315e5e43ad7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 + 5 = 15\n",
            "10 - 5 = 5\n",
            "10 * 5 = 50\n",
            "10 / 5 = 2.0\n"
          ]
        }
      ]
    }
  ]
}