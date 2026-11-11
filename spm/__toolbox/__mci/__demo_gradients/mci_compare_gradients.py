from spm._runtime import Runtime


def mci_compare_gradients(*args, **kwargs):
    r"""
      Compare methods for gradient computation  
        FORMAT [els,names] = mci_compare_gradients (model,cost,methods)  
         
        model     'phase', 'nmm-r2p2'  
        cost      'loglike', 'spm_mci_joint' (default)  
        methods   vector of integers indicating which methods to  
                  compare eg. [1,2,3,4,5] (default) for 1. SensMat,   
                  2. SensSun, 3. AdjMat, 4. AdjSun, 5. FD  
         
        els       Computation times  
        names     Names of compared methods  
         
        Note: 4. AdjSun may not work for nmm2-r2p2.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/demo-gradients/mci_compare_gradients.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_compare_gradients", *args, **kwargs)
