from spm._runtime import Runtime


def spm_RDP_reduce(*args, **kwargs):
    r"""
      places parameters in a recursive model  
        FORMAT RDP = spm_RDP_reduce(MDP,BMR)  
        MDP   - nested MDP: full  
        BMR   - Bayesian model reduction {'SIMPLE','MI','HARD','SOFT'}  
        param - {'a','A',...}  
         
        This routine applies various forms of Bayesian model reduction to the  
        Dirichlet parameters or mappings specified in param (as strings). The  
        simple or mutual information options will apply Bayesian model reduction  
        based upon comparing models with and without a particular parameter  
        (simple) or based upon models that increase mutual information (i.e.,  
        decrease expected free energy). The hard and soft options simply  
        threshold low probability entries; either using a hard threshold or by  
        increasing the precision of the specified probabilistic mapping. Note  
        that a soft option will convert Dirichlet parameters into a multinomial  
        distribution (that may require rescaling if necessary).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_RDP_reduce.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_RDP_reduce", *args, **kwargs)
