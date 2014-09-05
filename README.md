EPIC-PIDS
=========
[![DOI](https://zenodo.org/badge/1514/brucellino/EPIC-PIDS.png)](http://dx.doi.org/10.5281/zenodo.11613)

This repository contains demonstrator usage of the [EPIC](http://epic.grnet.gr/) Persistent Identifier (PID) [API](http://epic.grnet.gr/guides/api/).

# What it does.

This is a very simple, demonstrative python script which uses python [pandas](pandas.pydata.org) to extract a list of data sets from a CSV file, interrogate the API, and assign them handles. Handles are assigned to the URL of the data set, using the data set description as provided by the data catalogue as a suffix. 


# APHRC Use Case

The main use case of this script is a demonstrator. The work was funded by the  [CHAIN-REDS](http://www.chain-project), to support the [African Population and Health Research Centre](http://www.aphrc.org) in Nairobi.

APHRC runs a [NADA](http://www.ihsn.org/home/software/nada) microdata portal, provided by the [International Household Statistics Network (IHSN)](http://www.ihsn.org/home/) which uses the [ Data Documentation Initiative](http://www.ddialliance.org) metadata  schema. 

## Issueing PID's to APHRC's data sets

In order to reliably cite the APHRC's data sets, track usage and impact, the data sets should be issued with a persistent [handle](http://en.wikipedia.org/wiki/Handle_System) via the [EPIC cosortium](http://www.pidconsortium.eu/) handle server.

A CSV file describing the APHRC data sets, in their NADA [microdata portal](aphrc.org/catalog/microdata/index.php/catalog) is downloaded and parsed as a data frame. In order to construct the correct http request of the REST API, 
  1. the `dataCollectionNumber` is used to generated a URL referring to the data set
  2. the `dataCollectionName` is used to construct the [suffix](http://epic.grnet.gr/guides/glossary/)

that's it really :)

# Citing this work
Please use the [![DOI](https://zenodo.org/badge/1514/brucellino/EPIC-PIDS.png)](http://dx.doi.org/10.5281/zenodo.11613) to refer to this work when citing it.
