#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:24:55 2018

@author: user01
"""

#%% Logging

import logging

logging.basicConfig()

log=logging.getLogger()

log.setLevel(logging.INFO)


log.info("The system is running")


log.debug("Nothing said")


log.error("Now it's serious!")

#%% Debugging


import pdb #debug package

pdb.set_trace()# set a breakpoint and opens the debug console, type help



