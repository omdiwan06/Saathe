# Grievance Complaint Management System

## Overview

This repository contains the implementation of a Citizen Complaint Management System using Machine Learning for automatic complaint categorization and priority assignment.

## Features

- *Machine Learning Model:*
  - Automatic categorization of citizen complaints using a Transformer BERT model.
  - Priority assignment based on predefined pairs of 'avd_for' and 'type'.

## Web Application

The web application is built using Streamlit, providing an interface for users to submit complaints and view categorized results.

## Project Structure

- **ml_model/:**
  - Contains the code and resources for the Machine Learning model.
  - please refer to saarthe.ipynb
  

- **priority_assignment/:**
  - Implements the priority assignment logic.
  - tryone.py


- **web_app/:**
  -This directory holds the web application code.
  - -main.py --abcd.py --proxy.py

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/omdiwan_06/citizen-complaint-management.git
   cd Minor
