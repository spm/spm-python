from spm.__wrapper__ import Runtime


def spm_ov_reorient(*args, **kwargs):
    """
      Reorient tool - plugin for spm_orthviews  
         
        This tool provides the capabilities of the reorientation widget in SPM's  
        "Display" for any image displayed within spm_orthviews.  The control  
        fields are drawn in the SPM Interactive window and work as described in  
        the Display routine.  
        The advantage of using this tool within CheckReg is that it allows to  
        reorient images while comparing their position to reference images  
        simultaneously.  
         
        This routine is a plugin to spm_orthviews. For general help about  
        spm_orthviews and plugins type  
                    help spm_orthviews  
        at the MATLAB prompt.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_orthviews/spm_ov_reorient.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ov_reorient", *args, **kwargs)
