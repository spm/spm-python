from spm.__wrapper__ import Runtime


def spm_sections(*args, **kwargs):
    """
      Rendering of regional effects [SPM{.}] on orthogonal sections  
        FORMAT spm_sections(xSPM,hReg,img)  
         
        xSPM  - structure containing details of excursion set (see spm_getSPM)  
        hReg  - handle of MIP register  
        img   - filename of background image  
       __________________________________________________________________________  
         
        spm_sections is called by spm_results_ui and uses variable img to  
        create three orthogonal sections through a background image.  
        Regional foci from the selected xSPM are rendered on this image.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sections.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sections", *args, **kwargs, nargout=0)
