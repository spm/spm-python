from spm._runtime import Runtime


def spm_design_contrasts(*args, **kwargs):
    r"""
      Make contrasts for one, two or three-way ANOVAs  
        FORMAT con = spm_design_contrasts(SPM)  
        SPM           - SPM structure  
         
        con           - structure array of contrasts with fields  
          con(i).c    - Contrast matrix  
          con(i).name - Name  
       __________________________________________________________________________  
         
        This function generates contrasts on the basis of the current SPM  
        design. This is specified in SPM.factor (how the factors relate to the  
        conditions) and SPM.xBF.order (how many basis functions per condition).  
         
        This function generates (transposed) contrast matrices to test  
        for the average effect of condition, main effects of factors and  
        interactions.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_design_contrasts.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_design_contrasts", *args, **kwargs)
