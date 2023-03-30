#! /bin/bash
#$ -l h_vmem=100G ## amout RAM being requested
##$ -l gpu # request the more common P100 nodes
##$ -l A40 # to request the less common A40 nodes
## more details in https://sbia-wiki.uphs.upenn.edu/wiki/index.php/GPU_Computing
#$ -pe threaded 10 ## change number of CPU threads you want to request here
#$ -cwd
#$ -m b 
#$ -m e 
# this file is used to run gpu jobs on the cluster in a proper manner so 
# that the CUDA_VISIBLE_DEVICES environment variable is properly initialized
# ref: https://sbia-wiki.uphs.upenn.edu/wiki/index.php/GPU_Computing#Directing_Jobs_to_a_Specific_GPU_with_the_get_CUDA_VISIBLE_DEVICES_Utility
nvidia-smi
