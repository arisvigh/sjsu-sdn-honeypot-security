# Recovered source code

This repository contains a verified archival copy of `src/network_topology.py` from the 2015 SJSU group project.

The uploaded historical materials also include `HoneypotInSDN.py` and `AutomatedScriptOnAttack.py`. These two files were reviewed, but they are not currently published here.

## Code review findings

The topology creates five switches and 36 hosts, with nine hosts attached to each of four peripheral switches. The first switch has no directly attached hosts. It connects to the other four switches, which also have some connections between them.

The remaining files describe controller interactions, network rule management, log processing and scripted responses. They use legacy Python syntax and obsolete software APIs. They also contain demo credentials, fixed system configuration and other historical assumptions. None of the recovered scripts has been tested against a modern deployment.

In particular, the recovered logic does not by itself establish that individual observed IP addresses were used as matching criteria for network rules. Avoid treating this portfolio as a currently supported intrusion-prevention product.

These files are artifacts of a collaborative student project; individual code authorship has not been established.
