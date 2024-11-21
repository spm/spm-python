from spm.__wrapper__ import Runtime


def spm_dicom_convert(*args, **kwargs):
    """
      Convert DICOM images into something that SPM can use (e.g. NIfTI)  
        FORMAT out = spm_dicom_convert(Headers,opts,RootDirectory,format,OutputDirectory,meta)  
        Inputs:  
        Headers      - a cell array of DICOM headers from spm_dicom_headers  
        opts     - options:  
                     'all'      - all DICOM files [default]  
                     'mosaic'   - the mosaic images  
                     'standard' - standard DICOM files  
                     'spect'    - SIEMENS Spectroscopy DICOMs (some formats only)  
                                  This will write out a 5D NIFTI containing real  
                                  and imaginary part of the spectroscopy time   
                                  points at the position of spectroscopy voxel(s)  
                     'raw'      - convert raw FIDs (not implemented)  
        RootDirectory - 'flat'       - do not produce file tree [default]  
                     With all other options, files will be sorted into  
                     directories according to their sequence/protocol names:  
                   'date_time'  - Place files under ./<StudyDate-StudyTime>  
                   'patid'      - Place files under ./<PatID>  
                   'patid_date' - Place files under ./<PatID-StudyDate>  
                   'series'     - Place files in series folders, without  
                                  creating patient folders  
        format   - output format:  
                     'nii'      - Single file NIfTI format [default]  
                     'img'      - Two file (Headers+img) NIfTI format  
                   All images will contain a single 3D dataset, 4D images will  
                   not be created.  
        OutputDirectory  - output directory name [default: pwd]  
        meta     - save metadata as sidecar JSON file [default: false]  
         
        Output:  
        out      - a struct with a single field .files. out.files contains a  
                   cellstring with filenames of created files. If no files are  
                   created, a cell with an empty string {''} is returned.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dicom_convert.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dicom_convert", *args, **kwargs)
