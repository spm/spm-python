from mpython import Runtime


def spm_dcm_phase_results(*args, **kwargs):
    """
      Results for Dynamic Causal Modeling (DCM) for phase coupling
        FORMAT spm_dcm_phase_results(DCM,Action);
        Action:
            'Sin(Data) - Region j'
            'Coupling (As)'
            'Coupling (Bs)'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_phase_results.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_phase_results", *args, **kwargs)
