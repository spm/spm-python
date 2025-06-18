from mpython import Runtime


def DEMO_tvec_erp_mmn(*args, **kwargs):
    """
      DEMO_tvec_erp_mmn: Analyse modulatory dynamics in EEG Mismatch Negativity
        using Dynamic Causal Modeling of Time-Varying Connectivity.

        This script analyzes EEG mismatch negativity (MMN) data using dynamic
        causal modeling (DCM) in SPM. It includes data preparation,
        preprocessing, and both initial and advanced DCM analyses to
        explore neural connectivity and modulatory effects over time.

        The script assumes you have access to SPM and the necessary data files.
        If the data is unavailable, it will download the sample dataset.
        Customize file paths and parameters as needed.

        Key Steps:
        1. Data Preparation: Prepares directories and checks for necessary files.
        2. Data Preprocessing: Converts raw EEG data into SPM-compatible format,
        filters, and epochs the data.
        3. Initial DCM Analysis: Fits a basic DCM model to analyze ERP responses
        and estimate neural connections.
        4. Advanced Analysis: Refines the DCM model to assess synaptic plasticity
        and time-varying connectivity.
        5. Visualization: Projects connectivity changes over time and compares
        observed vs. modeled ERPs.

        Requirements:
        - MATLAB with SPM12 installed.
        - Access to raw EEG data or an internet connection for dataset download.

        For further details, refer to the paper:
          Medrano, J., Friston, K. J., & Zeidman, P. (2024).
          Dynamic Causal Models of Time-Varying Connectivity.

       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/DEMO_tvec_erp_mmn.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEMO_tvec_erp_mmn", *args, **kwargs, nargout=0)
