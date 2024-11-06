from spm.__wrapper__ import Runtime


def mci_compare_gradients(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/demo-gradients/mci_compare_gradients.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_compare_gradients", *args, **kwargs)
