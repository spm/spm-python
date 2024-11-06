from spm.__wrapper__ import Runtime


def bf_wizard_data(*args, **kwargs):
    """
      A handy command-line based batch filler with some defaults for DAiSS  
        data module, pick a few options and default for unpopulated fields. It  
        will by default run the batch for the user.  
         
        FORMAT [BF, batch, data] = bf_wizard_data(S)  
          S               - input structure  
        Optional fields of S:  
          S.D             - SPM MEEG object               - Default: REQUIRED  
          S.dir           - path to save DAiSS BF.mat     - Default: same as S.D  
          S.val           - which D.inv to use            - Default: 1  
          S.gradsource    - where to pool sensor information from  
                              (inv | sens)  
                                                          - Default: 'inv'  
          S.space         - which space to do calculations in  
                              (MNI-Aligned | Head | Native)  
                                                          - Default: MNI-Aligned  
          S.overwite      - Overwrite existing BF.mat     - Default: 1  
          S.run           - Run the batch, set to 0 to  
                            bypass the run for debugging  
                                                          - Default: 1  
          S.batch         - matlabbatch, of which this job  
                            can be appended to  
                                                          - Default: []  
         
        Output:  
         BF               - Resultant DAiSS BF structure  
         batch            - matlabbatch job for spm_jobman to run  
         data             - simplified summary of options selected  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_wizard_data", *args, **kwargs)
