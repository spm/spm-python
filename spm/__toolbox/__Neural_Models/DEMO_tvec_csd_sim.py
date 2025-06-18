from mpython import Runtime


def DEMO_tvec_csd_sim(*args, **kwargs):
    """
      DEMO_tvec_csd_sim - Demo script for modelling time-varying effective
        connectivity in a DCM for CSD.

        This script demonstrates key aspects of the modelling approach
        described in the paper. Specifically, it simulates and recovers
        a dynamic causal model (DCM) with time-varying connectivity,
        showcasing the use of temporal basis functions to model slow
        fluctuations in synaptic efficacy.

        Overview of this script:
        1. **Model Setup:**
           - Defines a simple two-region DCM with forward and backward connections.
           - Uses a cosine basis set to represent time-varying connectivity modulations.

        2. **Data Simulation:**
           - Generates synthetic neural responses based on predefined modulations.
           - Adds noise to simulate observed data.

        3. **Parameter Recovery:**
           - Implements Bayesian model inversion to estimate connectivity changes.

        4. **Visualization:**
           - Plots the true and recovered connectivity modulations.
           - Compares simulated, observed, and recovered neuronal responses.


        Outputs:
        - Visualization of true vs. recovered connectivity modulations.
        - Signal-to-noise ratio (SNR) of synthetic data.
        - Simulated, observed, and recovered neuronal responses.

        For further details, refer to the paper:
          Medrano, J., Friston, K. J., & Zeidman, P. (2024).
          Dynamic Causal Models of Time-Varying Connectivity.

       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/DEMO_tvec_csd_sim.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEMO_tvec_csd_sim", *args, **kwargs, nargout=0)
