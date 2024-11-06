from spm.__wrapper__ import Runtime


def spm_file_merge(*args, **kwargs):
    """
      Concatenate 3D volumes into a single 4D volume  
        FORMAT V4 = spm_file_merge(V,fname,dt,RT)  
        V      - images to concatenate (char array or spm_vol struct)  
        fname  - filename for output 4D volume [default: '4D.nii']  
                 Unless explicit, output folder is the one containing first image  
        dt     - datatype (see spm_type) [default: 0]  
                 0 means same datatype than first input volume  
        RT     - Interscan interval {seconds} [default: NaN]  
         
        V4     - spm_vol struct of the 4D volume  
       __________________________________________________________________________  
         
        For integer datatypes, the file scale factor is chosen as to maximise  
        the range of admissible values. This may lead to quantization error  
        differences between the input and output images values.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_file_merge.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_file_merge", *args, **kwargs)
