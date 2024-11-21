from spm.__wrapper__ import Runtime


def _cfg_justify(*args, **kwargs):
    """
      CFG_JUSTIFY Justifies a text string  
           OUT = CFG_JUSTIFY(N,TXT) justifies text string TXT to  
           the length specified by N.  
         
           OUT = CFG_JUSTIFY(OBJ,TXT), where OBJ is a handle to a 'listbox' style  
           uicontrol, justifies text string TXT to the width of the OBJ in  
           characters - 1.  
         
           If TXT is a cell array, then each element is treated  
           as a paragraph and justified, otherwise the string is  
           treated as a paragraph and is justified.  
           Non a-z or A-Z characters at the start of a paragraph  
           are used to define any indentation required (such as  
           for enumeration, bullets etc.  If less than one line  
           of text is returned, then no formatting is done.  
         
           Example:  
           out = cfg_justify(40,{['Statistical Parametric ',...  
           'Mapping refers to the construction and ',...  
           'assessment of spatially extended ',...  
           'statistical process used to test hypotheses ',...  
           'about [neuro]imaging data from SPECT/PET & ',...  
           'fMRI. These ideas have been instantiated ',...  
           'in software that is called SPM']});  
           strvcat(out{:})  
         
       __________________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_justify.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_justify", *args, **kwargs)
