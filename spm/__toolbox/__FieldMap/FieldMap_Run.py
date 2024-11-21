from spm.__wrapper__ import Runtime


def FieldMap_Run(*args, **kwargs):
    """
      Auxillary file for running FieldMap jobs  
        FORMAT vdm = FieldMap_Run(job)  
         
        job - FieldMap job structure containing various elements:  
              Common to all jobs:  
                defaults - cell array containing name string of the defaults file  
                options  - structure containing the following:  
                  epi - cell array containing name string of epi image to unwarp  
                  matchvdm - match vdm to epi or not (1/0)  
                  writeunwarped - write unwarped EPI or not (1/0)  
                  anat - cell array containing name string of anatomical image  
                  matchanat - match anatomical image to EPI or not (1/0)  
         
              Elements specific to job type:  
                precalcfieldmap - name of precalculated fieldmap  
         
                phase     - name of phase image for presubtracted phase/mag job  
                magnitude - name of magnitude image for presubtracted phase/mag job  
         
                shortphase - name of short phase image for phase/mag pair job  
                longphase  - name of short phase image for phase/mag pair job  
                shortmag   - name of short magnitude image for phase/mag pair job  
                longmag    - name of short magnitude image for phase/mag pair job  
         
                shortreal - name of short real image for real/imaginary job  
                longreal  - name of long real image for real/imaginary job  
                shortimag - name of short imaginary image for real/imaginary job  
                longimag  - name of long imaginary image for real/imaginary job  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/FieldMap_Run.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("FieldMap_Run", *args, **kwargs)
