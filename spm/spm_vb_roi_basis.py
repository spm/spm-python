from spm.__wrapper__ import Runtime


def spm_vb_roi_basis(*args, **kwargs):
    """
      Compare Hemodynamic Basis sets for a cluster of interest  
        FORMAT [F,pm] = spm_vb_roi_basis (VOI_fnames,SPM,bases,model)  
         
        VOI_fname     VOI filenames eg. VOI_fnames{1}='Test_VOI.mat'  
         
        SPM           SPM data structure (this must be loaded in from an   
                      SPM.mat file). If this field is not specified this function  
                      will prompt you for the name of an SPM.mat file  
         
        bases         Specifies which basis sets to compare:  
         
                      'all'   - the 7 default types (see help spm_get_bf)  
                      'fir'   - Finite Impulse Response with variable number of bins  
                      'fh'    - Fourier + Hanning window with variable number of bins  
                      'user'  - user specified models set by model variable   
                                (see below). This allows a user-specified set of  
                                models to be compared.  
         
                      The default option is 'all'  
         
        model         For ith basis set specify  
         
                      model(i).name - see help spm_get_bf  
                      model(i).sname - short name to be used in results histogram   
                      model(i).order - number of basis functions/number of bins  
                      model(i).length - overall window length in seconds  
         
                      for i=1..number of models  
         
                      This variable only needs to be specified if the bases option  
                      is set to 'user'.  
         
                      Typical function usages:   
         
                      [F,pm]=spm_vb_roi_basis('Test_VOI.mat');  
                      [F,pm]=spm_vb_roi_basis('Test_VOI.mat',SPM);  
                      [F,pm]=spm_vb_roi_basis('Test_VOI.mat',SPM,'fir');  
                      [F,pm]=spm_vb_roi_basis('Test_VOI.mat',SPM,'user',model);  
         
        F             model evidences   
        pm            posterior model probability  
         
        See W. Penny et al. (2007). Bayesian Model Comparison of Spatially   
        Regularised General Linear Models. Human Brain Mapping.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_roi_basis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_roi_basis", *args, **kwargs)
