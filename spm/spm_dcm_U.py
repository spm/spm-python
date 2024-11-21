from spm.__wrapper__ import Runtime


def spm_dcm_U(*args, **kwargs):
    """
      Insert new inputs into a DCM  
        FORMAT DCM = spm_dcm_U(DCM,SPM,sess,inputs)  
         
        DCM     - DCM structure or its filename  
        SPM     - SPM structure or its filename  
        sess    - session index     (integer)  
        inputs  - Inputs to include (cell array)  
         
        Examples of specification of parameter 'inputs':  
        * without parametric modulations:  
          {1, 0, 1} includes inputs 1 and 3.  
        * with parametric modulations:  
          {1,0,[0 0 1],[0 1]} includes the non-modulated first input, the second  
          PM of the third input and the first PM of the fourth input.  
        Note that this cell array only has to be specified up to the last input  
        that is replaced.  
         
        This function can be used, for example, to replace subject X's inputs by  
        subject Y's. The model can then be re-estimated without having to go  
        through model specification again.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_U.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_U", *args, **kwargs)
