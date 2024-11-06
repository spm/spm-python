from spm.__wrapper__ import Runtime


def mne_morph_data(*args, **kwargs):
    """
      MNE_MORPH_DATA   Returns data morphed to a new subject.  
         
          SYNTAX  
              [STCS] = MNE_MORPH_DATA(FROM, TO, STCS, GRADE)  
         
          from : name of origin subject  
          to : name of destination subject  
          stcs : stc data to morph  
          grade : (optional) resolution of the icosahedral mesh (typically 5)  
         
        Note : The functions requires to set MNE_ROOT and SUBJECTS_DIR variables.  
         
        Example:  
         from = 'sample';  
         to = 'fsaverage';  
         stcs_morph = mne_morph_data(from,to,stcs,5);  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_morph_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_morph_data", *args, **kwargs)
