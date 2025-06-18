from mpython import Runtime


def covLin(*args, **kwargs):
    """
      Covariance function for linear regression/classification
        FORMAT [K1,lambda] = covLin(lambda0,settings,args,lab)
        No usage documentation yet
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/covLin.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("covLin", *args, **kwargs)
