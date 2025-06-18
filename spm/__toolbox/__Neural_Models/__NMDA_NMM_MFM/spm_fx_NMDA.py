from mpython import Runtime


def spm_fx_NMDA(*args, **kwargs):
    """
      FORMAT [f] = spm_fx_NMDA(x_V,x_G,P,M)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/NMDA_NMM_MFM/spm_fx_NMDA.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_NMDA", *args, **kwargs)
