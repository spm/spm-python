from spm.__wrapper__ import Runtime


def FieldMap_preprocess(*args, **kwargs):
    """
      Function to prepare fieldmap data for processing  
         
        FORMAT VDM = FieldMap_preprocess(fm_dir,epi_dir,pm_defs,sessname)  
        fm_dir    - name of directory containing fieldmap images  
        epi_dir   - name of directory containing epi images (needs first epi in time  
                    series to match the fieldmap to).  
                    This can also be a cell array of directory names for creating  
                    session-specific versions of a vdm file where each vdm file  
                    is matched to the first image of each EPI directory specified.  
                    Each session specific vdm file will be saved with the name  
                    vdm5_XXXX_'sessname'N.img where 'sessname is 'session' by  
                    default or another name if specified by the user as the fourth  
                    argument to the script.  
        pm_defs   - vector containing following values (optional flags in brackets):  
                    [te1,te2,epifm,tert,kdir,(mask),(match),(write)];  
         
        te1       - short echo time  
        te2       - long echo time  
        epifm     - epi-based fieldmap (1/0)?  
        tert      - total echo readout time  
        kdir      - blip direction (+1/-1)  
        mask      - (optional flag, default=1) Do brain masking or not  
                    (only if non-epi fieldmap)  
        match     - (optional flag, default=1) Match fieldmap to epi or not  
         
        writeunwarped  
                  - (optional flag, default=1) Write unwarped epi or not  
         
        sessname  - (optional string, default='session') This will be the name  
                    extension followed by an incremented integer for session specific vdm files.  
         
        VDM       - cell array of file pointers to the VDM file(s) (voxel displacement map)  
                    required for the Unwarping process. This will be written to the  
                    same directory as the fieldmap data.  
         
        NB:  
        1) This function takes input directory names and parameters and puts them  
        into the correct format for creating fieldmaps  
        2) The function assumes that only the fieldmap images are in the  
        fieldmap directory  
         
        Below is a list of the most common sequences and parameter lists  
        used at the FIL:  
         
        Sonata Siemens fieldmap parameters and default EPI fMRI');  
        VDM=FieldMap_preprocess(fm_dir,epi_dir,[10.0,14.76,0,32,-1]);  
         
        Allegra Siemens fieldmap parameters and default EPI fMRI  
        VDM=FieldMap_preprocess(fm_dir,epi_dir,[10.0,12.46,0,21.12,-1]);  
         
        Allegra Siemens fieldmap parameters and extended FOV EPI fMRI  
        VDM=FieldMap_preprocess(fm_dir,epi_dir,[10.0,12.46,0,23.76,-1]);  
         
        Allegra Siemens fieldmap parameters and 128 EPI fMRI  
        VDM=FieldMap_preprocess(fm_dir,epi_dir,[10.0,12.46,0,71.68,-1]);  
         
        It is also possible to switch off the brain masking which is  
        done by default with a siemens field map (set 6th flag to 0)  
        and the matching of the fieldmap to the EPI (set 7th flag to 0).  
         
        This function generates session specific versions of the vdm file that  
        have been matched to the first image of each session.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/FieldMap_preprocess.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("FieldMap_preprocess", *args, **kwargs)
