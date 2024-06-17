```markdown
# Innovative Fistel Cipher (IFC)

Innovative Fistel Cipher (IFC) is a symmetric key encryption algorithm. This repository contains the implementation of the IFC algorithm in Python.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Details of the Algorithm](#details-of-the-algorithm)
  - [Initial Permutation](#initial-permutation)
  - [Round Function](#round-function)
  - [Key Generation](#key-generation)
  - [Final Permutation](#final-permutation)
- [Images](#images)

## Overview

IFC is designed to provide secure encryption through multiple rounds of permutation and substitution, using a master key to generate round keys. The algorithm follows the structure of a Fistel network.

## Installation

To install the necessary dependencies, you can use:

```bash
pip install -r requirements.txt
```

## Usage

To run the encryption, you can use the following command:

```bash
python IFC.py
```

## Details of the Algorithm

### Initial Permutation

The initial permutation step splits the 128-bit input into two 64-bit halves and applies a predefined permutation.

### Round Function

The round function `f` processes the left and right halves through several operations, including XOR, permutation, and keyed substitution.

### Key Generation

The master key is used to generate 32 round keys through a series of shifts and XOR operations.

### Final Permutation

The final permutation combines the left and right halves after 16 rounds to produce the encrypted output.

## Images

Here are the diagrams illustrating the IFC algorithm and its components:

### IFC Algorithm Overview

![IFC](https://github.com/amirhossein-izadi/Fistel-Cipher/tree/master/images/IFC.png)

### IFC Round Function

![IFC Round](https://github.com/amirhossein-izadi/Fistel-Cipher/tree/master/images/IFC-round.png)

### Key Generation

![Key Generation](https://github.com/amirhossein-izadi/Fistel-Cipher/tree/master/images/key-gen.png)

### Key Generation Round

![Key Generation Round](https://github.com/amirhossein-izadi/Fistel-Cipher/tree/master/images/key-gen-round.png)
```