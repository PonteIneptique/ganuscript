Ganuscrit
=========

[Paper](https://hal.science/hal-03335326)

## Install

Install `requirements.txt`

## IPython Notebook

Notebooks are used for evaluating the results of HTR and generate figure for the paper.

- `01` compiles a CSV of metadata, including links, about the training set
- `02` plot the amount of training elements for each source (IIIF vs. Mandragore) and for each century.
- `03` generates report from HTR test / prediction logs to average differences over 10 runs per configuration
- `03` generates report from segmentation test

## Kraken training and test

While Kraken 4.x should work, we recommand testing with Kraken 2.x.
