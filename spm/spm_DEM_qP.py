from mpython import Runtime


def spm_DEM_qP(*args, **kwargs):
    """
      Report on conditional estimates of parameters
        FORMAT spm_DEM_qP(qP,pP)

        qP.P   - conditional expectations
        qP.V   - conditional variance

        pP     - optional priors
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM_qP.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_qP", *args, **kwargs, nargout=0)
